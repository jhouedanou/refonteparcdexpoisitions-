# Référencement de la maquette — exécuté par generer.py juste avant l'écriture des pages (mêmes variables globales).
# Contenu : balises de chaque page (titre, description, canonique, Open Graph, Twitter), données structurées
# Schema.org (lieu, espaces, événements, fil d'Ariane, FAQ), sitemap.xml + robots.txt, et les nouvelles pages
# (4 pages par type d'événement, « Venir à Abidjan », une page par événement de l'agenda).
import html as _h
import json as _js

SITE = "https://pae-orpin.vercel.app/"  # adresse de la maquette : remplacer par le domaine du Parc à la mise en ligne
NAME_FR, NAME_EN = "Parc des Expositions d’Abidjan", "Abidjan Exhibition Center"
OG_DEFAULT = "slider/dome-rendu"
ADDRESS = {"@type": "PostalAddress", "streetAddress": "Boulevard de l’aéroport", "addressLocality": "Abidjan",
           "addressRegion": "Port-Bouët", "addressCountry": "CI"}
GEO = {"@type": "GeoCoordinates", "latitude": 5.2634735, "longitude": -3.9465668}
VENUE_ID = SITE + "#parc"

# ---------------------------------------------------------------- traductions des nouveaux textes
EN_EXTRA = {}


def t(fr, en):
    """Texte français de la page ; sa traduction anglaise est enregistrée pour la version en/."""
    EN_EXTRA[" ".join(fr.split())] = en
    return fr


for fr, en in [
    ("Salons, congrès et grands événements à Abidjan.", "Trade shows, congresses and major events in Abidjan."),
    ("Page de l’événement", "Event page"), ("Entreprises", "Corporate"), ("Venir à Abidjan", "Coming to Abidjan"),
    ("Accès, hôtels, visas : venir à Abidjan", "Access, hotels, visas: coming to Abidjan"),
    ("Par type d’événement", "By event type"), ("Salons professionnels", "Trade shows"),
    ("Congrès et conférences", "Congresses and conferences"), ("Événements d’entreprise", "Corporate events"),
    ("Concerts et spectacles", "Concerts and shows"), ("Autres types d’événements", "Other event types"),
    ("Sous-menu Nos espaces", "Our venues submenu"), ("Explorer le Parc à distance", "Explore the venue remotely"), ("Visite virtuelle 360°", "360° virtual tour"),
]:
    t(fr, en)


def tr_en(s):
    """Traduction d'une chaîne pour les balises (hors corps de page)."""
    core = " ".join(s.split())
    return EN_EXTRA.get(core) or EN_DICT.get(core) or s


def page_url(page, lang="fr"):
    base = SITE + ("en/" if lang == "en" else "")
    return base if page == "index.html" else base + page


def asset_url(name, size=1600):
    path = ROOT / f"assets/img/{name}-{size}.webp"
    if not path.exists():
        size = 800
    return SITE + f"assets/img/{name}-{size}.webp"


