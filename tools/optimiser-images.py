#!/usr/bin/env python3
"""Convertit les photos sources (dossier images/) en WebP optimisés dans assets/img/.

Usage : python3 tools/optimiser-images.py [--agenda]
  --agenda  télécharge aussi les visuels des événements depuis le site officiel du Parc.

Chaque image est produite en deux largeurs : <nom>-1600.webp (affichage large) et <nom>-800.webp
(vignettes, mobile), à utiliser avec srcset. Les originaux restent dans images/.
Prérequis : cwebp (libwebp) ; macOS : `brew install webp`.
"""
import pathlib
import re
import subprocess
import sys
import tempfile
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "images"
OUT = ROOT / "assets" / "img"
QUALITY = "78"
WIDTHS = (1600, 800)

# source (relative à images/) -> cible (relative à assets/img/, sans extension ni largeur)
IMAGES = {
    # Diaporama de l'accueil
    "slider/02.jpg": "slider/dome-rendu",
    "slider/606009051_122163966620753259_7291049295852643505_n.jpg": "slider/concert-foule",
    "slider/763226460_122186172746753259_8774153018624638017_n.jpg": "slider/concert-scene",
    "slider/768304823_122187093026753259_5125588101765966260_n.jpg": "slider/journee-internationale",
    "slider/674373392_122175866762753259_7878717289361739719_n.jpg": "slider/salon-rencontres",
    "slider/parcdesexpositionsabidjan_1790069500_3991714735372770409_72260507174.jpg": "slider/salon-vue-plongeante",
    "slider/parcdesexpositionsabidjan_1790965811_3999233523482918667_72260507174.jpg": "slider/spectacle-scene",
    "slider/parcdesexpositionsabidjan_1790965811_3999233525059974799_72260507174.jpg": "slider/percussions",
    # Hall d'exposition
    "Hall d’Exposition/477772975_122107041890753259_2650153596900344098_n.jpg": "espaces/hall/interieur",
    "Hall d’Exposition/490211711_122121974858753259_6208286369568576854_n.jpg": "espaces/hall/interieur-portes",
    "Hall d’Exposition/476914515_122107042250753259_8728577235295915139_n.jpg": "espaces/hall/galerie-couverte",
    # Le Dôme (dome/490211711… est la même photo que le Hall : non reprise)
    "dome/577673239_122157497864753259_8398378410935615261_n.jpg": "espaces/dome/exterieur",
    "dome/490001281_122121974888753259_3576997020463302622_n.jpg": "espaces/dome/entree-c",
    "dome/sous.jpg": "espaces/dome/auditorium",
    # Parvis & esplanades
    "parvis&esplanades/479554843_122107042028753259_7643480473486413329_n.jpg": "espaces/parvis/parvis-dome",
    "parvis&esplanades/565122750_122155092344753259_3487546577889466909_n.jpg": "espaces/parvis/vue-aerienne",
    "parvis&esplanades/565128525_122155092314753259_4792798698496201383_n.jpg": "espaces/parvis/allee-couverte",
    "parvis&esplanades/632365899_122168427080753259_271381240387927254_n.jpg": "espaces/parvis/parking-couvert",
    # Photothèque
    "phototeque/547366462_122151155276753259_44992948776841260_n.jpg": "phototheque/salon-stand",
    "phototeque/549765867_122151155306753259_3873749959226310186_n.jpg": "phototheque/salon-auto",
    "phototeque/605761734_122163382934753259_3970897914230427283_n.jpg": "phototheque/concert-artiste",
    "phototeque/633853898_122168822762753259_6384860526208616943_n.jpg": "phototheque/concert-arena",
    "phototeque/674373392_122175866762753259_7878717289361739719_n.jpg": "phototheque/salon-rencontres",
    "phototeque/719150247_17911174407411175_1953255073622428784_n.jpg": "phototheque/dome-lumieres",
    "phototeque/719863648_17911174425411175_3160210308160264887_n.jpg": "phototheque/public-gradins",
    "phototeque/721801714_17912266767411175_442157822933949159_n.jpg": "phototheque/boxe",
    "phototeque/724247224_17912578362411175_3912324225951179650_n.jpg": "phototheque/concert-nuit",
    "phototeque/724992703_17912578335411175_8639008114002658121_n.jpg": "phototheque/arena-rouge",
    "phototeque/768432842_122187093020753259_4605381970006322797_n.jpg": "phototheque/public-ambiance",
    # Instagram (exports du compte @parcdesexpositionsabidjan ; cible = code court de la publication)
    "instagram/parcdesexpositionsabidjan_1789669811_3988361898018305114_72260507174.jpg": "instagram/DdZggPXFXRa",
    "instagram/parcdesexpositionsabidjan_1789734610_3988905474581825225_72260507174.jpg": "instagram/DdbcGUfD4bJ",
    "instagram/parcdesexpositionsabidjan_1790186418_3992695515397321561_72260507174.jpg": "instagram/Ddo52rDjXNZ",
    "instagram/parcdesexpositionsabidjan_1790795009_3997800748381773696_72260507174.jpg": "instagram/Dd7CplyFh-A",
    "instagram/parcdesexpositionsabidjan_1790953700_3999131949042420699_72260507174.jpg": "instagram/Dd_xVHAlsvb",
    "instagram/parcdesexpositionsabidjan_1791021613_3999701645926683180_72260507174.jpg": "instagram/DeBy3SlAVIs",
    # Pages
    "contacts.jpg": "pages/contact-signaletique",
    "abidjan.jpg": "pages/destination-abidjan",  # visuel carré avec texte incrusté en bas : recadrer sur le haut
    "parleznousvotreprojet.jpg": "pages/parlez-nous",
}

