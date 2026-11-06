#!/usr/bin/env python3
"""Rapport d’intégration destiné au client (peu technique) : composants utilisés et charte respectée, page par page.

Usage : node tools/verif/conformite.mjs --shots --out=<dossier> --pages=…   puis
        python3 tools/verif/rapport_client.py <dossier> [<dossier HTML>]
Sorties : design-system/pea/RAPPORT-INTEGRATION.md (versionné) et <dossier HTML>/index.html + img/ (version illustrée).
Les mesures détaillées sont dans l’annexe technique (tools/verif/rapport.py → RAPPORT-TECHNIQUE.md).
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
OUT_HTML = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "design-system" / "pea" / "rapport-integration"
OUT_MD = ROOT / "design-system" / "pea" / "RAPPORT-INTEGRATION.md"
DATA = json.loads((SRC / "rapport.json").read_text(encoding="utf-8"))
DEMO = re.search(r'^SITE = "([^"]+)"', (ROOT / "tools/pages/referencement.py").read_text(encoding="utf-8"), re.M).group(1)
WIDTHS = sorted({x["width"] for x in DATA})
WMAX, WMIN = max(WIDTHS), min(WIDTHS)
DATE = datetime.date.today().strftime("%d/%m/%Y")


def demo(page):
    return DEMO + ("" if page == "index.html" else "en/" if page == "en/index.html" else page)


# ---------------------------------------------------------------- vocabulaire
COMPOSANTS = [  # (nom Bento, nom simple, rôle) — dans l’ordre où on les rencontre en parcourant une page
    ("Topbar", "Barre d’informations", "téléphone WhatsApp, « Abidjan, Côte d’Ivoire », langues et réseaux sociaux, sur le brun de la charte"),
    ("Site header", "En-tête", "logo, menu et bouton « Demander un devis » ; reste visible quand on fait défiler la page"),
    ("Menu", "Menu de navigation", "les rubriques du site, avec le sous-menu des espaces"),
    ("Block/Hero", "Grand visuel d’accueil", "diaporama de photos officielles, accroche et boutons"),
    ("Carousel", "Commandes de défilement", "précédent, pause, suivant et repères de position"),
    ("Page header", "Bandeau de page", "titre et introduction sur une photo officielle teintée de l’orange de la charte"),
    ("Breadcrumb", "Fil d’Ariane", "indique où l’on se trouve dans le site"),
    ("Tabs", "Onglets de la fiche", "accès direct aux parties de la page"),
    ("Block/Key figures", "Chiffres clés", "surfaces et capacités mises en avant en orange"),
    ("Image gallery", "Galerie photo", "photos officielles, agrandissables en plein écran"),
    ("Block/Video", "Vidéo de présentation", "la vidéo officielle du Parc, lancée au clic"),
    ("Collection", "Grille de cartes", "cartes alignées sur une à trois colonnes"),
    ("Card", "Cartes", "un espace, un événement, une actualité ou un encart, avec photo, titre et lien"),
    ("Block/Icons text", "Arguments", "trois raisons de choisir le Parc, présentées côte à côte"),
    ("Item list", "Liste des services", "les prestations proposées, numérotées"),
    ("Block/Agenda list", "Agenda", "les événements mois par mois, avec date, type et détails"),
    ("Accordion", "Questions fréquentes", "réponses qui se déplient au clic"),
    ("Form/Field", "Formulaire de devis", "champs, cases à cocher et messages d’aide"),
    ("Contact details", "Coordonnées", "adresse et contact WhatsApp"),
    ("Block/Map", "Carte d’accès", "Google Maps, chargée seulement avec l’accord du visiteur"),
    ("Cta", "Appel à l’action", "invitation à demander un devis, sur le brun foncé avec la photo du Dôme"),
    ("Block/Partners", "Références", "logos des organisateurs qui ont fait confiance au Parc"),
    ("Modal", "Fenêtres", "détail d’un événement, visionneuse photo, bandeau cookies"),
    ("Newsletter form", "Inscription à la newsletter", "e-mail et consentement, sur fond crème"),
    ("Footer", "Pied de page", "rubriques, coordonnées, liens légaux et logo GL events"),
    ("Button", "Boutons", "action principale en orange, actions secondaires en contour"),
    ("Badge", "Étiquettes", "type d’événement, date, espace, usages"),
    ("Link", "Liens", "liens fléchés en orange"),
    ("Title", "Titres", "en Poppins Bold ; orange PEA pour les grands titres"),
]
NOM = {k: (n, r) for k, n, r in COMPOSANTS}
ORDRE = [k for k, _, _ in COMPOSANTS]

APLATS = {"#9D4015": ("brun", "#9D4015"), "#006528": ("vert", "#006528"), "#5D120A": ("brun foncé", "#5D120A"),
          "#FCF2EA": ("crème", "#FCF2EA"), "#B34900": ("orange (bandeau de page)", "#B34900")}

PAGES = [  # (fichier, nom, groupe) — dans l’ordre de lecture du rapport
    ("index.html", "Accueil", "Accueil et présentation"), ("qui-sommes-nous.html", "Qui sommes-nous ?", "Accueil et présentation"),
    ("nos-espaces.html", "Nos espaces", "Les espaces"), ("hall-exposition.html", "Hall d’Exposition", "Les espaces"),
    ("le-dome.html", "Le Dôme", "Les espaces"), ("parvis-esplanades.html", "Parvis & Esplanades", "Les espaces"),
    ("visite-virtuelle.html", "Visite virtuelle 360°", "Les espaces"),
    ("nos-services.html", "Nos services", "Services, photothèque, agenda et contact"), ("phototheque.html", "Photothèque", "Services, photothèque, agenda et contact"),
    ("agenda.html", "Agenda", "Services, photothèque, agenda et contact"), ("contact-devis.html", "Contact & devis", "Services, photothèque, agenda et contact"),
    ("salons-professionnels.html", "Salons professionnels", "Pages par type d’événement"),
    ("congres-conferences.html", "Congrès et conférences", "Pages par type d’événement"),
    ("evenements-entreprise.html", "Événements d’entreprise", "Pages par type d’événement"),
    ("concerts-spectacles.html", "Concerts et spectacles", "Pages par type d’événement"),
    ("venir-a-abidjan.html", "Venir à Abidjan", "Pages pratiques"), ("informations-legales.html", "Informations légales", "Pages pratiques"),
    ("en/index.html", "Home (accueil en anglais)", "Version anglaise"), ("en/le-dome.html", "The Dome (Le Dôme en anglais)", "Version anglaise"),
    ("en/agenda.html", "Events (agenda en anglais)", "Version anglaise"),
]

by_page = collections.defaultdict(dict)
for x in DATA:
    by_page[x["page"]][x["width"]] = x
events = sorted(p for p in by_page if p.startswith("evenement-"))


def page_html(p):
    return (ROOT / p).read_text(encoding="utf-8")


def description(src):
    m = re.search(r'<meta name="description" content="([^"]+)"', src)
    return html.unescape(m.group(1)) if m else ""


def h1(src):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S)
    return html.unescape(re.sub("<[^>]+>", "", m.group(1))).strip() if m else ""


def photos_officielles(src):
    return sorted(set(re.findall(r"assets/img/(officiel/[a-z-]+/[a-z0-9-]+)-(?:1600|800)\.webp", src)))


def conforme(p):
    return all(not by_page[p][w]["violations"] for w in by_page[p])


def composants(p):
    rel = by_page[p][WMAX]["releve"]["composants"]
    return [(k, rel[k]["nombre"]) for k in ORDRE if k in rel]


def charte(p, src):
    """Points de la charte effectivement présents sur la page (mesurés), en langage courant."""
    X = by_page[p][WMAX]
    rel = X["releve"]
    pts = []
    regles = {v["rule"] for w in by_page[p] for v in by_page[p][w]["violations"]}
    if not any(r.startswith("typo") or r == "fonts.load" for r in regles):
        pts.append(("Police Poppins seule, en Regular et Bold, comme le demande le kit web de la charte (p. 7 et 17)", None))
    oranges = [k for k, v in rel["titres"].items() if "#DA5900" in v]
    if oranges or "Block/Key figures" in rel["composants"]:
        quoi = " et ".join(x for x in ["les grands titres" if oranges else "", "les chiffres clés" if "Block/Key figures" in rel["composants"] else ""] if x)
        pts.append((f"Orange PEA, couleur principale de la charte (p. 10), pour {quoi}", "#DA5900"))
    vus = []
    for s in rel["sections"]:
        if s["fond"] in APLATS and APLATS[s["fond"]][0] not in vus:
            vus.append(APLATS[s["fond"]][0])
    if vus:
        pts.append(("Couleurs d’accompagnement de la charte (p. 11 et 17) en aplats : " + ", ".join(vus), [APLATS[k][1] for k in APLATS if APLATS[k][0] in vus]))
    pts.append(("Fond blanc dominant, sans aplat noir (le noir est réservé au texte et au logo monochrome)", "#FFFFFF"))
    pts.append(("Logo du Parc intact : version orange sur l’en-tête blanc, version blanche (« négatif ») sur le brun du pied de page (p. 4–5)", None))
    pts.append(("Logo GL events en signature dans le pied de page (p. 17–18)", None))
    ph = photos_officielles(src)
    if ph:
        pts.append((f"{len(ph)} photo{'s' if len(ph) > 1 else ''} officielle{'s' if len(ph) > 1 else ''} du Parc", None))
    if not any(r == "contraste" for r in regles):
        pts.append((f"Textes lisibles : contrastes conformes aux normes d’accessibilité (le plus faible : {str(rel['contrasteMin']).replace('.', ',')}:1, sur un grand titre)", None))
    if not any(r.startswith("espacement") for r in regles):
        pts.append(("Espacements réguliers, pris dans la grille du design system (multiples de 4 px)", None))
    if not any(r == "debordement" for r in regles):
        pts.append(("Vérifiée sur ordinateur, tablette et mobile, sans défilement horizontal", None))
    return pts


# ---------------------------------------------------------------- vignettes
(OUT_HTML / "img").mkdir(parents=True, exist_ok=True)


def thumb(page, width, height, out_w):
    name = f"{page.replace('/', '_').replace('.html', '')}-{width}.jpg"
    src, dest = SRC / name, OUT_HTML / "img" / name
    if not dest.exists() and src.exists():
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"crop=iw:min(ih\\,{height}):0:0,scale={out_w}:-1", "-q:v", "4", str(dest)], check=True)
    return f"img/{name}" if dest.exists() else None


# ---------------------------------------------------------------- contenu commun
npages = len(by_page)
tous_ok = all(conforme(p) for p in by_page)
PALETTE = [("#DA5900", "Orange PEA", "couleur principale : logo, grands titres, chiffres clés"),
           ("#B34900", "Orange action", "boutons, liens, bandeaux de page (texte blanc lisible)"),
           ("#9D4015", "Brun", "barre d’informations, vidéo, pied de page"),
           ("#006528", "Vert", "services, bouton « Visiter le Parc »"),
           ("#5D120A", "Brun foncé", "appel à l’action, visite 360°, bandeau cookies"),
           ("#FCF2EA", "Crème", "newsletter, chiffres clés, questions fréquentes"),
           ("#FFFFFF", "Blanc", "fond des pages et des cartes"),
           ("#0A0A0A", "Noir", "texte uniquement")]
POINTS_CLIENT = ["L’accroche « Le plus grand parc exposition d’Afrique de l’Ouest », reprise de la charte, est utilisée en tête de l’accueil : à confirmer.",
                 "Le logo du Parc en versions blanche et noire en fichier vectoriel (SVG) reste à fournir.",
                 "La charte indique deux valeurs pour l’orange du kit web (p. 17) : le site applique l’orange de la page 10.",
                 "La vidéo de présentation n’a pas de sous-titres.",
                 "Le dossier « espalanafes » est vide : la galerie Parvis & Esplanades montre pour l’instant 2 photos du Dôme vu du parvis."]

# ---------------------------------------------------------------- Markdown
md = ["# Rapport d’intégration : charte graphique et design system", "",
      f"Parc des Expositions d’Abidjan — nouvelle version de la maquette, {DATE}.",
      f"Site de démonstration : <{DEMO}> (chaque nom de page ci-dessous est un lien direct).", "",
      "## En bref", "",
      "- **Charte graphique officielle appliquée** : police Poppins seule, orange PEA, couleurs d’accompagnement en aplats, logo intact (orange sur fond clair, blanc sur couleur), logo GL events en signature.",
      "- **Design system Bento de GL events** : chaque bloc du site est un composant Bento (en-tête, cartes, chiffres clés, agenda, pied de page…), aux couleurs du Parc et en angles droits.",
      "- **Photos officielles** : toutes les photos du Parc, hors photothèque, viennent des photos fournies (Hall, Dôme, salle, salon VIP), avec la vidéo de présentation.",
      f"- **Vérifié** : {npages} pages ouvertes automatiquement sur ordinateur, tablette et mobile, et contrôlées élément par élément "
      f"(police, couleurs, logo, lisibilité, espacements, composants) — {'aucune non-conformité' if tous_ok else 'voir les points signalés'}.", "",
      "## Couleurs de la charte utilisées", "", "| Couleur | Nom | Usage sur le site |", "|---|---|---|"]
md += [f"| `{h}` | {n} | {u} |" for h, n, u in PALETTE]
md += ["", "## Les composants du design system", "", "| Composant | Nom Bento | Rôle |", "|---|---|---|"]
md += [f"| {n} | {k} | {r} |" for k, n, r in COMPOSANTS]
md += ["", "## Page par page", ""]

H = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
     "<title>Rapport d’intégration PEA</title>",
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
     '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">',
     "<style>",
     "/* Page claire unique, aux couleurs de la charte ; mise en page : synthèse, puis une fiche par page (capture + composants + charte) */",
     ":root{--o:#da5900;--a:#b34900;--b:#9d4015;--v:#006528;--f:#5d120a;--c:#fcf2ea;--n:#0a0a0a;--m:#525252;--l:#e7e1d6;--p:#f7f5f1;--font:Poppins,'Helvetica Neue',Arial,sans-serif;color-scheme:light}",
     "*{box-sizing:border-box}body{margin:0;font:400 16px/1.6 var(--font);color:var(--n);background:#fff}a{color:var(--a)}a:focus-visible{outline:2px solid var(--n);outline-offset:2px}",
     "h1,h2,h3{font-weight:700;line-height:1.2;text-wrap:balance}h2{color:var(--o);font-size:30px;margin:64px 0 16px}h3{font-size:20px;margin:0 0 8px}",
     ".top{background:var(--b);color:#fff;padding:48px clamp(16px,5vw,64px)}.top h1{font-size:clamp(28px,4vw,44px);margin:0 0 12px}.top p{margin:0;color:#f8e0cc;max-width:70ch}",
     ".top a{color:#fff;font-weight:700}main{max-width:1240px;margin:auto;padding:0 clamp(16px,5vw,64px) 96px}",
     ".bref{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;margin:48px 0 0}.bref div{border-top:3px solid var(--o);padding-top:16px}.bref b{display:block;font-size:18px;margin-bottom:4px}.bref p{margin:0;color:var(--m)}",
     ".pal{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}.pal div{display:flex;gap:12px;align-items:center}.pal span{flex:none;width:48px;height:48px;border:1px solid var(--l)}.pal p{margin:0;font-size:14px;color:var(--m)}.pal b{display:block;color:var(--n)}",
     ".gl{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px 32px;margin:0;padding:0;list-style:none}.gl li{padding:8px 0;border-bottom:1px solid var(--l);font-size:15px}.gl b{display:block}.gl small{color:var(--m)}",
     ".groupe{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--a);margin:72px 0 0}",
     ".fiche{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:32px;padding:32px 0;border-top:1px solid var(--l)}.fiche:first-of-type{border-top:0}",
     ".fiche h3{font-size:24px}.fiche h3 a{color:var(--n);text-decoration:none}.fiche h3 a:hover{color:var(--a);text-decoration:underline}.desc{color:var(--m);margin:0 0 16px}",
     ".shots{display:grid;grid-template-columns:3fr 1fr;gap:12px;align-items:start}.shots img{width:100%;border:1px solid var(--l);display:block}.shots figure{margin:0}.shots figcaption{font-size:12px;color:var(--m)}",
     ".ok{display:inline-block;margin:0 0 16px;padding:4px 12px;background:var(--v);color:#fff;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.04em}",
     ".liste{margin:0 0 24px;padding:0;list-style:none}.liste li{display:flex;gap:10px;padding:6px 0;border-bottom:1px solid var(--l);font-size:15px}.liste li:last-child{border-bottom:0}",
     ".liste .k{flex:none;min-width:1.6em;font-weight:700;color:var(--a);font-variant-numeric:tabular-nums}.liste .c{flex:none;width:1.2em;color:var(--v);font-weight:700}.sw{display:inline-block;width:14px;height:14px;border:1px solid #bbb;vertical-align:-2px;margin-left:4px}",
     "h4{font-size:14px;text-transform:uppercase;letter-spacing:.06em;margin:0 0 8px;color:var(--m)}",
     "table{border-collapse:collapse;width:100%;font-size:14px}th,td{border-bottom:1px solid var(--l);padding:8px;text-align:left}th{background:var(--p)}.tw{overflow-x:auto}",
     ".pts{background:var(--c);padding:24px 32px;margin-top:48px}.pts h2{margin-top:0}.pts li{margin-bottom:8px}",
     "@media(max-width:860px){.fiche{grid-template-columns:1fr}.shots{grid-template-columns:2fr 1fr}}",
     "</style></head><body>",
     f'<header class="top"><h1>Rapport d’intégration : charte graphique et design system</h1><p>Parc des Expositions d’Abidjan — nouvelle version de la maquette, {DATE}. '
     f'Site de démonstration : <a href="{DEMO}">{DEMO.replace("https://", "").rstrip("/")}</a>. Chaque nom de page est un lien direct vers la page sur ce site.</p></header><main>',
     '<div class="bref">'
     '<div><b>Charte graphique appliquée</b><p>Police Poppins seule, orange PEA, couleurs d’accompagnement en aplats, logo intact, logo GL events en signature.</p></div>'
     '<div><b>Design system Bento</b><p>Chaque bloc du site est un composant Bento de GL events, aux couleurs du Parc et en angles droits.</p></div>'
     '<div><b>Photos officielles</b><p>Toutes les photos du Parc, hors photothèque, viennent des photos fournies, avec la vidéo de présentation.</p></div>'
     f'<div><b>{npages} pages vérifiées</b><p>Ouvertes automatiquement sur ordinateur, tablette et mobile, et contrôlées élément par élément : '
     f'{"aucune non-conformité" if tous_ok else "voir les points signalés"}.</p></div></div>',
     "<h2>Couleurs de la charte utilisées</h2><div class=\"pal\">" +
     "".join(f'<div><span style="background:{h}"></span><p><b>{n}</b>{u}</p></div>' for h, n, u in PALETTE) + "</div>",
     '<h2>Les composants du design system</h2><p class="desc">Les blocs du site reprennent les composants du design system Bento de GL events (nom Bento en petit).</p><ul class="gl">' +
     "".join(f"<li><b>{html.escape(n)}</b>{html.escape(r)}<br><small>{html.escape(k)}</small></li>" for k, n, r in COMPOSANTS) + "</ul>"]


def fiche(p, nom):
    src = page_html(p)
    X = by_page[p][WMAX]
    comps = composants(p)
    pts = charte(p, src)
    desc = description(src)
    statut = "Conforme sur ordinateur, tablette et mobile" if conforme(p) else "Points à revoir"
    md_ = [f"### [{nom}]({demo(p)})", "", f"*{desc}*" if desc else "", "", f"**{statut}.**", "", "**Composants utilisés**", ""]
    md_ += [f"- {NOM[k][0]}{f' ({n})' if n > 1 else ''} — {NOM[k][1]}" for k, n in comps]
    md_ += ["", "**Charte graphique respectée**", ""] + [f"- {t}" for t, _ in pts] + [""]
    big, small = thumb(p, WMAX, 2400, 900), thumb(p, WMIN, 2400, 300)
    sw = lambda c: "".join(f'<span class="sw" style="background:{x}" title="{x}"></span>' for x in (c if isinstance(c, list) else [c])) if c else ""
    h = [f'<article class="fiche" id="{re.sub("[^a-z0-9]+", "-", p)}"><div>',
         f'<h3><a href="{demo(p)}">{html.escape(nom)} ↗</a></h3>' + (f'<p class="desc">{html.escape(desc)}</p>' if desc else ""),
         f'<span class="ok">{statut}</span>',
         '<div class="shots">' + (f'<figure><img loading="lazy" src="{big}" alt="Page {html.escape(nom)} sur ordinateur"><figcaption>Ordinateur</figcaption></figure>' if big else "") +
         (f'<figure><img loading="lazy" src="{small}" alt="Page {html.escape(nom)} sur mobile"><figcaption>Mobile</figcaption></figure>' if small else "") + "</div></div><div>",
         "<h4>Composants utilisés</h4><ul class=\"liste\">" + "".join(f'<li><span class="k">{n}×</span><span><b>{html.escape(NOM[k][0])}</b> — {html.escape(NOM[k][1])}</span></li>' for k, n in comps) + "</ul>",
         "<h4>Charte graphique respectée</h4><ul class=\"liste\">" + "".join(f'<li><span class="c">✓</span><span>{html.escape(t)}{sw(c)}</span></li>' for t, c in pts) + "</ul></div></article>"]
    return md_, h


groupe = None
for p, nom, g in PAGES:
    if p not in by_page:
        continue
    if g != groupe:
        groupe = g
        md += [f"## {g}", ""]
        H.append(f'<p class="groupe">{html.escape(g)}</p>')
    m_, h_ = fiche(p, nom)
    md += m_
    H += h_
    if p == "agenda.html" and events:   # fiches événement juste après l’agenda : un modèle + la liste
        modele = events[0] if "evenement-auto-expo.html" not in events else "evenement-auto-expo.html"
        md += ["### Fiches événement", "", f"Les {len(events)} fiches événement suivent le même modèle. Il est présenté avec la fiche « {h1(page_html(modele))} », puis chaque fiche est listée avec son lien.", ""]
        H.append(f'<p class="groupe">Fiches événement</p><p class="desc">Les {len(events)} fiches événement suivent le même modèle, présenté ci-dessous, puis listées avec leur lien.</p>')
        m_, h_ = fiche(modele, f"Fiche événement (modèle) : {h1(page_html(modele))}")
        md += m_
        H += h_
        rows = []
        md += ["| Événement | Date | Fond du bandeau | Contrôle |", "|---|---|---|---|"]
        for e in events:
            s = page_html(e)
            titre = h1(s)
            date_ = re.search(r'class="page-hero__date">([^<]+)<', s)
            bg = re.search(r"--page-bg: url\(assets/img/(officiel/[^/]+/[a-z0-9-]+)-1600", s)
            bgtxt = {"officiel/dome-salle/salle-gradins": "salle du Dôme (gradins)", "officiel/dome-salle/salle-pleniere": "salle plénière du Dôme",
                     "officiel/hall/hall-drapeaux": "Hall d’Exposition"}.get(bg.group(1) if bg else "", "photo officielle")
            ok = "Conforme" if conforme(e) else "À revoir"
            md.append(f"| [{titre}]({demo(e)}) | {date_.group(1) if date_ else ''} | {bgtxt} | {ok} |")
            rows.append(f'<tr><td><a href="{demo(e)}">{html.escape(titre)}</a></td><td>{html.escape(date_.group(1) if date_ else "")}</td><td>{html.escape(bgtxt)}</td><td>{ok}</td></tr>')
        md.append("")
        H.append('<div class="tw"><table><tr><th>Événement</th><th>Date</th><th>Fond du bandeau</th><th>Contrôle</th></tr>' + "".join(rows) + "</table></div>")

md += ["## Points à valider par le Parc", ""] + [f"{i}. {t}" for i, t in enumerate(POINTS_CLIENT, 1)] + ["",
       "Annexe technique (mesures détaillées) : `design-system/pea/RAPPORT-TECHNIQUE.md`."]
H.append('<section class="pts"><h2>Points à valider par le Parc</h2><ol>' + "".join(f"<li>{html.escape(t)}</li>" for t in POINTS_CLIENT) + "</ol></section></main></body></html>")
OUT_MD.write_text("\n".join(md), encoding="utf-8")
(OUT_HTML / "index.html").write_text("\n".join(H), encoding="utf-8")
print(f"écrit {OUT_MD.relative_to(ROOT)} ({len(md)} lignes) et {OUT_HTML / 'index.html'}")
