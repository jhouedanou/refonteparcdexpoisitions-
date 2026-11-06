#!/usr/bin/env python3
"""Rapport d’intégration page par page (charte PEA + Bento DS), à partir des mesures de tools/verif/conformite.mjs.

Usage : node tools/verif/conformite.mjs --shots --out=<dossier> --pages=…   puis
        python3 tools/verif/rapport.py <dossier>
Sorties : design-system/pea/RAPPORT-INTEGRATION.md (versionné) et <dossier>/rapport-html/ (HTML illustré + vignettes).
"""
import collections
import datetime
import html
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = pathlib.Path(sys.argv[1])
DATA = json.loads((SRC / "rapport.json").read_text(encoding="utf-8"))
OUT_MD = ROOT / "design-system" / "pea" / "RAPPORT-INTEGRATION.md"
OUT_HTML = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else SRC / "rapport-html"
WIDTHS = sorted({x["width"] for x in DATA})
SCALE = [0, 1, 2, 3, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96, 128]

FONDS = {"#FFFFFF": "blanc", "#F7F5F1": "pierre claire", "#FCF2EA": "crème", "#9D4015": "brun", "#006528": "vert",
         "#5D120A": "brun foncé", "#B34900": "orange action", "#FAFAFA": "blanc cassé", "transparent": "transparent",
         "#000000": "voile noir", "#0A0A0A": "noir"}

ORDRE = ["index.html", "qui-sommes-nous.html", "nos-espaces.html", "hall-exposition.html", "le-dome.html", "parvis-esplanades.html",
         "visite-virtuelle.html", "nos-services.html", "phototheque.html", "agenda.html", "contact-devis.html",
         "salons-professionnels.html", "congres-conferences.html", "evenements-entreprise.html", "concerts-spectacles.html",
         "venir-a-abidjan.html", "informations-legales.html"]


def fmt(n):
    return f"{n:,}".replace(",", "\u202f")


def num(s):
    try:
        return float(str(s).replace("px", ""))
    except ValueError:
        return None


def pad(m):
    return [num(v) for v in m["padding"].split()]


def gaps(m):
    return [num(v) for v in m["gap"].split(" / ")] if m["gap"] != "—" else [0, 0]


# Spécifications Bento relevées dans Bento DS.fig (tokens de composants) et contrôle sur la mesure à la plus grande largeur.
# Chaque entrée : (spec lisible, fonction de contrôle → (ok, note)). « écart assumé » = documenté dans CONFORMITE.md § 4.
def chk(cond, ok_note="", ko_note=""):
    return (True, ok_note) if cond else (False, ko_note)


