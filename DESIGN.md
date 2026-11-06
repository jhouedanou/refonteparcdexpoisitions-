---
name: Parc des Expositions d’Abidjan
description: Charte graphique officielle (Poppins, orange #DA5900) appliquée aux composants Bento DS de GL events, en angles vifs
colors:
  brand: "#da5900"
  primary: "#b34900"
  primary-hover: "#9d4015"
  brown: "#9d4015"
  brown-dark: "#5d120a"
  orange-light: "#f3931b"
  terracotta: "#d68644"
  beige: "#ead1b8"
  stone: "#d5cebc"
  green: "#006528"
  green-light: "#95c11f"
  black: "#0a0a0a"
  black-2: "#171717"
  white: "#ffffff"
  base-200: "#f7f5f1"
  base-300: "#ece8df"
  muted: "#525252"
  muted-on-dark: "#a1a1a1"
  on-photo: "#e5e5e5"
  border: "#dcd6ca"
  border-dark: "#262626"
  field: "#737373"
  placeholder-text: "#6b6b6b"
  cream: "#f8e0cc"
  note-bg: "#fcf2ea"
  error: "#b42318"
typography:
  hero:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(2.125rem, 5vw, 4.25rem)"
    fontWeight: 600
    lineHeight: 1.1
  display:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.25rem)"
    fontWeight: 600
    lineHeight: 1.1
  headline:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.5rem, 2.5vw, 2.125rem)"
    fontWeight: 600
    lineHeight: 1.15
  title:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.0625rem, 1.25vw, 1.25rem)"
    fontWeight: 600
    lineHeight: 1.3
  figure:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.5rem, 2vw + .5rem, 2.125rem)"
    fontWeight: 700
    lineHeight: 1
  lead:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.0625rem, 1.3vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  small:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
  button:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
  label:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 600
    letterSpacing: "0.08em"
  badge:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
rounded:
  none: "0px"
  field: "2px"
spacing:
  s-1: "4px"
  s-2: "8px"
  s-3: "12px"
  s-4: "16px"
  s-5: "24px"
  s-6: "32px"
  s-7: "48px"
  s-8: "64px"
  s-9: "96px"
  s-10: "128px"
  section: "clamp(48px, 7vw, 96px)"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.white}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.black}"
    rounded: "{rounded.none}"
    padding: "12px 20px"
    height: "48px"
  button-secondary-hover:
    backgroundColor: "{colors.black}"
    textColor: "{colors.white}"
  button-tertiary:
    backgroundColor: "{colors.green}"
    textColor: "{colors.white}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.brown}"
    textColor: "{colors.cream}"
  page-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
  input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.black}"
    rounded: "{rounded.field}"
    padding: "12px 14px"
    height: "52px"
---

# Design System : Parc des Expositions d’Abidjan

> Système en vigueur depuis le 6 novembre 2026 : **charte graphique officielle** (`docs/retourclient/PARC DES EXPOSITIONS D'ABIDJAN_CHARTE GRAPHIQUE.pdf`) appliquée aux **composants Bento DS** de GL events (`docs/retourclient/Bento DS.fig`). La charte prévaut sur tout le reste. Tokens et correspondance des composants : `design-system/pea/BENTO-TOKENS.md` ; contrastes : `design-system/pea/MASTER.md`. États précédents : `design-system/pea/DESIGN-avant-charte.md` (direction B, Barlow), `DESIGN-avant-refonte.md`.

## Overview

**Creative North Star : « Signalétique & architecture », aux couleurs de la charte**

Le site se lit comme la signalétique d'un parc d'expositions : des repères orange qui indiquent où aller, des grilles en filets d'un pixel qui rappellent les plans de halls, et désormais les photos officielles des lieux (le Hall pavoisé, la coupole du Dôme, sa salle plénière). L'échelle se montre par les chiffres (6 500 m², 67 000 m²) et par la vidéo de présentation. Le motif de l'arche du logo signe les moments clés : héros, appel à l'action, visite 360°, bas de section, pied de page.

