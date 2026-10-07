#!/usr/bin/env python3
"""Génère toutes les pages de la maquette (FR à la racine, EN dans en/).

Usage : python3 tools/pages/generer.py
Prérequis : images WebP produites par tools/optimiser-images.py, dictionnaire tools/i18n/en.json, ffmpeg et sips (macOS).
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
HEAD_SRC = pathlib.Path(__file__).with_name("base.py").read_text(encoding="utf-8")
# Réutilise les constantes ARROW / ARCH / NAV / FONTS / head() du générateur initial
exec(HEAD_SRC[:HEAD_SRC.index("CUR = ")])

WA_URL = "https://wa.me/2252721710997?text=Bonjour%2C%20je%20souhaite%20des%20informations%20sur%20le%20Parc%20des%20Expositions%20d%E2%80%99Abidjan."
WA_ICON = ('<svg class="i i--wa" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
           '<path d="M12 3.2a8.8 8.8 0 0 0-7.6 13.2L3.2 20.8l4.5-1.2A8.8 8.8 0 1 0 12 3.2z"/>'
           '<path class="i--wa-handset" d="M9.1 7.6c-.3 0-.7.1-.9.5-.4.6-.6 1.4-.3 2.3.6 1.9 2.5 4 4.6 4.8.9.3 1.7.2 2.3-.2.4-.3.6-.7.5-1l-.2-.5-1.6-.8c-.3-.1-.5 0-.7.2l-.5.6c-1-.4-2-1.4-2.4-2.4l.6-.5c.2-.2.3-.4.2-.7l-.7-1.6c-.1-.3-.4-.4-.6-.4z"/></svg>')
TEL = f'<a class="wa-link" href="{WA_URL}" target="_blank" rel="noopener" aria-label="WhatsApp : +225 27 21 71 09 97 (nouvel onglet)">{WA_ICON}+225 27 21 71 09 97</a>'
MAPS_PLACE = ("https://www.google.com/maps/place/Abidjan+Exhibition+Center/@5.2634735,-3.9491417,17z/"
              "data=!3m1!4b1!4m6!3m5!1s0xfc1ef58a482d019:0x8268f3aea9d9066d!8m2!3d5.2634735!4d-3.9465668!16s%2Fg%2F11h9jwm292")
SECTION_OF = {"hall-exposition.html": "nos-espaces.html", "le-dome.html": "nos-espaces.html", "parvis-esplanades.html": "nos-espaces.html", "visite-virtuelle.html": "nos-espaces.html",
              "fiche-evenement.html": "agenda.html"}


def note(original):
    """Texte d’origine du cahier des charges, conservé pour le développeur."""
    return f"<!-- Note de maquette (texte d’origine) : {original} -->"


def header(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else (' aria-current="true"' if SECTION_OF.get(active) == href else "")
        items.append(f'      <li><a href="{href}"{cur}>{label}</a></li>')
    cta_cur = ' aria-current="page"' if active == "contact-devis.html" else ""
    return f"""<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="utility utility--overlay{' utility--on-orange' if active in PAGE_BG else ''}">
  <div class="wrap utility__inner">
    {TEL.replace('class="wa-link"', 'class="wa-link utility__tel"')}
    <div class="utility__end">
    <nav class="lang-switch" aria-label="Langue"><a href="__FR__" hreflang="fr" lang="fr" aria-current="true">FR</a><a href="__EN__" hreflang="en" lang="en">EN</a></nav>
    <ul class="social" role="list" aria-label="Réseaux sociaux">
      <li><a href="https://www.instagram.com/parcdesexpositionsabidjan/" target="_blank" rel="noopener" aria-label="Instagram du Parc des Expositions (nouvel onglet)"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__ig"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" class="social__dot"/></svg></a></li>
      <li><a href="https://www.facebook.com/profile.php?id=61572597774113" target="_blank" rel="noopener" aria-label="Facebook du Parc des Expositions (nouvel onglet)"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__fb"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.9v3h2.6V21z"/></svg></a></li>
      <li><a href="https://www.linkedin.com/company/parc-des-expositions-d-abidjan/" target="_blank" rel="noopener" aria-label="LinkedIn du Parc des Expositions (nouvel onglet)"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__fb"><path d="M4.6 9.2h3.1v10.3H4.6zM6.1 4.3a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6zM9.9 9.2h3v1.4c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.7 2 3.7 4.7v5.8h-3.1v-5.1c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7v5.2H9.9z"/></svg></a></li>
    </ul>
    </div>
  </div>
</div>
<header class="topbar topbar--overlay{' topbar--on-orange' if active in PAGE_BG else ''}">
  <div class="wrap topbar__inner">
    <a class="brand" href="index.html"><img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan — accueil" width="394" height="210"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-principale"><span class="menu-toggle__bars" aria-hidden="true"></span>Menu</button>
    <nav class="nav" id="nav-principale" aria-label="Navigation principale">
      <ul>
{chr(10).join(items)}
      </ul>
      <ul class="social social--menu" role="list" aria-label="Réseaux sociaux">
        <li><a href="{IG_URL}" target="_blank" rel="noopener" aria-label="Instagram du Parc des Expositions (nouvel onglet)">{IG_ICON}</a></li>
        <li><a href="{FB_URL}" target="_blank" rel="noopener" aria-label="Facebook du Parc des Expositions (nouvel onglet)">{FB_ICON}</a></li>
        <li><a href="{LI_URL}" target="_blank" rel="noopener" aria-label="LinkedIn du Parc des Expositions (nouvel onglet)">{LI_ICON}</a></li>
      </ul>
    </nav>
    <a class="btn btn--primary topbar__cta" href="contact-devis.html"{cta_cur}><span><span class="hide-sm">Demander un </span>devis</span></a>
  </div>
</header>
<main class="page" id="contenu" tabindex="-1">"""


FOOTER = f"""</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <img src="assets/logo-pea.webp" alt="" width="394" height="210" loading="lazy">
      <p><b>Parc des Expositions d’Abidjan</b><br>Boulevard de l’aéroport · Abidjan · Côte d’Ivoire<br>{TEL}</p>
    </div>
    <nav class="footer__nav" aria-label="Liens du pied de page">
      <ul role="list">
        <li><a href="nos-espaces.html">Espaces</a></li>
        <li><a href="nos-services.html">Services</a></li>
        <li><a href="qui-sommes-nous.html#destination">Destination</a></li>
        <li><a href="qui-sommes-nous.html#expertise">Expertise</a></li>
        <li class="footer__lang"><a href="__FR__" hreflang="fr" lang="fr" aria-current="true">FR</a> / <a href="__EN__" hreflang="en" lang="en">EN</a></li>
      </ul>
    </nav>
    <a class="footer__partner" href="https://www.gl-events.com/" target="_blank" rel="noopener" aria-label="GL events, expertise internationale (nouvel onglet)">
      <span class="footer__partner-logo"><img src="assets/logo-gl-events.png" alt="GL events" width="225" height="225" loading="lazy"></span>
      <span class="footer__partner-text">Expertise internationale</span>
    </a>
    <nav class="footer__legal" aria-label="Informations légales">
      <ul role="list">
        <li><a href="informations-legales.html#mentions-legales">Mentions légales</a></li>
        <li><a href="informations-legales.html#cookies">Politique cookies</a></li>
        <li><a href="informations-legales.html#confidentialite">Politique de confidentialité</a></li>
        <li><a href="informations-legales.html#cgu">CGU</a></li>
        <li><a href="informations-legales.html#ethique">Éthique et conformité</a></li>
        <li><button type="button" class="footer__cookies" data-consent-open>Gérer les cookies</button></li>
      </ul>
    </nav>
  </div>
</footer>
<a class="to-top" href="#contenu" aria-label="Retour en haut de page"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 19V5M6 11l6-6 6 6"/></svg></a>
<section class="cookie-banner" id="cookie-consent" aria-labelledby="consent-title" hidden>
  <div class="wrap consent__inner">
    <div class="consent__text">
      <h2 class="consent__title" id="consent-title">Cookies et contenus tiers</h2>
      <p>Ce site mémorise uniquement votre choix. Avec votre accord, la carte Google Maps, le fil Facebook et la visite virtuelle Matterport sont chargés et peuvent déposer leurs propres cookies. <a href="informations-legales.html#cookies">En savoir plus</a></p>
    </div>
    <div class="consent__actions">
      <button class="btn btn--secondary" type="button" data-consent="refused">Tout refuser</button>
      <button class="btn btn--secondary" type="button" data-consent="accepted">Tout accepter</button>
    </div>
  </div>
</section>
</body>
</html>
"""


def crumbs(*parts, ink=False):
    lis = []
    for i, (label, href) in enumerate(parts):
        if i == len(parts) - 1:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
        elif href:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            lis.append(f'<li><span>{label}</span></li>')
    cls = "breadcrumbs breadcrumbs--ink" if ink else "breadcrumbs"
    return f'<nav class="{cls}" aria-label="Fil d’Ariane"><ol role="list">{"".join(lis)}</ol></nav>'


def slug(t):
    t = t.lower()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("ô", "o"), ("’", ""), ("'", "")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def filters(label, items, target, key, row_label=None):
    """Groupe de filtres : « Tous » (valeur vide) actif par défaut."""
    btns = "".join(
        f'<button class="chip" type="button" aria-pressed="{"true" if i == 0 else "false"}" data-value="{"" if t == "Tous" else slug(t)}">{t}</button>'
        for i, t in enumerate(items)
    )
    group = f'<div class="filters" role="group" aria-label="{label}" data-filters="{target}" data-key="{key}">{btns}</div>'
    if row_label:
        return f'<div class="filter-row"><span class="filter-row__label" aria-hidden="true">{row_label}</span>{group}</div>'
    return group


def page_hero(crumb, eyebrow, h1, lead, extra="", compact=False, lead_note="", media=""):
    cls = ("page-hero page-hero--compact" if compact else "page-hero") + (" page-hero--media" if media else "")
    return f"""
<section class="{cls}">
  <div class="wrap">
    {crumb}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    {lead_note}
    <p class="lead">{lead}</p>{extra}{media}
  </div>