# ---------------------------------------------------------------- balises des pages existantes (titre Google, description, image de partage)
META = {
    "index.html": dict(image="slider/dome-rendu",
        fr=("Parc des Expositions d’Abidjan – Convention center & salons en Côte d’Ivoire",
            "Salons, congrès, conventions et concerts à Abidjan : le Dôme (5 023 places assises), un hall de 6 500 m² et 67 000 m² d’esplanades. Demandez votre devis."),
        en=("Abidjan Exhibition Center – Convention center & trade shows in Côte d’Ivoire",
            "Trade shows, congresses, conventions and concerts in Abidjan: the Dome (5,023 seats), a 6,500 m² hall and 67,000 m² of esplanades. Request a quote.")),
    "qui-sommes-nous.html": dict(image="slider/journee-internationale",
        fr=("Qui sommes-nous ? Le Parc des Expositions d’Abidjan, exploité par GL events",
            "Le Parc des Expositions d’Abidjan accueille salons, congrès et concerts d’Afrique de l’Ouest, avec l’expertise internationale de GL events."),
        en=("About us – the Abidjan Exhibition Center, operated by GL events",
            "The Abidjan Exhibition Center hosts West Africa’s trade shows, congresses and concerts, backed by GL events’ international expertise.")),
    "nos-espaces.html": dict(image="espaces/hall/salon-vue-plongeante",
        fr=("Espaces événementiels à Abidjan : Hall, Dôme, Esplanades | Parc des Expositions d’Abidjan",
            "Comparez les espaces du Parc des Expositions d’Abidjan : Hall d’exposition de 6 500 m², Dôme de 5 000 m², 67 000 m² de parvis et d’esplanades."),
        en=("Event venues in Abidjan: Hall, Dome, Esplanades | Abidjan Exhibition Center",
            "Compare the Abidjan Exhibition Center’s venues: a 6,500 m² exhibition hall, the 5,000 m² Dome and 67,000 m² of forecourts and esplanades.")),
    "hall-exposition.html": dict(image="espaces/hall/interieur",
        fr=("Hall d’exposition à Abidjan – 6 500 m², 17 m sous plafond | Parc des Expositions d’Abidjan",
            "Le Hall d’exposition du Parc : 6 500 m² d’un seul tenant, 17 m sous plafond, divisible en 2 ou 3 espaces pour vos salons et expositions."),
        en=("Exhibition hall in Abidjan – 6,500 m², 17 m ceiling | Abidjan Exhibition Center",
            "The venue’s exhibition hall: 6,500 m² in a single space, 17 m clear height, divisible into 2 or 3 areas for your trade shows and exhibitions.")),
    "le-dome.html": dict(image="espaces/parvis/dome-sous-le-nuage",
        fr=("Le Dôme, convention center d’Abidjan – 5 023 places assises | Parc des Expositions d’Abidjan",
            "Le Dôme : 5 000 m², 5 023 places assises et 9 588 personnes debout pour vos congrès, conventions, cérémonies et concerts à Abidjan."),
        en=("The Dome, Abidjan’s convention center – 5,023 seats | Abidjan Exhibition Center",
            "The Dome: 5,000 m², 5,023 seats and room for 9,588 standing guests for your congresses, conventions, ceremonies and concerts in Abidjan.")),
    "parvis-esplanades.html": dict(image="espaces/parvis/salon-plein-air-aerien",
        fr=("Esplanades événementielles à Abidjan – 67 000 m² en plein air | Parc des Expositions d’Abidjan",
            "Parvis et esplanades du Parc : 67 000 m² d’espaces extérieurs pour salons en plein air, expositions de véhicules et concerts à Abidjan."),
        en=("Outdoor event space in Abidjan – 67,000 m² | Abidjan Exhibition Center",
            "The venue’s forecourts and esplanades: 67,000 m² of outdoor space for open-air trade shows, vehicle exhibitions and concerts in Abidjan.")),
    "nos-services.html": dict(image="phototheque/salon-stand",
        fr=("Services événementiels à Abidjan : audiovisuel, restauration, sécurité | Parc des Expositions d’Abidjan",
            "Audiovisuel, mobilier, restauration, sécurité, accueil, nettoyage et logistique : un seul interlocuteur pour toutes les prestations de votre événement."),
        en=("Event services in Abidjan: audiovisual, catering, security | Abidjan Exhibition Center",
            "Audiovisual, furniture, catering, security, reception, cleaning and logistics: one point of contact for every service your event needs.")),
    "phototheque.html": dict(image="phototheque/dome-lumieres",
        fr=("Photothèque – salons, concerts et événements | Parc des Expositions d’Abidjan",
            "Les espaces et les événements du Parc des Expositions d’Abidjan en images : salons, concerts, congrès et grands rendez-vous."),
        en=("Photo library – trade shows, concerts and events | Abidjan Exhibition Center",
            "The Abidjan Exhibition Center’s venues and events in pictures: trade shows, concerts, congresses and major gatherings.")),
    "agenda.html": dict(image="slider/concert-scene",
        fr=("Agenda des salons, concerts et événements à Abidjan | Parc des Expositions d’Abidjan",
            "Salons, congrès, conférences et concerts à venir au Parc des Expositions d’Abidjan : dates, lieux et liens de réservation."),
        en=("Upcoming trade shows, concerts and events in Abidjan | Abidjan Exhibition Center",
            "Upcoming trade shows, congresses, conferences and concerts at the Abidjan Exhibition Center: dates, venues and booking links.")),
    "contact-devis.html": dict(image="pages/parlez-nous",
        fr=("Demander un devis pour votre événement à Abidjan | Parc des Expositions d’Abidjan",
            "Décrivez votre salon, congrès ou concert : l’équipe commerciale du Parc des Expositions d’Abidjan vous recontacte avec une proposition adaptée."),
        en=("Request a quote for your event in Abidjan | Abidjan Exhibition Center",
            "Tell us about your trade show, congress or concert: the Abidjan Exhibition Center’s sales team will get back to you with a tailored proposal.")),
    "visite-virtuelle.html": dict(image="espaces/parvis/vue-aerienne",
        fr=("Visite virtuelle 360° du Parc des Expositions d’Abidjan",
            "Parcourez le Parc des Expositions d’Abidjan en 360° : Hall, Dôme et esplanades, depuis votre bureau."),
        en=("360° virtual tour of the Abidjan Exhibition Center",
            "Explore the Abidjan Exhibition Center in 360°: the hall, the Dome and the esplanades, from your desk.")),
    "informations-legales.html": dict(image="espaces/hall/galerie-couverte",
        fr=("Mentions légales, cookies et confidentialité | Parc des Expositions d’Abidjan",
            "Mentions légales, politique cookies, politique de confidentialité, CGU et éthique du site du Parc des Expositions d’Abidjan."),
        en=("Legal notice, cookies and privacy | Abidjan Exhibition Center",
            "Legal notice, cookie policy, privacy policy, terms of use and ethics of the Abidjan Exhibition Center website.")),
}