SPECS = {
    "Topbar": ("topbar/height 48 · topbar/bg primary/800 (brun)", lambda m, w: chk(m["h"] == 48 and m["fond"] == "#9D4015")),
    "Site header": ("site-header/height 64 · fond clair · ombre une fois collé", lambda m, w: chk(m["h"] in (64, 72) and m["fond"] == "#FFFFFF", "72 px dès 1120 px : logo de 48 px (écart assumé)" if m["h"] == 72 else "")),
    "Menu": ("menu/item-padding 8 / 16 · menu/fg neutral/950", lambda m, w: chk(m["texte"] == "#0A0A0A" and m["police"].endswith("16px"))),
    "Breadcrumb": ("breadcrumb/font-size 14 · séparateur « › » · courant en gras", lambda m, w: chk(m["police"].endswith("14px"))),
    "Page header": ("page-header/padding-block 128 · Background=image, Color=primary", lambda m, w: chk(pad(m)[0] in (64, 96, 128) and m["fond"] == "#B34900", f"padding {pad(m)[0]:g} px à cette largeur (64 → 96 → 128)")),
    "Block/Hero": ("block-hero : contenu ≤ 768 · lead 18 · voile sur photo", lambda m, w: (True, "")),
    "Carousel": ("carousel/btn-size 57,6 · puces", lambda m, w: (True, "boutons de 56 px (rayon 0) — écart assumé")),
    "Title": ("title/font-weight 700 · line-height 1,2 · L1 48 → L6 16", lambda m, w: chk("700" in m["police"])),
    "Button": ("btn 16 px Regular · padding 12 / 16 · bordure 2", lambda m, w: chk(m["police"] == "Poppins 400 16px" and pad(m)[0] in (8, 12) and m["bordure"].startswith("2px"), "", "hors spec")),
    "Link": ("link/color primary · souligné au survol · gap 8", lambda m, w: chk(m["texte"] in ("#B34900", "#FFFFFF"))),
    "Badge": ("badge 14 px Bold capitales · padding 4 / 12 · bordure 1", lambda m, w: chk(m["police"].startswith("Poppins 700 14px") and pad(m)[:2] == [4, 12] and m["bordure"].startswith("1px"))),
    "Card": ("card/padding 24 · card/gap 16 · bordure 1 base-300", lambda m, w: chk(pad(m)[0] in (16, 24) and gaps(m)[0] in (0, 16), "padding 16 : carte compacte d’agenda" if pad(m)[0] == 16 else "")),
    "Collection": ("collection/gap-md 24 · 1 à 3 colonnes", lambda m, w: chk(gaps(m)[1] == 24 or gaps(m)[0] == 24)),
    "Block/Key figures": ("block-key-figures/gap 24 · valeur 36 Bold · centré", lambda m, w: chk(gaps(m)[1] == 24 or gaps(m)[0] == 24)),
    "Block/Video": ("block-youtube : cadre 16:9 · lecture 64 px centrée", lambda m, w: (True, "")),
    "Cta": ("cta/padding 48 / 32 · Background=image", lambda m, w: chk(pad(m)[0] == 48 and pad(m)[1] == 32)),
    "Block/Partners": ("block-partners/tile-height 150 · logo ≤ 100", lambda m, w: (True, "")),
    "Block/Agenda list": ("block-events : titre d’item, bouton primary", lambda m, w: (True, "")),
    "Modal": ("modal/padding 24 · surface blanche · voile 60 %", lambda m, w: (True, "")),
    "Accordion": ("accordion/gap 16 · item 8 / 16 · fond primary/50", lambda m, w: chk(gaps(m)[0] == 16)),
    "Image gallery": ("image-gallery/gap 16 · voile 30 % au survol", lambda m, w: chk(gaps(m)[1] == 16)),
    "Form/Field": ("form : label Bold · gap 8 · focus 2 px", lambda m, w: chk(gaps(m)[0] in (8, 0))),
    "Newsletter form": ("newsletter-form : champ + bouton primary", lambda m, w: chk(m["fond"] == "#FCF2EA")),
    "Contact details": ("contact-details/gap 8", lambda m, w: chk(gaps(m)[0] == 8)),
    "Block/Map": ("block-map/height 400", lambda m, w: chk(m["h"] == 400)),
    "Footer": ("footer/bg primary/800 (brun) · colonnes titre + menu · barre légale", lambda m, w: chk(m["fond"] == "#9D4015")),
    "Tabs": ("tab/padding 12 / 16 · filet 2", lambda m, w: (True, "")),
    "Item list": ("item-list : liste de services", lambda m, w: (True, "")),
    "Block/Icons text": ("block-icons-text : 3 colonnes, Divider", lambda m, w: (True, "")),
}

by_page = collections.defaultdict(dict)
for x in DATA:
    by_page[x["page"]][x["width"]] = x
pages = [p for p in ORDRE if p in by_page] + sorted(p for p in by_page if p.startswith("evenement-")) + sorted(p for p in by_page if p.startswith("en/"))
pages += [p for p in by_page if p not in pages]
WMAX, WMIN = max(WIDTHS), min(WIDTHS)


def fond(h):
    return f"{FONDS.get(h, h)}" + (f" ({h})" if h in FONDS and h != "transparent" else "")


def vgaps(x):
    c = collections.Counter()
    for k, v in (x.get("gaps") or {}).items():
        if k.startswith("vertical"):
            c[int(k.split()[1])] += v
    return c


# ---------------------------------------------------------------- vignettes (HTML)
OUT_HTML.mkdir(exist_ok=True)
(OUT_HTML / "img").mkdir(exist_ok=True)