</section>"""


import functools
import subprocess


@functools.lru_cache(None)
def dims(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(ROOT / path)], capture_output=True, text=True).stdout
    return int(re.search(r"pixelWidth:\s*(\d+)", out).group(1)), int(re.search(r"pixelHeight:\s*(\d+)", out).group(1))


def img(name, alt="", sizes="100vw", cls="", lazy=True, priority=False):
    """Image WebP produite par tools/optimiser-images.py (deux largeurs quand elles existent)."""
    large, small = f"assets/img/{name}-1600.webp", f"assets/img/{name}-800.webp"
    if (ROOT / large).exists():
        src, srcset = large, f' srcset="{small} {dims(small)[0]}w, {large} {dims(large)[0]}w" sizes="{sizes}"'
    else:
        src, srcset = small, ""
    w, h = dims(src)
    load = ' fetchpriority="high"' if priority else (' loading="lazy" decoding="async"' if lazy else "")
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{src}"{srcset} alt="{alt}" width="{w}" height="{h}"{load}>'


import collections
import colorsys


def _lum(rgb):
    f = lambda x: (x / 255) / 12.92 if x / 255 <= .03928 else ((x / 255 + .055) / 1.055) ** 2.4
    return .2126 * f(rgb[0]) + .7152 * f(rgb[1]) + .0722 * f(rgb[2])


@functools.lru_cache(None)
def slide_accent(name):
    """Couleur des boutons pour une image du diaporama : teinte dominante de l'image (hors noirs, blancs et gris),
    portée à la luminosité la plus haute qui garde un contraste >= 4,6:1 avec le texte blanc. Renvoie (normal, survol)."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(ROOT / f"assets/img/{name}-800.webp"), "-vf", "scale=48:48",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    buckets = collections.defaultdict(list)
    for i in range(0, len(raw), 3):
        r, g, b = raw[i], raw[i + 1], raw[i + 2]
        _, l, sat = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        if .12 <= l <= .9 and sat >= .25:
            buckets[(r // 32, g // 32, b // 32)].append((r, g, b))
    best = max(buckets.values(), key=len)
    dom = tuple(sum(c[k] for c in best) // len(best) for k in range(3))
    h, _, sat = colorsys.rgb_to_hls(*(c / 255 for c in dom))
    if 255 / 360 <= h <= 330 / 360:  # pas de violet : ramené au bleu
        h = 225 / 360
    sat = max(sat, .6)
    lo, hi = 0.0, 1.0
    for _ in range(30):
        mid = (lo + hi) / 2
        c = tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, mid, sat))
        lo, hi = (mid, hi) if 1.05 / (_lum(c) + .05) >= 4.6 else (lo, mid)
    hexa = lambda light: "#%02x%02x%02x" % tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, light, sat))
    # Titre : teinte claire de la même couleur, la plus saturée possible avec un contraste >= 7:1 sur l'encre du héros
    ink = _lum((17, 18, 23))
    t_lo, t_hi = lo, 1.0
    for _ in range(30):
        mid = (t_lo + t_hi) / 2
        c = tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, mid, sat))
        t_lo, t_hi = (t_lo, mid) if (_lum(c) + .05) / (ink + .05) >= 7 else (mid, t_hi)
    return hexa(lo), hexa(max(lo - .08, .03)), hexa(t_hi)


SPACE_URL = {"A": "hall-exposition.html", "B": "le-dome.html", "C": "parvis-esplanades.html"}
SPACE_IMG = {"A": "espaces/hall/interieur", "B": "espaces/parvis/dome-sous-le-nuage", "C": "espaces/parvis/salon-plein-air-aerien"}


def space(letter, title, sub, media=None, ink=False, h="h3", usage=""):
    data = f' data-usage="{usage}"' if usage else ""
    return f"""      <a class="space{' space--ink' if ink else ''}" href="{SPACE_URL[letter]}"{data}>
        <div class="space__media">{img(SPACE_IMG[letter], sizes="(min-width: 768px) 50vw, 100vw")}</div>
        <div class="space__plate"><span class="space__letter" aria-hidden="true">{letter}</span><div><{h}{' class="t3"' if h == "h2" else ""}>{title}</{h}><p>{sub}</p></div>{ARROW}</div>
      </a>"""


def event(date, title, place, h="h3", types="", href="fiche-evenement.html", image=None):
    data = f' data-type="{types}"' if types else ""
    thumb = img(f"agenda/{image}") if image else ""
    return f"""      <a class="event" href="{href}"{data}>
        <div class="event__thumb">{thumb}</div>
        <div class="event__body"><span class="date">{date}</span><{h}{' class="t3"' if h == "h2" else ""}>{title}</{h}><p>{place}</p></div>
      </a>"""


def results(target, text, empty):
    return (f'<p class="filter-status" role="status" data-status-for="{target}">{text}</p>'
            f'<p class="empty" data-empty-for="{target}" hidden>{empty}</p>')


PLAN_PDF = "https://www.parcdesexpositionsabidjan.com/sites/default/files/assets/fichier/dervin/2025-02/plan-commercial-pea.pdf"
A = "Accueil", "index.html"
PAGES = {}

