---
name: PEA — Parc des Expositions d'Abidjan (maquette v1)
description: Maquettes HTML statiques du site du Parc des Expositions d'Abidjan — état avant refonte
colors:
  orange: "#f36a00"
  ink: "#111217"
  muted: "#6f737b"
  paper: "#f7f5f0"
  white: "#ffffff"
  line: "#dfded9"
  sand: "#d6c4ad"
  green: "#0e6f54"
  dark-surface: "#1c2025"
  dark-line: "#2d3137"
  placeholder-from: "#ded9cf"
  placeholder-to: "#aeb6ae"
  note-bg: "#fff3ea"
  note-text: "#6c4d37"
typography:
  display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: "72px"
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: "48px"
    lineHeight: 1.03
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: "28px"
    lineHeight: 1.1
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "16px"
    lineHeight: 1.45
  label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    letterSpacing: "0.22em"
rounded:
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "18px"
  card: "22px"
  media: "26px"
  cta: "28px"
  pill: "999px"
spacing:
  section: "88px"
  hero-top: "110px"
  page-hero-top: "80px"
  grid-gap-sm: "12px"
  grid-gap: "14px"
  grid-gap-md: "18px"
  split-gap: "56px"
  intro-gap: "90px"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "14px 20px"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "14px 20px"
  button-light:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "14px 20px"
  kpi:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.card}"
    padding: "28px"
  service-card:
    backgroundColor: "{colors.dark-surface}"
    rounded: "{rounded.xl}"
    padding: "24px"
  chip:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  input:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "15px 16px"
---

# Design System: PEA — maquette v1 (état avant refonte)

> Instantané « scan mode » de `styles.css` au commit `70cea45`. Il documente l'existant avant la refonte.
> Le système cible (direction B « Signalétique & architecture ») est décrit dans `design-system/pea/MASTER.md`.

## Overview

**Creative North Star : « Le salon premium générique »**

Une maquette sobre de site institutionnel : fond blanc cassé chaud, encre presque noire, accent orange repris du logo. Les titres en Georgia veulent donner un ton éditorial, le texte est en Arial. La mise en page repose sur des cartes très arrondies (22–28px), des pilules et des placeholders en dégradé gris-vert. L'ensemble est propre mais peu spécifique : il pourrait servir à n'importe quel lieu événementiel.

**Key Characteristics:**
- Palette orange / encre / papier chaud, accent vert pour les dates.
- Contraste serif (titres) / sans-serif (texte) avec polices système.
- Cartes et boutons très arrondis, ombre douce unique.
- Un seul point de rupture responsive (900px).

## Colors

Palette chaude et restreinte, l'orange porte toute l'énergie.

### Primary
- **Orange PEA** (#f36a00) : boutons principaux, eyebrows, numéros de services, lien actif. *Contraste 3,06:1 avec le blanc — insuffisant pour du texte.*

### Secondary
- **Vert Lagune** (#0e6f54) : dates d'événements.

### Neutral
- **Encre** (#111217) : texte, fonds sombres, bouton secondaire.
- **Gris ardoise** (#6f737b) : paragraphes (4,37:1 sur papier — limite).
- **Papier chaud** (#f7f5f0) : fond de page.
- **Filet** (#dfded9) : bordures de cartes, header, footer.
- **Sable** (#d6c4ad) : déclaré mais inutilisé.

## Typography

**Display Font:** Georgia (fallback Times New Roman)
**Body Font:** Arial (fallback Helvetica)

**Character:** une serif d'édition classique sur un sans-serif bureautique ; ni l'une ni l'autre ne rappelle le sans arrondi du logo officiel.

### Hierarchy
- **Display** (72px, lh .98, -0.04em) : h1 héros. Passe à 48px sous 900px, aucune autre adaptation.
- **Headline** (48px, lh 1.03) : h2 de section, jamais réduit.
- **Title** (28px, lh 1.1) : h3 de cartes.
- **Body** (16px, lh 1.45) : paragraphes, gris ardoise.
- **Label** (11–13px, 700, uppercase, .14–.22em) : eyebrows, nav, boutons, breadcrumbs.

## Layout

Conteneur `.wrap` = `min(1280px, 100% - 64px)`. Sections de 88px verticaux. Grilles : intro 1.05fr/.95fr, split 1fr/1fr, cartes espaces 1.35fr/.8fr/.8fr, kpis et services en 4 colonnes, agenda en 3, sidebar 1fr/320px. Sous 900px : la nav disparaît (pas de menu mobile), les grilles passent en 1 ou 2 colonnes. Aucun réglage pour 375px.

## Elevation & Depth

Une seule ombre ambiante sur les cartes espaces (`0 16px 48px rgba(17,18,23,.08)`). La profondeur vient surtout de l'alternance fond papier / blanc / encre et des légendes sombres semi-opaques posées sur les visuels.

## Shapes

Langage très arrondi : pilules pour boutons et chips, 16–28px pour cartes, médias et CTA. Cercle orange translucide décoratif dans le bloc CTA.

## Components

- **Boutons** : pilules 13px gras, trois variantes (orange, encre, blanc) ; aucun état hover/focus défini.
- **KPI** : boîtes blanches bordées, chiffre Georgia 32px.
- **Carte espace** : visuel en dégradé + légende encre en bas.
- **Service** : carte sombre numérotée, 8 instances identiques.
- **Événement** : vignette photo + date verte + titre.
- **Formulaire** : champs 15px de padding, radius 12px, labels non associés.
- **Note** : encadré orange pâle avec bordure gauche.

## Do's and Don'ts

- **Don't** poser du texte blanc sur l'orange #f36a00 (3,06:1).
- **Don't** masquer la navigation sans alternative mobile.
- **Don't** multiplier les styles inline (footer, marges).
- **Do** garder l'orange comme couleur de marque rare et signifiante.
