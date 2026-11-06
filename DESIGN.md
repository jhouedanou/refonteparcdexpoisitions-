---
name: Parc des Expositions d’Abidjan
description: Charte graphique officielle (Poppins 100/400/700, orange #DA5900, aplats d’accompagnement) appliquée aux composants Bento DS de GL events, en angles vifs
colors:
  brand: "#da5900"
  primary: "#b34900"
  primary-hover: "#9d4015"
  aplat-brun: "#9d4015"
  aplat-vert: "#006528"
  aplat-brun-fonce: "#5d120a"
  aplat-creme: "#fcf2ea"
  beige: "#ead1b8"
  pierre: "#d5cebc"
  terracotta: "#c96b51"
  orange-clair: "#f3931b"
  vert-clair: "#95c11f"
  base-100: "#ffffff"
  base-200: "#f7f5f1"
  base-300: "#e7e1d6"
  base-content: "#0a0a0a"
  muted: "#525252"
  on-dark-muted: "#f8e0cc"
  field: "#737373"
  neutral-100: "#f5f5f5"
  neutral-200: "#e5e5e5"
  neutral-300: "#d4d4d4"
typography:
  title-l1:
    fontFamily: "Poppins, sans-serif"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.2
  title-l2:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1.875rem"
    fontWeight: 700
    lineHeight: 1.2
  title-l3:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.2
  title-l4:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.2
  title-l5:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.2
  figure:
    fontFamily: "Poppins, sans-serif"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: 1.1
  lead:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  small:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
  button:
    fontFamily: "Poppins, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1
  badge:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 700
  eyebrow:
    fontFamily: "Poppins, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
    letterSpacing: "0.08em"
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
    textColor: "{colors.base-100}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.base-content}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
  button-tertiary:
    backgroundColor: "{colors.aplat-vert}"
    textColor: "{colors.base-100}"
  button-invert:
    backgroundColor: "#fafafa"
    textColor: "{colors.base-content}"
  badge:
    backgroundColor: "{colors.base-200}"
    textColor: "{colors.base-content}"
    padding: "4px 12px"
  card:
    backgroundColor: "{colors.base-100}"
    padding: "24px"
  topbar:
    backgroundColor: "{colors.aplat-brun}"
    textColor: "{colors.base-100}"
    height: "48px"
  site-header:
    backgroundColor: "{colors.base-100}"
    height: "64px"
  page-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.base-100}"
  footer:
    backgroundColor: "{colors.aplat-brun}"
    textColor: "#fafafa"
  input:
    backgroundColor: "{colors.base-100}"
    textColor: "{colors.base-content}"
    rounded: "{rounded.field}"
    padding: "12px"
    height: "48px"
---

# Design System : Parc des Expositions d’Abidjan

> En vigueur depuis le 6 novembre 2026.
> - Sources : la **charte graphique officielle** (`docs/retourclient/PARC DES EXPOSITIONS D'ABIDJAN_CHARTE GRAPHIQUE.pdf`), qui prévaut, et le **Bento DS** de GL events (`docs/retourclient/Bento DS.fig`), qui fournit les composants et la structure des tokens.
> - Correspondance des tokens Bento et PEA : `design-system/pea/BENTO-TOKENS.md`.
> - Matrice de conformité et preuves : `design-system/pea/CONFORMITE.md`.
> - Contrôle automatique : `node tools/verif/conformite.mjs`.
> - États précédents archivés : `design-system/pea/DESIGN-avant-charte.md` (direction B) et `DESIGN-avant-refonte.md`.

## Overview

**Creative North Star : « Le Parc tel que le montre sa charte »**

Le site reprend le langage des supports officiels (PowerPoint et brochure de la charte) :
- un fond blanc ;
- de grandes photos des lieux : le Hall pavoisé, la coupole du Dôme, la salle plénière ;
- des aplats de couleurs d’accompagnement en panneaux : brun, vert, brun foncé, crème ;
- des chiffres mis en avant en orange ;
- le logo en orange sur fond clair, en blanc sur photo ou sur couleur.

Chaque bloc est un composant Bento DS, repérable dans le HTML par `data-bento="<nom Figma>"`. Les composants utilisés sont :
- structure : Topbar, Site header, Menu, Breadcrumb, Page header, Footer ;
- blocs : Block/Hero, Carousel, Block/Key figures, Card, Collection, Block/Video, Cta, Block/Partners, Block/Agenda list ;
- interactions et formulaires : Modal, Accordion, Image gallery, Form/Field, Newsletter form, Contact details, Block/Map ;
- éléments de base : Title, Button, Badge, Link.

Seul motif propre au Parc : l’**arche du logo**. La brochure de la charte reprend la même courbe. On la retrouve :
- au-dessus du titre du héros ;
- en bas des en-têtes de page et des aplats ;
- en haut du pied de page ;
- sur les chiffres-clés ;
- dans le soulignement du menu ;
- pendant le chargement.