EXT = '<svg class="i i--ext" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/></svg>'
MOIS = ["", "janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
MOIS_LONG = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
# (slug officiel, titre, début JJ/MM, fin JJ/MM ou None, type affiché, filtres, lien de réservation ou None, libellé du lien)
EVENTS = [
    ("auto-expo", "Auto Expo", "08/10", "10/10", "Salon", "salons expositions", None, None),
    ("horeca-expo", "Horeca Expo", "08/10", "10/10", "Salon", "salons expositions", None, None),
    ("agrofood-plastprintpack-west-africa-0", "Agrofood & Plastprintpack West Africa", "08/10", "10/10", "Salon", "salons expositions", None, None),
    ("food-expo-0", "Food Expo", "08/10", "10/10", "Salon", "salons expositions", None, None),
    ("concert-tayc", "Concert TAYC", "11/10", None, "Concert", "concerts", None, None),
    ("brands-licensing-africa", "Brands Licensing Africa", "15/10", "16/10", "Salon", "salons", "https://www.brandslicensingafrica.com/", "Réserver"),
    ("salon-des-collectivites-territoriales", "Salon des collectivités territoriales", "15/10", "17/10", "Salon", "salons", None, None),
    ("abidjan-border-forum", "Abidjan Border Forum", "20/10", "22/10", "Forum", "congres conferences", None, None),
    ("concert-milo", "Concert Milo", "24/10", None, "Concert", "concerts", None, None),
    ("concert-40-ans-de-carriere-gadji-celi", "Concert 40 ans de carrière Gadji Celi", "31/10", None, "Concert", "concerts", None, None),
    ("concert-mary-sy", "Concert Mary Sy", "01/11", None, "Concert", "concerts", None, None),
    ("concert-ismael-isaac", "Concert Ismaël Isaac", "07/11", None, "Concert", "concerts", None, None),
    ("ceremonie-primud", "Cérémonie PRIMUD", "08/11", None, "Cérémonie", "", None, None),
    ("salon-ivoirien-des-ressources-extractives-energetiques", "Salon ivoirien des ressources extractives & énergétiques", "18/11", "22/11", "Salon", "salons", None, None),
    ("salon-equip-auto", "Salon Equip Auto", "26/11", "28/11", "Salon", "salons", None, None),
    ("concert-kiff-no-beat", "Concert Kiff No Beat", "28/11", None, "Concert", "concerts", None, None),
    ("concert-25-ans-de-carriere-de-moliere", "Concert 25 ans de carrière de Molière", "05/12", None, "Concert", "concerts", "https://concertmoliereparcdesexpositionsabidjan.nbh.ci/event/HWLO89", "Réserver"),
    ("concert-serge-beynaud-0", "Concert Serge Beynaud", "05/12", None, "Concert", "concerts", "https://tikerama.com/fr/evenements/b-en-concert-a-lesplanade-du-parc-des-expositions", "Réserver"),
    ("concert-ariel-sheney", "Concert Ariel Sheney", "12/12", None, "Concert", "concerts", None, None),
    ("foire-europe-afrique-dabidjan", "Foire Europe Afrique d’Abidjan", "16/12", "19/12", "Foire", "salons expositions", None, None),
]
YEAR = 2026
# Publications Instagram exportées (images/instagram) : code court de la publication -> description
IG_ITEMS = [
    ("DeBy3SlAVIs", "Affiche du Salon international de l’alimentation, de l’emballage et de l’HoReCa, du 8 au 10 octobre 2026"),
    ("Dd_xVHAlsvb", "Affiche des Journées foncières d’Abidjan, du 5 au 7 octobre 2026"),
    ("Dd7CplyFh-A", "Agenda d’octobre du Parc des Expositions d’Abidjan"),
    ("Ddo52rDjXNZ", "Affiche de l’Africa Space Expo, du 24 au 26 septembre 2026"),
    ("DdbcGUfD4bJ", "Affiche du spectacle Ramatoulaye 2 Tenues, samedi 19 septembre"),
    ("DdZggPXFXRa", "Pourquoi choisir Abidjan pour votre prochain événement ?"),
]
IG_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__ig"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" class="social__dot"/></svg>'
FB_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__fb"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.9v3h2.6V21z"/></svg>'
LI_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="social__fb"><path d="M4.6 9.2h3.1v10.3H4.6zM6.1 4.3a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6zM9.9 9.2h3v1.4c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.7 2 3.7 4.7v5.8h-3.1v-5.1c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7v5.2H9.9z"/></svg>'
IG_URL = "https://www.instagram.com/parcdesexpositionsabidjan/"
FB_URL = "https://www.facebook.com/profile.php?id=61572597774113"
LI_URL = "https://www.linkedin.com/company/parc-des-expositions-d-abidjan/"
FB_PLUGIN = ("https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Fprofile.php%3Fid%3D61572597774113"
             "&amp;tabs=timeline&amp;width=500&amp;height=620&amp;small_header=true&amp;adapt_container_width=true"
             "&amp;hide_cover=true&amp;show_facepile=false&amp;locale=fr_FR")
DETAILS = {
    "auto-expo": dict(desc="Le salon de l’industrie automobile réunit plus de 15 nations participantes et 900 acheteurs professionnels, avec des rencontres B2B et des panels sectoriels.", site="https://ivorycoastautoexpo.com/", fiche="fiche-evenement.html"),
    "horeca-expo": dict(desc="Le rendez-vous des marques internationales de l’hôtellerie, de la restauration et des cafés, avec des rencontres B2B avec des acheteurs qualifiés et des conférences professionnelles.", site="https://ivorycoasthorecaexpo.com/"),
    "agrofood-plastprintpack-west-africa-0": dict(desc="Plus de 150 exposants venus de 25 pays présentent leurs produits et solutions pour le marché ivoirien et ouest-africain. Troisième édition des salons Agrofood, Plastprintpack et Afrik’embal à Abidjan.", org="Fairtrade Messe"),
    "food-expo-0": dict(desc="Les acteurs de l’agroalimentaire, de l’agriculture et de l’emballage : plus de 150 marques, 15 pays participants, plus de 25 conférences et 5 200 visiteurs professionnels attendus.", site="https://ivorycoastfoodexpo.com/"),
    "concert-tayc": dict(desc="Une star du R&B se produit pour la première fois au Parc des Expositions d’Abidjan."),
    "brands-licensing-africa": dict(desc="La plateforme dédiée aux licences et au développement des marques en Afrique : 3 000 visiteurs professionnels et des marques de 20 pays attendus, des biens de consommation aux jouets, au divertissement, aux cosmétiques et à la mode."),
    "salon-des-collectivites-territoriales": dict(desc="Thème de l’édition : « Décentralisation renforcée : maîtriser les transferts de compétences pour des territoires plus efficaces et autonomes »."),
    "abidjan-border-forum": dict(desc="Forum panafricain des acteurs frontaliers, qui aborde les frontières africaines comme des espaces de dialogue et de coopération. Thème : « Les peuples aux frontières : culture, intégration et sécurité ».", org="Parc des Expositions d’Abidjan"),
    "concert-milo": dict(desc="Une soirée qui rassemble le public autour d’un message spirituel."),
    "concert-40-ans-de-carriere-gadji-celi": dict(desc="Le Parc célèbre les 40 ans de carrière de Gadji Celi, grande figure de la scène musicale ivoirienne."),
    "concert-mary-sy": dict(desc="Mary Sy en concert au Parc des Expositions d’Abidjan."),
    "concert-ismael-isaac": dict(desc="Un concert anniversaire pour les 40 ans de carrière d’une figure emblématique du reggae."),
    "ceremonie-primud": dict(desc="Une cérémonie de remise de prix qui honore les acteurs de la musique urbaine et du divertissement."),
    "salon-ivoirien-des-ressources-extractives-energetiques": dict(desc="Le premier salon à réunir les secteurs des mines, du pétrole et de l’énergie en Côte d’Ivoire."),
    "salon-equip-auto": dict(desc="Salon international de l’automobile, des mobilités et des véhicules industriels : véhicules particuliers, poids lourds, transport, engins agricoles et de travaux publics. Première édition : plus de 150 exposants et environ 10 000 visiteurs attendus.", org="EQUIP’AUTO SAS, avec Interlinks Auto"),
    "concert-kiff-no-beat": dict(desc="Le groupe Kiff No Beat en concert au Parc des Expositions d’Abidjan, une nouvelle étape de son histoire."),
    "concert-25-ans-de-carriere-de-moliere": dict(desc="Le chanteur zouglou Molière fête ses 25 ans de carrière sur scène."),
    "concert-serge-beynaud-0": dict(desc="Serge Beynaud en concert sur l’esplanade du Parc.", lieu="Esplanade du Parc"),
    "concert-ariel-sheney": dict(desc="Ariel Sheney fait son retour sur scène avec son premier concert au Parc des Expositions d’Abidjan."),
    "foire-europe-afrique-dabidjan": dict(desc="Le premier rendez-vous commercial et culturel entre l’Europe et l’Afrique, autour de l’agriculture, du tourisme, de l’artisanat et de l’immobilier."),
}


def dm(t):
    d, m = t.split("/")
    return int(d), int(m)


def when_long(start, end):
    d1, m1 = dm(start)
    if not end:
        return f"Le {'1er' if d1 == 1 else d1} {MOIS_LONG[m1]} {YEAR}"
    d2, m2 = dm(end)
    return f"Du {d1} au {d2} {MOIS_LONG[m2]} {YEAR}" if m1 == m2 else f"Du {d1} {MOIS_LONG[m1]} au {d2} {MOIS_LONG[m2]} {YEAR}"


def when_short(start, end):
    d1, m1 = dm(start)
    if not end:
        return f"{d1} {MOIS[m1]} {YEAR}"
    d2, m2 = dm(end)
    return f"{d1}–{d2} {MOIS[m2]} {YEAR}" if m1 == m2 else f"{d1} {MOIS[m1]} – {d2} {MOIS[m2]} {YEAR}"


def timeline():
    out, month = [], None
    for slug_, title, start, end, kind, tags, resa, resa_label in EVENTS:
        d1, m1 = dm(start)
        if m1 != month:
            month = m1
            out.append(f'      <li class="timeline__month" data-heading><h2 class="timeline__month-title">{MOIS_LONG[m1].capitalize()} {YEAR}</h2></li>')
        iso1 = f"{YEAR}-{m1:02d}-{d1:02d}"
        if end:
            d2, m2 = dm(end)
            iso2 = f"{YEAR}-{m2:02d}-{d2:02d}"
            rest = f"→ {d2} {MOIS[m2]}" if m2 == m1 else f"{MOIS[m1]} → {d2} {MOIS[m2]}"
        else:
            iso2 = iso1
            rest = MOIS[m1]
        det = DETAILS.get(slug_, {})
        facts = [("Date", when_long(start, end)), ("Lieu", det.get("lieu", "Parc des Expositions d’Abidjan"))]
        if det.get("org"):
            facts.append(("Organisateur", det["org"]))
        facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
        links = []
        if resa:
            links.append(f'<a class="btn btn--primary btn--sm" href="{resa}" target="_blank" rel="noopener" aria-label="{resa_label} : {title} (nouvel onglet)">{resa_label} {EXT}</a>')
        if det.get("site"):
            links.append(f'<a class="link-arrow" href="{det["site"]}" target="_blank" rel="noopener" aria-label="Site officiel : {title} (nouvel onglet)">Site officiel {EXT}</a>')
        if det.get("fiche"):
            links.append(f'<a class="link-arrow" href="{det["fiche"]}">Fiche complète {ARROW}</a>')
        reserve = links[0] if resa else ""
        out.append(f"""      <li class="tl-item" id="{slug_}" data-type="{tags}" data-start="{iso1}" data-end="{iso2}">
        <p class="tl-date"><time datetime="{iso1}" class="tl-date__day">{d1:02d}</time><span class="tl-date__rest">{rest}</span></p>
        <div class="tl-card">
          <div class="tl-card__media">{img(f"agenda/{slug_}")}</div>
          <p class="tl-card__type">{kind}<span class="tl-card__next" hidden> · Prochainement</span></p>
          <h3 class="tl-card__title">{title}</h3>
          <p class="tl-card__when">{when_long(start, end)}</p>
          <div class="tl-card__more" data-event-more>
            <p class="ev-desc">{det.get("desc", "")}</p>
            <dl class="ev-facts">{facts_html}</dl>
            <div class="ev-links">{"".join(links)}</div>
          </div>
          <div class="tl-card__actions"><button class="link-arrow" type="button" data-event-open aria-haspopup="dialog" aria-label="Détails : {title}">Détails {ARROW}</button></div>
        </div>
      </li>""")
    return "\n".join(out)


IG_POSTS = "".join(
    f'<li><a class="wall__post" href="https://www.instagram.com/p/{code}/" target="_blank" rel="noopener" aria-label="Instagram : {alt} (nouvel onglet)">{img(f"instagram/{code}", sizes="(min-width: 1024px) 12vw, 33vw")}</a></li>'
    for code, alt in IG_ITEMS)

# Diaporama de l'accueil : ordre d'affichage (images produites par tools/optimiser-images.py)
SLIDES = ["slider/dome-rendu", "slider/salon-vue-plongeante", "slider/concert-foule", "slider/percussions",
          "slider/concert-scene", "slider/salon-rencontres", "slider/spectacle-scene", "slider/journee-internationale"]
SLIDES_HTML = "\n".join(
    f'    <figure class="slider__slide{" is-active" if i == 0 else ""}" data-accent="{slide_accent(n)[0]}" data-accent-hover="{slide_accent(n)[1]}" data-accent-title="{slide_accent(n)[2]}">'
    f'{img(n, sizes="100vw", priority=i == 0, lazy=i != 0)}</figure>' for i, n in enumerate(SLIDES))
SLIDER_DOTS = "".join(
    f'<li><button type="button" class="slider__dot" data-slide="{i}" aria-label="Afficher l’image {i + 1} sur {len(SLIDES)}"'
    f'{" aria-current=" + chr(34) + "true" + chr(34) if i == 0 else ""}></button></li>' for i in range(len(SLIDES)))

LOGOS = [  # images/logos -> assets/img/logos (tools/optimiser-images.py)
    ("ardci", "ARDCI — Assemblée des Régions et Districts de Côte d’Ivoire"),
    ("uvicoci", "UVICOCI — Union des Villes et Communes de Côte d’Ivoire"),
    ("cnfci", "CNFCI — Commission Nationale des Frontières de la Côte d’Ivoire"),
    ("abidjan-border-forum", "Abidjan Border Forum"),  # logo blanc sur transparent -> tuile sombre
    ("sirexe", "SIREXE 2026 — African Mining, Oil, Gas and Energy Exhibition"),
    ("conseil-cafe-cacao", "Le Conseil du Café-Cacao"),
    ("gibtp", "GIBTP — Groupement Ivoirien du Bâtiment et des Travaux Publics"),
    ("sara-2025", "SARA 2025, 7e édition"),
    ("ordre-architectes", "Ordre des Architectes de Côte d’Ivoire"),
    ("sila", "SILA — Salon International du Livre d’Abidjan"),
]
LOGOS_SOMBRES = {"abidjan-border-forum"}
LOGO_ITEMS = "".join(f'<li class="logos__item{" logos__item--dark" if n in LOGOS_SOMBRES else ""}">{img("logos/" + n, a)}</li>' for n, a in LOGOS)
CHEV_L = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 5l7 7-7 7"/></svg>'

# ---------------------------------------------------------------- Accueil
PAGES["index.html"] = ("Accueil — Parc des Expositions d’Abidjan", f"""
<section class="hero hero--slider hero--under-header" data-slider style="--slide-accent: {slide_accent(SLIDES[0])[0]}; --slide-accent-hover: {slide_accent(SLIDES[0])[1]}; --slide-title: {slide_accent(SLIDES[0])[2]}">
  <div class="slider" aria-hidden="true">
{SLIDES_HTML}
  </div>
  <a class="scroll-cue" href="#decouvrir" aria-label="Aller à la section suivante"><span class="scroll-cue__mouse" aria-hidden="true"></span></a>
  <div class="slider__controls" role="group" aria-label="Diaporama">
    <button type="button" class="slider__toggle" aria-pressed="false" aria-label="Mettre le diaporama en pause"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-pause"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-play"><path d="M8 5v14l11-7z"/></svg></button>
    <ol class="slider__dots" role="list">{SLIDER_DOTS}</ol>
  </div>
  <div class="wrap hero__inner">
    {ARCH.format(cls="arch")}
    <p class="eyebrow">Abidjan · Côte d’Ivoire</p>
    <h1>Le lieu des grands rendez-vous.</h1>
    <p class="lead">Des espaces modulables, des services complets et une destination au cœur de l’Afrique de l’Ouest.</p>
    <div class="actions"><a class="btn btn--primary" href="nos-espaces.html">Découvrir nos espaces {ARROW}</a><a class="btn btn--secondary" href="contact-devis.html">Demander un devis</a></div>
  </div>
</section>

<section class="section" id="decouvrir">
  <div class="wrap">
    <div class="intro">
      <div><p class="eyebrow">Pourquoi le Parc des Expositions ?</p><h2>Un lieu conçu pour faire grandir les événements.</h2></div>
      {note("Le site doit répondre immédiatement à une question : pourquoi organiser son événement au Parc des Expositions d’Abidjan ? La réponse s’articule autour de quatre piliers : espaces, services, destination et expertise.")}
      <p>Pourquoi organiser votre événement au Parc des Expositions d’Abidjan ? Pour quatre raisons : des espaces à grande échelle, des services intégrés, une destination attractive et une expertise internationale.</p>
    </div>
    <ul class="figures figures--4 figures--interactive" role="list">
      <li class="figure"><strong><span class="sr-only">6 500 m²</span><span aria-hidden="true"><span data-count="6500">6 500</span> m²</span></strong>Hall d’exposition</li>
      <li class="figure"><strong><span class="sr-only">5 000 m²</span><span aria-hidden="true"><span data-count="5000">5 000</span> m²</span></strong>Le Dôme</li>
      <li class="figure"><strong><span class="sr-only">67 000 m²</span><span aria-hidden="true"><span data-count="67000">67 000</span> m²</span></strong>Parvis & esplanades</li>
      <li class="figure"><strong><span class="sr-only">360°</span><span aria-hidden="true"><span data-count="360">360</span>°</span></strong><a class="btn btn--secondary btn--sm" href="visite-virtuelle.html#visite">Visiter le Parc {ARROW}</a></li>
    </ul>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Nos espaces</p><h2>À chaque projet, son espace.</h2></div>
    <div class="spaces">
{space("A", "Hall d’Exposition", "Salons · expositions · corporate")}
{space("B", "Le Dôme", "Conventions · conférences · concerts", ink=True)}
{space("C", "Parvis & Esplanades", "Formats outdoor · grands publics")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media media--top">{img("pages/destination-abidjan", "Abidjan de nuit : le pont et la lagune illuminés", "(min-width: 1024px) 50vw, 100vw")}<span class="plaque">Abidjan, destination MICE</span></div>
    <div>
      <p class="eyebrow">Une destination</p>
      <h2>Votre événement commence à Abidjan.</h2>
      {note("Accessibilité, hôtellerie, vie économique et rayonnement régional : la destination devient un argument commercial à part entière.")}
      <p>Accessibilité, hôtellerie, vie économique et rayonnement régional : Abidjan offre à vos participants une destination à la hauteur de votre événement.</p>
      <a class="btn btn--secondary" href="qui-sommes-nous.html#destination">Découvrir la destination {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Agenda</p><h2>Prochainement au Parc</h2></div>
    <div class="agenda">
{event("8–10 oct. 2026", "Auto Expo", "Salon de l’industrie automobile", href="agenda.html#auto-expo", image="auto-expo")}
{event("11 oct. 2026", "Concert TAYC", "Concert", href="agenda.html#concert-tayc", image="concert-tayc")}
{event("15–16 oct. 2026", "Brands Licensing Africa", "Salon des licences de marques", href="agenda.html#brands-licensing-africa", image="brands-licensing-africa")}
    </div>
    <p class="section__more"><a class="link-arrow" href="agenda.html">Voir tout l’agenda {ARROW}</a></p>
  </div>
</section>


<!-- Note de maquette : le fil Facebook utilise le Page Plugin officiel de Meta. Instagram et LinkedIn n’offrent pas de fil intégrable sans jeton : en production, les alimenter via un agrégateur (Curator.io, Juicer, Walls.io…) ou via les API Meta Graph et LinkedIn depuis Drupal. -->
<section class="section section--white" aria-labelledby="mur-titre">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Actualités</p><h2 id="mur-titre">Le Parc en direct</h2></div>
    <div class="wall">
      <article class="wall__tile wall__tile--fb" aria-labelledby="mur-fb">
        <header class="wall__head">{FB_ICON}<h3 class="wall__name t3" id="mur-fb">Facebook</h3><a class="wall__handle" href="{FB_URL}" target="_blank" rel="noopener" aria-label="Suivre le Parc sur Facebook (nouvel onglet)">Suivre {EXT}</a></header>
        <div class="wall__embed" data-embed-src="{FB_PLUGIN}" data-embed-title="Publications Facebook du Parc des Expositions d’Abidjan">
          <div class="embed-facade">
            <p>Le fil Facebook est fourni par Meta, qui peut déposer des cookies.</p>
            <button class="btn btn--secondary" type="button" data-embed-load>Afficher les publications</button>
          </div>
        </div>
      </article>
      <article class="wall__tile wall__tile--ig" aria-labelledby="mur-ig">
        <header class="wall__head">{IG_ICON}<h3 class="wall__name t3" id="mur-ig">Instagram</h3><a class="wall__handle" href="{IG_URL}" target="_blank" rel="noopener" aria-label="Suivre parcdesexpositionsabidjan sur Instagram (nouvel onglet)">@parcdesexpositionsabidjan {EXT}</a></header>
        <ul class="wall__grid" role="list">{IG_POSTS}</ul>
      </article>
      <article class="wall__tile wall__tile--li" aria-labelledby="mur-li">
        <header class="wall__head">{LI_ICON}<h3 class="wall__name t3" id="mur-li">LinkedIn</h3></header>
        <p>Salons, partenariats et actualités professionnelles du Parc des Expositions d’Abidjan.</p>
        <a class="btn btn--secondary" href="{LI_URL}" target="_blank" rel="noopener" aria-label="Suivre le Parc sur LinkedIn (nouvel onglet)">Suivre sur LinkedIn {EXT}</a>
      </article>
      <article class="wall__tile wall__tile--next" aria-labelledby="mur-next">
        <p class="wall__kicker">Prochainement au Parc</p>
        <h3 class="t3" id="mur-next">Auto Expo</h3>
        <p class="wall__date">8–10 oct. 2026</p>
        <p>Le salon de l’industrie automobile : plus de 15 nations et 900 acheteurs professionnels.</p>
        <a class="link-arrow" href="agenda.html#auto-expo">Voir l’agenda {ARROW}</a>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta cta--photo">
      <div class="cta__img" aria-hidden="true"></div>
      <p class="eyebrow">Votre prochain événement</p>
      <h2>Parlez-nous de votre projet.</h2>
      {note("Un parcours simple pour transformer une visite en demande commerciale qualifiée.")}
      <p>Décrivez votre événement en quelques minutes : notre équipe commerciale vous recontacte avec une proposition adaptée.</p>
      <a class="btn btn--primary" href="contact-devis.html">Demander un devis {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="refs-title">
  <div class="wrap">
    <div class="logos-head">
      <div><p class="eyebrow">Références</p><h2 id="refs-title">Ils nous ont fait confiance</h2></div>
      <div class="logos-controls" role="group" aria-label="Défilement des logos">
        <button class="logos__btn" type="button" data-logos-prev aria-label="Logos précédents">{CHEV_L}</button>
        <button class="logos__btn logos__toggle" type="button" aria-pressed="false" aria-label="Mettre le défilement en pause"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-pause"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-play"><path d="M8 5v14l11-7z"/></svg></button>
        <button class="logos__btn" type="button" data-logos-next aria-label="Logos suivants">{CHEV_R}</button>
      </div>
    </div>
    <div class="logos" data-logos aria-roledescription="carrousel" aria-label="Logos des organisateurs">
      <ul class="logos__track" role="list">{LOGO_ITEMS}</ul>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Qui sommes-nous
LIGHTBOX = """
<dialog class="lightbox" id="lightbox" aria-label="Visionneuse de photos">
  <figure class="lightbox__figure"><img class="lightbox__img" src="data:," alt=""><figcaption class="lightbox__caption"></figcaption></figure>
  <p class="lightbox__count" aria-live="polite"></p>
  <button class="lightbox__btn lightbox__close" type="button" aria-label="Fermer la visionneuse"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  <button class="lightbox__btn lightbox__prev" type="button" aria-label="Photo précédente"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M15 5l-7 7 7 7"/></svg></button>
  <button class="lightbox__btn lightbox__next" type="button" aria-label="Photo suivante"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 5l7 7-7 7"/></svg></button>
</dialog>"""


def gallery_item(name, alt, sizes, extra="", lazy=True):
    large = f"assets/img/{name}-1600.webp"
    return f'<a class="gallery__item" href="{large}" data-lightbox-item data-caption="{alt}"{extra}>{img(name, alt, sizes, lazy=lazy)}</a>'


DESTINATION = [  # visuels de la série « destination » (légende incrustée reprise en texte alternatif)
    ("destination/infrastructures", "Une ville aux infrastructures modernes : vue aérienne d’Abidjan, du stade et du port"),
    ("destination/aerien", "Plus d’une vingtaine de compagnies aériennes desservent Abidjan : l’aéroport vu du ciel"),
    ("destination/hotellerie", "Une offre hôtelière variée : un hôtel du Plateau au crépuscule"),
    ("pages/destination-abidjan", "Une vie culturelle dynamique : Abidjan de nuit, le pont et la lagune illuminés"),
]
DESTINATION_ITEMS = "".join(gallery_item(n, a, "(min-width: 1024px) 25vw, 50vw") for n, a in DESTINATION)

PAGES["qui-sommes-nous.html"] = ("Qui sommes-nous ? — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Qui sommes-nous ?", None)), "Le Parc",
    "Un équipement majeur au service des grands événements.",
    "Salons, congrès, concerts : à Abidjan, le Parc accueille les grands rendez-vous professionnels et grand public d’Afrique de l’Ouest.",
    lead_note=note("Une présentation institutionnelle plus éditoriale, orientée vers la preuve, la destination et l’expertise.")) + f"""

<section class="section section--white">
  <div class="wrap split">
    <div class="media">{img("slider/journee-internationale", "Grand événement institutionnel dans le Dôme", "(min-width: 1024px) 50vw, 100vw")}</div>
    <div>
      <p class="eyebrow">Notre ambition</p>
      <h2>Faire d’Abidjan un point de rencontre régional.</h2>
      <p>Le Parc des Expositions d’Abidjan accueille salons, expositions, conventions, conférences, concerts et grands rendez-vous professionnels.</p>
      <ul class="figures figures--tight" role="list">
        <li class="figure"><strong>3</strong>grands univers d’espaces</li>
        <li class="figure figure--ink"><strong>GL events</strong>expertise internationale</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="destination">
  <div class="wrap">
  <div class="intro">
    <div><p class="eyebrow">Une destination</p><h2>Abidjan, ville d’affaires et d’expériences.</h2></div>
    {note("Cette section valorise l’accessibilité, l’hôtellerie, le dynamisme économique, culturel et touristique de la Côte d’Ivoire afin de soutenir la visibilité internationale du Parc.")}
    <p>Accessibilité, offre hôtelière, dynamisme économique, culturel et touristique : la Côte d’Ivoire réunit tout ce qu’il faut pour accueillir vos participants venus de la région et du monde entier.</p>
  </div>
    <div class="destination-grid block-gap" data-lightbox>{DESTINATION_ITEMS}</div>
  </div>
</section>

<section class="section section--ink" id="expertise">
  <div class="wrap">
    <p class="eyebrow">Expertise</p>
    <h2>Un savoir-faire événementiel international.</h2>
    {note("Bloc destiné à présenter le rôle de GL events, ses standards d’exploitation et sa capacité à accompagner les organisateurs.")}
    <p class="lead">Le Parc s’appuie sur l’expertise de GL events et ses standards d’exploitation pour accompagner les organisateurs à chaque étape, de la conception à l’accueil du public.</p>
  </div>
</section>
{LIGHTBOX}
""")

# ---------------------------------------------------------------- Nos espaces
PAGES["nos-espaces.html"] = ("Nos espaces — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Nos espaces", None)), "Espaces",
    "Des espaces à la hauteur de vos ambitions.",
    "Comparez nos espaces par capacité, usage et configuration, explorez-les en visite virtuelle et téléchargez leurs fiches techniques.",
    "\n    " + filters("Filtrer par usage", ["Tous", "Salon", "Congrès", "Conférence", "Convention", "Concert", "Corporate"], "espaces", "usage"),
    lead_note=note("Une entrée simple par capacité, usage et configuration, avec accès direct à la visite virtuelle et aux fiches techniques.")) + f"""

<section class="section section--white">
  <div class="wrap">
    {results("espaces", "3 espaces", "Aucun espace ne correspond à cet usage. Parlez-nous de votre projet : nous étudions chaque configuration.")}
    <!-- Usages par espace (déduits des légendes de l’accueil) : à confirmer et administrer dans Drupal -->
    <div class="spaces" id="espaces">
{space("A", "Hall d’Exposition", "6 500 m² · 17 m sous plafond", h="h2", usage="salon corporate")}
{space("B", "Le Dôme", "5 000 m² · 5 023 assis · 9 588 debout", ink=True, h="h2", usage="congres conference convention concert")}
{space("C", "Parvis & Esplanades", "67 000 m² d’espaces extérieurs", h="h2", usage="concert salon")}
    </div>
  </div>
</section>

<!-- Comparatif : données de la page officielle /fr/nos-espaces-services -->
<section class="section section--white" aria-labelledby="comparer">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Comparer</p><h2 id="comparer">Nos espaces en un coup d’œil</h2></div>
    <table class="compare">
      <caption class="sr-only">Comparatif des espaces : surface, hauteur, capacité, usages, documents et devis</caption>
      <thead><tr><th scope="col">Espace</th><th scope="col">Surface</th><th scope="col">Hauteur</th><th scope="col">Capacité</th><th scope="col">Usages</th><th scope="col">Documents</th><th scope="col"><span class="sr-only">Devis</span></th></tr></thead>
      <tbody>
        <tr><th scope="row"><a href="hall-exposition.html">Hall d’Exposition</a></th><td data-label="Surface">6 500 m²</td><td data-label="Hauteur">17 m</td><td data-label="Capacité">Divisible en 2 ou 3 espaces</td><td data-label="Usages">Salons, expositions, corporate</td><td data-label="Documents"><a href="assets/fiche-technique-hall-exposition.pdf" download>Fiche technique (PDF)</a></td><td><a class="btn btn--primary btn--sm" href="contact-devis.html?espace=hall#devis" aria-label="Demander un devis pour le Hall d’Exposition">Devis</a></td></tr>
        <tr><th scope="row"><a href="le-dome.html">Le Dôme</a></th><td data-label="Surface">5 000 m²</td><td data-label="Hauteur">Non communiquée</td><td data-label="Capacité">5 023 assis · 9 588 debout</td><td data-label="Usages">Conférences, institutionnel, salons, concerts</td><td data-label="Documents"><a href="{PLAN_PDF}" target="_blank" rel="noopener" aria-label="Plan du Parc, PDF (nouvel onglet)">Plan du Parc (PDF)</a></td><td><a class="btn btn--primary btn--sm" href="contact-devis.html?espace=dome#devis" aria-label="Demander un devis pour le Dôme">Devis</a></td></tr>
        <tr><th scope="row"><a href="parvis-esplanades.html">Parvis & Esplanades</a></th><td data-label="Surface">67 000 m²</td><td data-label="Hauteur">Plein air</td><td data-label="Capacité">Parvis 11 000 m² · 2 esplanades de 28 000 m²</td><td data-label="Usages">Expositions extérieures, formats outdoor</td><td data-label="Documents"><a href="{PLAN_PDF}" target="_blank" rel="noopener" aria-label="Plan du Parc, PDF (nouvel onglet)">Plan du Parc (PDF)</a></td><td><a class="btn btn--primary btn--sm" href="contact-devis.html?espace=parvis#devis" aria-label="Demander un devis pour le Parvis & Esplanades">Devis</a></td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Visite virtuelle</p>
      <h2>Explorez les espaces avant votre visite.</h2>
      {note("Un accès direct à la visite 360° depuis la page Espaces permet d’accélérer la qualification commerciale.")}
      <p>Parcourez le Parc en 360° pour imaginer votre configuration avant même de vous déplacer.</p>
      <a class="btn btn--secondary" href="visite-virtuelle.html#visite">Lancer la visite virtuelle {ARROW}</a>
    </div>
    <a class="media media--arch media--link" href="visite-virtuelle.html#visite" aria-label="Lancer la visite virtuelle"><span class="plaque">360°</span></a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta">
      <p class="eyebrow">Votre projet</p>
      <h2>Un espace vous intéresse ?</h2>
      <p>Indiquez l’espace, vos dates et votre jauge : notre équipe commerciale vous recontacte avec une proposition adaptée.</p>
      <a class="btn btn--primary" href="contact-devis.html#devis">Demander un devis {ARROW}</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Fiche espace
# Textes alternatifs des photos (assets/img/<groupe>/<nom>) ; une photo absente de cette table reçoit un texte générique
ALTS = {
    "interieur": "Intérieur du Hall d’Exposition, vide, sous sa charpente métallique",
    "interieur-portes": "Portes de chargement numérotées du Hall d’Exposition",
    "galerie-couverte": "Galerie couverte longeant le Hall d’Exposition",
    "salon-vue-plongeante": "Allées d’un salon vues d’en haut, entre les stands",
    "stands-connect": "Stands régionaux du salon Connect Côte d’Ivoire",
    "panel-connect": "Panel du salon Connect Côte d’Ivoire sur la grande scène, stands au premier plan",
    "spectacle-ramatoulaye": "Spectacle de DJ Ramatoulaye devant le public assis",
    "spectacle-scene": "Spectacle sur scène, costumes et décor illuminé",
    "entree-c": "Entrée C du Dôme, façade cuivrée",
    "auditorium": "Auditorium du Dôme équipé de sièges orange face à la scène",
    "dome-sous-le-nuage": "Le Dôme vu depuis le parvis sous un ciel nuageux",
    "parvis-dome": "Le parvis devant le Dôme",
    "vue-aerienne": "Vue aérienne des ombrières des esplanades",
    "allee-couverte": "Allée couverte menant au Dôme",
    "parking-couvert": "Parking couvert sous les ombrières",
    "engins-devant-le-dome": "Engins de chantier exposés sur le parvis devant le Dôme",
    "salon-plein-air-aerien": "Vue aérienne d’un salon en plein air sur l’esplanade",
}


def folder_photos(group, featured, label):
    """Toutes les photos d’un groupe (une par nom), image vedette en premier."""
    names = sorted({f.name[: -len("-1600.webp")] for f in (ROOT / "assets/img" / group).glob("*-1600.webp")})
    names.sort(key=lambda n: n != featured)
    out = []
    for n in names:
        if n not in ALTS:
            print(f"  ATTENTION : texte alternatif manquant pour {group}/{n}")
        out.append((f"{group}/{n}", ALTS.get(n, f"Photo — {label}")))
    return out


SPACES = [
    dict(file="hall-exposition.html", title="Hall d’Exposition", letter="A", code="hall",
         lead="Un espace de grande capacité dédié aux salons, expositions et événements corporate.",
         figures=[("6 500 m²", "Surface"), ("17 m", "Hauteur libre sous plafond"), ("2 ou 3", "Espaces d’exposition distincts")],
         h2="Un espace pensé pour les événements de grande ampleur.",
         note_txt="La fiche espace concentre l’information commerciale et technique : usages possibles, capacité, configuration, prestations associées et documents à télécharger.",
         text="Avec 6 500 m² d’un seul tenant et 17 m libres sous plafond, le Hall d’Exposition peut être divisé en 2 ou 3 espaces d’exposition distincts pour accueillir salons, expositions et grands événements d’entreprise.",
         usages=["Salon professionnel", "Exposition", "Lancement", "Convention"], equip=None,
         photos=folder_photos("espaces/hall", "interieur", "Hall d’Exposition"),
         doc=("assets/fiche-technique-hall-exposition.pdf", "Télécharger la fiche technique", True)),
    dict(file="le-dome.html", title="Le Dôme", letter="B", code="dome",
         lead="Le Convention Center du Parc : une salle de 5 000 m² équipée pour les conférences, les événements institutionnels, les salons et les concerts.",
         figures=[("5 000 m²", "Surface exploitable"), ("5 023", "Places assises"), ("9 588", "Personnes debout")],
         h2="Une salle de prestige pour les grands rendez-vous.", note_txt=None,
         text="Avec 5 000 m² exploitables, le Dôme accueille jusqu’à 5 023 personnes assises et 9 588 debout, avec une infrastructure technique pensée pour les événements professionnels comme pour le grand public.",
         usages=["Conférence internationale", "Événement institutionnel", "Salon & exposition", "Concert & spectacle"],
         equip=["96 enceintes", "365 projecteurs", "240 m² d’écran LED"],
         photos=folder_photos("espaces/dome", "panel-connect", "Le Dôme"),
         doc=(None, None, False)),
    dict(file="parvis-esplanades.html", title="Parvis & Esplanades", letter="C", code="parvis",
         lead="67 000 m² d’espaces extérieurs pour les expositions et les événements en plein air.",
         figures=[("11 000 m²", "Parvis"), ("28 000 m²", "Esplanade Est"), ("28 000 m²", "Esplanade Nord-Est")],
         h2="De grands espaces extérieurs, à l’échelle de vos projets.", note_txt=None,
         text="Le Parvis et les esplanades Est et Nord-Est totalisent 67 000 m² pour les expositions extérieures, les formats outdoor et les événements grand public.",
         usages=["Exposition extérieure", "Format outdoor", "Événement grand public", "Concert"], equip=None,
         photos=folder_photos("espaces/parvis", "dome-sous-le-nuage", "Parvis & Esplanades"),
         doc=(None, None, False)),
]


def space_page(sp):
    figs = "".join(f'<li class="figure{" figure--ink" if i == 0 else ""}"><strong>{v}</strong>{l}</li>' for i, (v, l) in enumerate(sp["figures"]))
    n = len(sp["photos"])
    items = "".join(gallery_item(name, alt, "(min-width: 768px) 33vw, 50vw", lazy=i > 2)
                    for i, (name, alt) in enumerate(sp["photos"]))
    usages = "".join(f"<li>{u}</li>" for u in sp["usages"])
    equip = ""
    if sp["equip"]:
        equip_items = "".join(f"<li>{e}</li>" for e in sp["equip"])
        equip = ("\n      <h3 class=\"block-gap\" id=\"equipements\">Équipements</h3>"
                 f"\n      <ul class=\"tags\" role=\"list\">{equip_items}</ul>")
    doc_url, doc_label, local = sp["doc"]
    docs = ""
    if doc_url:
        docs += f'\n      <a class="btn btn--secondary btn--block" href="{doc_url}" download>{doc_label} <span class="btn__meta">PDF</span></a>'
    docs += f'\n      <a class="link-arrow" href="{PLAN_PDF}" target="_blank" rel="noopener" aria-label="Plan du Parc, PDF (nouvel onglet)">Plan du Parc (PDF) {EXT}</a>'
    subnav_equip = '<a href="#equipements">Équipements</a>' if sp["equip"] else ""
    lead_note = note(sp["note_txt"]) if sp["note_txt"] else ""
    return (f"{sp['title']} — Parc des Expositions d’Abidjan", page_hero(
        crumbs(A, ("Nos espaces", "nos-espaces.html"), (sp["title"], None)), f"Espace {sp['letter']}",
        sp["title"], sp["lead"], compact=True) + f"""

<section class="section section--white section--tight">
  <div class="wrap">
    <nav class="subnav" aria-label="Sections de la fiche">
      <a href="#caracteristiques">Caractéristiques</a><a href="#galerie">Galerie</a><a href="#presentation">Présentation</a>{subnav_equip}<a href="#services-associes">Services associés</a><a href="#documents">Documents</a>
    </nav>
    <ul class="figures figures--3" id="caracteristiques" role="list">{figs}</ul>
    <div class="gallery block-gap" id="galerie" data-lightbox>{items}</div>
  </div>
</section>

<section class="section">
  <div class="wrap with-aside">
    <div>
      <h2 id="presentation">{sp["h2"]}</h2>
      {lead_note}
      <p>{sp["text"]}</p>
      <h3 class="block-gap">Usages recommandés</h3>
      <ul class="tags" role="list">{usages}</ul>{equip}
      <h3 class="block-gap" id="services-associes">Services associés</h3>
      <p>Audiovisuel · mobilier · restauration · sécurité · accueil · nettoyage · logistique.</p>
    </div>
    <aside class="aside-box" id="documents" aria-labelledby="aside-espace">
      <p class="eyebrow">Organiser ici</p>
      <h3 id="aside-espace">Votre projet {"au" if sp["code"] == "dome" else ("dans le" if sp["code"] == "hall" else "sur le")} {sp["title"].replace("Le ", "").replace("Hall d’Exposition", "Hall")} ?</h3>
      <p>Accédez au formulaire de devis avec l’espace pré-sélectionné.</p>
      <a class="btn btn--primary btn--block" href="contact-devis.html?espace={sp["code"]}#devis">Demander un devis {ARROW}</a>{docs}
    </aside>
  </div>
</section>
{LIGHTBOX}
""")


for _sp in SPACES:
    PAGES[_sp["file"]] = space_page(_sp)

# ---------------------------------------------------------------- Nos services
SERVICES = [
    ("Audiovisuel", "Son, lumière, vidéo et dispositifs techniques."),
    ("Mobilier", "Configurations adaptées à chaque format."),
    ("Restauration", "Solutions food & beverage selon le projet."),
    ("Sécurité", "Dispositifs adaptés aux flux et jauges."),
    ("Accueil", "Orientation, protocole et assistance visiteurs."),
    ("Nettoyage", "Préparation et maintien opérationnel."),
    ("Technique", "Accompagnement avant et pendant l’événement."),
    ("Logistique", "Coordination, accès et exploitation."),
]
service_items = "\n".join(
    f'      <li class="service"><span>{i:02d}</span><h2 class="t3">{n}</h2><p>{d}</p></li>'
    for i, (n, d) in enumerate(SERVICES, 1)
)
PAGES["nos-services.html"] = ("Nos services — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Nos services", None)), "Services",
    "Tout ce qu’il faut pour faire fonctionner votre événement.",
    "Au-delà des espaces, le Parc réunit chez un seul interlocuteur les prestations nécessaires à votre événement.",
    lead_note=note("Une présentation claire des prestations pour transformer le Parc en solution complète, pas seulement en location d’espace.")) + f"""

<section class="section section--ink">
  <div class="wrap">
    <ul class="services" role="list">
{service_items}
    </ul>
  </div>
</section>

<!-- Contenus repris de la page officielle /fr/nos-espaces-services (relevé du 7 octobre 2026) -->
<section class="section">
  <div class="wrap support">
    <div>
      <p class="eyebrow">Prestations de services</p>
      <h2>Une équipe à vos côtés, de la préparation au jour J.</h2>
      <p class="lead">Nos équipes accompagnent et conseillent au quotidien les organisateurs dans la réalisation de leur événement, en mettant à disposition les espaces et l’ensemble des prestations nécessaires à son bon déroulement : restauration, matériel audiovisuel, mobilier, sécurité, nettoyage… Sur site, elles coordonnent l’ensemble des prestations d’accueil.</p>
    </div>
    <section class="support__building" aria-labelledby="batiment">
      <h3 id="batiment">Bâtiment administratif</h3>
      <p>Un accueil disponible 24h/24 et des équipements au service de votre événement.</p>
      <ul class="support__list" role="list">
        <li><strong>24h/24</strong>Accueil</li>
        <li><strong>Sécurité</strong>Poste de sécurité</li>
        <li><strong>Police</strong>Poste de police</li>
        <li><strong>Santé</strong>Infirmerie</li>
        <li><strong>Technique</strong>Équipements techniques</li>
        <li><strong>Stockage</strong>Locaux de stockage</li>
      </ul>
    </section>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="intro">
      <div><p class="eyebrow">Politique RSE</p><h2>Des événements plus responsables.</h2></div>
      <p>En cohérence avec la politique RSE du groupe GL events, le réseau GL events Venues, dont fait partie le Parc, s’engage sur trois priorités.</p>
    </div>
    <ol class="commitments" role="list">
      <li><span aria-hidden="true">01</span><p>Réduire l’empreinte carbone des événements et du site.</p></li>
      <li><span aria-hidden="true">02</span><p>Limiter l’utilisation du jetable et développer l’économie circulaire.</p></li>
      <li><span aria-hidden="true">03</span><p>Développer la diversité et soutenir les territoires.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media">{img("phototheque/salon-stand", "Stand d’exposant aménagé lors d’un salon", "(min-width: 1024px) 50vw, 100vw")}</div>
    <div>
      <p class="eyebrow">Sur mesure</p>
      <h2>Composez les services adaptés à votre événement.</h2>
      {note("Chaque service renvoie vers une demande qualifiée, afin que l’équipe commerciale récupère immédiatement le contexte du besoin.")}
      <p>Cochez les services dont vous avez besoin dans votre demande de devis : l’équipe commerciale construit une proposition sur mesure.</p>
      <a class="btn btn--primary" href="contact-devis.html#besoins">Demander un devis {ARROW}</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Photothèque
PHOTOS = [  # (fichier, espace, type, texte alternatif) — espaces et types déduits des photos, à confirmer
    ("phototheque/salon-stand", "hall", "salons", "Stand d’exposant lors d’un salon professionnel"),
    ("phototheque/dome-lumieres", "dome", "concerts", "Public sous les lumières bleues du Dôme"),
    ("phototheque/salon-auto", "hall", "salons", "Véhicules exposés lors d’un salon automobile"),
    ("phototheque/concert-artiste", "dome", "concerts", "Artiste en concert face au public"),
    ("phototheque/boxe", "dome", "sport", "Gala de boxe : le vainqueur salue le public sur le ring"),
    ("phototheque/concert-arena", "dome", "concerts", "Grande scène de concert vue depuis les gradins"),
    ("phototheque/salon-rencontres", "hall", "salons", "Échanges entre visiteurs et exposants sur un salon"),
    ("phototheque/arena-rouge", "dome", "concerts", "Salle plongée dans une lumière rouge pendant un spectacle"),
    ("phototheque/public-gradins", "dome", "concerts", "Public assis dans les gradins"),
    ("phototheque/concert-nuit", "dome", "concerts", "Scène de concert illuminée dans l’obscurité"),
    ("phototheque/public-ambiance", "dome", "concerts", "Spectatrices photographiant la scène"),
]
photo_items = "".join(
    gallery_item(n, a, "(min-width: 768px) 33vw, 50vw", f' data-espace="{e}" data-type="{t}"') for n, e, t, a in PHOTOS)
PAGES["phototheque.html"] = ("Photothèque — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Photothèque", None)), "Photothèque",
    "Le Parc en images.",
    "Parcourez les espaces et les événements accueillis au Parc, par lieu ou par type d’événement.",
    "\n    <div class=\"filter-rows\">"
    + filters("Filtrer par espace", ["Tous", "Hall", "Dôme"], "photos", "espace", row_label="Espace")
    + filters("Filtrer par type d’événement", ["Tous", "Salons", "Concerts", "Sport"], "photos", "type", row_label="Type")
    + "</div>",
    lead_note=note("Une galerie immersive organisée par espace et par type d’événement, pensée autant pour l’inspiration que pour la preuve commerciale.")) + f"""