# ---------------------------------------------------------------- pages par type d'événement
def reasons(items):
    lis = "".join(f'<li><h3>{h}</h3><p>{p}</p></li>' for h, p in items)
    return f'<ul class="reasons" role="list">{lis}</ul>'


def cta_block(title, href):
    return f"""<section class="section">
  <div class="wrap">
    <div class="cta cta--photo">
      <div class="cta__img" aria-hidden="true"></div>
      <p class="eyebrow">{t("Votre projet", "Your project")}</p>
      <h2>{title}</h2>
      <p>{t("Décrivez votre événement en quelques minutes : notre équipe commerciale vous recontacte avec une proposition adaptée.", "Describe your event in a few minutes: our sales team will get back to you with a tailored proposal.")}</p>
      <a class="btn btn--primary" href="{href}">{t("Demander un devis", "Request a quote")} {ARROW}</a>
    </div>
  </div>
</section>"""


def ev_short(slug_):
    e = next(x for x in EVENTS if x[0] == slug_)
    return e


def event_cards(slugs):
    cards = []
    for s_ in slugs:
        e = ev_short(s_)
        place = DETAILS.get(s_, {}).get("lieu", e[4])
        cards.append(event(when_short(e[2], e[3]), e[1], place, href=f"evenement-{s_}.html", image=s_))
    return "\n".join(cards)


def landing(name, eyebrow, h1, lead, why, spaces_html, events, cta_title, devis_type):
    evs = ""
    if events:
        evs = f"""
<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">{t("Au Parc", "At the venue")}</p><h2>{t("Prochainement au Parc", "Coming up at the venue")}</h2></div>
    <div class="agenda">
{event_cards(events)}
    </div>
    <p class="section__more"><a class="link-arrow" href="agenda.html">{t("Voir tout l’agenda", "See the full events calendar")} {ARROW}</a></p>
  </div>
</section>"""
    t(h1.rstrip("."), EN_EXTRA[" ".join(h1.split())].rstrip("."))  # intitulé du fil d'Ariane
    body = page_hero(crumbs(A, (h1.rstrip("."), None)), eyebrow, h1, lead, compact=True) + f"""

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">{t("Pourquoi le Parc", "Why the venue")}</p><h2>{t("Trois raisons de choisir le Parc.", "Three reasons to choose the venue.")}</h2></div>
    {reasons(why)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">{t("Les espaces", "The venues")}</p><h2>{t("Les espaces adaptés.", "The right venues.")}</h2></div>
    <div class="spaces{" spaces--2" if spaces_html.count('<a class="space') == 2 else ""}">
{spaces_html}
    </div>
    {type_links(name, t("Autres types d’événements", "Other event types"))}
  </div>
</section>
{evs}
{cta_block(cta_title, f"contact-devis.html?type={devis_type}")}
"""
    PAGES[name] = (h1, body)


landing(
    "salons-professionnels.html", t("Organiser un salon", "Hosting a trade show"),
    t("Votre salon professionnel à Abidjan.", "Your trade show in Abidjan."),
    t("Un hall de 6 500 m² modulable, des esplanades pour les grands formats et des services intégrés : le Parc accueille les salons de référence d’Afrique de l’Ouest.",
      "A modular 6,500 m² hall, esplanades for large formats and integrated services: the venue hosts West Africa’s leading trade shows."),
    [(t("6 500 m² d’un seul tenant", "6,500 m² in a single space"),
      t("Le Hall d’exposition, 17 m sous plafond, se divise en 2 ou 3 espaces pour accueillir un ou plusieurs salons.", "The exhibition hall, with 17 m clear height, can be split into 2 or 3 areas for one or several trade shows.")),
     (t("Des extérieurs pour les grands formats", "Outdoor space for large formats"),
      t("67 000 m² de parvis et d’esplanades pour les véhicules, les engins et les démonstrations en plein air.", "67,000 m² of forecourts and esplanades for vehicles, machinery and open-air demonstrations.")),
     (t("Un seul interlocuteur", "One point of contact"),
      t("Montage, mobilier, audiovisuel, restauration, sécurité et nettoyage : nos équipes coordonnent toutes les prestations.", "Set-up, furniture, audiovisual, catering, security and cleaning: our teams coordinate every service."))],
    "\n".join([space("A", "Hall d’Exposition", "6 500 m² · 17 m sous plafond"), space("C", "Parvis & Esplanades", "67 000 m² d’espaces extérieurs")]),
    ["auto-expo", "horeca-expo", "brands-licensing-africa"],
    t("Parlez-nous de votre salon.", "Tell us about your trade show."), "salon")