# Événements de l'agenda : slug de la fiche sur parcdesexpositionsabidjan.com
AGENDA = [
    "auto-expo", "horeca-expo", "agrofood-plastprintpack-west-africa-0", "food-expo-0", "concert-tayc",
    "brands-licensing-africa", "salon-des-collectivites-territoriales", "abidjan-border-forum", "concert-milo",
    "concert-40-ans-de-carriere-gadji-celi", "concert-mary-sy", "concert-ismael-isaac", "ceremonie-primud",
    "salon-ivoirien-des-ressources-extractives-energetiques", "salon-equip-auto", "concert-kiff-no-beat",
    "concert-25-ans-de-carriere-de-moliere", "concert-serge-beynaud-0", "concert-ariel-sheney",
    "foire-europe-afrique-dabidjan",
]
SITE = "https://www.parcdesexpositionsabidjan.com/fr/"


MAX_BYTES = 380 * 1024  # au-delà, nouvelle passe avec une qualité plus basse (photos très détaillées)


def source_width(src):
    out = subprocess.run(["sips", "-g", "pixelWidth", str(src)], capture_output=True, text=True).stdout
    m = re.search(r"pixelWidth:\s*(\d+)", out)
    return int(m.group(1)) if m else None


def cwebp(src, dest, width):
    dest.parent.mkdir(parents=True, exist_ok=True)
    original = source_width(src)
    resize = ["-resize", str(width), "0"] if not original or original > width else []  # jamais d'agrandissement
    for quality in (QUALITY, "70", "62"):
        subprocess.run(["cwebp", "-quiet", "-q", quality, "-metadata", "none", *resize,
                        str(src), "-o", str(dest)], check=True)
        if dest.stat().st_size <= MAX_BYTES:
            break


def ko(n):
    return f"{n / 1024:,.0f} Ko".replace(",", " ")


def convert_images():
    before = after = 0
    for rel, target in IMAGES.items():
        src = SRC / rel
        if not src.exists():
            print(f"  absent : images/{rel}")
            continue
        before += src.stat().st_size
        for w in WIDTHS:
            dest = OUT / f"{target}-{w}.webp"
            cwebp(src, dest, w)
            after += dest.stat().st_size
        print(f"  {rel} -> assets/img/{target}-{{1600,800}}.webp")
    print(f"Photos : {ko(before)} en JPEG -> {ko(after)} en WebP (deux largeurs comprises)")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (maquette PEA)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def download_agenda():
    total = 0
    for slug in AGENDA:
        html = fetch(SITE + slug).decode("utf-8", "replace")
        m = re.search(r'property="og:image"\s+content="([^"]+)"', html) or re.search(r'og:image"[^>]*content="([^"]+)"', html)
        if not m:
            print(f"  pas d'image : {slug}")
            continue
        url = m.group(1).replace("&amp;", "&")
        with tempfile.NamedTemporaryFile(suffix=".webp") as tmp:
            tmp.write(fetch(url))
            tmp.flush()
            dest = OUT / "agenda" / f"{slug}-800.webp"
            cwebp(tmp.name, dest, 800)
            total += dest.stat().st_size
        print(f"  agenda : {slug}")
    print(f"Agenda : {ko(total)} au total")


if __name__ == "__main__":
    convert_images()
    if "--agenda" in sys.argv:
        download_agenda()