<section class="section section--white">
  <div class="wrap">
    {results("photos", f"{len(PHOTOS)} photos", "Aucune photo pour cette combinaison. Essayez un autre espace ou un autre type d’événement.")}
    <!-- Espaces et types des photos déduits des images : à confirmer par le Parc -->
    <div class="photo-grid" id="photos" data-lightbox>{photo_items}</div>
  </div>
</section>
{LIGHTBOX}
""")

# ---------------------------------------------------------------- Agenda
PAGES["agenda.html"] = ("Agenda — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Agenda", None)), "Agenda",
    "Les prochains événements au Parc.",
    "Salons, congrès, conférences, concerts : retrouvez les prochains rendez-vous accueillis au Parc.",
    "\n    " + filters("Filtrer par catégorie", ["Tous", "Salons", "Congrès", "Conférences", "Concerts", "Expositions"], "evenements", "type"),
    compact=True,
    lead_note=note("Un listing filtrable par date et catégorie, avec une URL dédiée pour chaque événement afin de soutenir le référencement.")) + f"""

<section class="section section--white">
  <div class="wrap">
    {results("evenements", f"{len(EVENTS)} événements", "Aucun événement à venir dans cette catégorie pour le moment.")}
    <!-- Événements relevés le 7 octobre 2026 sur parcdesexpositionsabidjan.com/fr/liste-des-agendas (types déduits des intitulés) -->
    <ol class="timeline" id="evenements" role="list">
{timeline()}
    </ol>
    <dialog class="event-dialog" id="event-dialog" aria-labelledby="event-dialog-title">
      <button class="event-dialog__close" type="button" aria-label="Fermer la fenêtre"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
      <img class="event-dialog__img" src="data:," alt="" width="800" height="450" hidden>
      <div class="event-dialog__head">
        {ARCH.format(cls="event-dialog__arch")}
        <p class="event-dialog__type"></p>
        <h2 class="event-dialog__title" id="event-dialog-title"></h2>
        <p class="event-dialog__when"></p>
      </div>
      <div class="event-dialog__body"></div>
      <div class="event-dialog__foot">
        <button class="link-arrow" type="button" data-event-ics>Ajouter à mon agenda</button>
      </div>
    </dialog>
  </div>
