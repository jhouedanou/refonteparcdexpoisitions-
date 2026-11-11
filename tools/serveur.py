#!/usr/bin/env python3
"""Serveur de prévisualisation local avec rechargement à chaud.

Usage : python3 tools/serveur.py [--port 8000] [--open]

- .css modifié  -> la feuille est rechargée dans la page, sans perdre le défilement ni l’état ;
- .scss modifié -> compilé en .css à côté du fichier (styles.scss -> styles.css), puis rechargé à chaud ;
                   les fichiers partiels (_nom.scss) ne sont pas compilés seuls mais déclenchent la compilation ;
- .html / .js   -> la page est rechargée ;
- tools/pages/*.py, tools/i18n/en.py -> les pages sont régénérées (generer.py), puis rechargées.

Aucune dépendance pour le CSS. Le SCSS demande `sass` (npm i -g sass) ; à défaut, `npx sass` est utilisé.
Rien n’est écrit dans les pages : le script de rechargement est ajouté à la volée, à l’envoi.
"""
import argparse
import http.server
import os
import pathlib
import queue
import shutil
import subprocess
import sys
import threading
import time
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent.parent
IGNORES = {".git", "node_modules", "__pycache__", "images", "docs", "design", "img", "video", ".claude"}
SUIVIS = {".css", ".scss", ".html", ".js", ".py"}
GENERATEURS = ("tools/pages/", "tools/i18n/en.py")
CLIENTS = set()
VERROU = threading.Lock()

SCRIPT = b"""<script>/* rechargement a chaud : tools/serveur.py */
(function () {
  var es = new EventSource('/__live');
  es.addEventListener('css', function () {
    document.querySelectorAll('link[rel="stylesheet"]').forEach(function (l) {
      var u = new URL(l.href);
      if (u.origin !== location.origin) return;
      u.searchParams.set('v', Date.now());
      l.href = u.href;
    });
  });
  es.addEventListener('reload', function () { location.reload(); });
  es.addEventListener('erreur', function (e) { console.error('[serveur]\\n' + JSON.parse(e.data)); });
})();
</script>"""


def diffuser(evenement, donnees="1"):
    with VERROU:
        for q in list(CLIENTS):
            q.put((evenement, donnees))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def log_message(self, *a):  # terminal lisible : seuls les changements sont affichés
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path.split("?")[0] == "/__live":
            return self.flux()
        chemin = pathlib.Path(self.translate_path(self.path))
        if chemin.is_dir() and self.path.split("?")[0].endswith("/"):
            chemin = chemin / "index.html"
        if chemin.suffix == ".html" and chemin.is_file():
            corps = chemin.read_bytes()
            i = corps.rfind(b"</body>")
            corps = corps[:i] + SCRIPT + corps[i:] if i >= 0 else corps + SCRIPT
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)
            return
        super().do_GET()

    def flux(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        q = queue.Queue()
        with VERROU:
            CLIENTS.add(q)
        try:
            while True:
                try:
                    evenement, donnees = q.get(timeout=15)
                    self.wfile.write(f"event: {evenement}\ndata: {donnees}\n\n".encode())
                except queue.Empty:
                    self.wfile.write(b": ping\n\n")  # garde la connexion ouverte
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            with VERROU:
                CLIENTS.discard(q)


class Serveur(http.server.ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def etat():
    """Date de modification de chaque fichier suivi."""
    vus = {}
    for dossier, sous, fichiers in os.walk(ROOT):
        sous[:] = [d for d in sous if d not in IGNORES]
        for f in fichiers:
            if os.path.splitext(f)[1] in SUIVIS:
                p = os.path.join(dossier, f)
                try:
                    vus[p] = os.stat(p).st_mtime_ns
                except OSError:
                    pass
    return vus


def executer(commande, libelle):
    r = subprocess.run(commande, cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        message = (r.stderr or r.stdout).strip()
        print(f"  ERREUR {libelle}\n{message}")
        import json
        diffuser("erreur", json.dumps(f"{libelle}\n{message}"))
        return False
    return True


def compiler_scss():
    sass = [shutil.which("sass")] if shutil.which("sass") else (["npx", "--yes", "sass"] if shutil.which("npx") else None)
    if not sass:
        print("  SCSS ignoré : installer sass (npm i -g sass)")
        return False
    ok = True
    for src in sorted(p for p in etat() if p.endswith(".scss") and not os.path.basename(p).startswith("_")):
        dest = src[:-5] + ".css"
        ok &= executer(sass + ["--no-source-map", src, dest], f"sass {os.path.relpath(src, ROOT)}")
        if ok:
            print(f"  compilé {os.path.relpath(src, ROOT)} -> {os.path.relpath(dest, ROOT)}")
    return ok


def surveiller():
    avant = etat()
    while True:
        time.sleep(0.3)
        apres = etat()
        modifies = [os.path.relpath(p, ROOT) for p, m in apres.items() if avant.get(p) != m]
        if not modifies:
            avant = apres
            continue
        print(time.strftime("%H:%M:%S"), ", ".join(modifies[:4]) + (" …" if len(modifies) > 4 else ""))
        ext = {os.path.splitext(p)[1] for p in modifies}
        if ".scss" in ext:
            compiler_scss()
        if any(p.startswith(GENERATEURS) and p.endswith(".py") for p in modifies):
            if "tools/i18n/en.py" in modifies:
                executer([sys.executable, "tools/i18n/en.py"], "en.py")
            if executer([sys.executable, "tools/pages/generer.py"], "generer.py"):
                print("  pages régénérées")
            ext.add(".html")
        diffuser("reload" if ext & {".html", ".js"} else "css")
        avant = etat()  # inclut les fichiers écrits par la compilation / la génération


def main():
    ap = argparse.ArgumentParser(description="Prévisualisation locale avec rechargement à chaud.")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--open", action="store_true", help="ouvre le navigateur")
    args = ap.parse_args()
    if any(p.endswith(".scss") for p in etat()):
        compiler_scss()
    serveur = Serveur(("127.0.0.1", args.port), Handler)
    threading.Thread(target=surveiller, daemon=True).start()
    url = f"http://127.0.0.1:{args.port}/"
    print(f"Prévisualisation : {url}  (Ctrl+C pour arrêter)")
    if args.open:
        webbrowser.open(url)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt.")


if __name__ == "__main__":
    main()