landing(
    "congres-conferences.html", t("Organiser un congrès", "Hosting a congress"),
    t("Congrès et conférences à Abidjan.", "Congresses and conferences in Abidjan."),
    t("Le Dôme, convention center du Parc, accueille jusqu’à 5 023 participants assis pour vos congrès, assemblées et conférences internationales.",
      "The Dome, the venue’s convention center, seats up to 5,023 participants for your congresses, general assemblies and international conferences."),
    [(t("5 023 places assises", "5,023 seats"),
      t("Le Dôme offre 5 000 m² exploitables et accueille jusqu’à 9 588 personnes debout pour les grandes plénières.", "The Dome offers 5,000 m² of usable space and holds up to 9,588 standing guests for large plenary sessions.")),
     (t("Une équipe pour vos délégations", "A team for your delegations"),
      t("Accueil, protocole, audiovisuel, restauration et sécurité sont coordonnés par un seul interlocuteur.", "Reception, protocol, audiovisual, catering and security are coordinated by a single point of contact.")),
     (t("Abidjan, porte d’entrée régionale", "Abidjan, a regional gateway"),
      t("Plus d’une vingtaine de compagnies aériennes desservent Abidjan, et le Parc se trouve à quelques minutes de l’aéroport.", "More than twenty airlines serve Abidjan, and the venue is just minutes from the airport."))],
    "\n".join([space("B", "Le Dôme", "5 000 m² · 5 023 assis · 9 588 debout", ink=True), space("A", "Hall d’Exposition", "6 500 m² · 17 m sous plafond")]),
    ["abidjan-border-forum"],
    t("Parlez-nous de votre congrès.", "Tell us about your congress."), "congres")

landing(
    "evenements-entreprise.html", t("Organiser un événement d’entreprise", "Hosting a corporate event"),
    t("Vos événements d’entreprise à Abidjan.", "Your corporate events in Abidjan."),
    t("Conventions, lancements de produits, assemblées générales, soirées de gala : trois univers d’espaces et une équipe dédiée pour un événement à votre image.",
      "Conventions, product launches, general meetings, gala evenings: three types of venue and a dedicated team for an event that reflects your brand."),
    [(t("Le bon format", "The right format"),
      t("Le Dôme pour les plénières et les soirées, le Hall pour les conventions avec exposition, les esplanades pour le plein air.", "The Dome for plenaries and evenings, the hall for conventions with an exhibition, the esplanades for open-air formats.")),
     (t("Des services clés en main", "Turnkey services"),
      t("Audiovisuel, mobilier, restauration, accueil et sécurité, coordonnés par un seul interlocuteur.", "Audiovisual, furniture, catering, reception and security, coordinated by a single point of contact.")),
     (t("Une expertise internationale", "International expertise"),
      t("Le Parc s’appuie sur les standards d’exploitation de GL events, organisateur et gestionnaire de sites dans le monde entier.", "The venue relies on the operating standards of GL events, an event organizer and venue operator worldwide."))],
    "\n".join([space("B", "Le Dôme", "Plénières · soirées · cérémonies", ink=True), space("A", "Hall d’Exposition", "Conventions avec exposition"), space("C", "Parvis & Esplanades", "Formats en plein air")]),
    ["ceremonie-primud", "abidjan-border-forum"],
    t("Parlez-nous de votre événement d’entreprise.", "Tell us about your corporate event."), "corporate")

landing(
    "concerts-spectacles.html", t("Organiser un concert", "Hosting a concert"),
    t("Concerts et spectacles à Abidjan.", "Concerts and shows in Abidjan."),
    t("Le Dôme et les esplanades du Parc accueillent les grands artistes ivoiriens et internationaux, devant des milliers de spectateurs.",
      "The venue’s Dome and esplanades host leading Ivorian and international artists in front of thousands of spectators."),
    [(t("Jusqu’à 9 588 spectateurs", "Up to 9,588 spectators"),
      t("Le Dôme accueille 9 588 personnes debout ou 5 023 assises.", "The Dome holds 9,588 standing or 5,023 seated spectators.")),
     (t("Le plein air sur l’esplanade", "Open air on the esplanade"),
      t("Pour les grands concerts en extérieur, comme celui de Serge Beynaud en décembre 2026.", "For large outdoor concerts, such as Serge Beynaud’s in December 2026.")),
     (t("Un public bien accueilli", "A well-hosted audience"),
      t("Sécurité, gestion des flux et accueil du public sont adaptés aux grandes jauges.", "Security, crowd flow and audience reception are designed for large capacities."))],
    "\n".join([space("B", "Le Dôme", "9 588 debout · 5 023 assis", ink=True), space("C", "Parvis & Esplanades", "Concerts en plein air")]),
    ["concert-tayc", "concert-milo", "concert-40-ans-de-carriere-gadji-celi"],
    t("Parlez-nous de votre concert.", "Tell us about your concert."), "concert")

for fr, en in [("Plénières · soirées · cérémonies", "Plenaries · evenings · ceremonies"), ("Conventions avec exposition", "Conventions with an exhibition"),
               ("Formats en plein air", "Open-air formats"), ("9 588 debout · 5 023 assis", "9,588 standing · 5,023 seated"),
               ("Concerts en plein air", "Open-air concerts")]:
    t(fr, en)