</section>
""")

# ---------------------------------------------------------------- Fiche événement
PAGES["fiche-evenement.html"] = ("Événement — Parc des Expositions d’Abidjan", f"""
<section class="hero hero--small hero--under-header">
  <div class="hero__img" aria-hidden="true">{img("agenda/auto-expo", priority=True, lazy=False)}</div>
  <div class="wrap hero__inner">
    {crumbs(A, ("Agenda", "agenda.html"), ("Auto Expo", None), ink=True)}
    {note("Agenda · Exemple de gabarit")}
    <p class="eyebrow">Agenda · Salon</p>
    <h1>Auto Expo</h1>
    {note("Un gabarit événement optimisé pour la lisibilité, le partage social et le référencement.")}
    <p class="lead">Dates, lieu, programme et informations pratiques : tout pour préparer votre venue.</p>
  </div>
</section>

<section class="section section--white">
  <div class="wrap with-aside">
    <div>
      <ul class="figures figures--3 figures--facts" role="list">
        <li class="figure"><span class="figure__label">Date</span><strong>8–10 oct. 2026</strong></li>
        <li class="figure"><span class="figure__label">Lieu</span><strong>Parc des Expositions</strong></li>
        <li class="figure"><span class="figure__label">Public</span><strong>Professionnels</strong></li>
      </ul>
      <h2 class="block-gap">À propos de l’événement</h2>
      {note("Zone administrable Drupal pour la présentation, le programme, les liens utiles, l’organisateur et les informations pratiques.")}
      <p>Le salon de l’industrie automobile réunit plus de 15 nations participantes et 900 acheteurs professionnels, avec des rencontres B2B et des panels sectoriels pour développer vos relations commerciales à l’international.</p>
      <p><a class="link-arrow" href="https://ivorycoastautoexpo.com/" target="_blank" rel="noopener" aria-label="Site officiel de l’événement (nouvel onglet)">Site officiel de l’événement {EXT}</a></p>
      <div class="media block-gap">{img("phototheque/salon-auto", "Véhicules exposés lors d’un salon automobile", "(min-width: 1024px) 60vw, 100vw")}</div>
    </div>
    <aside class="aside-box" aria-labelledby="aside-event">
      <p class="eyebrow">Informations</p>
      <h3 id="aside-event">Préparez votre visite</h3>
      <p>Accès, horaires, transport, parking et informations visiteurs.</p>
      <a class="btn btn--primary btn--block" href="contact-devis.html#nous-contacter">Contacter le Parc {ARROW}</a>
    </aside>
  </div>
