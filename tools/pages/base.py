#!/usr/bin/env python3
"""Constantes partagées (icônes, arche, navigation, polices, <head>) — importées par generer.py."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

ARROW = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
ARCH = ('<svg class="{cls}" viewBox="16 -1 360 68" aria-hidden="true" focusable="false">'
        '<path d="M20 61C70 54 120 25.5 150 12C164 5.7 182 0 196 0C210 0 228 5.7 242 12C272 25.5 322 54 372 61L372 61.5C322 54.5 272 31 242 17.5C226 10.5 210 6.5 196 6.5C182 6.5 166 10.5 150 17.5C120 31 70 54.5 20 61.5Z"/><path d="M36 64.8C100 54 150 47 200 47C250 47 300 54 364 64.8L364 65.3C300 57 250 50.5 200 50.5C150 50.5 100 57 36 65.3Z"/></svg>')

NAV = [
    ("qui-sommes-nous.html", "Qui sommes-nous ?"),
    ("nos-espaces.html", "Nos espaces"),
    ("nos-services.html", "Nos services"),
    ("phototheque.html", "Photothèque"),
    ("agenda.html", "Agenda"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800'
         '&amp;family=Barlow:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">')


def head(title):
    return f"""<!doctype html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<script>document.documentElement.classList.replace('no-js','js')</script>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="styles.css">
<script src="assets/site.js" defer></script>
</head>"""


CUR = ' aria-current="page"'


def header(active):
    items = "\n".join(
        f'      <li><a href="{href}"{CUR if href == active else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="topbar">
  <div class="wrap topbar__inner">
    <a class="brand" href="accueil.html"><img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan — accueil" width="394" height="210"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-principale"><span class="menu-toggle__bars" aria-hidden="true"></span>Menu</button>
    <nav class="nav" id="nav-principale" aria-label="Navigation principale">
      <ul>
{items}
      </ul>
    </nav>
    <a class="btn btn--primary topbar__cta" href="contact-devis.html"{CUR if active == "contact-devis.html" else ""}><span><span class="hide-sm">Demander un </span>devis</span></a>
  </div>
</header>
<main class="page" id="contenu" tabindex="-1">"""


FOOTER = """</main>
<footer class="footer">
  <div class="wrap footer__grid">
    <div class="footer__brand">
      <img src="assets/logo-pea.webp" alt="" width="394" height="210" loading="lazy">
      <p><b>PEA — Parc des Expositions d’Abidjan</b><br>Boulevard de l’aéroport · Abidjan · Côte d’Ivoire</p>
    </div>
    <p class="footer__links">Espaces · Services · Destination · Expertise · FR / EN</p>
  </div>
</footer>
</body>
</html>
"""


def crumbs(*parts):
    """parts: (label, href|None) ; le dernier est la page courante."""
    lis = []
    for i, (label, href) in enumerate(parts):
        if i == len(parts) - 1:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
        else:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Fil d’Ariane"><ol role="list">{"".join(lis)}</ol></nav>'


def filters(label, items, cls="filters"):
    btns = "".join(
        f'<button class="chip" type="button" aria-pressed="{"true" if i == 0 else "false"}">{t}</button>'
        for i, t in enumerate(items)
    )
    return f'<div class="{cls}" role="group" aria-label="{label}" data-filters>{btns}</div>'


def page_hero(crumb, eyebrow, h1, lead, extra=""):
    return f"""
<section class="page-hero">
  <div class="wrap">
    {crumb}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>{extra}
  </div>
</section>"""


def space(letter, title, sub, media, ink=False, h="h3"):
    return f"""      <a class="space{' space--ink' if ink else ''}" href="fiche-espace.html">
        <div class="space__media {media}"></div>
        <div class="space__plate"><span class="space__letter" aria-hidden="true">{letter}</span><div><{h}{' class="t3"' if h == "h2" else ""}>{title}</{h}><p>{sub}</p></div>{ARROW}</div>
      </a>"""


def event(tag, date, title, place, h="h3"):
    href = ' href="fiche-evenement.html"' if tag == "a" else ""
    return f"""      <{tag} class="event"{href}>
        <div class="event__thumb"></div>
        <div class="event__body"><span class="date">{date}</span><{h}{' class="t3"' if h == "h2" else ""}>{title}</{h}><p>{place}</p></div>
      </{tag}>"""


A = "Accueil", "accueil.html"

PAGES = {}