LANDING_META = {
    "salons-professionnels.html": ("espaces/hall/salon-vue-plongeante",
        ("Salon professionnel à Abidjan – Hall de 6 500 m² | Parc des Expositions d’Abidjan",
         "Organisez votre salon professionnel à Abidjan : hall d’exposition modulable de 6 500 m², 67 000 m² d’espaces extérieurs, services intégrés et équipe dédiée."),
        ("Trade show venue in Abidjan – 6,500 m² hall | Abidjan Exhibition Center",
         "Host your trade show in Abidjan: a modular 6,500 m² exhibition hall, 67,000 m² of outdoor space, integrated services and a dedicated team.")),
    "congres-conferences.html": ("slider/journee-internationale",
        ("Congrès et conférences à Abidjan – Le Dôme, 5 023 places | Parc des Expositions d’Abidjan",
         "Votre congrès ou conférence à Abidjan : le Dôme offre 5 000 m² et 5 023 places assises, avec audiovisuel, restauration et accueil des délégations."),
        ("Congress & conference venue in Abidjan – the Dome, 5,023 seats | Abidjan Exhibition Center",
         "Host your congress or conference in Abidjan: the Dome offers 5,000 m² and 5,023 seats, with audiovisual, catering and delegate reception services.")),
    "evenements-entreprise.html": ("slider/salon-rencontres",
        ("Événement d’entreprise à Abidjan – conventions, lancements, galas | Parc des Expositions d’Abidjan",
         "Convention, lancement de produit, assemblée, soirée de gala : le Parc accueille vos événements d’entreprise à Abidjan, jusqu’à près de 10 000 invités."),
        ("Corporate events in Abidjan – conventions, launches, galas | Abidjan Exhibition Center",
         "Conventions, product launches, general meetings, gala evenings: the Abidjan Exhibition Center hosts your corporate events for up to nearly 10,000 guests.")),
    "concerts-spectacles.html": ("slider/concert-foule",
        ("Salle de concert à Abidjan – le Dôme, jusqu’à 9 588 spectateurs | Parc des Expositions d’Abidjan",
         "Concerts, spectacles et grands shows à Abidjan : le Dôme accueille jusqu’à 9 588 spectateurs debout, et les esplanades les événements en plein air."),
        ("Concert venue in Abidjan – the Dome, up to 9,588 spectators | Abidjan Exhibition Center",
         "Concerts, shows and major productions in Abidjan: the Dome holds up to 9,588 standing spectators, and the esplanades host open-air events.")),
}
for n, (bg, fr_, en_) in LANDING_META.items():
    META[n] = dict(image=bg, fr=fr_, en=en_)
    PAGE_BG[n] = bg

# ---------------------------------------------------------------- Venir à Abidjan (accès, hébergement, visas, FAQ)
FAQ = [
    (t("Le Parc est-il loin de l’aéroport ?", "Is the venue far from the airport?"),
     t("Non : le Parc se trouve boulevard de l’aéroport, à Port-Bouët, à quelques minutes de l’aéroport international Félix-Houphouët-Boigny.",
       "No: the venue is on Boulevard de l’aéroport in Port-Bouët, just minutes from Félix-Houphouët-Boigny International Airport.")),
    (t("Faut-il un visa pour venir en Côte d’Ivoire ?", "Do I need a visa to visit Côte d’Ivoire?"),
     t("Les ressortissants des pays de la CEDEAO n’en ont pas besoin. Les autres voyageurs demandent un visa biométrique en ligne avant leur départ.",
       "ECOWAS nationals do not. Other travellers apply for a biometric visa online before departure.")),
    (t("Le Parc peut-il aider à loger une délégation ?", "Can the venue help accommodate a delegation?"),
     t("Notre équipe peut vous orienter vers des hôtels adaptés à la taille de votre délégation et à votre budget.",
       "Our team can point you to hotels suited to the size of your delegation and your budget.")),
    (t("Quelle est la monnaie utilisée ?", "Which currency is used?"),
     t("Le franc CFA (XOF). Les cartes bancaires internationales sont acceptées dans la plupart des hôtels.",
       "The CFA franc (XOF). International bank cards are accepted in most hotels.")),
    (t("Comment obtenir un devis pour mon événement ?", "How do I get a quote for my event?"),
     t("Décrivez votre projet dans le formulaire de devis : notre équipe commerciale vous recontacte avec une proposition adaptée.",
       "Describe your project in the quote form: our sales team will get back to you with a tailored proposal.")),
]
FAQ_HTML = "".join(f'<details class="faq__item"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
PRACTICAL = [(t("Monnaie", "Currency"), t("Franc CFA (XOF)", "CFA franc (XOF)")),
             (t("Langue", "Language"), t("Français", "French")),
             (t("Fuseau horaire", "Time zone"), t("GMT (UTC+0), toute l’année", "GMT (UTC+0), all year round")),
             (t("Indicatif téléphonique", "Country code"), "+225")]
PRACTICAL_HTML = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in PRACTICAL)