</section>
""")

# ---------------------------------------------------------------- Contact & devis
REQ = ' <span class="req" aria-hidden="true">*</span>'
OPT = ' <span class="opt">(facultatif)</span>'


def field(fid, label, control, required=False, error="", full=False):
    mark = REQ if required else OPT
    err = f'<p class="field__error" id="{fid}-error" hidden>{error}</p>' if required else ""
    return f'        <div class="field{" field--full" if full else ""}"><label for="{fid}">{label}{mark}</label>{control}{err}</div>'


SERVICE_CHECKS = "".join(
    f'<label class="check"><input type="checkbox" name="services" value="{slug(n)}"> {n}</label>' for n, _ in SERVICES
)
TYPES = ["Salon", "Congrès", "Conférence", "Convention", "Concert", "Exposition", "Corporate", "Autre"]
TYPE_OPTS = '<option value="" disabled selected>Choisir…</option>' + "".join(f'<option value="{slug(t)}">{t}</option>' for t in TYPES)

FORM = f"""    <div class="form-col">
      <p class="contact-strip">Vous préférez en parler ? Écrivez-nous sur WhatsApp : {TEL}</p>
      <form class="form" id="devis" aria-label="Demande de devis" novalidate data-quote-form>
        <p class="form__intro">Les champs marqués d’un astérisque (*) sont obligatoires.</p>
        <fieldset class="form__group">
          <legend>Vous</legend>
          <div class="form__grid">
{field("nom", "Nom", '<input id="nom" name="nom" autocomplete="name" placeholder="Votre nom" required>', True, "Indiquez votre nom.")}
{field("entreprise", "Entreprise", '<input id="entreprise" name="entreprise" autocomplete="organization" placeholder="Votre entreprise">')}
{field("email", "E-mail", '<input id="email" name="email" type="email" autocomplete="email" placeholder="nom@entreprise.com" required>', True, "Indiquez une adresse e-mail valide, par exemple nom@entreprise.com.")}
{field("telephone", "Téléphone", '<input id="telephone" name="telephone" type="tel" autocomplete="tel" placeholder="+225 …">')}
          </div>
        </fieldset>
        <fieldset class="form__group">
          <legend>Votre événement</legend>
          <div class="form__grid">
{field("type", "Type d’événement", f'<select id="type" name="type" required>{TYPE_OPTS}</select>', True, "Choisissez le type d’événement.")}
{field("participants", "Nombre de participants", '<input id="participants" name="participants" type="number" min="1" step="1" inputmode="numeric" placeholder="Ex. 800">')}
{field("espace", "Espace envisagé", '<select id="espace" name="espace"><option value="">Je ne sais pas encore</option><option value="hall">Hall d’Exposition</option><option value="dome">Le Dôme</option><option value="parvis">Parvis & Esplanades</option></select>')}
            <fieldset class="field field--full dates">
              <legend>Date envisagée{OPT}</legend>
              <div class="dates__row">
                <div class="field"><label for="date-debut">Du</label><input id="date-debut" name="date_debut" type="date"></div>
                <div class="field"><label for="date-fin">Au</label><input id="date-fin" name="date_fin" type="date"></div>
              </div>
              <label class="check"><input type="checkbox" name="dates_flexibles"> Mes dates sont flexibles</label>
            </fieldset>
          </div>
        </fieldset>
        <fieldset class="form__group" id="besoins">
          <legend>Vos besoins</legend>
          <fieldset class="checks">
            <legend>Services nécessaires{OPT}</legend>
            <div class="checks__grid">{SERVICE_CHECKS}</div>
          </fieldset>
{field("projet", "Décrivez votre projet", '<textarea id="projet" name="projet" placeholder="Quelques lignes sur votre événement"></textarea>', full=True)}
        </fieldset>
        <div class="field consent">
          <label class="check"><input type="checkbox" id="consent" name="consent" required> J’accepte que mes informations soient utilisées pour traiter ma demande.{REQ}</label>
          <p class="field__error" id="consent-error" hidden>Cochez cette case pour envoyer votre demande.</p>
        </div>
        <div class="form__submit">
          <button class="btn btn--primary" type="submit">Envoyer ma demande {ARROW}</button>
          <p class="form__reassure">Notre équipe commerciale vous répond dans les meilleurs délais.</p>
        </div>
      </form>
      <!-- Maquette : l’envoi est simulé dans assets/site.js ; le traitement réel est à brancher sur un webform Drupal. -->
      <div class="form-success" id="devis-ok" role="status" tabindex="-1" hidden>
        <h2 class="t3">Demande envoyée</h2>
        <p>Merci. Notre équipe commerciale étudie votre projet et vous recontacte dans les meilleurs délais.</p>
        <dl class="ev-facts form-success__recap" data-recap></dl>
        <a class="btn btn--secondary" href="nos-espaces.html">Découvrir nos espaces {ARROW}</a>
      </div>
    </div>"""

# Photo du totem : dans l’encadré « Nous contacter » (et non plus dans l’en-tête)
CONTACT_TOTEM = img("pages/contact-signaletique", "Totem de signalétique du Parc des Expositions d’Abidjan devant le Dôme", "(min-width: 1024px) 340px, 100vw")
PAGES["contact-devis.html"] = ("Contact & Devis — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Contact", None), ("Devis", None)),
    "Contact",
    "Parlez-nous de votre projet.",
    "Décrivez votre événement : notre équipe commerciale vous recontacte avec une proposition adaptée.",
    compact=True,
    lead_note=note("Le formulaire devient un véritable outil de qualification commerciale.")) + f"""