**Key Characteristics**
- Poppins seule, en Thin, Regular et Bold (100, 400, 700 : kit web p. 17).
- L’orange PEA #DA5900 sert à la marque et aux titres de 24 px et plus. L’orange action #B34900 sert aux boutons et aux liens.
- Les fonds sont blancs ou en aplats de la charte, jamais noirs. Le noir #0A0A0A est réservé au texte et au logo monochrome.
- Angles vifs : les rayons Bento sont ramenés à 0 ; les champs de formulaire gardent 2 px.
- Ombres Bento : en-tête collé, sous-menu, modale, survol des cartes.

## Colors

### Primary
- **Orange PEA** (#DA5900, RVB 218-89-0) : logo, arche, titres L1 à L3 (24 px et plus, 3,88:1 sur blanc), valeurs des chiffres-clés (36 px).
- **Orange action** (#B34900) : fond des boutons primaires (texte blanc 5,43:1), liens, sur-titres, fond des en-têtes de page, filtres actifs. Au survol, il passe au brun #9D4015.

### Aplats d’accompagnement (charte p. 11, 16 et 17)

| Aplat | Texte | Rôle |
|---|---|---|
| Brun #9D4015 | blanc, accents crème | barre du haut (Topbar), section vidéo, pied de page |
| Vert #006528 | blanc | liste des services, bâtiment administratif |
| Brun foncé #5D120A | blanc | appel à l’action, visite 360°, bandeau cookies, message de succès, tuile « Prochainement » |
| Crème #FCF2EA | noir, titres orange | bloc newsletter, fond des chiffres-clés, accordéon |
| Beige #EAD1B8, pierre #D5CEBC, terracotta #C96B51, orange clair #F3931B, vert clair #95C11F | — | en réserve : aplats sans texte orange |

### Neutral
- Fonds : blanc (page, cartes) et pierre très claire #F7F5F1 (alternance douce des sections).
- Texte : #0A0A0A. Texte secondaire : #525252 (7,2:1).
- Bordures : #E7E1D6 pour les cartes, #737373 pour les champs.
- Voiles noirs, uniquement sur photo : héros, visionneuse, modale (60 %), survol de galerie (30 %), façade vidéo (18 %).

### Named Rules
**La règle des deux oranges.** #DA5900 pour la marque et les grands textes. #B34900 dès qu’un petit texte orange ou un bouton à texte blanc doit être lu sur fond clair.
**La règle des aplats.** Une section colorée prend une couleur de la charte, jamais du noir. Sur un aplat sombre, le texte est blanc et les accents sont crème (#F8E0CC). L’orange n’y est jamais utilisé : 1,7:1 sur le brun.
**La règle du logo intact.** Positif sur fond clair, Négatif blanc sur photo ou couleur (`filter: brightness(0) invert(1)`), Monochrome. Aucune autre teinte et aucune déformation : le script le contrôle.

## Typography

**Police unique :** Poppins (Google Fonts), chargée en 100, 400, 700 et 400 italique.

### Hierarchy (composant Bento « Title »)

| Niveau | Taille | Couleur | Usage |
|---|---|---|---|
| L1 | 48 px (36 px sous 768 px) | orange ; blanc sur photo | h1 |
| L2 | 30 px (26 px sous 768 px) | orange | h2 de section |
| L3 | 24 px | orange | intertitres d’agenda, newsletter |
| L4 | 20 px | noir | titres de cartes, encarts, h3 |
| L5 | 18 px | noir ; blanc sur aplat | titres du pied de page, cookies |

Tous les niveaux sont en Bold 700, avec un interligne de 1,2 et une marge basse de 32 px. Les classes `title title--lN` sont posées par `bentoize()` (`tools/pages/generer.py`) selon le niveau visuel du titre, pas selon sa balise.

Autres rôles :
- **Texte** : 16 px Regular, interligne 1,65.
- **Chapô** : 18 px.
- **Bouton** : 16 px Regular, en casse normale.
- **Badge** : 14 px Bold, en capitales.
- **Sur-titre** : 13 px Bold, en capitales, interlettrage .08em ; orange action, blanc sur photo, crème sur aplat.
- **Chiffre-clé** : 36 px Bold, en orange.

### Named Rules
**La règle des capitales.** Seuls les sur-titres, les badges et les éléments de la barre du haut sont en capitales. Les titres en capitales ont été refusés le 07/10, et la brochure de la charte est en casse normale.
**La règle des trois graisses.** Seules les graisses 100, 400 et 700 sont utilisées. Toute graisse Bento à 500 ou 600 passe à 700 ; le script le contrôle.

## Layout

- Conteneur : `min(1320px, 100% − 2 × gouttière)`.
- Gouttière : 16 px, puis 32 px à partir de 768 px et 64 px à partir de 1280 px.
- Hauteur des sections : de 48 à 96 px.
- Grilles en « Collection » Bento : 1 à 3 colonnes, espacement de 24 px.
- Points de rupture : 480, 600, 768, 1024, 1120 (menu complet) et 1280 px.
- Barre du haut : 48 px. En-tête : 64 px, puis 72 px à partir de 1120 px.
- En-tête de page : de 48 à 96 px en haut et en bas, plus la place de l’arche.

## Elevation & Depth

Ombres Bento :
- survol des cartes : `shadow-md` ;
- en-tête collé : `0 2px 8px rgba(0,0,0,.12)` ;
- sous-menu et menu mobile : `shadow-lg` ;
- modale et bandeau cookies : `shadow-xl`.

Ailleurs, la profondeur vient de l’alternance entre blanc, pierre et aplats.

## Shapes

- Angles vifs partout ; 2 px pour les champs. Seule exception : le coin du logo GL events, qui fait partie du fichier officiel.
- L’arche du logo est le seul élément courbe : tracés exacts, viewBox `16 -1 360 68`, jamais étirés.

## Components

Le détail des composants (specs Bento et état) est dans `design-system/pea/CONFORMITE.md` § 2. Voici les points propres au Parc.

- **Topbar** :
  - WhatsApp et « Abidjan, Côte d’Ivoire » à gauche ; FR | EN et réseaux à droite ;
  - sous 768 px, seuls le téléphone et la langue restent.
- **Site header** :
  - logo Positif, menu, WhatsApp (visible une fois l’en-tête collé), bouton « Demander un devis » (« Devis » sous 600 px) ;
  - sous 1120 px, un burger de 44 px ouvre un panneau blanc de 384 px ;
  - le sous-menu « Nos espaces » est blanc, avec une description par lien.
- **Page header** :
  - photo désaturée, fondue dans l’orange action ; arche à la couleur de la section suivante ;
  - pages événement : `meta` (« Tout l’agenda », date, type) et `addons` (Réserver, badge du lieu) ; l’affiche passe dans le contenu.
- **Block/Hero** :
  - diaporama des photos officielles, contenu de 768 px au plus ;
  - sur-titre « Le plus grand parc exposition d’Afrique de l’Ouest », l’accroche de la charte (à valider par le client) ;
  - boutons primaire et « invert » ;
  - Carousel : puces de 10 px, boutons de 56 px.
- **Card** : espaces au format paysage (badge « Espace A/B/C ») ; événements au format affiche (badge de date) ; tuiles du mur d’actualité ; encarts latéraux.
- **Block/Key figures** : éléments centrés, valeur en orange, arche tracée au-dessus ; fond crème sur l’accueil (`figures--light`).
- **Block/Video** : section brune, bouton de lecture de 64 px centré. Le MP4 n’est chargé qu’au clic : 1080p, ou 720p sous 768 px.
- **Block/Agenda list** :
  - intertitres de mois en Title L3 ;
  - cartes compactes avec badge de type et bouton « Détails » primaire ;
  - l’événement suivant est bordé d’orange ;
  - modale d’événement blanche.
- **Footer** :
  - bloc Newsletter crème juste avant ;
  - trois colonnes : le Parc (logo Négatif, coordonnées), « Nos espaces », « Votre événement » ;
  - barre légale : logo GL events en gris, © 2026, liens légaux, crédit Big Five.
- **Filtres** : boutons à bascule à contour noir de 2 px ; orange action une fois pressés.

## Correspondance Bento DS

| Composant Bento | Site |
|---|---|
| Topbar · Site header · Menu / Submenu / Menu/Mobile | `.utility`, `.topbar`, `.nav`, `.nav__sub` |
| Breadcrumb · Page header · Tabs | `.breadcrumbs`, `.page-hero`, `.subnav` |
| Title · Button · Link · Badge · Divider | `.title--l1…l6`, `.btn--*`, `.link-arrow`, `.badge--*`, `.reasons li::before` |
| Block/Hero · Carousel | `.hero--slider`, `.ctrl` |
| Block/Key figures | `.figures` |
| Card · Collection | `.card`, `.card--space`, `.card--event`, `.wall__tile`, `.aside-box`, `.collection--2/3` |
| Block/Video · Cta · Block/Partners | `.video-block`, `.tour`, `.cta`, `.logos` |
| Block/Agenda list · Modal | `.timeline`, `.tl-card`, `.event-dialog`, `.lightbox`, `.cookie-banner` |
| Accordion · Image gallery | `.faq__list`, `.gallery`, `.photo-grid`, `.destination-grid` |
| Form/Field · Newsletter form · Contact details · Block/Map | `.field`, `.newsletter-block`, `.contact-details`, `.footer__contact`, `.access__map` |
| Item list · Block/Icons text · Table | `.services`, `.reasons`, `.compare` |
| Footer | `.footer` |

## Do's and Don'ts

- **Do** lancer `node tools/verif/conformite.mjs` après chaque changement (0 écart attendu).
- **Do** poser `data-bento` sur tout nouveau composant et choisir son aplat dans la charte.
- **Don't** utiliser du noir en fond de section, une graisse autre que 100, 400 ou 700, ou une autre police que Poppins.
- **Don't** poser de texte orange #DA5900 de moins de 24 px sur fond clair, ni d’orange sur un aplat sombre.
- **Don't** recolorer ou déformer le logo.
- **Don't** réintroduire les grilles jointives de 1 px, le filet orange sous l’en-tête ou les lettres de hall : ils ont été retirés au profit des composants Bento.
- **Don't** utiliser de rayon (pilules, 8 px), de dégradé violet ou d’emoji en guise d’icône.