PAGES["venir-a-abidjan.html"] = ("Venir à Abidjan", page_hero(
    crumbs(A, ("Qui sommes-nous ?", "qui-sommes-nous.html"), ("Venir à Abidjan", None)), t("Destination", "Destination"),
    t("Venir à Abidjan.", "Coming to Abidjan."),
    t("Accès, hébergement, formalités : tout ce qu’il faut pour accueillir vos participants venus de la région et du monde entier.",
      "Access, accommodation, formalities: everything you need to welcome attendees from the region and around the world."), compact=True) + f"""

<section class="section section--white">
  <div class="wrap">
    <ul class="reasons" role="list">
      <li><h2 class="t3">{t("Rejoindre le Parc", "Getting to the venue")}</h2>
        <p>{t("Le Parc se trouve boulevard de l’aéroport, à Port-Bouët, à quelques minutes de l’aéroport international Félix-Houphouët-Boigny.", "The venue is on Boulevard de l’aéroport in Port-Bouët, just minutes from Félix-Houphouët-Boigny International Airport.")}</p>
        <p>{t("Plus d’une vingtaine de compagnies aériennes relient Abidjan à l’Afrique et au reste du monde.", "More than twenty airlines connect Abidjan with Africa and the rest of the world.")}</p>
        <p><a class="link-arrow" href="contact-devis.html#acces">{t("Voir la carte d’accès", "See the access map")} {ARROW}</a></p></li>
      <li><h2 class="t3">{t("Où loger", "Where to stay")}</h2>
        <p>{t("Abidjan offre une hôtellerie variée, des hôtels d’affaires du Plateau aux établissements de Marcory, de la Riviera et de Port-Bouët, proches du Parc.", "Abidjan offers a wide range of hotels, from business hotels in Le Plateau to establishments in Marcory, Riviera and Port-Bouët, close to the venue.")}</p>
        <p>{t("Notre équipe peut vous orienter selon la taille de votre délégation.", "Our team can advise you according to the size of your delegation.")}</p></li>
      <li><h2 class="t3">{t("Visas et formalités", "Visas and formalities")}</h2>
        <p>{t("Les ressortissants des pays de la CEDEAO entrent en Côte d’Ivoire sans visa. Les autres voyageurs demandent un visa biométrique en ligne avant le départ.", "ECOWAS nationals enter Côte d’Ivoire without a visa. Other travellers apply for a biometric visa online before departure.")}</p>
        {note("Formalités à faire confirmer par le Parc et les autorités avant publication.")}
        <p><a class="link-arrow" href="https://www.snedai.com/" target="_blank" rel="noopener" aria-label="{t("Demande de visa en ligne (nouvel onglet)", "Online visa application (new tab)")}">{t("Demande de visa en ligne", "Online visa application")} {EXT}</a></p></li>
    </ul>
    <dl class="ev-facts practical block-gap">{PRACTICAL_HTML}</dl>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap faq">
    <div class="section__head"><p class="eyebrow">FAQ</p><h2>{t("Questions fréquentes", "Frequently asked questions")}</h2></div>
    <div class="faq__list">{FAQ_HTML}</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">{t("Une destination", "A destination")}</p><h2>{t("Abidjan, ville d’affaires et d’expériences.", "Abidjan, a city of business and experiences.")}</h2></div>
    <div class="destination-grid" data-lightbox>{DESTINATION_ITEMS}</div>
  </div>
</section>
{LIGHTBOX}
{cta_block(t("Parlez-nous de votre événement.", "Tell us about your event."), "contact-devis.html")}
""")
META["venir-a-abidjan.html"] = dict(image="pages/destination-abidjan",
    fr=("Venir à Abidjan : accès, hôtels et visas | Parc des Expositions d’Abidjan",
        "Préparez la venue de vos participants : accès au Parc depuis l’aéroport, hébergement à Abidjan, formalités de visa et informations pratiques."),
    en=("Coming to Abidjan: access, hotels and visas | Abidjan Exhibition Center",
        "Plan your attendees’ trip: getting to the venue from the airport, accommodation in Abidjan, visa formalities and practical information."))
PAGE_BG["venir-a-abidjan.html"] = "espaces/parvis/vue-aerienne"  # photo sans texte incrusté

# ---------------------------------------------------------------- une page par événement de l'agenda
MONTHS_EN = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def when_en(start, end):
    d1, m1 = dm(start)
    if not end:
        return f"{d1} {MONTHS_EN[m1]} {YEAR}"
    d2, m2 = dm(end)
    return f"{d1}–{d2} {MONTHS_EN[m2]} {YEAR}" if m1 == m2 else f"{d1} {MONTHS_EN[m1]} – {d2} {MONTHS_EN[m2]} {YEAR}"


def iso(t_):
    d, m = dm(t_)
    return f"{YEAR}-{m:02d}-{d:02d}"


def cut(s, n=155):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"