<section class="section section--white section--tight">
  <div class="wrap with-aside">
{FORM}
    <aside class="aside-box" id="nous-contacter" aria-labelledby="aside-contact">
      <figure class="aside-box__media">{CONTACT_TOTEM}</figure>
      <p class="eyebrow">Parc des Expositions d’Abidjan</p>
      <h2 class="t3" id="aside-contact">Nous contacter</h2>
      <p>{TEL}</p>
      <p>Boulevard de l’aéroport<br>Abidjan · Côte d’Ivoire</p>
      {note("Les soumissions peuvent être enregistrées dans Drupal et routées vers l’équipe commerciale.")}
    </aside>
  </div>
</section>

<section class="section" id="acces">
  <div class="wrap access">
    <div class="access__text">
      <p class="eyebrow">Accès</p>
      <h2>Venir au Parc</h2>
      <p>Boulevard de l’aéroport<br>Abidjan · Côte d’Ivoire</p>
      <p>{TEL}</p>
      <div class="actions">
        <a class="btn btn--secondary" href="https://www.google.com/maps/dir/?api=1&amp;destination=5.2634735,-3.9465668" target="_blank" rel="noopener" aria-label="Itinéraire vers le Parc (Google Maps, nouvel onglet)">Itinéraire {ARROW}</a>
        <a class="btn btn--secondary" href="{MAPS_PLACE}" target="_blank" rel="noopener" aria-label="Ouvrir dans Google Maps (nouvel onglet)">Ouvrir dans Google Maps {EXT}</a>
      </div>
    </div>
    <div class="access__map" data-embed-src="https://maps.google.com/maps?q=5.2634735,-3.9465668&amp;hl=fr&amp;z=16&amp;output=embed" data-embed-title="Carte : localisation du Parc des Expositions d’Abidjan">
      <div class="embed-facade">
        <p>La carte est fournie par Google Maps, qui peut déposer des cookies.</p>
        <button class="btn btn--secondary" type="button" data-embed-load>Afficher la carte</button>
      </div>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Visite virtuelle
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 4v16l13-8z"/></svg>'
PAGES["visite-virtuelle.html"] = ("Visite virtuelle — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Nos espaces", "nos-espaces.html"), ("Visite virtuelle", None)), "Visite 360°",
    "Explorez le Parc à distance.",
    "Parcourez le Parc en 360° depuis votre bureau, comme si vous y étiez.",
    compact=True,
    lead_note=note("Un gabarit léger pour intégrer le module de visite virtuelle existant ou futur sans casser la navigation du site.")) + f"""

<section class="section section--white section--tight">
  <div class="wrap">
    <div class="tour" id="visite">
      <a class="tour__launch" href="https://my.matterport.com/show/?m=aNcgwUfY8uk" target="_blank" rel="noopener" data-tour-src="https://my.matterport.com/show/?m=aNcgwUfY8uk&amp;play=1" data-tour-title="Visite virtuelle 360° du Parc des Expositions d’Abidjan">{PLAY}<span>Lancer <br>la visite <br>360°</span></a>
    </div>
    <div class="tour__legend"><p class="filter-row__label" id="tour-espaces">Espaces visitables</p><ul class="tags" role="list" aria-labelledby="tour-espaces"><li>Hall d’Exposition</li><li>Le Dôme</li><li>Parvis</li><li>Esplanades</li></ul></div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Informations légales
EN_COURS = '<p class="legal__pending">Contenu en cours de rédaction.</p>'
PAGES["informations-legales.html"] = ("Informations légales — Parc des Expositions d’Abidjan", page_hero(
    crumbs(A, ("Informations légales", None)), "Informations légales",
    "Informations légales",
    "Mentions légales, cookies, confidentialité, conditions d’utilisation et engagements éthiques du Parc des Expositions d’Abidjan.",
    compact=True) + f"""

