---
name: Parc des Expositions d’Abidjan
description: Signalétique & architecture — le site parle comme la signalétique d'un grand parc d'expositions
colors:
  ink: "#111217"
  ink-2: "#1a1c21"
  paper: "#f5f3ee"
  paper-2: "#ebe8e1"
  white: "#ffffff"
  muted: "#55595f"
  muted-dark: "#b9bbc0"
  hero-text: "#e3e4e7"
  line: "#d9d7d1"
  line-dark: "#2e3138"
  field: "#84878d"
  placeholder-text: "#6b6f75"
  orange: "#f36a00"
  orange-title: "#db5913"
  orange-action: "#c2410c"
  orange-action-hover: "#9a3412"
  green: "#0e6f54"
  note-bg: "#fff3ea"
  note-text: "#6f4a2f"
typography:
  hero:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 600
    lineHeight: 1.1
  display:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(2rem, 4.2vw, 3.5rem)"
    fontWeight: 600
    lineHeight: 1.1
  headline:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.5rem, 2.6vw, 2.25rem)"
    fontWeight: 600
    lineHeight: 1.15
  title:
    fontFamily: "Poppins, sans-serif"
    fontSize: "clamp(1.125rem, 1.3vw, 1.3125rem)"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  figure:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(2rem, 3vw + .75rem, 3rem)"
    fontWeight: 800
    lineHeight: 0.9
  lead:
    fontFamily: "Barlow, sans-serif"
    fontSize: "clamp(1.0625rem, 1.4vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Barlow, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 700
    letterSpacing: "0.12em"
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
    backgroundColor: "{colors.orange-action}"
    textColor: "{colors.white}"
    rounded: "{rounded.none}"
    padding: "8px 24px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.orange-action-hover}"
    textColor: "{colors.white}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "8px 24px"
    height: "48px"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  chip-filter:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 16px"
    height: "44px"
  chip-filter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  figure-cell:
    backgroundColor: "{colors.white}"
    textColor: "{colors.muted}"
    padding: "32px 24px 24px"
  figure-cell-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-dark}"
  space-letter:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.ink}"
    size: "48px"
  input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "12px 14px"
    height: "52px"
---

# Design System : Parc des Expositions d’Abidjan

> Système en vigueur après la refonte (direction B). Détails, contrastes et anti-patterns : `design-system/pea/MASTER.md`. L'état précédent est archivé dans `design-system/pea/DESIGN-avant-refonte.md`.

## Overview

**Creative North Star : « Signalétique & architecture »**

Le site se lit comme la signalétique d'un parc d'expositions : des titres condensés en capitales, des repères orange qui indiquent où aller et des grilles en filets d'un pixel qui rappellent les plans de halls. L'échelle se montre par les chiffres (6 500 m², 67 000 m²), pas par des effets. Le motif de l'arche du logo (une cloche effilée au-dessus d'un arc plat, relevée au pixel près sur le logo) signe les moments clés : le héros, le bloc d'appel à l'action, la visite 360° et les visuels provisoires.

La densité est généreuse sur les sections (64 à 128 px) et serrée dans les grilles, où les cellules sont jointives. Les surfaces restent planes : aucune ombre, aucun arrondi au-delà de 2 px, aucun dégradé décoratif.