La structure des composants suit Bento DS (Button, Badge, Title, Page header, Block/Hero, Key figures, Card, Cta, Footer, Block/Video…), avec ses trois couches de tokens. Choix PEA : angles vifs (rayons Bento ramenés à 0, 2 px pour les champs).

**Key Characteristics:**
- Poppins seule, comme toute la communication du Parc (charte p. 7).
- Orange PEA #DA5900 pour la marque, ombré en #B34900 dès qu'un texte ou un bouton doit être lu sur fond clair.
- Couleurs d'accompagnement de la charte : brun #9D4015 (pied de page, survols), vert #006528 (dates, statut), beige et pierre (surfaces).
- Logo en version Positif sur fond clair, Négatif blanc sur photo, orange ou brun, jamais recoloré.
- Grilles visibles, cellules de tailles inégales ; aucune ombre, aucun arrondi.

## Colors

### Primary
- **Orange PEA** (#DA5900, charte RVB 218-89-0) : logo, aplats (lettres de hall, plaques), arche, h1/h2 ≥ 24 px (3,88:1 sur blanc, grand texte), chiffres et accents sur noir (5,1:1).
- **Orange action** (#B34900) : fond des boutons primaires (texte blanc 5,43:1), liens, eyebrows et page active sur fond clair, fond des en-têtes de page. Survol : brun #9D4015 (6,61:1).
- **Orange clair** (#F3931B, kit web) : aplats sans texte, badge « reporté » (texte noir).

### Secondary (charte, couleurs d'accompagnement)
- **Brun** (#9D4015) : fond du pied de page (Bento `footer/bg → brand/primary/800`), survol des boutons.
- **Vert** (#006528) : dates, statut « à venir », bouton tertiaire (7,26:1). **Vert clair** (#95C11F) : aplats sans texte.
- **Beige** (#EAD1B8), **Pierre** (#D5CEBC), **Terracotta** (#D68644), **Brun foncé** (#5D120A) : surfaces et encarts.

### Neutral
- **Noir** (#0A0A0A, version Monochrome) : texte, sections sombres (vidéo, services, encarts).
- **Pierre très claire** (#F7F5F1) : fond de page ; **#ECE8DF** : visuels provisoires.
- **Texte secondaire** (#525252, 7,18:1) ; sur noir **#A1A1A1** (7,66:1) ; filets **#DCD6CA** et **#262626**.

### Named Rules
**La règle des deux oranges.** #DA5900 pour la marque et les grands titres, #B34900 dès qu'un petit texte ou un bouton à texte blanc doit être lu sur fond clair.
**La règle du pied brun.** Sur le brun, l'orange disparaît (1,7:1) : accents crème #F8E0CC (5,2:1), logo Négatif, logo GL events en signature grise.
**La règle du logo intact.** Positif, Négatif ou Monochrome, jamais d'autre teinte, jamais déformé (charte p. 4–5).

## Typography

**Police unique :** Poppins (Google Fonts), 400 / 500 / 600 / 700 ; repli `sans-serif`.

**Character :** la voix du logo partout. Les titres en Poppins 600 orange, les labels en Poppins 600 en petites capitales espacées, le texte courant en Poppins 400. Barlow et Barlow Condensed sont retirés.

### Hierarchy
- **Hero** (600, clamp 34→68 px, lh 1.1) : titre du diaporama de l’accueil, en blanc.
- **Display** (600, clamp 32→52 px, lh 1.1) : h1 de page, blanc sur l’en-tête orange ; 30→44 px dans les en-têtes compacts.
- **Headline** (600, clamp 24→34 px, lh 1.15, #DA5900) : h2 de section ; blanc dans le pied de page.
- **Title** (600, clamp 17→20 px, lh 1.3, noir ou blanc) : titres de cartes ; pas d'orange à cette taille. La classe `.t3` applique ce style à un h2.
- **Figure** (700, clamp 24→34 px) : chiffres-clés.
- **Lead** (400, 17→19 px, lh 1.55, 60ch max) ; **Body** (400, 16 px, lh 1.65, 68ch max).
- **Button** (600, 15 px, casse normale, comme Bento `btn/text-transform: none`).
- **Label** (600, 13 px, .08em, capitales) : eyebrows avec un trait orange de 2 px à gauche, dates, plaques ; **Badge** (600, 12 px, capitales).

### Named Rules
**La règle des capitales.** Seuls les labels, eyebrows et badges sont en capitales ; titres, boutons et texte restent en casse normale.
**La règle du titre logo.** h1 et h2 prennent l'orange du logo ; sur photo, sur l'en-tête orange et dans le pied de page brun ils sont blancs ; les h3 restent noirs.
**La règle du sur-titre discret.** L'eyebrow orange n'apparaît que dans les héros, la vidéo et l'appel à l'action ; dans le corps des pages, il passe en gris.

## Layout

Conteneur `min(1320px, 100% − 2 × gouttière)`, avec une gouttière de 16 px sous 768 px, 32 px de 768 à 1279 px et 64 px au-delà. La mise en page est mobile-first, avec des points de rupture à 480, 600, 768, 1024 et 1120 px (70em, menu complet). Les grilles « plan de hall » utilisent `gap: 1px` sur fond de filet : les cellules se touchent et la grille se voit. Les compositions sont volontairement variées : bande de chiffres de largeurs inégales (1.35/1/1.15/.85), bento des espaces (1.45/1, la première cellule sur deux rangées), agenda avec une vedette et une liste, services en tableau sur deux colonnes, photothèque sur 12 colonnes.

## Elevation & Depth

Aucune ombre. La profondeur vient uniquement de l'alternance des surfaces (noir, blanc, pierre claire, brun) et des filets. L'en-tête collant est séparé du contenu par un filet orange #DA5900 de 4 px.

## Shapes

Angles vifs partout (0 px, choix PEA appliqué aux rayons Bento `radius-*`) ; 2 px seulement sur les champs de formulaire. L'arche du logo est le seul élément courbe. Elle est formée de deux surfaces pleines effilées : la cloche (épaisse de 6,5 unités au sommet, en pointe aux extrémités) et l'arc plat dessous (3,5 unités au centre), dans un viewBox `16 -1 360 68`. On la trouve en SVG inline dans le héros et le CTA, et en image de fond dans les visuels du Dôme, la visite 360° et les emplacements photo.

## Components

- **Bouton** (Bento « Button ») : primaire orange action #B34900, texte blanc, Poppins 600 15 px en casse normale, hauteur minimale 48 px, angles vifs, flèche SVG qui glisse de 3 px au survol ; variantes `.btn--secondary` (contour), `.btn--tertiary` (vert), `.btn--default` (sans fond), `.btn--outline`.
- **Bouton secondaire** : contour 2 px de la couleur du texte. Il s'inverse au survol (noir ou blanc selon le fond).
- **En-tête** : logo officiel (`assets/logo-pea.webp`), navigation avec `aria-current`, CTA. Sous 1120 px, un bouton « Menu » (`aria-expanded`) ouvre un panneau noir, et le CTA se réduit à « Devis » sous 600 px.
- **Bande de chiffres** : cellules blanches ; sur l’accueil (`.figures--interactive`), le style noir + chiffre orange devient l’effet de survol et de focus. Les chiffres comptent jusqu’à leur valeur à l’apparition (valeur finale en `sr-only`, désactivé si mouvement réduit). « Visiter le Parc » est un bouton secondaire.
- **Carte espace** : photo pleine carte (`object-fit: cover`), dégradé noir en bas, plaque avec la lettre de hall (A/B/C) sur carré orange, le nom, les données et une flèche ; zoom léger au survol. Liens vers les pages dédiées (hall-exposition, le-dome, parvis-esplanades).
- **Ligne de service** : numéro orange, titre, description, filet sombre.
- **Filtres** : `<button aria-pressed>` avec contour noir, l'état actif est plein.
- **En-tête de page intérieure** : à partir de 1024 px, deux colonnes (titre 1.65fr, chapô 1fr aligné en bas), pour éviter le vide à droite. Pas de césure automatique dans les titres.
- **Visite 360°** : façade (arche et bouton « Lancer la visite 360° »). Au clic, l'iframe Matterport est injectée sur place (`play=1`, plein écran autorisé). Sans JavaScript, le lien ouvre Matterport dans un nouvel onglet.
- **Encart** : bordure noir 1 px, collant à partir de 1024 px.
- **En-tête compact** (`.page-hero--compact`) : sur les fiches, l'agenda, le contact et la visite, le h1 descend à `clamp(2.5rem, 5.5vw, 4.5rem)` pour que le contenu utile apparaisse au-dessus du pli.
- **Filtres** : le groupe commence toujours par « Tous », actif par défaut. Un compteur `role="status"` (« 3 espaces ») annonce le résultat et un état vide en pointillés s'affiche quand aucun élément ne correspond. Les données sont portées par des attributs `data-usage` / `data-espace` / `data-type`, à administrer dans Drupal.
- **Formulaire de devis** : trois `fieldset` (Vous, Votre événement, Vos besoins) séparés par un filet noir. Les champs obligatoires portent un astérisque orange, les autres la mention « (facultatif) ». La date est une période (du / au) avec une case « dates flexibles », les services sont des cases à cocher et un consentement est requis. Les erreurs s'affichent sous le champ (#b42318, `aria-invalid` + `aria-describedby`), le focus va sur le premier champ en erreur, et le succès s'affiche dans un bloc noir. L'espace peut être pré-rempli via `?espace=hall|dome|parvis`.
- **Barre utilitaire** (sur mobile : WhatsApp et FR | EN seulement ; réseaux sociaux dans le menu) : bandeau noir de 44 px au-dessus de l'en-tête collant : numéro en lien WhatsApp (`wa.me`) à gauche ; à droite, le sélecteur de langue FR | EN (langue active soulignée d’orange, `aria-current`) et les icônes Instagram, Facebook, LinkedIn (cibles de 44 px).
- **Frise de l'agenda (compacte)** : vignette carrée de 72 px (affiche entière sur noir), type, titre, date et un seul bouton « Détails » ; « Réserver » et « Site officiel » sont dans la fenêtre. Description d’origine : intertitres de mois collants (carré orange et titre condensé), puis une colonne date (jour en très grand, fin de période ou mois en label), un rail de 1 px et un repère carré. Les cartes sont sur fond pierre claire ; le prochain événement, calculé d'après la date du jour, a un repère orange, une carte blanche bordée d'noir et la mention « Prochainement ». Les actions sont « Réserver » (bouton primaire), quand un lien existe, et « Détails » (lien fléché ou icône de lien externe).
- **Fenêtre de détails d'événement** (`<dialog>`) : affiche officielle entière (`contain` sur noir, 48vh max) au-dessus de en-tête noir avec l'arche en ton sourd, le type, le titre et la date, puis la description, une liste de faits (Date, Lieu, Organisateur) et les liens. Elle se ferme avec le bouton, la touche Échap ou un clic sur le fond, et le focus revient au bouton « Détails ». Sans JavaScript, les détails s'affichent directement dans la carte.
- **Mur d'actualité** : grille jointive de 1 px. La tuile Facebook occupe deux rangées, la tuile Instagram (grille de vignettes) deux colonnes ; puis LinkedIn sur fond pierre claire et « Prochainement au Parc » sur fond noir.
- **Intégrations tierces** (`data-embed-src`) : une façade pierre claire avec l'arche et un bouton « Afficher… » tant que le visiteur n'a pas donné son accord ; l'iframe est injectée après accord ou au clic.
- **Bandeau cookies** : fixé en bas, fond noir ; « Tout refuser » et « Tout accepter » sont deux boutons secondaires de même poids.
- **Bloc « Parlez-nous de votre projet » (`.cta--photo`)** : il utilise la photo officielle de la coupole du Dôme (`assets/img/espaces/dome/officiel-dome-ciel`), dont le toit reprend l'arche du logo. À partir de 1024 px, la photo occupe les 70 % de droite sous un dégradé noir horizontal (opaque jusqu'à 36 %, 0,92 à 46 %) et le texte est limité à 38ch pour rester sur l'noir. Sous 1024 px, la photo est placée en bas du bloc, avec un fondu vertical court.
- **Carte d'accès** : iframe Google Maps chargée en différé, au ratio 4:3 sur mobile et 16:10 sur grand écran, à côté de l'adresse et des boutons Itinéraire / Google Maps.
- **Pied de page** : une vraie navigation (Espaces, Services, Destination, Expertise), le téléphone et le logo GL events en signature grise (kit web de la charte ; le carré est recadré en CSS, avec son coin arrondi). Fond brun #9D4015 (Bento `footer/bg`), logo PEA en version Négatif, accents crème #F8E0CC. L’arche du logo, en brun, monte dans la section précédente en haut du pied de page. Mise en page compacte : newsletter, puis trois colonnes (le Parc et ses coordonnées, menu, GL events), puis une barre basse (liens légaux à gauche, « Design par Big Five » à droite, lien suivi vers bigfive.solutions). Le sélecteur de langue n’est que dans la barre du haut.
- **Diaporama Ken Burns** (héros de l’accueil, 90vh) : 8 images en fondu enchaîné toutes les 7 s avec zoom lent ; contrôle de défilement (`.ctrl--on-photo` : compteur « 01 / 08 », barre qui se remplit pendant 7 s, Précédent / Pause / Suivant) ; boutons orange, titre blanc ; parallaxe légère au défilement (la photo descend de 14 % du défilement) ; mouvement réduit = fondu sans zoom ni parallaxe. Indicateur « souris » animé (4 cycles) vers la section suivante.
- **Références (accueil, avant le pied de page)** : « Ils nous ont fait confiance », carrousel de 10 logos d’organisateurs (`images/logos` → `assets/img/logos`, 400 px), 5 par page dès 1024 px (3 dès 600 px, 2 en dessous). Tuiles blanches en 3:2, logos désaturés (gris, opacité .75), couleur au survol (toujours en couleur sur écran tactile). Le logo Abidjan Border Forum, blanc sur transparent, a une tuile noir. Défilement automatique d’une page toutes les 5 s (retour au début à la fin), contrôle de défilement (`.ctrl` : compteur « 1 / 2 », barre qui se remplit pendant 5 s, Précédent / Pause / Suivant), pause au survol, au focus et quand l’onglet est masqué ; aucune animation si mouvement réduit.
- **En-tête de page (`.page-hero--bg`)** : la photo du sujet (`PAGE_BG`, `tools/pages/generer.py`) en fond, désaturée et fondue à 60 % dans l'orange action #B34900 (elle ne peut que foncer l'orange : texte blanc ≥ 5,43:1 ; fil d'Ariane en graisse 500). En bas à droite, la silhouette exacte de l'arche du logo (360 × 62,5, jamais étirée) prend la couleur de la section suivante, qui monte dans l'en-tête ; texte à gauche (52 %). Sous 1024 px, l'arche passe sous le texte. Parallaxe légère : la photo descend de 18 % du défilement (aucune si mouvement réduit). Motif et autres usages : `design-system/pea/MASTER.md` § 9 et la planche [L'arche du Parc](https://claude.ai/artifact/3NKB1kd9hXu4pcyu4AbF8W).
- **En-tête transparent (toutes les pages)** : comme sur l’accueil, barre utilitaire et en-tête se posent sur le héros ou l’en-tête orange ; sur l’orange, logo passé en blanc (filtre), page active soulignée de blanc, bouton devis noir, langues en blanc. Barre utilitaire : léger fond noir translucide (noir 32 %).
- **Logo sur photo** : dans l’en-tête transparent, le logo passe en version Négatif (blanc) sur le diaporama comme sur l’orange (charte p. 4).
- **En-tête transparent (accueil)** : avec JavaScript, la barre utilitaire et l’en-tête se posent sur le diaporama (fond et filet transparents, liens et bouton « Menu » en blanc, page active en orange, bouton devis orange), au-dessus d’un voile noir dédié (.82 → 0 sur 260 px ; texte blanc ≥ 7,6:1 dans le pire cas). Fond blanc et filet orange dès 8 px de défilement ou menu ouvert. Sans JavaScript : en-tête blanc.
- **Pages par type d’événement** (salons, congrès, entreprise, concerts) : en-tête photo, trois raisons (`.reasons`, filet orange en tête), espaces adaptés (cartes, deux colonnes s’il n’y en a que deux), liens vers les autres types (`.type-links`, puces), prochains événements, bloc devis avec le type pré-rempli.
- **Venir à Abidjan** : accès, hébergement, visas (`.reasons`), infos pratiques (`.ev-facts`), FAQ (`<details>`, `.faq__item`), série destination, bloc devis.
- **Page événement** (`evenement-*.html`) : héros photo sombre, description, faits (date, lieu, type, organisateur), liens de réservation et site officiel, encadré « Votre événement au Parc ? », événements suivants.
- **Sous-menu « Nos espaces »** : à partir de 1120 px, un bouton chevron (44 px, `aria-expanded`) à côté du lien ouvre un panneau noir à filet orange de 3 px : Hall, Dôme, Parvis & Esplanades, Visite virtuelle, chacun avec une ligne de description ; il s’ouvre aussi au survol et se ferme avec Échap, au clic à l’extérieur ou quand le focus sort. Dans le menu mobile, les quatre liens sont toujours affichés sous « Nos espaces », en retrait derrière un filet orange.
- **WhatsApp dans l’en-tête fixe** : quand l’en-tête devient blanc au défilement (la barre du haut a disparu), l’icône WhatsApp apparaît à côté du logo, avec le numéro à partir de 1280 px ; elle ouvre wa.me avec le message pré-rempli.
- **Newsletter (pied de page)** : inscription aux prochains événements (e-mail + consentement), validation accessible, confirmation annoncée ; simulée dans la maquette.
- **Retour en haut** : carré noir de 48 px fixé en bas à droite, visible après un écran de défilement ; remonte au-dessus du bandeau cookies (`--banner-h`). Icône : silhouette du dôme du logo.
- **Galeries et visionneuse** : sur les pages espaces, toutes les photos du dossier source (1 grande en 2×2, chargée immédiatement, puis vignettes en grille dense 4 colonnes) ; vignettes jointives (4 px) en `cover` ; chaque vignette ouvre une visionneuse `<dialog>` plein écran (légende, compteur, précédent/suivant au clavier, Échap, retour du focus). Photothèque en grille dense 4 colonnes avec une vignette sur cinq en 2×2.
- **Pages espaces** : bande de 3 chiffres officiels, galerie, présentation, usages (étiquettes à puce), équipements (Dôme), encart devis pré-rempli et documents (fiche technique, plan du site PDF).
- **Accompagnement (Services)** : texte d’accompagnement + bloc noir « Bâtiment administratif » en grille 2 colonnes ; engagements RSE en liste numérotée sur 3 colonnes.
- **Série « destination »** (Qui sommes-nous) : 4 visuels carrés à légende incrustée, affichés entiers (`contain`), légende reprise en texte alternatif, ouverts dans la visionneuse.
- **Comparatif des espaces** (`.compare`, Nos espaces) : tableau surface / hauteur / capacité / usages / documents / devis pré-rempli ; sous 1024 px, chaque ligne devient une fiche avec libellés (`data-label`).
- **Message de succès du devis** : récapitule type d’événement, espace et dates saisis.
- **Version anglaise** : pages générées dans `en/` à partir du dictionnaire `tools/i18n/en.json` (chaînes entières), `hreflang` réciproques.
- **Vidéo de présentation** (Bento « Block/Video », accueil et Qui sommes-nous) : section noire, façade avec l’affiche tirée de la vidéo officielle (vue aérienne du site), bouton de lecture carré orange action et libellé « Voir la vidéo de présentation · 1 min 37 · en français ». La vidéo (H.264, `assets/video/presentation-pea-1080.mp4` 25 Mo, `-720.mp4` 14 Mo sous 768 px) n’est chargée qu’au clic, puis lue avec le son ; sans JS, le lien ouvre le MP4. Pas de sous-titres fournis.
- **Badge** (Bento « Badge ») : Poppins 600 12 px en capitales, angles vifs ; `.badge--primary`, `--secondary`, `--outline` et statuts `--full`, `--postponed`, `--cancelled` en couleurs de la charte.
- **Champ** : label visible relié par `for`, bordure #84878d (3,6:1), focus orange action.
- **Focus** : contour de 3 px orange action, décalé de 3 px ; orange PEA sur fond sombre.


## Correspondance Bento DS

| Composant Bento | Site | Notes |
|---|---|---|
| Button · Link · Title · Badge | `.btn*`, `.link-arrow`, h1–h3 / `.t3`, `.badge*` | rayons à 0 |
| Topbar · Site header · Menu / Submenu / Mobile | `.utility`, `.topbar`, `.nav`, `.nav__sub` | |
| Breadcrumb · Page header (Background=image, Color=primary) | `.breadcrumbs`, `.page-hero--bg` | |
| Block/Hero (image overlay) · Block/Slider | diaporama de l’accueil | photos officielles |
| Block/Key figures | `.figures` | |
| Card (landscape / poster) · Block/Agenda list · Block/Events | `.space`, `.event`, frise de l’agenda | |
| Block/Partners (carousel) | `.logos` | |
| Cta (Background=image) | `.cta--photo` | |
| Accordion · Image gallery · Modal | FAQ, galeries, visionneuse, fenêtre d’événement | |
| Form/Field · Newsletter form · Contact details · Block/Map | devis, newsletter, accès | |
| Footer (Columns=3) | `.footer` | fond `brand/primary/800` = brun charte |
| Block/Video | `.video-block` | nouveau |

Tokens : `design-system/pea/BENTO-TOKENS.md`.

## Do's and Don'ts

- **Do** garder deux niveaux de boutons (primaire orange, secondaire contour) ; les liens fléchés sont des liens, pas des boutons.
- **Do** vérifier chaque paire texte/fond (4,5:1 minimum, 3:1 pour le gros texte et l'UI).
- **Do** varier les compositions d'une section à l'autre.
- **Do** utiliser exclusivement des Google Fonts.
- **Don't** utiliser de bordure latérale épaisse sur une carte (side-tab), d'ombre, de pilule ou de rayon supérieur à 2 px.
- **Don't** utiliser de dégradés violets, de rayures en dégradé ni d'emojis comme icônes.
- **Don't** poser du texte orange #DA5900 de moins de 24 px sur un fond clair (utiliser #B34900).
- **Don't** recolorer ou déformer le logo, ni utiliser une autre police que Poppins.
- **Don't** réintroduire les rayons Bento (pilules, 8 px) : le Parc garde des angles vifs.