<section class="section section--white section--tight">
  <div class="wrap legal">
    <nav class="legal__toc" aria-label="Sommaire">
      <ol role="list">
        <li><a href="#mentions-legales">Mentions légales</a></li>
        <li><a href="#cookies">Politique cookies</a></li>
        <li><a href="#confidentialite">Politique de confidentialité</a></li>
        <li><a href="#cgu">CGU</a></li>
        <li><a href="#ethique">Éthique et conformité</a></li>
      </ol>
    </nav>
    <div class="legal__body">
      <!-- Note de maquette : textes juridiques à fournir et valider par le Parc ; seuls les faits connus sont renseignés. -->
      <section id="mentions-legales" aria-labelledby="t-mentions">
        <h2 id="t-mentions">Mentions légales</h2>
        <dl class="ev-facts">
          <div><dt>Éditeur</dt><dd>Parc des Expositions d’Abidjan</dd></div>
          <div><dt>Adresse</dt><dd>Boulevard de l’aéroport, Abidjan, Côte d’Ivoire</dd></div>
          <div><dt>Contact</dt><dd>{TEL}</dd></div>
        </dl>
        {EN_COURS}
      </section>
      <section id="cookies" aria-labelledby="t-cookies">
        <h2 id="t-cookies">Politique cookies</h2>
        <p>Ce site ne dépose pas de cookie publicitaire ni de mesure d’audience. Il mémorise uniquement, dans votre navigateur, votre choix concernant les contenus tiers.</p>
        <p>Avec votre accord, trois services externes sont chargés et peuvent déposer leurs propres cookies : la carte Google Maps de la page Contact, le fil Facebook de l’accueil et la visite virtuelle Matterport. Sans accord, la carte et le fil Facebook ne s’affichent que si vous le demandez, et la visite virtuelle ne se charge qu’au clic sur « Lancer la visite 360° ».</p>
        <p><button type="button" class="btn btn--secondary" data-consent-open>Modifier mon choix</button></p>
      </section>
      <section id="confidentialite" aria-labelledby="t-confidentialite">
        <h2 id="t-confidentialite">Politique de confidentialité</h2>
        <p>Les informations saisies dans le formulaire de demande de devis servent uniquement à traiter votre demande.</p>
        {EN_COURS}
      </section>
      <section id="cgu" aria-labelledby="t-cgu">
        <h2 id="t-cgu">CGU</h2>
        {EN_COURS}
      </section>
      <section id="ethique" aria-labelledby="t-ethique">
        <h2 id="t-ethique">Éthique et conformité</h2>
        {EN_COURS}
      </section>
    </div>
  </div>
</section>
""")

import html as _html
import json as _json

EN_DICT = _json.loads((ROOT / "tools/i18n/en.json").read_text(encoding="utf-8"))
_SKIP = re.compile(r"<(script|style)\b.*?</\1>|<!--.*?-->", re.S)
_ATTR = re.compile(r'\b(alt|aria-label|aria-roledescription|title|placeholder|data-caption|data-tour-title|data-embed-title)="([^"]*)"')
_TEXT = re.compile(r">([^<]+)<")


_PATTERNS = [  # libellés composés : « Détails : <événement> », etc.
    (re.compile(r"^Détails : (.+)$"), "Details: {}"),
    (re.compile(r"^Réserver : (.+) \(nouvel onglet\)$"), "Book: {} (new tab)"),
    (re.compile(r"^Site officiel : (.+) \(nouvel onglet\)$"), "Official website: {} (new tab)"),
]


def _tr(text):
    core = " ".join(_html.unescape(text).split())
    for rx, tpl in _PATTERNS:
        m = rx.match(core)
        if m and core not in EN_DICT:
            name = m.group(1)
            return tpl.format(EN_DICT.get(name, name))  # texte brut : échappé par l'appelant
    if core in EN_DICT:
        lead = text[: len(text) - len(text.lstrip())]
        trail = text[len(text.rstrip()):]
        return lead + EN_DICT[core] + trail
    return None


def to_english(page, src):
    """Version anglaise d'une page : chaînes entières traduites (tools/i18n/en.json), chemins relatifs à en/."""
    src = src.replace('<html lang="fr"', '<html lang="en"')
    src = re.sub(r'(href="index\.html"[^>]*>)Accueil(?=[\s<])', r"\1Home", src)  # « Accueil » = page d'accueil (sinon : service d'accueil)
    parts, last = [], 0
    for m in _SKIP.finditer(src):
        parts.append((src[last:m.start()], True)); parts.append((m.group(0), False)); last = m.end()
    parts.append((src[last:], True))
    out = []
    for chunk, translate in parts:
        if translate:
            def _text(m):
                t = _tr(m.group(1))
                return ">" + (m.group(1) if t is None else _html.escape(t, quote=False)) + "<"

            def _attr(m):
                t = _tr(m.group(2))
                return f'{m.group(1)}="{m.group(2) if t is None else _html.escape(t)}"'
            chunk = _TEXT.sub(_text, chunk)
            chunk = _ATTR.sub(_attr, chunk)
        out.append(chunk)
    src = "".join(out)
    # chemins : ressources partagées à la racine
    src = re.sub(r'(?<=["\s,(])(assets/|styles\.css)', r"../\1", src)
    # sélecteur de langue : FR -> page française, EN -> page courante
    src = src.replace(f'href="../{page}" hreflang="fr" lang="fr" aria-current="true">FR', f'href="../{page}" hreflang="fr" lang="fr">FR')
    src = src.replace(f'href="{page}" hreflang="en" lang="en">EN', f'href="{page}" hreflang="en" lang="en" aria-current="true">EN')
    src = src.replace('aria-label="Langue"', 'aria-label="Language"')
    src = src.replace("assets/fiche-technique-hall-exposition.pdf", "assets/fiche-technique-hall-exposition-en.pdf")
    return src


def with_lang_links(page, src, lang):
    fr, en = (page, f"en/{page}") if lang == "fr" else (f"../{page}", page)
    src = src.replace("__FR__", fr).replace("__EN__", en)
    alt = f'<link rel="alternate" hreflang="fr" href="{fr}">\n<link rel="alternate" hreflang="en" href="{en}">\n</head>'
    return src.replace("</head>", alt, 1)


# Image de l’en-tête de chaque page : photo désaturée fondue (produit) dans l’orange du logo ; l’en-tête transparent s’y pose
PAGE_BG = {
    "qui-sommes-nous.html": "slider/dome-rendu",
    "nos-espaces.html": "espaces/hall/salon-vue-plongeante",
    "hall-exposition.html": "espaces/hall/interieur",
    "le-dome.html": "espaces/parvis/dome-sous-le-nuage",
    "parvis-esplanades.html": "espaces/parvis/salon-plein-air-aerien",
    "nos-services.html": "phototheque/salon-stand",
    "phototheque.html": "phototheque/dome-lumieres",
    "agenda.html": "slider/concert-foule",
    "contact-devis.html": "pages/parlez-nous",
    "visite-virtuelle.html": "espaces/parvis/vue-aerienne",
    "informations-legales.html": "espaces/hall/galerie-couverte",
}


def with_page_bg(name, src):
    bg = PAGE_BG.get(name)
    if not bg:
        return src
    return src.replace('<section class="page-hero', f'<section style="--page-bg: url(assets/img/{bg}-1600.webp)" class="page-hero page-hero--bg', 1)


(ROOT / "en").mkdir(exist_ok=True)
for name, (title, body) in PAGES.items():
    fr_html = with_page_bg(name, head(title) + "\n" + header(name) + body + FOOTER)
    (ROOT / name).write_text(with_lang_links(name, fr_html, "fr"), encoding="utf-8")
    en_html = to_english(name, fr_html.replace("__FR__", "../" + name).replace("__EN__", name))
    (ROOT / "en" / name).write_text(with_lang_links(name, en_html, "en"), encoding="utf-8")
    print("écrit", name, "+ en/" + name)

# ---------------------------------------------------------------- Planche d’index (inchangée sur le fond)
LINKS = [("index.html", "Accueil"), ("qui-sommes-nous.html", "Qui Sommes Nous"), ("nos-espaces.html", "Nos Espaces"),
         ("hall-exposition.html", "Hall Exposition"), ("le-dome.html", "Le Dome"), ("parvis-esplanades.html", "Parvis Esplanades"), ("nos-services.html", "Nos Services"), ("phototheque.html", "Phototheque"),
         ("agenda.html", "Agenda"), ("fiche-evenement.html", "Fiche Evenement"), ("contact-devis.html", "Contact Devis"),
         ("visite-virtuelle.html", "Visite Virtuelle"), ("informations-legales.html", "Informations Legales")]
links = "\n".join(f'      <li><a href="{h}">{t} {ARROW}</a></li>' for h, t in LINKS)
index = head("Parc des Expositions d’Abidjan — Planche HTML") + f"""
<body>
<main class="hub" id="contenu">
  <div class="wrap">
    <img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan" width="394" height="210" class="hub__logo">
    <p class="eyebrow">Parc des Expositions d’Abidjan · Proposition 1 · The Seed-inspired</p>
    <h1>Planches HTML — sous-pages</h1>
    <p class="lead">Chaque page ci-dessous correspond à une planche distincte et réutilise le même socle CSS.</p>
    <ul class="hub__links" role="list">
{links}
    </ul>
  </div>
</main>
</body>
</html>
"""
(ROOT / "planches.html").write_text(with_lang_links("planches.html", index, "fr"), encoding="utf-8")
(ROOT / "en" / "planches.html").write_text(with_lang_links("planches.html", to_english("planches.html", index), "en"), encoding="utf-8")
print("écrit planches.html")

# Ancienne adresse de l’accueil : redirection vers index.html (liens et favoris existants)
REDIRECT = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>Parc des Expositions d’Abidjan</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="index.html">
<meta http-equiv="refresh" content="0; url=index.html">
</head>
<body><p><a href="index.html">{label}</a></p></body>
</html>
"""
(ROOT / "accueil.html").write_text(REDIRECT.format(lang="fr", label="Accueil du Parc des Expositions d’Abidjan"), encoding="utf-8")
(ROOT / "en" / "accueil.html").write_text(REDIRECT.format(lang="en", label="Abidjan Exhibition Center home page"), encoding="utf-8")
print("écrit accueil.html (redirection)")