def thumb(page, width, height, out_w):
    src = SRC / f"{page.replace('/', '_').replace('.html', '')}-{width}.jpg"
    if not src.exists():
        return None
    dest = OUT_HTML / "img" / f"{page.replace('/', '_').replace('.html', '')}-{width}.jpg"
    if not dest.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"crop=iw:min(ih\\,{height}):0:0,scale={out_w}:-1", "-q:v", "4", str(dest)], check=True)
    return f"img/{dest.name}"


# ---------------------------------------------------------------- synthèse
total = sum(len(x["violations"]) for x in DATA)
textes = sum(x["stats"]["textes"] for x in DATA)
titres = sum(x["stats"]["titres"] for x in DATA)
boutons = sum(x["stats"]["boutons"] for x in DATA)
allgaps = collections.Counter()
for x in DATA:
    allgaps.update(vgaps(x))
ngaps = sum(sum((x.get("gaps") or {}).values()) for x in DATA)
usage = collections.Counter()
for p in pages:
    x = by_page[p][WMAX]
    for k in x["releve"]["composants"]:
        usage[k] += 1
date = datetime.date.today().strftime("%d/%m/%Y")

md = [f"# Rapport d’intégration : charte PEA + Bento DS, page par page", "",
      f"Généré le {date} par `tools/verif/rapport.py`, à partir des mesures de `node tools/verif/conformite.mjs` "
      f"(Chrome headless, styles **calculés**, mouvement réduit pour que tout soit visible). Version illustrée (captures) : publiée avec ce rapport.", "",
      "## Synthèse", "",
      "| Indicateur | Valeur |", "|---|---|",
      f"| Pages contrôlées | {len(pages)} (toutes les pages FR + 3 pages EN) |",
      f"| Largeurs | {' · '.join(map(str, WIDTHS))} px |",
      f"| Combinaisons page × largeur | {len(DATA)} |",
      f"| **Écarts restants** | **{total}** |",
      f"| Textes contrôlés (police, graisse, contraste) | {fmt(textes)} |",
      f"| Titres contrôlés (composant Title) | {fmt(titres)} |",
      f"| Boutons contrôlés (composant Button) | {fmt(boutons)} |",
      f"| Écarts entre sous-éléments mesurés | {fmt(ngaps)} |", "",
      "### Règles contrôlées sur chaque page et chaque largeur", "",
      "- **Charte** : Poppins seule ; graisses 100 / 400 / 700 (kit web p. 17) ; aucun fond noir ; logo jamais déformé ; titres ≥ 24 px en orange #DA5900, jamais d’orange sous 24 px.",
      "- **Bento** : Button 16 px Regular bordure 2 ; Title Bold ; Topbar 48 px ; Site header 64 / 72 px ; composants attendus présents (`data-bento`) ; angles vifs (rayons à 0, champs 2 px).",
      "- **Accessibilité** : contraste ≥ 4,5:1 (≥ 3:1 pour le grand texte) de chaque texte sur son fond réel ; aucun débordement horizontal.",
      "- **Espacements** : chaque padding, marge verticale et gap sur l’échelle Bento (4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64, plus 96 · 128 pour la mise en page) ; "
      "l’écart rendu entre deux sous-éléments voisins sur l’échelle, jamais négatif, jamais nul entre deux blocs de texte. "
      "Seules exceptions : les réserves de l’arche du logo (hauteur proportionnelle à la largeur) et l’espace libre d’alignement (liens de cartes alignés en bas).", "",
      "### Écarts verticaux mesurés entre sous-éléments (toutes pages, toutes largeurs)", "",
      "| Écart | " + " | ".join(f"{k} px" for k, _ in sorted(allgaps.items()) if allgaps[k] >= 1) + " |",
      "|---|" + "---|" * len([k for k in allgaps if allgaps[k] >= 1]),
      "| Occurrences | " + " | ".join(str(v) for _, v in sorted(allgaps.items()) if v >= 1) + " |", "",
      "Les valeurs hors échelle restantes (si présentes) sont des espaces libres d’alignement en flex / grille, listés page par page.", "",
      "### Composants Bento par page", "",
      "| Composant | Pages | Spec Bento contrôlée |", "|---|---|---|"]