EVENT_PAGES = {}
for i, (slug_, title, start, end, kind, tags, resa, resa_label) in enumerate(EVENTS):
    name = f"evenement-{slug_}.html"
    det = DETAILS.get(slug_, {})
    desc = det.get("desc", "")
    lieu = det.get("lieu", NAME_FR)
    facts = [("Date", when_long(start, end)), ("Lieu", lieu), (t("Type", "Type"), kind)]
    t(f"Agenda · {kind}", f"Events · {tr_en(kind)}")
    if det.get("org"):
        facts.append(("Organisateur", det["org"]))
    facts_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    links = []
    if resa:
        links.append(f'<a class="btn btn--primary" href="{resa}" target="_blank" rel="noopener" aria-label="{resa_label} : {title} (nouvel onglet)">{resa_label} {EXT}</a>')
    if det.get("site"):
        links.append(f'<a class="link-arrow" href="{det["site"]}" target="_blank" rel="noopener" aria-label="Site officiel : {title} (nouvel onglet)">Site officiel {EXT}</a>')
    others = [e[0] for e in EVENTS[i + 1:i + 4]] or [e[0] for e in EVENTS[:3]]
    PAGES[name] = (title, f"""
<section class="hero hero--small hero--under-header">
  <div class="hero__img" aria-hidden="true">{img(f"agenda/{slug_}", priority=True, lazy=False)}</div>
  <div class="wrap hero__inner">
    {crumbs(A, ("Agenda", "agenda.html"), (title, None), ink=True)}
    <p class="eyebrow">Agenda · {kind}</p>
    <h1>{title}</h1>
    <p class="lead">{when_long(start, end)}</p>
  </div>
</section>

<section class="section section--white">
  <div class="wrap with-aside">
    <div>
      <h2>{t("À propos de l’événement", "About the event")}</h2>
      <p class="lead">{desc}</p>
      <dl class="ev-facts block-gap">{facts_html}</dl>
      <div class="ev-links block-gap">{"".join(links)}</div>
      {note("Zone administrable Drupal : présentation, programme, organisateur, informations pratiques.")}
    </div>
    <aside class="aside-box" aria-labelledby="aside-{slug_}">
      <p class="eyebrow">{t("Organisateurs", "Organizers")}</p>
      <h2 class="t3" id="aside-{slug_}">{t("Votre événement au Parc ?", "Your event at the venue?")}</h2>
      <p>{t("Salons, congrès, concerts : parlez-nous de votre projet.", "Trade shows, congresses, concerts: tell us about your project.")}</p>
      <a class="btn btn--primary btn--block" href="contact-devis.html">{t("Demander un devis", "Request a quote")} {ARROW}</a>
    </aside>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section__head"><p class="eyebrow">Agenda</p><h2>{t("À suivre au Parc", "Next at the venue")}</h2></div>
    <div class="agenda">
{event_cards(others)}
    </div>
    <p class="section__more"><a class="link-arrow" href="agenda.html">{t("Voir tout l’agenda", "See the full events calendar")} {ARROW}</a></p>
  </div>
</section>
""")
    SECTION_OF[name] = "agenda.html"
    when_fr, when_en_ = when_long(start, end), when_en(start, end)
    t(when_fr, when_en_)  # dates de l'en-tête et des fiches en anglais
    title_en = tr_en(title)
    META[name] = dict(image=f"agenda/{slug_}",
        fr=(f"{title} – {when_short(start, end)} à Abidjan | {NAME_FR}", cut(f"{title} au Parc des Expositions d’Abidjan, {when_fr[0].lower() + when_fr[1:]}. {desc}")),
        en=(f"{title_en} – {when_en_} in Abidjan | {NAME_EN}", cut(f"{title_en} at the Abidjan Exhibition Center, {when_en_}. {tr_en(desc)}")))
    EVENT_PAGES[name] = dict(slug=slug_, title=title, start=iso(start), end=iso(end or start), desc=desc, lieu=lieu,
                             org=det.get("org"), resa=resa, site=det.get("site"))

for fr, en in [("Type", "Type"), ("Organisateurs", "Organizers")]:
    t(fr, en)

# ---------------------------------------------------------------- données structurées (Schema.org, JSON-LD)
SPACE_LD = {
    "hall-exposition.html": dict(name="Hall d’Exposition", en="Exhibition Hall", cap=None),
    "le-dome.html": dict(name="Le Dôme", en="The Dome", cap=9588),
    "parvis-esplanades.html": dict(name="Parvis & Esplanades", en="Forecourts & Esplanades", cap=None),
}


def venue_graph(lang):
    nm = NAME_EN if lang == "en" else NAME_FR
    org = {"@type": "Organization", "@id": SITE + "#organisation", "name": nm, "url": page_url("index.html", lang),
           "logo": SITE + "assets/logo-pea.webp", "telephone": "+225 27 21 71 09 97",
           "sameAs": [IG_URL, FB_URL, LI_URL],
           "parentOrganization": {"@type": "Organization", "name": "GL events", "url": "https://www.gl-events.com/"}}
    venue = {"@type": "EventVenue", "@id": VENUE_ID, "name": nm, "url": page_url("index.html", lang), "address": ADDRESS, "geo": GEO,
             "telephone": "+225 27 21 71 09 97", "maximumAttendeeCapacity": 9588, "image": asset_url("slider/dome-rendu"),
             "hasMap": MAPS_PLACE, "publicAccess": True}
    return [org, venue]


