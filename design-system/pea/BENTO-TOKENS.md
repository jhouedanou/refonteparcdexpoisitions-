# Tokens Bento DS : thème « PEA »

Ce document est destiné à l'équipe Drupal (thème `webgl_bento_ds_theme`). Il donne les valeurs à appliquer aux variables Figma de **Bento DS** (`docs/retourclient/Bento DS.fig`) pour obtenir le Parc des Expositions d'Abidjan conforme à sa **charte graphique**. Dans la maquette, ces valeurs sont dans `styles.css` (`:root`). Les noms CSS reprennent les noms Figma, avec `-` à la place de `/`.

Flux Bento à respecter : jeton de composant → **Semantic** → **Brand** (un nœud n'est jamais lié directement à Brand ou à Primitives).

## Brand : nouveau mode « PEA » (à ajouter aux modes Défaut, Chaud et Sombre)

| Variable Figma | PEA | Origine charte |
|---|---|---|
| brand/primary/50 | #FCF2EA | teinte |
| brand/primary/100 | #F8E0CC | teinte (accents du pied de page) |
| brand/primary/200 | #EAD1B8 | Beige 234-209-184 |
| brand/primary/300 | #F3931B | Orange clair 243-147-27 |
| brand/primary/400 | #D68644 | Terracotta 214-134-68 |
| brand/primary/500 | #DD5F2E | 221-95-46 |
| **brand/primary/600** | **#DA5900** | **Orange PEA 218-89-0 (logo)** |
| brand/primary/700 | #B34900 | ombre de l'orange (texte blanc 5,43:1) |
| brand/primary/800 | #9D4015 | Brun 157-64-21 |
| brand/primary/900 | #5D120A | Brun foncé 93-18-10 |
| brand/primary/950 | #3A0B06 | ombre |
| brand/secondary/200 | #95C11F | Vert clair 149-193-31 |
| brand/secondary/600 | #006528 | Vert 0-101-40 |
| brand/secondary/700 | #00521F | ombre |
| brand/tertiary/200 | #D5CEBC | Pierre 213-206-188 |
| brand/tertiary/600 | #5D120A | Brun foncé |

## Primitives (écarts avec Bento)

| Variable | Bento | PEA | Pourquoi |
|---|---|---|---|
| font/family/base | system-ui, sans-serif | **Poppins, sans-serif** | charte p. 7 : Poppins pour toute la communication |
| font/family/display | → base | → base | |
| radius/sm, md, lg | 2 / 6 / 8 | **0** | choix PEA : angles vifs |
| radius/full | 9999 | **0** (boutons, champs) | idem |
| radius-field | → radius/full | **2 px** | champs de formulaire seulement |
| color/neutral/950 | #0A0A0A | #0A0A0A | = Noir de la charte (Monochrome) |

## Semantic (écarts avec Bento)

| Variable | Bento | PEA | Pourquoi |
|---|---|---|---|
| color/primary | → brand/primary/600 | **→ brand/primary/700** | les boutons à texte blanc doivent atteindre 4,5:1 (#DA5900 : 3,88:1) |
| color/primary-hover | → brand/primary/700 | → brand/primary/800 | brun de la charte |
| color/primary-content | → brand/primary/50 | #FFFFFF | |
| *color/brand* (nouveau) | — | → brand/primary/600 | logo, aplats, arche, titres ≥ 24 px |
| color/secondary | → brand/secondary/600 | → brand/secondary/600 | vert charte |
| color/base-100 | → neutral/50 | #FFFFFF | |
| color/base-200 | → neutral/100 | #F7F5F1 | pierre très claire (fond de page) |
| color/base-300 | → neutral/200 | #ECE8DF | |
| color/overlay-scrim | → brand/primary/950 | #0A0A0A | voile noir sur photo |

## Composants (écarts avec Bento)

| Variable | Bento | PEA |
|---|---|---|
| btn/radius | → radius-field (pilule) | 0 |
| btn/padding-x / padding-y | 16 / 12 | 20 / 12 (hauteur min. 48 px) |
| btn/font-weight | 400 | 600 |
| btn/font-size | 16 | 15 |
| btn/text-transform | none | none |
| badge/radius, badge/radius-pill | 6 / full | 0 |
| card/radius, cta/radius, tab/radius | 8 | 0 |
| menu/submenu-radius | 6 | 0 |
| menu/submenu-bg | blanc | noir #0A0A0A (filet orange 3 px) |
| menu/submenu-shadow | 0 10px 15px | aucune |
| footer/bg | → brand/primary/800 | → brand/primary/800 (= brun #9D4015) |
| page-header/back-radius | full | 0 |
| site-header/bg | neutral/50 | blanc (transparent sur photo, logo Négatif) |

## Correspondance des composants

Voir le tableau « Correspondance Bento DS » dans `DESIGN.md`. Nouveau composant utilisé : **Block/Video** (vidéo de présentation, façade avec affiche et lecture au clic).

## Contrastes

Tous les couples texte/fond sont vérifiés dans `MASTER.md` § 2. Seuls les titres h1/h2 en #DA5900 sont sous 4,5:1 (3,88:1 sur blanc, 3,56:1 sur pierre) : ils restent ≥ 24 px, donc du « grand texte » (seuil 3:1).
