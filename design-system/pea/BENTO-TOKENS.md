# Tokens Bento DS : thème « PEA »

Ce document est destiné à l’équipe Drupal (thème `webgl_bento_ds_theme`). Il donne les valeurs à appliquer aux variables Figma de **Bento DS** (`docs/retourclient/Bento DS.fig`) pour obtenir le Parc des Expositions d’Abidjan conforme à sa **charte graphique**.

Dans la maquette, ces valeurs sont dans `styles.css`, section 1. Les noms CSS reprennent les noms Figma, avec `-` à la place de `/`. Le contrôle de conformité et la liste complète des écarts sont dans `CONFORMITE.md`.

Flux Bento à respecter : jeton de composant → **Semantic** → **Brand**. Un nœud n’est jamais lié directement à Brand ou à Primitives.

## Brand : mode « PEA » (à ajouter aux modes Défaut, Chaud et Sombre)

| Variable Figma | PEA | Origine charte |
|---|---|---|
| brand/primary/50 | #FCF2EA | teinte (aplat crème, `accordion/background-color`, `card/primary-bg`) |
| brand/primary/100 | #F8E0CC | teinte (accents sur aplats sombres) |
| brand/primary/200 | #EAD1B8 | Beige 234-209-184 |
| brand/primary/300 | #F3931B | Orange clair 243-147-27 |
| brand/primary/400 | #D68644 | 214-134-68 |
| brand/primary/500 | #DD5F2E | 221-95-46 (`accordion/icon-color`) |
| **brand/primary/600** | **#DA5900** | **Orange PEA 218-89-0 (logo)** |
| brand/primary/700 | #B34900 | ombre de l’orange (texte blanc 5,43:1) |
| brand/primary/800 | #9D4015 | Brun 157-64-21 (`topbar/bg`, `footer/bg`, `menu/fg-active`) |
| brand/primary/900 | #5D120A | Brun foncé 93-18-10 |
| brand/primary/950 | #3A0B06 | ombre (`accordion/title-color`) |
| brand/secondary/200 | #95C11F | Vert clair 149-193-31 |
| brand/secondary/600 | #006528 | Vert 0-101-40 |
| brand/secondary/700 | #00521F | ombre |
| brand/tertiary/200 | #D5CEBC | Pierre 213-206-188 |
| brand/tertiary/500 | #C96B51 | Terracotta 201-107-81 |
| brand/tertiary/600 | #5D120A | Brun foncé |

## Primitives (écarts avec Bento)

| Variable | Bento | PEA | Pourquoi |
|---|---|---|---|
| font/family/base | system-ui, sans-serif | **Poppins, sans-serif** | charte p. 7 |
| graisses utilisées | 400 · 500 · 600 · 700 | **100 · 400 · 700** | kit web p. 17 (Thin, Regular, Bold) : 500 et 600 passent à 700 |
| radius/sm · md · lg · full | 2 · 6 · 8 · 9999 | **0** | choix PEA : angles vifs |
| radius-field | → radius/full | **2 px** | champs uniquement |

## Semantic (écarts avec Bento)

| Variable | Bento | PEA | Pourquoi |
|---|---|---|---|
| color/primary | → brand/primary/600 | **→ brand/primary/700** | boutons à texte blanc ≥ 4,5:1 (#DA5900 : 3,88:1) |
| color/primary-hover | → brand/primary/700 | → brand/primary/800 | brun de la charte |
| color/primary-content | → brand/primary/50 | #FFFFFF | |
| *color/brand* (nouveau) | — | → brand/primary/600 | logo, arche, titres, chiffres |
| color/base-100 · 200 · 300 | neutral 50 · 100 · 200 | #FFFFFF · #F7F5F1 · #E7E1D6 | fond blanc de la charte |
| color/overlay-scrim | → brand/primary/950 | #000 (voile sur photo uniquement) | |

## Composants (écarts avec Bento)

| Variable | Bento | PEA |
|---|---|---|
| title/color | → brand/primary/800 | **→ brand/primary/600** pour L1–L3 ; base-content pour L4–L6 |
| title/font-weight | 700 | 700 |
| btn/radius, badge/radius, card/radius, cta/radius, tab/radius, modal/radius, accordion/radius, image-gallery/radius, block-map/radius | 6 à 9999 | 0 |
| btn/font-weight · font-size | 400 · 16 | 400 · 16 (conforme) |
| site-header/logo-height | 32 px | 40 px (mobile) / 48 px : logo PEA sur trois lignes |
| site-header/height | 64 | 64 (72 dès 1120 px, avec le logo de 48 px) |
| form/field-border-color | neutral/300 | neutral/500 (#737373) : 3:1 |
| form/field-min-height · font-size | 40 · 14 | 48 · 16 |
| tab/selected/fg | primary/500 | primary/700 (texte) ; filet en primary/600 |
| block-events/tags-filter-bg-checked | base-content | primary (pas de fond noir) |
| block-key-figures/value-color | base-content | brand/primary/600 (charte p. 16 : chiffres en orange) |

Tous les autres tokens de composants utilisés (espacements, paddings, tailles, ombres, voiles) reprennent les valeurs Bento.