# ---------------------------------------------------------------- Accueil
PAGES["accueil.html"] = ("Accueil — PEA", f"""
<section class="hero">
  <div class="hero__img" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    {ARCH.format(cls="arch")}
    <p class="eyebrow">Abidjan · Côte d’Ivoire</p>
    <h1>Le lieu des grands rendez-vous.</h1>
    <p class="lead">Des espaces modulables, des services complets et une destination au cœur de l’Afrique de l’Ouest.</p>
    <div class="actions"><a class="btn btn--primary" href="nos-espaces.html">Découvrir nos espaces {ARROW}</a><a class="btn btn--secondary" href="contact-devis.html">Demander un devis</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="intro">
      <div><p class="eyebrow">Pourquoi le PEA ?</p><h2>Un lieu conçu pour faire grandir les événements.</h2></div>
      <p>Le site doit répondre immédiatement à une question : pourquoi organiser son événement au Parc des Expositions d’Abidjan ? La réponse s’articule autour de quatre piliers : espaces, services, destination et expertise.</p>
    </div>
    <ul class="figures figures--4" role="list">
      <li class="figure figure--ink"><strong>6 500 m²</strong>Hall d’exposition</li>
      <li class="figure"><strong>5 000 m²</strong>Le Dôme</li>
      <li class="figure"><strong>67 000 m²</strong>Parvis & esplanades</li>
      <li class="figure"><strong>360°</strong>Visite virtuelle</li>
    </ul>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Nos espaces</p><h2>À chaque projet, son espace.</h2></div>
    <div class="spaces">
{space("A", "Hall d’Exposition", "Salons · expositions · corporate", "media--photo")}
{space("B", "Le Dôme", "Conventions · conférences · concerts", "media--arch", ink=True)}
{space("C", "Parvis & Esplanades", "Formats outdoor · grands publics", "media--plan")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media media--photo"><span class="plaque">Abidjan, destination MICE</span></div>
    <div>
      <p class="eyebrow">Une destination</p>
      <h2>Votre événement commence à Abidjan.</h2>
      <p>Accessibilité, hôtellerie, vie économique et rayonnement régional : la destination devient un argument commercial à part entière.</p>
      <a class="btn btn--secondary" href="qui-sommes-nous.html">Découvrir la destination {ARROW}</a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Agenda</p><h2>Prochainement au Parc</h2></div>
    <div class="agenda">
{event("article", "À VENIR", "Salon professionnel", "Hall d’Exposition")}
{event("article", "À VENIR", "Convention d’entreprise", "Le Dôme")}
{event("article", "À VENIR", "Événement grand public", "Parvis & Esplanades")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta">
      {ARCH.format(cls="cta__arch")}
      <p class="eyebrow">Votre prochain événement</p>
      <h2>Parlez-nous de votre projet.</h2>
      <p>Un parcours simple pour transformer une visite en demande commerciale qualifiée.</p>
      <a class="btn btn--primary" href="contact-devis.html">Demander un devis {ARROW}</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Qui sommes-nous
PAGES["qui-sommes-nous.html"] = ("Qui sommes-nous ? — PEA", page_hero(
    crumbs(A, ("Qui sommes-nous ?", None)), "Le Parc",
    "Un équipement majeur au service des grands événements.",
    "Une présentation institutionnelle plus éditoriale, orientée vers la preuve, la destination et l’expertise.") + f"""

<section class="section section--white">
  <div class="wrap split">
    <div class="media media--photo"></div>
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

<section class="section">
  <div class="wrap intro">
    <div><p class="eyebrow">Une destination</p><h2>Abidjan, ville d’affaires et d’expériences.</h2></div>
    <p>Cette section valorise l’accessibilité, l’hôtellerie, le dynamisme économique, culturel et touristique de la Côte d’Ivoire afin de soutenir la visibilité internationale du Parc.</p>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <p class="eyebrow">Expertise</p>
    <h2>Un savoir-faire événementiel international.</h2>
    <p class="lead">Bloc destiné à présenter le rôle de GL events, ses standards d’exploitation et sa capacité à accompagner les organisateurs.</p>
  </div>
</section>
""")

# ---------------------------------------------------------------- Nos espaces
PAGES["nos-espaces.html"] = ("Nos espaces — PEA", page_hero(
    crumbs(A, ("Nos espaces", None)), "Espaces",
    "Des espaces à la hauteur de vos ambitions.",
    "Une entrée simple par capacité, usage et configuration, avec accès direct à la visite virtuelle et aux fiches techniques.",
    "\n    " + filters("Filtrer par usage", ["Salon", "Congrès", "Conférence", "Convention", "Concert", "Corporate"])) + f"""

<section class="section section--white">
  <div class="wrap">
    <div class="spaces">
{space("A", "Hall d’Exposition", "6 500 m² · 17 m sous plafond", "media--photo", h="h2")}
{space("B", "Le Dôme", "5 000 m² · 5 023 assis · 9 588 debout", "media--arch", ink=True, h="h2")}
{space("C", "Parvis & Esplanades", "67 000 m² d’espaces extérieurs", "media--plan", h="h2")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Visite virtuelle</p>
      <h2>Explorez les espaces avant votre visite.</h2>
      <p>Un accès direct à la visite 360° depuis la page Espaces permet d’accélérer la qualification commerciale.</p>
      <a class="btn btn--primary" href="visite-virtuelle.html#visite">Lancer la visite virtuelle {ARROW}</a>
    </div>
    <div class="media media--arch"><span class="plaque">360°</span></div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Fiche espace
PAGES["fiche-espace.html"] = ("Hall d’Exposition — PEA", page_hero(
    crumbs(A, ("Nos espaces", "nos-espaces.html"), ("Hall d’Exposition", None)), "Fiche espace",
    "Hall d’Exposition",
    "Un espace de grande capacité dédié aux salons, expositions et événements corporate.") + f"""

<section class="section section--white">
  <div class="wrap">
    <div class="gallery" id="galerie"><div></div><div></div><div></div><div></div><div></div></div>
    <ul class="figures figures--3 figures--tight" id="caracteristiques" role="list">
      <li class="figure figure--ink"><strong>6 500 m²</strong>Surface</li>
      <li class="figure"><strong>17 m</strong>Hauteur sous plafond</li>
      <li class="figure"><strong>Modulable</strong>Configurations multiples</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap with-aside">
    <div>
      <nav class="subnav" aria-label="Sections de la fiche">
        <a href="#presentation" aria-current="true">Présentation</a><a href="#caracteristiques">Caractéristiques</a><a href="#equipements">Équipements</a><a href="#galerie">Galerie</a><a href="#documents">Documents</a>
      </nav>
      <h2 id="presentation">Un espace pensé pour les événements de grande ampleur.</h2>
      <p>La fiche espace concentre l’information commerciale et technique : usages possibles, capacité, configuration, prestations associées et documents à télécharger.</p>
      <h3 class="block-gap">Usages recommandés</h3>
      <ul class="tags" role="list"><li>Salon professionnel</li><li>Exposition</li><li>Lancement</li><li>Convention</li></ul>
      <h3 class="block-gap" id="equipements">Services associés</h3>
      <p>Audiovisuel · mobilier · restauration · sécurité · accueil · nettoyage · logistique.</p>
    </div>
    <aside class="aside-box" id="documents" aria-labelledby="aside-espace">
      <p class="eyebrow">Organiser ici</p>
      <h3 id="aside-espace">Votre projet dans le Hall ?</h3>
      <p>Accédez au formulaire de devis avec l’espace pré-sélectionné.</p>
      <a class="btn btn--primary btn--block" href="contact-devis.html">Demander un devis {ARROW}</a>
      <a class="btn btn--secondary btn--block" href="#documents">Télécharger la fiche technique</a>
    </aside>
  </div>
</section>
""")

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
PAGES["nos-services.html"] = ("Nos services — PEA", page_hero(
    crumbs(A, ("Nos services", None)), "Services",
    "Tout ce qu’il faut pour faire fonctionner votre événement.",
    "Une présentation claire des prestations pour transformer le Parc en solution complète, pas seulement en location d’espace.") + f"""

<section class="section section--ink">
  <div class="wrap">
    <ul class="services" role="list">
{service_items}
    </ul>
  </div>
</section>

<section class="section section--white">
  <div class="wrap split">
    <div class="media media--plan"></div>
    <div>
      <p class="eyebrow">Sur mesure</p>
      <h2>Composez les services adaptés à votre événement.</h2>
      <p>Chaque service renvoie vers une demande qualifiée, afin que l’équipe commerciale récupère immédiatement le contexte du besoin.</p>
      <a class="btn btn--primary" href="contact-devis.html">Demander un service {ARROW}</a>
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Photothèque
PAGES["phototheque.html"] = ("Photothèque — PEA", page_hero(
    crumbs(A, ("Photothèque", None)), "Photothèque",
    "Le Parc en images.",
    "Une galerie immersive organisée par espace et par type d’événement, pensée autant pour l’inspiration que pour la preuve commerciale.",
    "\n    " + filters("Filtrer les photos", ["Tous", "Hall", "Dôme", "Extérieurs", "Salons", "Concerts"])) + """

<section class="section section--white">
  <div class="wrap">
    <div class="photo-grid"><div></div><div></div><div></div><div></div><div></div></div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Agenda
PAGES["agenda.html"] = ("Agenda — PEA", page_hero(
    crumbs(A, ("Agenda", None)), "Agenda",
    "Les prochains événements au Parc.",
    "Un listing filtrable par date et catégorie, avec une URL dédiée pour chaque événement afin de soutenir le référencement.",
    "\n    " + filters("Filtrer par catégorie", ["Tous", "Salons", "Congrès", "Conférences", "Concerts", "Expositions"])) + f"""

<section class="section section--white">
  <div class="wrap">
    <div class="agenda">
{event("a", "EXEMPLE · À VENIR", "Salon professionnel", "Hall d’Exposition", h="h2")}
{event("a", "EXEMPLE · À VENIR", "Convention business", "Le Dôme", h="h2")}
{event("a", "EXEMPLE · À VENIR", "Concert grand public", "Parvis", h="h2")}
    </div>
  </div>
</section>
""")

# ---------------------------------------------------------------- Fiche événement
PAGES["fiche-evenement.html"] = ("Événement — PEA", f"""
<section class="hero hero--small">
  <div class="hero__img" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    {crumbs(A, ("Agenda", "agenda.html"), ("Salon professionnel", None)).replace('class="breadcrumbs"', 'class="breadcrumbs breadcrumbs--ink"')}
    <p class="eyebrow">Agenda · Exemple de gabarit</p>
    <h1>Salon professionnel</h1>
    <p class="lead">Un gabarit événement optimisé pour la lisibilité, le partage social et le référencement.</p>
  </div>
</section>

<section class="section section--white">
  <div class="wrap with-aside">
    <div>
      <ul class="figures figures--3 figures--facts" role="list">
        <li class="figure"><strong>Date</strong>À renseigner</li>
        <li class="figure"><strong>Lieu</strong>Hall d’Exposition</li>
        <li class="figure"><strong>Public</strong>Professionnels</li>
      </ul>
      <h2 class="block-gap">À propos de l’événement</h2>
      <p>Zone administrable Drupal pour la présentation, le programme, les liens utiles, l’organisateur et les informations pratiques.</p>
      <div class="media media--plan block-gap"></div>
    </div>
    <aside class="aside-box" aria-labelledby="aside-event">
      <p class="eyebrow">Informations</p>
      <h3 id="aside-event">Préparez votre visite</h3>
      <p>Accès, horaires, transport, parking et informations visiteurs.</p>
      <a class="btn btn--primary btn--block" href="contact-devis.html">Contacter le Parc {ARROW}</a>
    </aside>
  </div>
</section>
""")

# ---------------------------------------------------------------- Contact & devis
def field(fid, label, control, full=False):
    return f'      <div class="field{" field--full" if full else ""}"><label for="{fid}">{label}</label>{control}</div>'

FORM = "\n".join([
    field("nom", "Nom", '<input id="nom" name="nom" autocomplete="name" placeholder="Votre nom">'),
    field("entreprise", "Entreprise", '<input id="entreprise" name="entreprise" autocomplete="organization" placeholder="Votre entreprise">'),
    field("email", "E-mail", '<input id="email" name="email" type="email" autocomplete="email" placeholder="nom@entreprise.com">'),
    field("telephone", "Téléphone", '<input id="telephone" name="telephone" type="tel" autocomplete="tel" placeholder="+225 …">'),
    field("type", "Type d’événement", '<select id="type" name="type"><option>Salon</option><option>Congrès</option><option>Conférence</option><option>Convention</option><option>Concert</option></select>'),
    field("participants", "Nombre de participants", '<input id="participants" name="participants" inputmode="numeric" placeholder="Ex. 800">'),
    field("espace", "Espace envisagé", '<select id="espace" name="espace"><option>Je ne sais pas encore</option><option>Hall d’Exposition</option><option>Le Dôme</option><option>Parvis & Esplanades</option></select>'),
    field("date", "Date envisagée", '<input id="date" name="date" type="text" inputmode="numeric" placeholder="JJ/MM/AAAA">'),
    field("services", "Services nécessaires", '<input id="services" name="services" placeholder="Audiovisuel, mobilier, restauration…">', full=True),
    field("projet", "Décrivez votre projet", '<textarea id="projet" name="projet" placeholder="Quelques lignes sur votre événement"></textarea>', full=True),
    f'      <div class="field field--full"><button class="btn btn--primary" type="button">Envoyer ma demande {ARROW}</button></div>',
])

PAGES["contact-devis.html"] = ("Contact & Devis — PEA", page_hero(
    crumbs(A, ("Contact", None)).replace('<li><span aria-current="page">Contact</span></li>',
                                         '<li><span>Contact</span></li><li><span aria-current="page">Devis</span></li>'),
    "Contact",
    "Parlez-nous de votre projet.",
    "Le formulaire devient un véritable outil de qualification commerciale.") + f"""

<section class="section section--white">
  <div class="wrap with-aside">
    <form class="form" aria-label="Demande de devis">
{FORM}
    </form>
    <aside class="aside-box" aria-labelledby="aside-contact">
      <p class="eyebrow">Parc des Expositions d’Abidjan</p>
      <h2 class="t3" id="aside-contact">Nous contacter</h2>
      <p><a href="tel:+2252721710997">+225 27 21 71 09 97</a></p>
      <p>Boulevard de l’aéroport<br>Abidjan · Côte d’Ivoire</p>
      <p class="note">Les soumissions peuvent être enregistrées dans Drupal et routées vers l’équipe commerciale.</p>
    </aside>
  </div>
</section>
""")

# ---------------------------------------------------------------- Visite virtuelle
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 4v16l13-8z"/></svg>'
PAGES["visite-virtuelle.html"] = ("Visite virtuelle — PEA", page_hero(
    crumbs(A, ("Nos espaces", "nos-espaces.html"), ("Visite virtuelle", None)), "Visite 360°",
    "Explorez le Parc à distance.",
    "Un gabarit léger pour intégrer le module de visite virtuelle existant ou futur sans casser la navigation du site.") + f"""

<section class="section section--white">
  <div class="wrap">
    <div class="tour" id="visite">
      <a class="tour__launch" href="https://my.matterport.com/show/?m=aNcgwUfY8uk" target="_blank" rel="noopener" data-tour-src="https://my.matterport.com/show/?m=aNcgwUfY8uk&amp;play=1" data-tour-title="Visite virtuelle 360° du Parc des Expositions d’Abidjan">{PLAY}<span>Lancer <br>la visite <br>360°</span></a>
    </div>
    {filters("Choisir un espace", ["Hall d’Exposition", "Le Dôme", "Parvis", "Esplanades"])}
  </div>
</section>
""")

# ---------------------------------------------------------------- Écriture
for name, (title, body) in PAGES.items():
    html = head(title) + "\n" + header(name) + body + FOOTER
    (ROOT / name).write_text(html, encoding="utf-8")
    print("écrit", name)

# ---------------------------------------------------------------- Planche d'index
LINKS = [("accueil.html", "Accueil"), ("qui-sommes-nous.html", "Qui Sommes Nous"), ("nos-espaces.html", "Nos Espaces"),
         ("fiche-espace.html", "Fiche Espace"), ("nos-services.html", "Nos Services"), ("phototheque.html", "Phototheque"),
         ("agenda.html", "Agenda"), ("fiche-evenement.html", "Fiche Evenement"), ("contact-devis.html", "Contact Devis"),
         ("visite-virtuelle.html", "Visite Virtuelle")]
links = "\n".join(f'      <li><a href="{h}">{t} {ARROW}</a></li>' for h, t in LINKS)
index = head("PEA — Planche HTML").replace('<html lang="fr" class="no-js">', '<html lang="fr" class="no-js">') + f"""
<body>
<main class="hub" id="contenu">
  <div class="wrap">
    <img src="assets/logo-pea.webp" alt="Parc des Expositions d’Abidjan" width="394" height="210" class="hub__logo">
    <p class="eyebrow">PEA · Proposition 1 · The Seed-inspired</p>
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
(ROOT / "index.html").write_text(index, encoding="utf-8")
print("écrit index.html")
