#!/usr/bin/env python3
"""Convertit les photos sources (dossier images/) en WebP optimisés dans assets/img/.

Usage : python3 tools/optimiser-images.py [--agenda] [--video]
  --agenda  télécharge aussi les visuels des événements depuis le site officiel du Parc.
  --video   réencode la vidéo de présentation officielle (ffmpeg) et son affiche.

Chaque image est produite en deux largeurs : <nom>-1600.webp (affichage large) et <nom>-800.webp
(vignettes, mobile), à utiliser avec srcset. Les originaux restent dans images/.
Prérequis : cwebp (libwebp) ; macOS : `brew install webp`.
"""
import pathlib
import re
import subprocess
import sys
import tempfile
import unicodedata
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
    # Plaquette commerciale (JPEG d’origine extraits du PDF, images/plaquette ; les doublons des photos officielles ne sont pas publiés)
    "plaquette/dome-acces-aerien.jpg": "plaquette/dome-acces-aerien",
    "plaquette/salle-panorama.jpg": "plaquette/salle-panorama",
    "plaquette/salle-scene.jpg": "plaquette/salle-scene",
    "plaquette/ecran-led-arriere.jpg": "plaquette/ecran-led-arriere",
    "plaquette/loges-signaletique.jpg": "plaquette/loges-signaletique",
    "plaquette/loge-miroirs.jpg": "plaquette/loge-miroirs",
    "plaquette/loge-coiffeuse.jpg": "plaquette/loge-coiffeuse",
    "plaquette/loges-couloir.jpg": "plaquette/loges-couloir",
    "plaquette/pas-perdus-salon.jpg": "plaquette/pas-perdus-salon",
    "plaquette/pas-perdus-fauteuils.jpg": "plaquette/pas-perdus-fauteuils",
    "plaquette/parvis-auvent.jpg": "plaquette/parvis-auvent",
    "plaquette/esplanade-ombrieres-aerien.jpg": "plaquette/esplanade-ombrieres-aerien",
    "plaquette/esplanade-ombriere.jpg": "plaquette/esplanade-ombriere",
    "plaquette/abidjan-plateau-tours.jpg": "plaquette/abidjan-plateau-tours",
    "plaquette/abidjan-panorama.jpg": "plaquette/abidjan-panorama",
    "plaquette/abidjan-cathedrale.jpg": "plaquette/abidjan-cathedrale",
}

# Dossiers pilotés : TOUTES leurs images sont converties (ajouter une photo = la déposer dans le dossier).
# Le nom de sortie vient de NOMS (par nom de fichier, quel que soit le dossier), sinon « photo-<identifiant> ».
DOSSIERS = {
    "Hall d’Exposition": "espaces/hall",
    "dome": "espaces/dome",
    "parvis&esplanades": "espaces/parvis",
    "abidjan": "destination",
}
NOMS = {
    "477772975_122107041890753259_2650153596900344098_n.jpg": "interieur",
    "490211711_122121974858753259_6208286369568576854_n.jpg": "interieur-portes",
    "476914515_122107042250753259_8728577235295915139_n.jpg": "galerie-couverte",
    "parcdesexpositionsabidjan_1790069500_3991714735372770409_72260507174.jpg": "salon-vue-plongeante",
    "parcdesexpositionsabidjan_1790965811_3999233523323538066_72260507174.jpg": "stands-connect",
    "490001281_122121974888753259_3576997020463302622_n.jpg": "entree-c",
    "sous.jpg": "auditorium",
    "parcdesexpositionsabidjan_1790101809_3991985760953252531_72260507174.jpg": "spectacle-ramatoulaye",
    "parcdesexpositionsabidjan_1790965811_3999233523482918667_72260507174.jpg": "spectacle-scene",
    "parcdesexpositionsabidjan_1790965811_3999233527912086219_72260507174.jpg": "panel-connect",
    "577673239_122157497864753259_8398378410935615261_n.jpg": "dome-sous-le-nuage",
    "479554843_122107042028753259_7643480473486413329_n.jpg": "parvis-dome",
    "565122750_122155092344753259_3487546577889466909_n.jpg": "vue-aerienne",
    "565128525_122155092314753259_4792798698496201383_n.jpg": "allee-couverte",
    "632365899_122168427080753259_271381240387927254_n.jpg": "parking-couvert",
    "parcdesexpositionsabidjan_1790069500_3991714735590910548_72260507174.jpg": "engins-devant-le-dome",
    "parcdesexpositionsabidjan_1790069500_3991714735960020700_72260507174.jpg": "salon-plein-air-aerien",
    "parcdesexpositionsabidjan_1789669811_3988361898169273366_72260507174.jpg": "infrastructures",
    "parcdesexpositionsabidjan_1789669811_3988361898446149406_72260507174.jpg": "aerien",
    "parcdesexpositionsabidjan_1789669811_3988361899058494058_72260507174.jpg": "hotellerie",
}
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def nom_auto(fichier):
    if fichier.name in NOMS:
        return NOMS[fichier.name]
    nombres = re.findall(r"\d{6,}", fichier.stem)
    return "photo-" + (nombres[1] if len(nombres) > 1 else nombres[0] if nombres else re.sub(r"[^a-z0-9]+", "-", fichier.stem.lower()))