**Key Characteristics:**
- Encre, blanc et papier chaud, avec l'orange réservé aux signaux et aux actions.
- Titres en Poppins 600 orange logo (#DB5913), la police du logo ; Barlow Condensed en capitales pour les labels, boutons et chiffres ; Barlow pour la lecture. Polices 100 % Google Fonts.
- Grilles visibles, cellules de tailles inégales : bento, bandes de chiffres, une vedette et une liste.
- Angles vifs, pas d'ombres, filet orange de 4 px sous l'en-tête.

## Colors

Une palette de chantier noble : de l'encre profonde, un papier chaud et un orange qui sert de balise.

### Primary
- **Orange PEA** (#f36a00) : la couleur du logo. Elle sert aux aplats (lettres de hall, plaques), au filet d'en-tête, aux chiffres et aux accents sur fond encre. Jamais pour du texte sur fond clair (3,06:1).
- **Orange Action** (#c2410c) : fond des boutons principaux (texte blanc, 5,18:1), eyebrows et page active sur fond clair. Au survol : #9a3412.
- **Orange Titre** (#db5913) : couleur du texte du logo, réservée aux h1/h2 (Poppins 600, ≥ 24 px). Grand texte uniquement : 3,85:1 sur blanc, 3,5:1 sur papier, 4,87:1 sur encre. Jamais pour un texte de moins de 24 px.

### Secondary
- **Vert Lagune** (#0e6f54) : dates et statut « à venir » (6,14:1 sur blanc).

### Neutral
- **Encre** (#111217) : texte, héros, section services, pied de page, encarts.
- **Encre 2** (#1a1c21) : cellules et visuels sur fond sombre.
- **Papier chaud** (#f5f3ee) : fond de page. C'est le « blanc chaud » de l'identité.
- **Papier 2** (#ebe8e1) : fond des visuels provisoires, avec l'arche en trait.
- **Ardoise** (#55595f) : texte secondaire sur fond clair (6,35:1 sur papier).
- **Brume** (#b9bbc0) : texte secondaire sur encre (9,74:1).
- **Filet** (#d9d7d1) et **Filet sombre** (#2e3138) : lignes de grille.

### Teintes du diaporama (calculées)
Chaque image du diaporama fournit une teinte dominante calculée à la génération (`slide_accent()`). En « Signalétique stricte » (seconde passe, choix B1), elle ne colore que l’indicateur actif et la molette de l’indicateur de défilement : titre et boutons restent dans la charte (blanc, orange action).

### Named Rules
**La règle du signal unique.** L'orange indique toujours une direction, un repère ou une action, jamais un remplissage.
**La règle des deux oranges.** #f36a00 sur fond sombre ou sans texte, #c2410c dès qu'un texte doit être lu sur fond clair.

## Typography

**Title Font :** Poppins 600 (Google Fonts), la police du logo, couleur #DB5913, casse normale
**Signage Font :** Barlow Condensed (Google Fonts) : labels, boutons, dates, chiffres-clés
**Body Font :** Barlow (Google Fonts), repli `sans-serif`

**Character :** les titres parlent avec la voix du logo (géométrique, arrondie, orange) ; la grotesque condensée reste la couche de signalétique (labels, boutons, chiffres) ; Barlow assure la lecture. L'ancienne police des titres (Barlow Condensed 800 en capitales) est archivée dans `design-system/pea/ARCHIVE-TITRES-BARLOW.md`.

### Hierarchy
- **Hero** (Poppins 600, clamp 32→56 px, lh 1.1) : titre du diaporama de l’accueil, en blanc (sur photo).
- **Display** (Poppins 600, clamp 32→56 px, lh 1.1) : h1 de page, blanc sur l’en-tête orange ; 30→44 px dans les en-têtes compacts.
- **Headline** (Poppins 600, clamp 24→36 px, lh 1.15, #DB5913) : h2 de section (≥ 24 px : grand texte, 3,85:1 sur blanc, 4,87:1 sur encre).
- **Title** (Poppins 600, clamp 18→21 px, lh 1.3, encre ou blanc) : titres de cartes, de services et d'encarts ; pas d'orange à cette taille (3,85:1 < 4,5:1). La classe `.t3` applique ce style à un h2 pour garder une hiérarchie correcte.
- **Figure** (800, clamp 32→48 px) : chiffres-clés, jamais plus grands que les titres de section.
- **Lead** (400, 17→20 px, lh 1.55, 60ch max) : chapô.
- **Body** (400, 17 px, lh 1.6, 68ch max) : texte courant.
- **Label** (700, 14 px, .12em, MAJ) : eyebrows avec un trait orange de 2 px à gauche (bordure, pas de pseudo-élément), dates, plaques.

### Named Rules
**La règle du trait.** Les eyebrows portent un simple trait orange de 2 px en bordure gauche ; aucun carré ni pseudo-élément décoratif.
**La règle des capitales.** Seuls les labels et boutons (Barlow Condensed) sont en capitales ; titres (Poppins) et texte courant restent en casse normale (les titres en capitales ont été essayés puis écartés).
**La règle du titre logo.** h1 et h2 prennent la police et l'orange du logo (Poppins 600, #DB5913) ; sur photo ils restent blancs, et les petits titres (h3) restent encre.
**La règle du sur-titre discret.** Le sur-titre orange (carré de 10 px) n'apparaît que dans les héros et le bloc d'appel à l'action. Dans le corps des pages, il passe en ardoise avec un tiret de 16 px.

## Layout

Conteneur `min(1320px, 100% − 2 × gouttière)`, avec une gouttière de 16 px sous 768 px, 32 px de 768 à 1279 px et 64 px au-delà. La mise en page est mobile-first, avec des points de rupture à 480, 600, 768, 1024 et 1120 px (70em, menu complet). Les grilles « plan de hall » utilisent `gap: 1px` sur fond de filet : les cellules se touchent et la grille se voit. Les compositions sont volontairement variées : bande de chiffres de largeurs inégales (1.35/1/1.15/.85), bento des espaces (1.45/1, la première cellule sur deux rangées), agenda avec une vedette et une liste, services en tableau sur deux colonnes, photothèque sur 12 colonnes.

## Elevation & Depth

Aucune ombre. La profondeur vient uniquement de l'alternance des surfaces (encre, blanc, papier) et des filets. L'en-tête collant est séparé du contenu par un filet orange de 4 px.

## Shapes

Angles vifs partout (0 px) ; 2 px seulement sur les champs de formulaire. L'arche du logo est le seul élément courbe. Elle est formée de deux surfaces pleines effilées : la cloche (épaisse de 6,5 unités au sommet, en pointe aux extrémités) et l'arc plat dessous (3,5 unités au centre), dans un viewBox `16 -1 360 68`. On la trouve en SVG inline dans le héros et le CTA, et en image de fond dans les visuels du Dôme, la visite 360° et les emplacements photo.

## Components

- **Bouton primaire** : orange action, texte blanc, Barlow Condensed 700 MAJ 15 px, hauteur minimale 48 px, flèche SVG qui glisse de 3 px au survol.
- **Bouton secondaire** : contour 2 px de la couleur du texte. Il s'inverse au survol (encre ou blanc selon le fond).
- **En-tête** : logo officiel (`assets/logo-pea.webp`), navigation avec `aria-current`, CTA. Sous 1120 px, un bouton « Menu » (`aria-expanded`) ouvre un panneau encre, et le CTA se réduit à « Devis » sous 600 px.
- **Bande de chiffres** : cellules blanches ; sur l’accueil (`.figures--interactive`), le style encre + chiffre orange devient l’effet de survol et de focus. Les chiffres comptent jusqu’à leur valeur à l’apparition (valeur finale en `sr-only`, désactivé si mouvement réduit). « Visiter le Parc » est un bouton secondaire.
- **Carte espace** : photo pleine carte (`object-fit: cover`), dégradé encre en bas, plaque avec la lettre de hall (A/B/C) sur carré orange, le nom, les données et une flèche ; zoom léger au survol. Liens vers les pages dédiées (hall-exposition, le-dome, parvis-esplanades).
- **Ligne de service** : numéro orange, titre, description, filet sombre.
- **Filtres** : `<button aria-pressed>` avec contour encre, l'état actif est plein.
- **En-tête de page intérieure** : à partir de 1024 px, deux colonnes (titre 1.65fr, chapô 1fr aligné en bas), pour éviter le vide à droite. Pas de césure automatique dans les titres.
- **Visite 360°** : façade (arche et bouton « Lancer la visite 360° »). Au clic, l'iframe Matterport est injectée sur place (`play=1`, plein écran autorisé). Sans JavaScript, le lien ouvre Matterport dans un nouvel onglet.
- **Encart** : bordure encre 1 px, collant à partir de 1024 px.
- **En-tête compact** (`.page-hero--compact`) : sur les fiches, l'agenda, le contact et la visite, le h1 descend à `clamp(2.5rem, 5.5vw, 4.5rem)` pour que le contenu utile apparaisse au-dessus du pli.
- **Filtres** : le groupe commence toujours par « Tous », actif par défaut. Un compteur `role="status"` (« 3 espaces ») annonce le résultat et un état vide en pointillés s'affiche quand aucun élément ne correspond. Les données sont portées par des attributs `data-usage` / `data-espace` / `data-type`, à administrer dans Drupal.
- **Formulaire de devis** : trois `fieldset` (Vous, Votre événement, Vos besoins) séparés par un filet encre. Les champs obligatoires portent un astérisque orange, les autres la mention « (facultatif) ». La date est une période (du / au) avec une case « dates flexibles », les services sont des cases à cocher et un consentement est requis. Les erreurs s'affichent sous le champ (#b42318, `aria-invalid` + `aria-describedby`), le focus va sur le premier champ en erreur, et le succès s'affiche dans un bloc encre. L'espace peut être pré-rempli via `?espace=hall|dome|parvis`.
- **Barre utilitaire** (sur mobile : WhatsApp et FR | EN seulement ; réseaux sociaux dans le menu) : bandeau encre de 44 px au-dessus de l'en-tête collant : numéro en lien WhatsApp (`wa.me`) à gauche ; à droite, le sélecteur de langue FR | EN (langue active soulignée d’orange, `aria-current`) et les icônes Instagram, Facebook, LinkedIn (cibles de 44 px).
- **Frise de l'agenda (compacte)** : vignette carrée de 72 px (affiche entière sur encre), type, titre, date et un seul bouton « Détails » ; « Réserver » et « Site officiel » sont dans la fenêtre. Description d’origine : intertitres de mois collants (carré orange et titre condensé), puis une colonne date (jour en très grand, fin de période ou mois en label), un rail de 1 px et un repère carré. Les cartes sont sur fond papier ; le prochain événement, calculé d'après la date du jour, a un repère orange, une carte blanche bordée d'encre et la mention « Prochainement ». Les actions sont « Réserver » (bouton primaire), quand un lien existe, et « Détails » (lien fléché ou icône de lien externe).
- **Fenêtre de détails d'événement** (`<dialog>`) : affiche officielle entière (`contain` sur encre, 48vh max) au-dessus de en-tête encre avec l'arche en ton sourd, le type, le titre et la date, puis la description, une liste de faits (Date, Lieu, Organisateur) et les liens. Elle se ferme avec le bouton, la touche Échap ou un clic sur le fond, et le focus revient au bouton « Détails ». Sans JavaScript, les détails s'affichent directement dans la carte.
- **Mur d'actualité** : grille jointive de 1 px. La tuile Facebook occupe deux rangées, la tuile Instagram (grille de vignettes) deux colonnes ; puis LinkedIn sur fond papier et « Prochainement au Parc » sur fond encre.
- **Intégrations tierces** (`data-embed-src`) : une façade papier avec l'arche et un bouton « Afficher… » tant que le visiteur n'a pas donné son accord ; l'iframe est injectée après accord ou au clic.
- **Bandeau cookies** : fixé en bas, fond encre ; « Tout refuser » et « Tout accepter » sont deux boutons secondaires de même poids.
- **Bloc « Parlez-nous de votre projet » (`.cta--photo`)** : il utilise le rendu du Dôme (`images/parleznousvotreprojet.jpg`), dont le toit reprend l'arche du logo. À partir de 1024 px, la photo occupe les 70 % de droite sous un dégradé encre horizontal (opaque jusqu'à 36 %, 0,92 à 46 %) et le texte est limité à 38ch pour rester sur l'encre. Sous 1024 px, la photo est placée en bas du bloc, avec un fondu vertical court.
- **Carte d'accès** : iframe Google Maps chargée en différé, au ratio 4:3 sur mobile et 16:10 sur grand écran, à côté de l'adresse et des boutons Itinéraire / Google Maps.
- **Pied de page** : une vraie navigation (Espaces, Services, Destination, Expertise), le téléphone et le logo GL events (le carré rouge est recadré en CSS, avec son coin arrondi, pour supprimer la marge blanche du fichier). FR / EN renvoient vers la page équivalente dans l’autre langue.
- **Diaporama Ken Burns** (héros de l’accueil, 90vh) : 8 images en fondu enchaîné toutes les 7 s avec zoom lent ; bouton Pause/Lecture (`aria-pressed`) et 8 indicateurs (l’actif prend la teinte de l’image) ; boutons orange, titre blanc ; mouvement réduit = fondu sans zoom. Indicateur « souris » animé (4 cycles) vers la section suivante.
- **Références (accueil, avant le pied de page)** : « Ils nous ont fait confiance », carrousel de 10 logos d’organisateurs (`images/logos` → `assets/img/logos`, 400 px), 5 par page dès 1024 px (3 dès 600 px, 2 en dessous). Tuiles blanches en 3:2, logos désaturés (gris, opacité .75), couleur au survol (toujours en couleur sur écran tactile). Le logo Abidjan Border Forum, blanc sur transparent, a une tuile encre. Défilement automatique d’une page toutes les 5 s (retour au début à la fin), boutons Précédent / Pause / Suivant de 48 px, pause au survol, au focus et quand l’onglet est masqué ; aucune animation si mouvement réduit.
- **En-tête de page orange (`.page-hero--bg`)** : fond orange logo #DB5913 ; la photo du sujet (choix dans `PAGE_BG`, `tools/pages/generer.py`), désaturée, s’y fond en mode produit à 60 % (elle ne peut que foncer l’orange), sous un voile encre de 14 %. Pire cas #bf4f14 : texte blanc 4,85:1. Titre, chapô, sur-titre, fil d’Ariane, filtres (contour blanc, actif blanc plein) et focus passent en blanc. Fiche événement : héros photo sombre.
- **En-tête transparent (toutes les pages)** : comme sur l’accueil, barre utilitaire et en-tête se posent sur le héros ou l’en-tête orange ; sur l’orange, logo passé en blanc (filtre), page active soulignée de blanc, bouton devis encre, langues en blanc. Barre utilitaire : léger fond noir translucide (encre 32 %).
- **En-tête transparent (accueil)** : avec JavaScript, la barre utilitaire et l’en-tête se posent sur le diaporama (fond et filet transparents, liens et bouton « Menu » en blanc, page active en orange, bouton devis orange), au-dessus d’un voile encre dédié (.82 → 0 sur 260 px ; texte blanc ≥ 7,6:1 dans le pire cas). Fond blanc et filet orange dès 8 px de défilement ou menu ouvert. Sans JavaScript : en-tête blanc.
- **Retour en haut** : carré encre de 48 px fixé en bas à droite, visible après un écran de défilement ; remonte au-dessus du bandeau cookies (`--banner-h`).
- **Galeries et visionneuse** : sur les pages espaces, toutes les photos du dossier source (1 grande en 2×2, chargée immédiatement, puis vignettes en grille dense 4 colonnes) ; vignettes jointives (4 px) en `cover` ; chaque vignette ouvre une visionneuse `<dialog>` plein écran (légende, compteur, précédent/suivant au clavier, Échap, retour du focus). Photothèque en grille dense 4 colonnes avec une vignette sur cinq en 2×2.
- **Pages espaces** : bande de 3 chiffres officiels, galerie, présentation, usages (étiquettes à puce), équipements (Dôme), encart devis pré-rempli et documents (fiche technique, plan du site PDF).
- **Accompagnement (Services)** : texte d’accompagnement + bloc encre « Bâtiment administratif » en grille 2 colonnes ; engagements RSE en liste numérotée sur 3 colonnes.
- **Série « destination »** (Qui sommes-nous) : 4 visuels carrés à légende incrustée, affichés entiers (`contain`), légende reprise en texte alternatif, ouverts dans la visionneuse.
- **Comparatif des espaces** (`.compare`, Nos espaces) : tableau surface / hauteur / capacité / usages / documents / devis pré-rempli ; sous 1024 px, chaque ligne devient une fiche avec libellés (`data-label`).
- **Message de succès du devis** : récapitule type d’événement, espace et dates saisis.
- **Version anglaise** : pages générées dans `en/` à partir du dictionnaire `tools/i18n/en.json` (chaînes entières), `hreflang` réciproques.
- **Champ** : label visible relié par `for`, bordure #84878d (3,6:1), focus orange action.
- **Focus** : contour de 3 px orange action, décalé de 3 px ; orange PEA sur fond sombre.

## Do's and Don'ts

- **Do** garder deux niveaux de boutons (primaire orange, secondaire contour) ; les liens fléchés sont des liens, pas des boutons.
- **Do** vérifier chaque paire texte/fond (4,5:1 minimum, 3:1 pour le gros texte et l'UI).
- **Do** varier les compositions d'une section à l'autre.
- **Do** utiliser exclusivement des Google Fonts.
- **Don't** utiliser de bordure latérale épaisse sur une carte (side-tab), d'ombre, de pilule ou de rayon supérieur à 2 px.
- **Don't** utiliser de dégradés violets, de rayures en dégradé ni d'emojis comme icônes.
- **Don't** poser du texte orange #f36a00 sur un fond clair.
