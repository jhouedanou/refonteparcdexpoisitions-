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
              "venir-a-abidjan.html": "qui-sommes-nous.html"}


def note(original):
    """Texte d’origine du cahier des charges, conservé pour le développeur."""
    return f"<!-- Note de maquette (texte d’origine) : {original} -->"


PIN_ICON = ('<svg class="i i--pin" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            '<path d="M12 21s-6.5-6.1-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.9 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.3"/></svg>')
SUB_ESPACES = [("hall-exposition.html", "Hall d’Exposition", "6 500 m² · 12 m sous plafond"),
               ("le-dome.html", "Le Dôme", "5 000 m² · 4 800 assis · 9 353 assis/debout"),
               ("parvis-esplanades.html", "Parvis & Esplanades", "67 000 m² d’espaces extérieurs"),
               ("visite-virtuelle.html", "Visite virtuelle 360°", "Explorer le Parc à distance")]


def header(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else (' aria-current="true"' if SECTION_OF.get(active) == href else "")
        if href == "nos-espaces.html":
            subs = "".join(
                f'<li><a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == active else ""}><span class="nav__sub-title">{t_}</span><span class="nav__sub-desc">{d}</span></a></li>'
                for h, t_, d in SUB_ESPACES)
            items.append(f'      <li class="nav__item--sub"><a href="{href}"{cur}>{label}</a>'
                         f'<button class="nav__subtoggle" type="button" aria-expanded="false" aria-controls="sub-espaces" aria-label="Sous-menu Nos espaces">'
                         f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6"/></svg></button>'
                         f'<ul class="nav__sub" id="sub-espaces" role="list">{subs}</ul></li>')
            continue
        items.append(f'      <li><a href="{href}"{cur}>{label}</a></li>')
    cta_cur = ' aria-current="page"' if active == "contact-devis.html" else ""
    return f"""<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="utility" data-bento="Topbar">
  <div class="wrap utility__inner">
    <ul class="utility__items" role="list">
      <li class="utility__item">{TEL.replace('class="wa-link"', 'class="wa-link utility__tel"')}</li>
      <li class="utility__item utility__item--place">{PIN_ICON}<span>Abidjan, Côte d’Ivoire</span></li>
    </ul>
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
<header class="topbar topbar--overlay" data-bento="Site header">
  <div class="wrap topbar__inner">
    <a class="brand" href="index.html"><img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan — accueil" width="394" height="210"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-principale"><span class="menu-toggle__bars" aria-hidden="true"></span><span class="sr-only">Menu</span></button>
    <nav class="nav" id="nav-principale" aria-label="Navigation principale" data-bento="Menu">
      <ul>
{chr(10).join(items)}
      </ul>
      <ul class="social social--menu" role="list" aria-label="Réseaux sociaux">
        <li><a href="{IG_URL}" target="_blank" rel="noopener" aria-label="Instagram du Parc des Expositions (nouvel onglet)">{IG_ICON}</a></li>
        <li><a href="{FB_URL}" target="_blank" rel="noopener" aria-label="Facebook du Parc des Expositions (nouvel onglet)">{FB_ICON}</a></li>
        <li><a href="{LI_URL}" target="_blank" rel="noopener" aria-label="LinkedIn du Parc des Expositions (nouvel onglet)">{LI_ICON}</a></li>
      </ul>
    </nav>
    <a class="topbar__wa" href="{WA_URL}" target="_blank" rel="noopener" aria-label="WhatsApp : +225 27 21 71 09 97 (nouvel onglet)">{WA_ICON}<span class="topbar__wa-num">+225 27 21 71 09 97</span></a>
    <a class="btn btn--primary topbar__cta" href="contact-devis.html"{cta_cur}><span class="hide-sm">Demander un devis</span><span class="show-sm">Devis</span></a>
  </div>
</header>
<main class="page" id="contenu" tabindex="-1">"""


FOOTER = f"""</main>
<!-- Note de maquette : inscription simulée ; à brancher sur l’outil d’e-mailing du Parc (Brevo, Mailchimp…) via Drupal -->
<section class="newsletter-block" id="newsletter" aria-labelledby="nl-title" data-bento="Newsletter form">
  <div class="wrap newsletter">
    <div class="newsletter__intro">
      <p class="eyebrow">Newsletter</p>
      <h2 class="newsletter__title" id="nl-title">Les prochains événements du Parc, dans votre boîte mail</h2>
      <p>Une lettre par mois : salons, congrès et concerts à venir. Désinscription en un clic.</p>
    </div>
    <form class="newsletter__form" data-newsletter novalidate>
      <label class="newsletter__field-label" for="nl-email">Votre adresse e-mail</label>
      <div class="newsletter__row">
        <input id="nl-email" name="email" type="email" autocomplete="email" required placeholder="nom@exemple.com" aria-describedby="nl-email-error">
        <button class="btn btn--primary" type="submit">S’inscrire</button>
      </div>
      <p class="newsletter__error" id="nl-email-error" hidden>Indiquez une adresse e-mail valide, par exemple nom@exemple.com.</p>
      <label class="check newsletter__consent"><input id="nl-consent" type="checkbox" required aria-describedby="nl-consent-error"><span>J’accepte de recevoir la newsletter du Parc. Voir la <a href="informations-legales.html#confidentialite">politique de confidentialité</a>.</span></label>
      <p class="newsletter__error" id="nl-consent-error" hidden>Cochez la case pour confirmer votre inscription.</p>
    </form>
    <p class="newsletter__ok" role="status" tabindex="-1" hidden></p>
  </div>
</section>
<footer class="footer" data-bento="Footer">
  <div class="wrap footer__columns">
    <div class="footer__col footer__col--brand">
      <img class="footer__logo" src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan" width="394" height="210" loading="lazy">
      <address class="footer__contact" data-bento="Contact details">
        <span>Boulevard de l’aéroport<br>Abidjan · Côte d’Ivoire</span>
        {TEL}
      </address>
    </div>
    <nav class="footer__col" aria-labelledby="ft-espaces">
      <h2 class="footer__title" id="ft-espaces">Nos espaces</h2>
      <ul class="footer__menu" role="list">
        <li><a href="hall-exposition.html">Hall d’Exposition</a></li>
        <li><a href="le-dome.html">Le Dôme</a></li>
        <li><a href="parvis-esplanades.html">Parvis & Esplanades</a></li>
        <li><a href="visite-virtuelle.html">Visite virtuelle 360°</a></li>
        <li><a href="nos-services.html">Nos services</a></li>
      </ul>
    </nav>
    <nav class="footer__col" aria-labelledby="ft-evenement">
      <h2 class="footer__title" id="ft-evenement">Votre événement</h2>
      <ul class="footer__menu" role="list">
        <li><a href="salons-professionnels.html">Salons</a></li>
        <li><a href="congres-conferences.html">Congrès</a></li>
        <li><a href="evenements-entreprise.html">Entreprises</a></li>
        <li><a href="concerts-spectacles.html">Concerts</a></li>
        <li><a href="venir-a-abidjan.html">Venir à Abidjan</a></li>
        <li><a href="contact-devis.html">Demander un devis</a></li>
        <li><a href="assets/plaquette-commerciale-pea.pdf" download>Plaquette commerciale (PDF)</a></li>
      </ul>
    </nav>
  </div>
  <div class="wrap footer__legal-wrap">
    <div class="footer__legal-bar">
      <a class="footer__partner" href="https://www.gl-events.com/" target="_blank" rel="noopener" aria-label="GL events, expertise internationale (nouvel onglet)">
        <span class="footer__partner-logo"><img src="assets/logo-gl-events.png" alt="GL events" width="225" height="225" loading="lazy"></span>
      </a>
      <p class="footer__copyright">© 2026 Parc des Expositions d’Abidjan · GL events</p>
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
      <p class="footer__credit">Design par <a href="https://bigfive.solutions/" target="_blank" rel="noopener" aria-label="Big Five, design du site (nouvel onglet)">Big Five</a></p>
    </div>
  </div>
</footer>
<a class="to-top" href="#contenu" aria-label="Retour en haut de page"><svg viewBox="16 -1 360 62.5" aria-hidden="true" focusable="false"><path d="M20 61C70 54 120 25.5 150 12C164 5.7 182 0 196 0C210 0 228 5.7 242 12C272 25.5 322 54 372 61Z"/></svg></a>
<section class="cookie-banner" data-bento="Modal" id="cookie-consent" aria-labelledby="consent-title" hidden>
  <div class="wrap consent__inner">
    <div class="consent__text">
      <h2 class="consent__title" id="consent-title">Cookies et contenus tiers</h2>
      <p>Ce site mémorise uniquement votre choix. Avec votre accord, la carte Google Maps, le fil Facebook et la visite virtuelle Matterport sont chargés et peuvent déposer leurs propres cookies. <a href="informations-legales.html#cookies">En savoir plus</a></p>
    </div>
    <div class="consent__actions">
      <button class="btn btn--invert btn--outline" type="button" data-consent="refused">Tout refuser</button>
      <button class="btn btn--invert btn--outline" type="button" data-consent="accepted">Tout accepter</button>
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
    return f'<nav class="breadcrumbs" aria-label="Fil d’Ariane" data-bento="Breadcrumb"><ol role="list">{"".join(lis)}</ol></nav>'


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


def page_hero(crumb, eyebrow, h1, lead, extra="", compact=False, lead_note="", media="", meta="", addons=""):
    """Composant Bento « Page header » (Background=image, Color=primary) : meta · titre · summary · addons."""
    cls = ("page-hero page-hero--compact" if compact else "page-hero") + (" page-hero--media" if media else "")
    meta_html = f'\n    <div class="page-hero__meta">{meta}</div>' if meta else f'\n    <p class="eyebrow">{eyebrow}</p>'
    addons_html = f'\n    <div class="page-hero__addons">{addons}</div>' if addons else ""
    return f"""
<section class="{cls}" data-bento="Page header">
  <div class="wrap">
    {crumb}{meta_html}
    <h1>{h1}</h1>
    {lead_note}
    <p class="lead">{lead}</p>{extra}{addons_html}{media}
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



SPACE_URL = {"A": "hall-exposition.html", "B": "le-dome.html", "C": "parvis-esplanades.html"}
SPACE_IMG = {"A": "officiel/hall/hall-drapeaux", "B": "officiel/dome-exterieur/dome-ciel", "C": "officiel/dome-exterieur/dome-panorama"}


def space(letter, title, sub, media=None, ink=False, h="h3", usage=""):
    """Composant Bento « Card » (vertical, landscape) : image + badge, titre, description, lien."""
    data = f' data-usage="{usage}"' if usage else ""
    return f"""      <a class="card card--space" href="{SPACE_URL[letter]}"{data} data-bento="Card">
        <div class="card__media">{img(SPACE_IMG[letter], sizes="(min-width: 1024px) 33vw, (min-width: 768px) 50vw, 100vw")}<span class="badge badge--primary card__badge">Espace {letter}</span></div>
        <div class="card__content"><{h} class="card__title{' t3' if h == "h2" else ''}">{title}</{h}><p class="card__desc">{sub}</p><span class="card__link">Découvrir {ARROW}</span></div>
      </a>"""


def event(date, title, place, h="h3", types="", href="fiche-evenement.html", image=None):
    """Composant Bento « Card » (vertical, poster) : affiche + badge de date, titre, lieu, lien."""
    data = f' data-type="{types}"' if types else ""
    thumb = img(f"agenda/{image}", sizes="(min-width: 1024px) 33vw, 100vw") if image else ""
    return f"""      <a class="card card--event" href="{href}"{data} data-bento="Card">
        <div class="card__media card__media--poster">{thumb}<span class="badge card__badge">{date}</span></div>
        <div class="card__content"><{h} class="card__title{' t3' if h == "h2" else ''}">{title}</{h}><p class="card__desc">{place}</p><span class="card__link">Voir l’événement {ARROW}</span></div>
      </a>"""


def results(target, text, empty):
    return (f'<p class="filter-status" role="status" data-status-for="{target}">{text}</p>'
            f'<p class="empty" data-empty-for="{target}" hidden>{empty}</p>')


TYPE_PAGES = [("salons-professionnels.html", "Salons professionnels"), ("congres-conferences.html", "Congrès et conférences"),
              ("evenements-entreprise.html", "Événements d’entreprise"), ("concerts-spectacles.html", "Concerts et spectacles")]


def type_links(current=None, title="Par type d’événement"):
    items = "".join(f'<li><a class="chip chip--link" href="{h}">{t}</a></li>' for h, t in TYPE_PAGES if h != current)
    return f'<nav class="type-links block-gap" aria-label="{title}"><p class="type-links__label">{title}</p><ul role="list">{items}</ul></nav>'


TYPE_LINKS = type_links()
PLAN_PDF = "https://www.parcdesexpositionsabidjan.com/sites/default/files/assets/fichier/dervin/2025-02/plan-commercial-pea.pdf"
PLAQUETTE_PDF = "assets/plaquette-commerciale-pea.pdf"  # plaquette commerciale du client (9 pages, 12 Mo)
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
    "auto-expo": dict(desc="Le salon de l’industrie automobile réunit plus de 15 nations participantes et 900 acheteurs professionnels, avec des rencontres B2B et des panels sectoriels.", site="https://ivorycoastautoexpo.com/"),
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
        links.append(f'<a class="link-arrow" href="evenement-{slug_}.html">Page de l’événement {ARROW}</a>')
        reserve = links[0] if resa else ""
        out.append(f"""      <li class="tl-item" id="{slug_}" data-type="{tags}" data-start="{iso1}" data-end="{iso2}">
        <p class="tl-date"><time datetime="{iso1}" class="tl-date__day">{d1:02d}</time><span class="tl-date__rest">{rest}</span></p>
        <div class="tl-card" data-bento="Card">
          <div class="tl-card__media">{img(f"agenda/{slug_}")}</div>
          <p class="tl-card__type badge">{kind}<span class="tl-card__next" hidden> · Prochainement</span></p>
          <h3 class="tl-card__title"><a href="evenement-{slug_}.html">{title}</a></h3>
          <p class="tl-card__when">{when_long(start, end)}</p>
          <div class="tl-card__more" data-event-more>
            <p class="ev-desc">{det.get("desc", "")}</p>
            <dl class="ev-facts">{facts_html}</dl>
            <div class="ev-links">{"".join(links)}</div>
          </div>
          <div class="tl-card__actions"><button class="btn btn--primary btn--sm" type="button" data-event-open aria-haspopup="dialog" aria-label="Détails : {title}">Détails {ARROW}</button></div>
        </div>
      </li>""")
    return "\n".join(out)


IG_POSTS = "".join(
    f'<li><a class="wall__post" href="https://www.instagram.com/p/{code}/" target="_blank" rel="noopener" aria-label="Instagram : {alt} (nouvel onglet)">{img(f"instagram/{code}", sizes="(min-width: 1024px) 12vw, 33vw")}</a></li>'
    for code, alt in IG_ITEMS)

# Diaporama de l'accueil : ordre d'affichage (images produites par tools/optimiser-images.py)
# Uniquement des photos officielles du client (docs/retourclient/images) : Dôme, Hall, parvis
SLIDES = ["officiel/dome-exterieur/dome-ciel", "officiel/hall/hall-drapeaux", "officiel/dome-salle/salle-pleniere",
          "officiel/dome-exterieur/dome-aerien", "officiel/dome-exterieur/dome-panorama", "officiel/dome-salle/salle-gradins",
          "officiel/hall/hall-perspective", "officiel/dome-salle/salle-parterre"]
SLIDES_HTML = "\n".join(
    f'    <figure class="slider__slide{" is-active" if i == 0 else ""}">'
    f'{img(n, sizes="100vw", priority=i == 0, lazy=i != 0)}</figure>' for i, n in enumerate(SLIDES))
SLIDER_DOTS = "".join(f'<li><span class="ctrl__seg"{" aria-current=" + chr(34) + "true" + chr(34) if i == 0 else ""}></span></li>' for i in range(len(SLIDES)))

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
LOGO_ITEMS = "".join(f'<li class="logos__item{" logos__item--dark" if n in LOGOS_SOMBRES else ""}">{img("logos/" + n, a, sizes="200px")}</li>' for n, a in LOGOS)
CHEV_L = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 5l7 7-7 7"/></svg>'

# ---------------------------------------------------------------- Vidéo de présentation (composant Bento « Block/Video »)
# Façade (affiche + bouton) : la vidéo n'est chargée qu'au clic (assets/site.js). Sans JS, le lien ouvre le MP4.
# Source : docs/retourclient/images/Vidéo présentation PEA FRANÇAIS.mp4 (4K HEVC, 333 Mo) recompressée en H.264 1080p / 720p.
PLAY_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5v14l11-7z"/></svg>'


def video_block(heading_id, h="h2"):
    return f"""
<section class="section section--brun video-block" aria-labelledby="{heading_id}" data-bento="Block/Video">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Le Parc en vidéo</p><{h} id="{heading_id}">Découvrez le Parc en 1 min 37.</{h}></div>
    <div class="video" data-video>
      <a class="video__facade" href="assets/video/presentation-pea-1080.mp4" data-video-hd="assets/video/presentation-pea-1080.mp4" data-video-sd="assets/video/presentation-pea-720.mp4" data-video-title="Vidéo de présentation du Parc des Expositions d’Abidjan">
        {img("video/presentation-poster", "", "(min-width: 1320px) 1320px, 100vw")}
        <span class="video__play" aria-hidden="true">{PLAY_ICON}</span>
        <span class="sr-only">Voir la vidéo de présentation (1 min 37, en français)</span>
      </a>
    </div>
    <p class="video__meta">1 min 37 · en français</p>
  </div>
</section>
"""


# ---------------------------------------------------------------- Accueil
PAGES["index.html"] = ("Accueil — Parc des Expositions d’Abidjan", f"""
<section class="hero hero--slider hero--under-header" data-slider data-bento="Block/Hero">
  <div class="slider" aria-hidden="true">
{SLIDES_HTML}
  </div>
  <span class="hero__arch" aria-hidden="true"></span>
  <a class="scroll-cue" href="#decouvrir" aria-label="Aller à la section suivante"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6"/></svg></a>
  <div class="ctrl ctrl--on-photo slider__controls" role="group" aria-label="Diaporama" data-bento="Carousel">
    <p class="ctrl__count"><span class="sr-only">Image </span><span data-ctrl-current>01</span> / {len(SLIDES):02d}</p>
    <ol class="ctrl__track" role="list" aria-hidden="true">{SLIDER_DOTS}</ol>
    <button type="button" class="ctrl__btn" data-slide-prev aria-label="Image précédente">{CHEV_L}</button>
    <button type="button" class="ctrl__btn slider__toggle" aria-pressed="false" aria-label="Mettre le diaporama en pause"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-pause"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-play"><path d="M8 5v14l11-7z"/></svg></button>
    <button type="button" class="ctrl__btn" data-slide-next aria-label="Image suivante">{CHEV_R}</button>
  </div>
  <div class="wrap hero__inner">
    {ARCH.format(cls="arch")}
    <p class="eyebrow">Le plus grand parc exposition d’Afrique de l’Ouest</p>
    <h1>Salons, congrès et grands événements à Abidjan.</h1>
    <p class="lead">Des espaces modulables, des services complets et une destination au cœur de l’Afrique de l’Ouest.</p>
    <div class="actions"><a class="btn btn--primary" href="nos-espaces.html">Découvrir nos espaces {ARROW}</a><a class="btn btn--invert" href="contact-devis.html">Demander un devis</a></div>
  </div>
</section>

<section class="section" id="decouvrir">
  <div class="wrap">
    <div class="intro">
      <div><p class="eyebrow">Pourquoi le Parc des Expositions ?</p><h2>Un lieu conçu pour faire grandir les événements.</h2></div>
      {note("Le site doit répondre immédiatement à une question : pourquoi organiser son événement au Parc des Expositions d’Abidjan ? La réponse s’articule autour de quatre piliers : espaces, services, destination et expertise.")}
      <p>Pourquoi organiser votre événement au Parc des Expositions d’Abidjan ? Pour quatre raisons : des espaces à grande échelle, des services intégrés, une destination attractive et une expertise internationale.</p>
    </div>
    <ul class="figures figures--4 figures--light" role="list" data-bento="Block/Key figures">
      <li class="figure"><strong><span class="sr-only">6 500 m²</span><span aria-hidden="true"><span data-count="6500">6 500</span> m²</span></strong>Hall d’exposition</li>
      <li class="figure"><strong><span class="sr-only">5 000 m²</span><span aria-hidden="true"><span data-count="5000">5 000</span> m²</span></strong>Le Dôme</li>
      <li class="figure"><strong><span class="sr-only">67 000 m²</span><span aria-hidden="true"><span data-count="67000">67 000</span> m²</span></strong>Parvis & esplanades</li>
      <li class="figure"><strong><span class="sr-only">360°</span><span aria-hidden="true"><span data-count="360">360</span>°</span></strong><a class="btn btn--tertiary btn--sm" href="visite-virtuelle.html#visite">Visiter le Parc {ARROW}</a></li>
    </ul>
  </div>
</section>
{video_block("video-titre")}
<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Nos espaces</p><h2>À chaque projet, son espace.</h2></div>
    <div class="collection collection--3" data-bento="Collection">
{space("A", "Hall d’Exposition", "Salons · expositions · corporate")}
{space("B", "Le Dôme", "Conventions · conférences · concerts", ink=True)}
{space("C", "Parvis & Esplanades", "Formats outdoor · grands publics")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media media--top">{img("pages/destination-abidjan", "Abidjan de nuit : le pont et la lagune illuminés", "(min-width: 1024px) 50vw, 100vw")}<span class="badge badge--primary media__badge">Abidjan, destination MICE</span></div>
    <div>
      <p class="eyebrow">Une destination</p>
      <h2>Votre événement commence à Abidjan.</h2>
      {note("Accessibilité, hôtellerie, vie économique et rayonnement régional : la destination devient un argument commercial à part entière.")}
      <p>Accessibilité, hôtellerie, vie économique et rayonnement régional : Abidjan offre à vos participants une destination à la hauteur de votre événement.</p>
      <a class="btn btn--secondary" href="venir-a-abidjan.html">Venir à Abidjan {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Agenda</p><h2>Prochainement au Parc</h2></div>
    <div class="collection collection--3" data-bento="Collection">
{event("8–10 oct. 2026", "Auto Expo", "Salon de l’industrie automobile", href="evenement-auto-expo.html", image="auto-expo")}
{event("11 oct. 2026", "Concert TAYC", "Concert", href="evenement-concert-tayc.html", image="concert-tayc")}
{event("15–16 oct. 2026", "Brands Licensing Africa", "Salon des licences de marques", href="evenement-brands-licensing-africa.html", image="brands-licensing-africa")}
    </div>
    <p class="section__more"><a class="link-arrow" href="agenda.html">Voir tout l’agenda {ARROW}</a></p>
  </div>
</section>


<!-- Note de maquette : le fil Facebook utilise le Page Plugin officiel de Meta. Instagram et LinkedIn n’offrent pas de fil intégrable sans jeton : en production, les alimenter via un agrégateur (Curator.io, Juicer, Walls.io…) ou via les API Meta Graph et LinkedIn depuis Drupal. -->
<section class="section section--white" aria-labelledby="mur-titre">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Actualités</p><h2 id="mur-titre">Le Parc en direct</h2></div>
    <div class="wall" data-bento="Collection">
      <article class="card wall__tile wall__tile--fb" data-bento="Card" aria-labelledby="mur-fb">
        <header class="wall__head">{FB_ICON}<h3 class="wall__name t3" id="mur-fb">Facebook</h3><a class="wall__handle" href="{FB_URL}" target="_blank" rel="noopener" aria-label="Suivre le Parc sur Facebook (nouvel onglet)">Suivre {EXT}</a></header>
        <div class="wall__embed" data-embed-src="{FB_PLUGIN}" data-embed-title="Publications Facebook du Parc des Expositions d’Abidjan">
          <div class="embed-facade">
            <p>Le fil Facebook est fourni par Meta, qui peut déposer des cookies.</p>
            <button class="btn btn--secondary" type="button" data-embed-load>Afficher les publications</button>
          </div>
        </div>
      </article>
      <article class="card wall__tile wall__tile--ig" data-bento="Card" aria-labelledby="mur-ig">
        <header class="wall__head">{IG_ICON}<h3 class="wall__name t3" id="mur-ig">Instagram</h3><a class="wall__handle" href="{IG_URL}" target="_blank" rel="noopener" aria-label="Suivre parcdesexpositionsabidjan sur Instagram (nouvel onglet)">@parcdesexpositionsabidjan {EXT}</a></header>
        <ul class="wall__grid" role="list">{IG_POSTS}</ul>
      </article>
      <article class="card wall__tile wall__tile--li" data-bento="Card" aria-labelledby="mur-li">
        <header class="wall__head">{LI_ICON}<h3 class="wall__name t3" id="mur-li">LinkedIn</h3></header>
        <p>Salons, partenariats et actualités professionnelles du Parc des Expositions d’Abidjan.</p>
        <a class="btn btn--secondary" href="{LI_URL}" target="_blank" rel="noopener" aria-label="Suivre le Parc sur LinkedIn (nouvel onglet)">Suivre sur LinkedIn {EXT}</a>
      </article>
      <article class="card wall__tile wall__tile--next" data-bento="Card" aria-labelledby="mur-next">
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
    <div class="cta cta--photo" data-bento="Cta">
      <div class="cta__img" aria-hidden="true"></div>
      <p class="eyebrow">Votre prochain événement</p>
      <h2>Parlez-nous de votre projet.</h2>
      {note("Un parcours simple pour transformer une visite en demande commerciale qualifiée.")}
      <p>Décrivez votre événement en quelques minutes : notre équipe commerciale vous recontacte avec une proposition adaptée.</p>
      <a class="btn btn--primary" href="contact-devis.html">Demander un devis {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="refs-title" data-bento="Block/Partners">
  <div class="wrap">
    <div class="logos-head">
      <div><p class="eyebrow">Références</p><h2 id="refs-title">Ils nous ont fait confiance</h2></div>
      <div class="ctrl logos-controls" role="group" aria-label="Défilement des logos" data-bento="Carousel">
        <p class="ctrl__count"><span class="sr-only">Page </span><span data-ctrl-current>1</span> / <span data-ctrl-total>2</span></p>
        <ol class="ctrl__track" role="list" aria-hidden="true" data-logos-pages></ol>
        <button class="ctrl__btn" type="button" data-logos-prev aria-label="Logos précédents">{CHEV_L}</button>
        <button class="ctrl__btn logos__toggle" type="button" aria-pressed="false" aria-label="Mettre le défilement en pause"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-pause"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" class="slider__icon-play"><path d="M8 5v14l11-7z"/></svg></button>
        <button class="ctrl__btn" type="button" data-logos-next aria-label="Logos suivants">{CHEV_R}</button>
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
<dialog class="lightbox" id="lightbox" aria-label="Visionneuse de photos" data-bento="Modal">
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
    <div class="media">{img("officiel/dome-salle/salle-pleniere", "La salle plénière du Dôme, fauteuils face à la scène", "(min-width: 1024px) 50vw, 100vw")}</div>
    <div>
      <p class="eyebrow">Notre ambition</p>
      <h2>Faire d’Abidjan un point de rencontre régional.</h2>
      <p>Le Parc des Expositions d’Abidjan accueille salons, expositions, conventions, conférences, concerts et grands rendez-vous professionnels.</p>
      <p>Œuvre de l’architecte Pierre Fakhoury, ouvert au public en juillet 2023, le Parc s’étend sur 16 hectares : un Convention Center, un hall d’exposition et des espaces extérieurs.</p>
      <ul class="figures figures--tight" role="list" data-bento="Block/Key figures">
        <li class="figure"><strong>3</strong>grands univers d’espaces</li>
        <li class="figure"><strong>GL events</strong>expertise internationale</li>
      </ul>
    </div>
  </div>
</section>
{video_block("video-titre")}
<section class="section" id="destination">
  <div class="wrap">
  <div class="intro">
    <div><p class="eyebrow">Une destination</p><h2>Abidjan, ville d’affaires et d’expériences.</h2></div>
    {note("Cette section valorise l’accessibilité, l’hôtellerie, le dynamisme économique, culturel et touristique de la Côte d’Ivoire afin de soutenir la visibilité internationale du Parc.")}
    <p>Accessibilité, offre hôtelière, dynamisme économique, culturel et touristique : la Côte d’Ivoire réunit tout ce qu’il faut pour accueillir vos participants venus de la région et du monde entier.</p>
  </div>
    <div class="destination-grid block-gap" data-lightbox data-bento="Image gallery">{DESTINATION_ITEMS}</div>
    <p class="section__more"><a class="link-arrow" href="venir-a-abidjan.html">Accès, hôtels, visas : venir à Abidjan {ARROW}</a></p>
  </div>
</section>

<section class="section section--brun-fonce" id="expertise">
  <div class="wrap">
    <p class="eyebrow">Expertise</p>
    <h2>Un savoir-faire événementiel international.</h2>
    {note("Bloc destiné à présenter le rôle de GL events, ses standards d’exploitation et sa capacité à accompagner les organisateurs.")}
    <p class="lead">Le Parc s’appuie sur l’expertise de GL events et ses standards d’exploitation pour accompagner les organisateurs à chaque étape, de la conception à l’accueil du public.</p>
    <p>Depuis le 15 janvier 2025, le Parc est géré et exploité par la société Abidjan Events PEA, filiale du groupe GL events.</p>
    <p>Fort de 45 ans d’expérience, GL events gère un réseau de 61 sites événementiels en Europe, en Amérique du Sud, en Asie et en Afrique.</p>
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
    <div class="collection collection--3" id="espaces" data-bento="Collection">
{space("A", "Hall d’Exposition", "6 500 m² · 12 m sous plafond", h="h2", usage="salon corporate")}
{space("B", "Le Dôme", "5 000 m² · 4 800 assis · 9 353 assis/debout", ink=True, h="h2", usage="congres conference convention concert")}
{space("C", "Parvis & Esplanades", "67 000 m² d’espaces extérieurs", h="h2", usage="concert salon")}
    </div>
    {TYPE_LINKS}
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
        <tr><th scope="row"><a href="hall-exposition.html">Hall d’Exposition</a></th><td data-label="Surface">6 500 m²</td><td data-label="Hauteur">12 m</td><td data-label="Capacité">6 500 personnes</td><td data-label="Usages">Salons, expositions, corporate</td><td data-label="Documents"><a href="assets/fiche-technique-hall-exposition.pdf" download>Fiche technique (PDF)</a></td><td><a class="btn btn--primary btn--sm" href="contact-devis.html?espace=hall#devis" aria-label="Demander un devis pour le Hall d’Exposition">Devis</a></td></tr>
        <tr><th scope="row"><a href="le-dome.html">Le Dôme</a></th><td data-label="Surface">5 000 m²</td><td data-label="Hauteur">Non communiquée</td><td data-label="Capacité">4 800 assis · 9 353 assis/debout</td><td data-label="Usages">Conférences, institutionnel, salons, concerts</td><td data-label="Documents"><a href="{PLAN_PDF}" target="_blank" rel="noopener" aria-label="Plan du Parc, PDF (nouvel onglet)">Plan du Parc (PDF)</a></td><td><a class="btn btn--primary btn--sm" href="contact-devis.html?espace=dome#devis" aria-label="Demander un devis pour le Dôme">Devis</a></td></tr>
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
      <a class="btn btn--tertiary" href="visite-virtuelle.html#visite">Lancer la visite virtuelle {ARROW}</a>
    </div>
    <a class="media media--arch media--link" href="visite-virtuelle.html#visite" aria-label="Lancer la visite virtuelle"><span class="badge badge--primary media__badge">360°</span></a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta" data-bento="Cta">
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
    # Photos officielles (docs/retourclient/images, organisation du client du 6 novembre 2026)
    "hall-drapeaux": "Le Hall d’Exposition vide, pavoisé des drapeaux des nations sous sa charpente noire",
    "hall-portes": "Grand volume du Hall d’Exposition et ses portes de chargement",
    "hall-perspective": "Perspective du Hall d’Exposition, sol béton et charpente pavoisée",
    "dome-ciel": "La coupole du Dôme sous un ciel bleu",
    "dome-aerien": "Le Dôme vu du ciel, au milieu des esplanades",
    "dome-toiture": "La toiture ondulée du Dôme, vue de près",
    "dome-panorama": "Le Dôme et son parvis, vus depuis l’esplanade",
    "salle-pleniere": "La salle plénière du Dôme : fauteuils face à la scène",
    "salle-fauteuils": "Rangées de fauteuils de la salle du Dôme",
    "salle-parterre": "Le parterre du Dôme dégagé, sous la charpente en bois",
    "salle-gradins": "Gradins et parterre de la salle du Dôme",
    "salon-vip-galerie": "La galerie boisée des Pas Perdus du Dôme",
    "salon-vip-banc": "Les Pas Perdus du Dôme : banc et appliques murales",
    "salon-vip-oeuvre": "Les Pas Perdus du Dôme et leur œuvre d’art",
    "salon-vip-accueil": "La banque d’accueil des Pas Perdus du Dôme",
    # Plaquette commerciale (images/plaquette, tools/optimiser-images.py)
    "dome-acces-aerien": "L’allée d’accès et les parkings couverts menant au Dôme, vus du ciel",
    "salle-panorama": "Vue panoramique de la salle du Dôme, des gradins jusqu’à la scène",
    "salle-scene": "La scène du Dôme et son écran, face aux fauteuils",
    "ecran-led-arriere": "L’arrière de l’écran LED géant du Dôme",
    "loges-signaletique": "Signalétique menant aux loges d’artistes du Dôme",
    "loge-miroirs": "Loge d’artiste du Dôme : plan de travail et miroirs",
    "loge-coiffeuse": "Loge d’artiste du Dôme : coiffeuse et miroir",
    "loges-couloir": "Le couloir des loges d’artistes du Dôme",
    "pas-perdus-salon": "L’espace cocktail des Pas Perdus : fauteuils et plantes sous les boiseries",
    "pas-perdus-fauteuils": "Fauteuils et tables basses en marbre des Pas Perdus",
    "parvis-auvent": "L’auvent du Parc et sa charpente, au bord du parvis",
    "esplanade-ombrieres-aerien": "Les ombrières et une esplanade du Parc, vues du ciel",
    "esplanade-ombriere": "Une esplanade du Parc et son ombrière",
}


def official_photos(groups, featured, label, extra=()):
    """Photos officielles du client (assets/img/officiel/…, tools/optimiser-images.py) : tous les dossiers indiqués,
    plus des photos isolées (extra), image vedette en premier. Le dossier « esplanades » se remplit tout seul."""
    names = []
    for group in groups:
        names += sorted(f"{group}/{f.name[: -len('-1600.webp')]}" for f in (ROOT / "assets/img" / group).glob("*-1600.webp"))
    names += [e for e in extra if e not in names]
    names.sort(key=lambda n: n.rsplit("/", 1)[1] != featured)
    out = []
    for n in names:
        key = n.rsplit("/", 1)[1]
        if key not in ALTS:
            print(f"  ATTENTION : texte alternatif manquant pour {n}")
        out.append((n, ALTS.get(key, f"Photo — {label}")))
    return out


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
         figures=[("6 500 m²", "Surface"), ("12 m", "Hauteur libre sous plafond"), ("6 500", "Personnes accueillies")],
         h2="Un espace pensé pour les événements de grande ampleur.",
         note_txt="La fiche espace concentre l’information commerciale et technique : usages possibles, capacité, configuration, prestations associées et documents à télécharger.",
         text="Avec 6 500 m² et 12 m libres sous plafond, le Hall d’Exposition accueille jusqu’à 6 500 personnes pour vos expositions, lancements de produits, salons et conférences.",
         more=["Le Hall mesure 119,3 m de long sur 59,29 m de large, pour 12,38 m de haut.",
               "Il compte 3 bars-restaurants au rez-de-chaussée, ainsi qu’un espace lounge et une salle de réunion à l’étage."],
         usages=["Salon professionnel", "Exposition", "Lancement", "Convention"], equip=None,
         photos=official_photos(["officiel/hall"], "hall-drapeaux", "Hall d’Exposition"),
         doc=("assets/fiche-technique-hall-exposition.pdf", "Télécharger la fiche technique", True)),
    dict(file="le-dome.html", title="Le Dôme", letter="B", code="dome",
         lead="Le Convention Center du Parc : une salle de 5 000 m² équipée pour les conférences, les événements institutionnels, les salons et les concerts.",
         figures=[("5 000 m²", "Surface exploitable"), ("4 800", "Places assises en convention"), ("9 353", "Personnes en assis/debout")],
         h2="Une salle de prestige pour les grands rendez-vous.", note_txt=None,
         text="Avec 5 000 m² exploitables, le Dôme accueille 4 800 personnes assises en convention, 5 183 en dîner de gala et jusqu’à 9 353 en configuration assis/debout, avec une infrastructure technique pensée pour les événements professionnels comme pour le grand public.",
         more=["Son auditorium à gradins rétractables se prête aux congrès, conventions, salons, conférences et dîners de gala.",
               "Le Dôme dispose de 8 loges d’artistes et de 2 bureaux organisateurs.",
               "Les Pas Perdus, un espace cocktail de 581,5 m², reçoivent jusqu’à 160 personnes."],
         usages=["Conférence internationale", "Événement institutionnel", "Salon & exposition", "Concert & spectacle"],
         equip=["96 enceintes", "365 projecteurs", "240 m² d’écran LED", "Gradins rétractables", "8 loges d’artistes", "2 bureaux organisateurs"],
         photos=official_photos(["officiel/dome-salle", "officiel/dome-exterieur", "officiel/dome-salon-vip"], "salle-pleniere", "Le Dôme",
                                extra=["plaquette/" + n for n in ("salle-panorama", "salle-scene", "ecran-led-arriere", "pas-perdus-salon", "pas-perdus-fauteuils",
                                                                  "loges-signaletique", "loge-miroirs", "loge-coiffeuse", "loges-couloir", "dome-acces-aerien")]),
         doc=(None, None, False)),
    dict(file="parvis-esplanades.html", title="Parvis & Esplanades", letter="C", code="parvis",
         lead="67 000 m² d’espaces extérieurs pour les expositions et les événements en plein air.",
         figures=[("11 000 m²", "Parvis"), ("28 000 m²", "Esplanade Est"), ("28 000 m²", "Esplanade Nord-Est")],
         h2="De grands espaces extérieurs, à l’échelle de vos projets.", note_txt=None,
         text="Le Parvis et les esplanades Est et Nord-Est totalisent 67 000 m² pour les expositions extérieures, les formats outdoor et les événements grand public.",
         more=["Des chapiteaux éphémères peuvent y prolonger les expositions en plein air."],
         usages=["Exposition extérieure", "Format outdoor", "Événement grand public", "Concert"], equip=None,
         photos=official_photos(["officiel/esplanades"], "dome-panorama", "Parvis & Esplanades",
                                extra=["officiel/dome-exterieur/dome-panorama", "plaquette/parvis-auvent", "plaquette/esplanade-ombrieres-aerien",
                                       "plaquette/esplanade-ombriere", "officiel/dome-exterieur/dome-aerien"]),
         doc=(None, None, False)),
]


def space_page(sp):
    figs = "".join(f'<li class="figure"><strong>{v}</strong>{l}</li>' for v, l in sp["figures"])
    n = len(sp["photos"])
    items = "".join(gallery_item(name, alt, "(min-width: 768px) 33vw, 50vw", lazy=i > 2)
                    for i, (name, alt) in enumerate(sp["photos"]))
    usages = "".join(f'<li class="badge badge--outline">{u}</li>' for u in sp["usages"])
    equip = ""
    if sp["equip"]:
        equip_items = "".join(f'<li class="badge">{e}</li>' for e in sp["equip"])
        equip = ("\n      <h3 class=\"block-gap\" id=\"equipements\">Équipements</h3>"
                 f"\n      <ul class=\"tags\" role=\"list\">{equip_items}</ul>")
    more = "".join(f"\n      <p>{m}</p>" for m in sp.get("more", ()))
    doc_url, doc_label, local = sp["doc"]
    docs = ""
    if doc_url:
        docs += f'\n      <a class="btn btn--secondary btn--block" href="{doc_url}" download>{doc_label} <span class="btn__meta">PDF</span></a>'
    docs += f'\n      <a class="btn btn--secondary btn--block" href="{PLAQUETTE_PDF}" download>Télécharger la plaquette commerciale <span class="btn__meta">PDF</span></a>'
    docs += f'\n      <a class="link-arrow" href="{PLAN_PDF}" target="_blank" rel="noopener" aria-label="Plan du Parc, PDF (nouvel onglet)">Plan du Parc (PDF) {EXT}</a>'
    subnav_equip = '<a href="#equipements">Équipements</a>' if sp["equip"] else ""
    lead_note = note(sp["note_txt"]) if sp["note_txt"] else ""
    return (f"{sp['title']} — Parc des Expositions d’Abidjan", page_hero(
        crumbs(A, ("Nos espaces", "nos-espaces.html"), (sp["title"], None)), f"Espace {sp['letter']}",
        sp["title"], sp["lead"], compact=True) + f"""

<section class="section section--white section--tight">
  <div class="wrap">
    <nav class="subnav" aria-label="Sections de la fiche" data-bento="Tabs">
      <a href="#caracteristiques">Caractéristiques</a><a href="#galerie">Galerie</a><a href="#presentation">Présentation</a>{subnav_equip}<a href="#services-associes">Services associés</a><a href="#documents">Documents</a>
    </nav>
    <ul class="figures figures--3" id="caracteristiques" role="list" data-bento="Block/Key figures">{figs}</ul>
    <div class="gallery block-gap" id="galerie" data-lightbox data-bento="Image gallery">{items}</div>
  </div>
</section>

<section class="section">
  <div class="wrap with-aside">
    <div>
      <h2 id="presentation">{sp["h2"]}</h2>
      {lead_note}
      <p>{sp["text"]}</p>{more}
      <h3 class="block-gap">Usages recommandés</h3>
      <ul class="tags" role="list">{usages}</ul>{equip}
      <h3 class="block-gap" id="services-associes">Services associés</h3>
      <p>Audiovisuel · mobilier · restauration · sécurité · accueil · nettoyage · logistique.</p>
    </div>
    <aside class="aside-box card" id="documents" aria-labelledby="aside-espace" data-bento="Card">
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

<section class="section section--vert">
  <div class="wrap">
    <ul class="services" role="list" data-bento="Item list">
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
    <section class="support__building" aria-labelledby="batiment" data-bento="Card">
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
    <div class="media">{img("officiel/hall/hall-perspective", "Le Hall d’Exposition, sol béton et charpente pavoisée, prêt à être aménagé", "(min-width: 1024px) 50vw, 100vw")}</div>
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
    ("officiel/dome-exterieur/dome-ciel", "dome", "lieux", "La coupole du Dôme sous un ciel bleu"),
    ("officiel/hall/hall-drapeaux", "hall", "lieux", "Le Hall d’Exposition pavoisé des drapeaux des nations"),
    ("officiel/dome-salle/salle-pleniere", "dome", "lieux", "La salle plénière du Dôme"),
    ("officiel/dome-salon-vip/salon-vip-oeuvre", "dome", "lieux", "Les Pas Perdus du Dôme et leur œuvre d’art"),
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
    + filters("Filtrer par type d’événement", ["Tous", "Lieux", "Salons", "Concerts", "Sport"], "photos", "type", row_label="Type")
    + "</div>",
    lead_note=note("Une galerie immersive organisée par espace et par type d’événement, pensée autant pour l’inspiration que pour la preuve commerciale.")) + f"""

<section class="section section--white">
  <div class="wrap">
    {results("photos", f"{len(PHOTOS)} photos", "Aucune photo pour cette combinaison. Essayez un autre espace ou un autre type d’événement.")}
    <!-- Espaces et types des photos déduits des images : à confirmer par le Parc -->
    <div class="photo-grid" id="photos" data-lightbox data-bento="Image gallery">{photo_items}</div>
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
    <ol class="timeline" id="evenements" role="list" data-bento="Block/Agenda list">
{timeline()}
    </ol>
    <dialog class="event-dialog" id="event-dialog" aria-labelledby="event-dialog-title" data-bento="Modal">
      <button class="event-dialog__close" type="button" aria-label="Fermer la fenêtre"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
      <img class="event-dialog__img" src="data:," alt="" width="800" height="450" hidden>
      <div class="event-dialog__head">
        <p class="event-dialog__type badge badge--primary"></p>
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
        <a class="btn btn--invert" href="nos-espaces.html">Découvrir nos espaces {ARROW}</a>
      </div>
    </div>"""

# Photo du totem : dans l’encadré « Nous contacter » (et non plus dans l’en-tête)
CONTACT_TOTEM = img("officiel/dome-salon-vip/salon-vip-accueil", "La banque d’accueil des Pas Perdus du Dôme", "(min-width: 1024px) 340px, 100vw")
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
    <aside class="aside-box card" id="nous-contacter" aria-labelledby="aside-contact" data-bento="Card">
      <figure class="aside-box__media">{CONTACT_TOTEM}</figure>
      <p class="eyebrow">Parc des Expositions d’Abidjan</p>
      <h2 class="t3" id="aside-contact">Nous contacter</h2>
      <address class="contact-details" data-bento="Contact details"><span>{TEL}</span><span>Boulevard de l’aéroport<br>Abidjan · Côte d’Ivoire</span></address>
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
    <div class="access__map" data-bento="Block/Map" data-embed-src="https://maps.google.com/maps?q=5.2634735,-3.9465668&amp;hl=fr&amp;z=16&amp;output=embed" data-embed-title="Carte : localisation du Parc des Expositions d’Abidjan">
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
    <div class="tour" id="visite" data-bento="Block/Video">
      <a class="tour__launch" href="https://my.matterport.com/show/?m=aNcgwUfY8uk" target="_blank" rel="noopener" data-tour-src="https://my.matterport.com/show/?m=aNcgwUfY8uk&amp;play=1" data-tour-title="Visite virtuelle 360° du Parc des Expositions d’Abidjan">{PLAY}<span>Lancer <br>la visite <br>360°</span></a>
    </div>
    <div class="tour__legend"><p class="filter-row__label" id="tour-espaces">Espaces visitables</p><ul class="tags" role="list" aria-labelledby="tour-espaces"><li class="badge badge--outline">Hall d’Exposition</li><li class="badge badge--outline">Le Dôme</li><li class="badge badge--outline">Parvis</li><li class="badge badge--outline">Esplanades</li></ul></div>
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
    fr_abs, en_abs = page_url(page, "fr"), page_url(page, "en")
    alt = (f'<link rel="alternate" hreflang="fr" href="{fr_abs}">\n<link rel="alternate" hreflang="en" href="{en_abs}">\n'
           f'<link rel="alternate" hreflang="x-default" href="{fr_abs}">\n</head>')
    return src.replace("</head>", alt, 1)


# Image de l’en-tête de chaque page : photo dans la silhouette exacte de l’arche du logo (variante E2 « dôme posé »)
PAGE_BG = {
    "qui-sommes-nous.html": "officiel/dome-exterieur/dome-ciel",
    "nos-espaces.html": "officiel/dome-exterieur/dome-aerien",
    "hall-exposition.html": "officiel/hall/hall-perspective",
    "le-dome.html": "officiel/dome-exterieur/dome-toiture",
    "parvis-esplanades.html": "officiel/dome-exterieur/dome-panorama",
    "nos-services.html": "officiel/hall/hall-portes",
    "phototheque.html": "phototheque/dome-lumieres",
    "agenda.html": "officiel/dome-salle/salle-gradins",
    "contact-devis.html": "officiel/dome-salle/salle-fauteuils",
    "visite-virtuelle.html": "officiel/dome-salle/salle-parterre",
    "informations-legales.html": "officiel/dome-salon-vip/salon-vip-galerie",
}


def with_page_id(page, src):
    """Pose sur <body> un id et une classe au nom de la page (fichier sans .html)."""
    slug = page.removesuffix(".html")
    return src.replace("<body>", f'<body id="{slug}" class="{slug}">', 1)


def with_page_bg(name, src):
    bg = PAGE_BG.get(name)
    if not bg:
        return src
    return src.replace('<section class="page-hero', f'<section style="--page-bg: url(assets/img/{bg}-1600.webp)" class="page-hero page-hero--bg', 1)


# Référencement (balises, données structurées, sitemap) et nouvelles pages : tools/pages/referencement.py
exec(pathlib.Path(__file__).with_name("referencement.py").read_text(encoding="utf-8"))

# ---------------------------------------------------------------- Composants Bento : marquage explicite
# Chaque composant porte data-bento="<nom Figma>" (contrôlé par tools/verif/conformite.mjs). Les titres reçoivent
# la classe du composant « Title » selon leur niveau VISUEL (pas seulement la balise) :
#   h1 → L1 (48 px) · h2 → L2 (30 px) · h2.t3 / h3 → L4 (20 px, cartes et encarts) · intertitres d’agenda → L3 (24 px)
TITLE_LEVEL_BY_CLASS = {"timeline__month-title": 3, "newsletter__title": 3, "event-dialog__title": 2, "footer__title": 5,
                        "consent__title": 5, "card__title": 4, "t3": 4}


def _title_level(tag, classes):
    for k, v in TITLE_LEVEL_BY_CLASS.items():
        if k in classes:
            return v
    return {"h1": 1, "h2": 2, "h3": 4, "h4": 5}[tag]


def bentoize(src):
    def heading(m):
        tag, attrs = m.group(1), m.group(2) or ""
        cm = re.search(r'class="([^"]*)"', attrs)
        classes = cm.group(1).split() if cm else []
        lvl = _title_level(tag, classes)
        new = " ".join(dict.fromkeys(classes + ["title", f"title--l{lvl}"]))
        attrs = attrs.replace(cm.group(0), f'class="{new}"') if cm else f' class="{new}"' + attrs
        return f'<{tag}{attrs} data-bento="Title">'
    src = re.sub(r'<(h[1-4])(\s[^>]*)?>', heading, src)
    def mark(cls, name):
        return lambda s: re.sub(r'(<[a-z]+ [^>]*class="(?:[^"]* )?' + cls + r'(?: [^"]*)?")(?![^>]*data-bento)', r'\1 data-bento="' + name + '"', s)
    for cls, name in (("btn", "Button"), ("badge", "Badge"), ("field", "Form/Field"), ("link-arrow", "Link")):
        src = mark(cls, name)(src)
    return src


(ROOT / "en").mkdir(exist_ok=True)
for name, (title, body) in PAGES.items():
    fr_html = bentoize(with_page_bg(name, head(title) + "\n" + header(name) + body + FOOTER))
    en_html = to_english(name, fr_html.replace("__FR__", "../" + name).replace("__EN__", name))
    (ROOT / name).write_text(with_page_id(name, with_lang_links(name, apply_seo(name, fr_html, "fr"), "fr")), encoding="utf-8")
    (ROOT / "en" / name).write_text(with_page_id(name, with_lang_links(name, apply_seo(name, en_html, "en"), "en")), encoding="utf-8")
    print("écrit", name, "+ en/" + name)
write_sitemap()

# ---------------------------------------------------------------- Planche d’index (inchangée sur le fond)
LINKS = [("index.html", "Accueil"), ("qui-sommes-nous.html", "Qui Sommes Nous"), ("nos-espaces.html", "Nos Espaces"),
         ("hall-exposition.html", "Hall Exposition"), ("le-dome.html", "Le Dome"), ("parvis-esplanades.html", "Parvis Esplanades"), ("nos-services.html", "Nos Services"), ("phototheque.html", "Phototheque"),
         ("agenda.html", "Agenda"), ("evenement-auto-expo.html", "Page événement (Auto Expo)"), ("contact-devis.html", "Contact Devis"),
         ("salons-professionnels.html", "Salons professionnels"), ("congres-conferences.html", "Congrès et conférences"),
         ("evenements-entreprise.html", "Événements d’entreprise"), ("concerts-spectacles.html", "Concerts et spectacles"), ("venir-a-abidjan.html", "Venir à Abidjan"),
         ("visite-virtuelle.html", "Visite Virtuelle"), ("informations-legales.html", "Informations Legales")]
links = "\n".join(f'      <li><a href="{h}">{t} {ARROW}</a></li>' for h, t in LINKS)
index = head("Parc des Expositions d’Abidjan — Planche HTML").replace("</head>", '<meta name="robots" content="noindex">\n</head>') + f"""
<body>
<main class="hub" id="contenu">
  <div class="wrap">
    <img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan" width="394" height="210" class="hub__logo">
    <p class="eyebrow">Parc des Expositions d’Abidjan · Charte officielle + Bento DS</p>
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
index = bentoize(index)
(ROOT / "planches.html").write_text(with_page_id("planches.html", with_lang_links("planches.html", index, "fr")), encoding="utf-8")
(ROOT / "en" / "planches.html").write_text(with_page_id("planches.html", with_lang_links("planches.html", to_english("planches.html", index), "en")), encoding="utf-8")
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
(ROOT / "accueil.html").write_text(with_page_id("accueil.html", REDIRECT.format(lang="fr", label="Accueil du Parc des Expositions d’Abidjan")), encoding="utf-8")
(ROOT / "en" / "accueil.html").write_text(with_page_id("accueil.html", REDIRECT.format(lang="en", label="Abidjan Exhibition Center home page")), encoding="utf-8")
# Ancienne fiche événement (gabarit) : remplacée par une page par événement
_to_auto = lambda t: t.replace("index.html", "evenement-auto-expo.html")
(ROOT / "fiche-evenement.html").write_text(with_page_id("fiche-evenement.html", _to_auto(REDIRECT.format(lang="fr", label="Auto Expo au Parc des Expositions d’Abidjan"))), encoding="utf-8")
(ROOT / "en" / "fiche-evenement.html").write_text(with_page_id("fiche-evenement.html", _to_auto(REDIRECT.format(lang="en", label="Auto Expo at the Abidjan Exhibition Center"))), encoding="utf-8")
print("écrit accueil.html (redirection)")