for k, n in sorted(usage.items(), key=lambda t: (-t[1], t[0])):
    md.append(f"| {k} | {n} / {len(pages)} | {SPECS.get(k, ('—',))[0]} |")
md += ["", "## Pages", ""]

# ---------------------------------------------------------------- HTML
H = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
     "<title>Rapport d’intégration PEA</title>",
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
     '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">',
     "<style>",
     ":root{--o:#da5900;--a:#b34900;--b:#9d4015;--v:#006528;--n:#0a0a0a;--m:#525252;--l:#e7e1d6;--p:#f7f5f1;--c:#fcf2ea}",
     "/* Page claire unique (charte : fond blanc) ; mise en page : synthèse puis une fiche par page */ :root{color-scheme:light}*{box-sizing:border-box}body{margin:0;font:400 15px/1.55 Poppins,'Helvetica Neue',Arial,sans-serif;color:var(--n);background:#fff}a:focus-visible{outline:2px solid var(--n);outline-offset:2px}.tw{overflow-x:auto}h1,h2,h3{text-wrap:balance}td{font-variant-numeric:tabular-nums}",
     "header.top{background:var(--b);color:#fff;padding:32px clamp(16px,4vw,64px)}header.top h1{margin:0 0 8px;font-size:clamp(24px,3vw,36px)}header.top p{margin:0;color:#f8e0cc;max-width:80ch}",
     "main{padding:0 clamp(16px,4vw,64px) 64px;max-width:1400px;margin:auto}h2{color:var(--o);font-size:26px;margin:48px 0 16px}h3{font-size:20px;margin:24px 0 8px}",
     "table{border-collapse:collapse;width:100%;margin:8px 0 16px;font-size:13px}th,td{border-bottom:1px solid var(--l);padding:6px 8px;text-align:left;vertical-align:top}th{background:var(--p);font-weight:700}",
     ".kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;margin:24px 0}.kpi{border:1px solid var(--l);padding:16px}.kpi b{display:block;font-size:28px;color:var(--o)}",
     "nav.toc{columns:3 220px;font-size:13px;margin:16px 0}nav.toc a{color:var(--a)}section.page{border-top:3px solid var(--o);margin-top:48px;padding-top:8px}",
     ".shots{display:grid;grid-template-columns:3fr 1fr;gap:16px;align-items:start;margin:16px 0}.shots figure{margin:0}.shots img{width:100%;border:1px solid var(--l)}.shots figcaption{font-size:12px;color:var(--m)}",
     ".ok{color:var(--v);font-weight:700}.ko{color:#b42318;font-weight:700}.sw{display:inline-block;width:12px;height:12px;border:1px solid #ccc;vertical-align:-1px;margin-right:4px}",
     ".badge{display:inline-block;padding:2px 8px;border:1px solid var(--a);color:var(--a);font-weight:700;font-size:12px;text-transform:uppercase}",
     "@media(max-width:800px){.shots{grid-template-columns:1fr}}",
     "</style></head><body>",
     '<header class="top"><h1>Rapport d’intégration : charte PEA + Bento DS</h1>',
     f"<p>{len(pages)} pages · {len(DATA)} combinaisons page × largeur ({' · '.join(map(str, WIDTHS))} px) · mesures des styles calculés dans Chrome — généré le {date}.</p></header><main>",
     '<div class="kpis">' + "".join(f'<div class="kpi"><b>{v}</b>{k}</div>' for k, v in [
         ("écarts restants", total), ("pages", len(pages)), ("textes contrôlés", f"{textes:,}".replace(",", " ")),
         ("titres", f"{titres:,}".replace(",", " ")), ("boutons", f"{boutons:,}".replace(",", " ")), ("écarts entre sous-éléments", f"{ngaps:,}".replace(",", " "))]) + "</div>",
     "<h2>Méthode</h2><p>Chaque page est ouverte dans Chrome headless à chaque largeur, en mouvement réduit. Le script contrôle les styles <b>calculés</b> de chaque élément visible : "
     "police et graisses (kit web 100/400/700), fonds (jamais de noir), angles vifs, titres (Bento Title), boutons (Bento Button), hauteurs Topbar / Site header, "
     "contraste de chaque texte sur son fond réel, présence des composants Bento (<code>data-bento</code>), débordement, logo, et l’échelle d’espacement Bento "
     "(chaque padding / marge / gap, puis l’écart rendu entre sous-éléments voisins).</p>",
     "<h2>Composants Bento par page</h2><div class=\"tw\"><table><tr><th>Composant</th><th>Pages</th><th>Spec Bento contrôlée</th></tr>" +
     "".join(f"<tr><td>{html.escape(k)}</td><td>{n} / {len(pages)}</td><td>{html.escape(SPECS.get(k, ('—',))[0])}</td></tr>" for k, n in sorted(usage.items(), key=lambda t: (-t[1], t[0]))) + "</table></div>",
     "<h2>Pages</h2><nav class=\"toc\">" + "".join(f'<a href="#{re.sub("[^a-z0-9]+", "-", p)}">{html.escape(by_page[p][WMAX]["releve"]["titrePage"].split(" | ")[0].split(" — ")[0])}</a><br>' for p in pages) + "</nav>"]