def convert_folders():
    before = after = 0
    for dossier, groupe in DOSSIERS.items():
        src_dir, out_dir = SRC / dossier, OUT / groupe
        if not src_dir.is_dir():
            print(f"  dossier absent : images/{dossier}")
            continue
        # sorties régénérées à chaque passage : pas d'image orpheline quand une photo est retirée ou déplacée
        if out_dir.is_dir():
            for old in out_dir.glob("*.webp"):
                old.unlink()
        for src in sorted(p for p in src_dir.iterdir() if p.suffix.lower() in EXTENSIONS):
            name = nom_auto(src)
            before += src.stat().st_size
            for w in WIDTHS:
                dest = out_dir / f"{name}-{w}.webp"
                cwebp(src, dest, w)
                after += dest.stat().st_size
            print(f"  {dossier}/{src.name} -> assets/img/{groupe}/{name}-{{1600,800}}.webp")
    print(f"Dossiers pilotés : {ko(before)} -> {ko(after)}")


# Photos officielles fournies par le client (docs/retourclient/images, non versionné : 1 Go, vidéo > 100 Mo).
# Organisation du client (6 novembre 2026) : un dossier par lieu. TOUTES les photos d’un dossier sont converties
# (déposer une photo dans un dossier suffit) vers assets/img/officiel/<groupe>/<nom>-{1600,800}.webp.
# Les TIF sont d’abord convertis en JPG à côté de l’original (sips, qualité 92) ; un TIF qui a déjà son JPG est ignoré.
# Les doublons « … - Copie » sont ignorés. Nom de sortie : NOMS_OFFICIELS, sinon nom de fichier normalisé.
OFFICIELLES_SRC = ROOT / "docs" / "retourclient" / "images"
DOSSIERS_OFFICIELS = {
    "hall exposition": "officiel/hall",
    "dome": "officiel/dome-exterieur",
    "dome/salle": "officiel/dome-salle",
    "dome/salon vip": "officiel/dome-salon-vip",
    "espalanafes": "officiel/esplanades",
}
NOMS_OFFICIELS = {
    "Hall 1 bis": "hall-drapeaux", "_DSF6401": "hall-portes", "_DSF6404": "hall-perspective",
    "IMG_3429": "dome-ciel", "IMG_3415": "dome-aerien", "IMG_3413": "dome-toiture", "Dôme Panorama": "dome-panorama",
    "6C2A7053": "salle-pleniere", "6C2A7050": "salle-fauteuils", "_DSF6430": "salle-parterre", "_DSF6437": "salle-gradins",
    "_DSF6457": "salon-vip-galerie", "_DSF6458": "salon-vip-banc", "_DSF6459": "salon-vip-oeuvre", "_DSF6460": "salon-vip-accueil",
}


def tif_en_jpg():
    """Convertit chaque TIF officiel en JPG (même dossier, même nom) s’il n’a pas déjà son JPG."""
    for tif in sorted(OFFICIELLES_SRC.rglob("*.tif")):
        jpg = tif.with_suffix(".jpg")
        if not jpg.exists():
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", str(tif), "--out", str(jpg)], check=True, capture_output=True)
            print(f"  TIF -> JPG : {jpg.relative_to(OFFICIELLES_SRC)}")