def breadcrumb_ld(src, name, lang):
    nav = re.search(r'<nav class="breadcrumbs[^"]*"[^>]*>(.*?)</nav>', src, re.S)
    if not nav:
        return None
    items = []
    for i, li in enumerate(re.findall(r"<li>(.*?)</li>", nav.group(1), re.S), start=1):
        href = re.search(r'href="([^"]+)"', li)
        label = _h.unescape(re.sub(r"<[^>]+>", "", li)).strip()
        url = page_url(href.group(1).split("#")[0], lang) if href else page_url(name, lang)
        items.append({"@type": "ListItem", "position": i, "name": label, "item": url})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def event_ld(name, lang):
    e = EVENT_PAGES[name]
    tx = (lambda s: tr_en(s)) if lang == "en" else (lambda s: s)
    ev = {"@type": "Event", "name": tx(e["title"]), "startDate": e["start"], "endDate": e["end"],
          "eventStatus": "https://schema.org/EventScheduled", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
          "url": page_url(name, lang), "image": [asset_url(f"agenda/{e['slug']}")], "description": tx(e["desc"]),
          "location": {"@type": "Place", "name": tx(e["lieu"]), "address": ADDRESS}}
    if e["org"]:
        ev["organizer"] = {"@type": "Organization", "name": e["org"]}
    if e["resa"]:
        ev["offers"] = {"@type": "Offer", "url": e["resa"], "availability": "https://schema.org/InStock"}
    elif e["site"]:
        ev["sameAs"] = e["site"]
    return ev


def jsonld(name, src, lang):
    graph = []
    if name in ("index.html", "contact-devis.html", "venir-a-abidjan.html", "qui-sommes-nous.html"):
        graph += venue_graph(lang)
    if name in SPACE_LD:
        sp = SPACE_LD[name]
        node = {"@type": "EventVenue", "name": sp["en"] if lang == "en" else sp["name"], "url": page_url(name, lang),
                "containedInPlace": {"@id": VENUE_ID}, "address": ADDRESS, "image": asset_url(META[name]["image"])}
        if sp["cap"]:
            node["maximumAttendeeCapacity"] = sp["cap"]
        graph.append(node)
    if name in EVENT_PAGES:
        graph.append(event_ld(name, lang))
    if name == "agenda.html":
        graph.append({"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i, "url": page_url(n, lang)} for i, n in enumerate(EVENT_PAGES, start=1)]})
    if name == "venir-a-abidjan.html":
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": tr_en(q) if lang == "en" else q,
             "acceptedAnswer": {"@type": "Answer", "text": tr_en(a) if lang == "en" else a}} for q, a in FAQ]})
    bc = breadcrumb_ld(src, name, lang)
    if bc:
        graph.append(bc)
    if not graph:
        return ""
    data = _js.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{data}\n</script>'


# ---------------------------------------------------------------- balises du <head>
def apply_seo(name, src, lang):
    m = META.get(name)
    if not m:
        return src
    title, desc = m[lang]
    url = page_url(name, lang)
    image = asset_url(m.get("image", OG_DEFAULT))
    e = lambda s: _h.escape(s, quote=True)
    og_type = "event" if name in EVENT_PAGES else "website"
    tags = [
        f'<meta name="description" content="{e(desc)}">',
        f'<link rel="canonical" href="{url}">',
        f'<meta property="og:type" content="{og_type}">',
        f'<meta property="og:site_name" content="{e(NAME_EN if lang == "en" else NAME_FR)}">',
        f'<meta property="og:locale" content="{"en_GB" if lang == "en" else "fr_FR"}">',
        f'<meta property="og:locale:alternate" content="{"fr_FR" if lang == "en" else "en_GB"}">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{image}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(title)}">',
        f'<meta name="twitter:description" content="{e(desc)}">',
        f'<meta name="twitter:image" content="{image}">',
    ]
    ld = jsonld(name, src, lang)
    if ld:
        tags.append(ld)
    src = re.sub(r"<title>.*?</title>", f"<title>{e(title)}</title>", src, count=1, flags=re.S)
    return src.replace("</head>", "\n".join(tags) + "\n</head>", 1)


def write_sitemap():
    urls = []
    for name in PAGES:
        if name not in META:
            continue
        fr, en = page_url(name, "fr"), page_url(name, "en")
        for loc in (fr, en):
            urls.append(f"""  <url>
    <loc>{loc}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr}"/>
  </url>""")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nDisallow: /planches.html\nDisallow: /en/planches.html\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    print("écrit sitemap.xml (", len(urls), "adresses ) + robots.txt")


EN_DICT.update(EN_EXTRA)