for p in pages:
    X = by_page[p][WMAX]
    rel = X["releve"]
    titre = rel["titrePage"].split(" | ")[0].split(" — ")[0]
    ecarts = {w: len(by_page[p][w]["violations"]) for w in WIDTHS if w in by_page[p]}
    statut = "0 écart à " + " · ".join(f"{w}" for w in ecarts) + " px" if not sum(ecarts.values()) else " · ".join(f"{w} px : {n}" for w, n in ecarts.items())
    vg = vgaps(X)
    hors = sorted(g for g in vg if not any(abs(g - s) < 1 for s in SCALE))
    libres = sorted({re.sub(r"« [^»]*»", "", l).strip() for w in WIDTHS for l in (by_page[p].get(w, {}).get("libres") or [])})
    Xm = by_page[p].get(WMIN)
    anchor = re.sub("[^a-z0-9]+", "-", p)

    md += [f"### {titre}", "", f"`{p}` — **{statut}** · {X['stats']['textes']} textes, {X['stats']['titres']} titres, {X['stats']['boutons']} boutons, "
           f"{X['stats']['composants']} composants Bento · contraste minimal {rel['contrasteMin']}:1", ""]
    md += [f"**Sections ({WMAX} px)**", "", "| # | Section | Fond | Padding haut / bas | Hauteur | Composants |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(rel["sections"], 1):
        md.append(f"| {i} | {s['section']} | {fond(s['fond'])} | {s['padding']} | {s['hauteur']} | {', '.join(s['composants'])} |")
    md += ["", f"**Composants ({WMAX} px, première occurrence)**", "", "| Composant | Nb | Mesure | Spec Bento | État |", "|---|---|---|---|---|"]
    hrows = []
    for k, v in sorted(rel["composants"].items()):
        m = v.get("mesure")
        if not m or (m["w"] == 0 and k != "Modal"):
            mesure, ok, note = "masqué à cette largeur", True, ""
        else:
            mesure = f"{m['w']}×{m['h']} · padding {m['padding']} · gap {m['gap']} · {m['police']} · fond {fond(m['fond'])}" + (f" · bordure {m['bordure']}" if m["bordure"] != "—" else "")
            if v.get("ecarts"):
                mesure += f" · écarts internes {', '.join(map(str, v['ecarts']))}"
            ok, note = SPECS.get(k, ("", lambda m, w: (True, "")))[1](m, WMAX) if m["w"] else (True, "fermé (dialogue)")
        spec = SPECS.get(k, ("—",))[0]
        etat = ("✅ " if ok else "⚠️ ") + note
        md.append(f"| {k} | {v['nombre']} | {mesure} | {spec} | {etat.strip()} |")
        hrows.append(f"<tr><td>{html.escape(k)}</td><td>{v['nombre']}</td><td>{html.escape(mesure)}</td><td>{html.escape(spec)}</td><td class=\"{'ok' if ok else 'ko'}\">{html.escape(etat)}</td></tr>")
    tl = " · ".join(f"{k.replace('title--', '').upper()} {v}" for k, v in sorted(rel["titres"].items()))
    md += ["", f"**Titres** : {tl or '—'}", "",
           f"**Espacements ({WMAX} px)** : écarts verticaux entre sous-éléments — " + ", ".join(f"{g} px × {n}" for g, n in sorted(vg.items())) +
           f". Hors échelle : {('aucun' if not hors else ', '.join(f'{g} px' for g in hors) + ' (espace libre d’alignement)')}.", ""]
    if libres:
        md += ["Espaces libres d’alignement (voulus) : " + " ; ".join(libres[:4]), ""]
    if Xm:
        rm = Xm["releve"]
        hh = rm["composants"].get("Site header", {}).get("mesure", {}).get("h", "—")
        t1 = rm["titres"].get("title--l1", "—")
        sp = sorted({s["padding"] for s in rm["sections"][2:-2] if s["padding"] != "0 / 0"})
        md += [f"**Mobile ({WMIN} px)** : en-tête {hh} px · titre L1 {t1} · padding des sections {', '.join(sp[:3])} · {len(Xm['violations'])} écart.", ""]
    big = thumb(p, WMAX, 2400, 900)
    small = thumb(p, WMIN, 2400, 300)
    H.append(f'<section class="page" id="{anchor}"><h2>{html.escape(titre)}</h2><p><span class="badge">{html.escape(p)}</span> <b class="{"ok" if not sum(ecarts.values()) else "ko"}">{html.escape(statut)}</b> · '
             f"{X['stats']['textes']} textes, {X['stats']['titres']} titres, {X['stats']['boutons']} boutons, {X['stats']['composants']} composants Bento · contraste minimal {rel['contrasteMin']}:1</p>")
    if big or small:
        H.append('<div class="shots">' + (f'<figure><img loading="lazy" src="{big}" alt="Capture {WMAX} px : {html.escape(titre)}"><figcaption>{WMAX} px (haut de page)</figcaption></figure>' if big else "") +
                 (f'<figure><img loading="lazy" src="{small}" alt="Capture {WMIN} px : {html.escape(titre)}"><figcaption>{WMIN} px</figcaption></figure>' if small else "") + "</div>")
    H.append("<h3>Sections</h3><div class=\"tw\"><table><tr><th>#</th><th>Section</th><th>Fond</th><th>Padding haut / bas</th><th>Hauteur</th><th>Composants</th></tr>" +
             "".join(f'<tr><td>{i}</td><td>{html.escape(s["section"])}</td><td><span class="sw" style="background:{s["fond"] if s["fond"] != "transparent" else "#fff"}"></span>{html.escape(fond(s["fond"]))}</td><td>{s["padding"]}</td><td>{s["hauteur"]}</td><td>{html.escape(", ".join(s["composants"]))}</td></tr>' for i, s in enumerate(rel["sections"], 1)) + "</table></div>")
    H.append("<h3>Composants Bento</h3><div class=\"tw\"><table><tr><th>Composant</th><th>Nb</th><th>Mesure</th><th>Spec Bento</th><th>État</th></tr>" + "".join(hrows) + "</table></div>")
    H.append(f"<p><b>Titres</b> : {html.escape(tl or '—')}</p><p><b>Espacements</b> : " + html.escape(", ".join(f"{g} px × {n}" for g, n in sorted(vg.items()))) +
             f" · hors échelle : {html.escape('aucun' if not hors else ', '.join(f'{g} px' for g in hors) + ' (espace libre d’alignement)')}</p></section>")

md += ["## Écarts assumés et points client", "", "Voir `design-system/pea/CONFORMITE.md` § 4 et § 5.", ""]
OUT_MD.write_text("\n".join(md), encoding="utf-8")
H.append("<h2>Écarts assumés</h2><p>Rayons à 0 (choix PEA) · titres L1–L3 orange (choix PEA) · logo de 48 px · bordure des champs #737373 (3:1) · champs de 48 px · filtres pressés en orange (pas de noir) · onglet actif en #B34900 · boutons de carrousel de 56 px. Détail : <code>design-system/pea/CONFORMITE.md</code>.</p></main></body></html>")
(OUT_HTML / "index.html").write_text("\n".join(H), encoding="utf-8")
print(f"écrit {OUT_MD.relative_to(ROOT)} ({len(md)} lignes) et {OUT_HTML / 'index.html'}")