def convert_officielles():
    if not OFFICIELLES_SRC.is_dir():
        print("  photos officielles absentes : docs/retourclient/images")
        return
    tif_en_jpg()
    before = after = 0
    with tempfile.TemporaryDirectory() as tmp:
        for dossier, groupe in DOSSIERS_OFFICIELS.items():
            src_dir, out_dir = OFFICIELLES_SRC / dossier, OUT / groupe
            if not src_dir.is_dir():
                print(f"  dossier absent : {dossier}")
                continue
            if out_dir.is_dir():
                for old in out_dir.glob("*.webp"):
                    old.unlink()
            for src in sorted(p for p in src_dir.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"} and "copie" not in p.stem.lower()):
                stem = unicodedata.normalize("NFC", src.stem)  # noms de fichiers macOS en NFD (« Dôme »)
                name = NOMS_OFFICIELS.get(stem, re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode().lower()).strip("-"))
                before += src.stat().st_size
                mid = pathlib.Path(tmp) / f"{name}.jpg"
                subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", "-Z", "3200", str(src), "--out", str(mid)], check=True, capture_output=True)
                for w in WIDTHS:
                    dest = out_dir / f"{name}-{w}.webp"
                    cwebp(mid, dest, w)
                    after += dest.stat().st_size
                print(f"  officielle {dossier}/{src.name} -> assets/img/{groupe}/{name}-{{1600,800}}.webp")
    print(f"Photos officielles : {ko(before)} -> {ko(after)}")


VIDEO_SRC = OFFICIELLES_SRC / "Vidéo présentation PEA FRANÇAIS.mp4"


def convert_video():
    """Vidéo de présentation : H.264 1080p (~25 Mo) et 720p (~14 Mo), affiche WebP tirée de la 4e seconde (vue aérienne)."""
    if not VIDEO_SRC.exists():
        print("  vidéo source absente : docs/retourclient/images")
        return
    out = ROOT / "assets" / "video"
    out.mkdir(parents=True, exist_ok=True)
    for width, crf, maxrate, audio in ((1920, "28", "2000k", "128k"), (1280, "28", "1100k", "96k")):
        name = "1080" if width == 1920 else "720"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VIDEO_SRC), "-vf", f"scale={width}:-2",
                        "-c:v", "libx264", "-preset", "slow", "-crf", crf, "-maxrate", maxrate, "-bufsize", str(int(maxrate[:-1]) * 2) + "k",
                        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", audio, "-movflags", "+faststart",
                        str(out / f"presentation-pea-{name}.mp4")], check=True)
    with tempfile.TemporaryDirectory() as tmp:
        frame = pathlib.Path(tmp) / "poster.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "4", "-i", str(VIDEO_SRC), "-frames:v", "1",
                        "-vf", "scale=1920:-2", str(frame)], check=True)
        for w in WIDTHS:
            cwebp(frame, OUT / "video" / f"presentation-poster-{w}.webp", w)
    print("  vidéo -> assets/video/presentation-pea-{1080,720}.mp4 + affiche")


# Logos des références (images/logos) : une seule largeur, transparence conservée
LOGOS_NOMS = {"images.png": "sara-2025"}


def convert_logos():
    src_dir, out_dir = SRC / "logos", OUT / "logos"
    if not src_dir.is_dir():
        return
    if out_dir.is_dir():
        for old in out_dir.glob("*.webp"):
            old.unlink()
    for src in sorted(p for p in src_dir.iterdir() if p.suffix.lower() in EXTENSIONS):
        name = LOGOS_NOMS.get(src.name, re.sub(r"[^a-z0-9]+", "-", src.stem.lower()).strip("-"))
        dest = out_dir / f"{name}-800.webp"
        cwebp(src, dest, 400)
        print(f"  logos/{src.name} -> assets/img/logos/{name}-800.webp")


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
    convert_folders()
    convert_officielles()
    convert_logos()
    if "--agenda" in sys.argv:
        download_agenda()
    if "--video" in sys.argv:
        convert_video()
