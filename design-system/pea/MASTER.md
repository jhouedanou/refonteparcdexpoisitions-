# PEA — Design System MASTER

**Charte graphique officielle (novembre 2026) + composants Bento DS (GL events)**
Source de vérité globale pour les maquettes du Parc des Expositions d'Abidjan. Les règles d'une page dans `pages/<page>.md` (s'il existe) priment sur ce fichier. État précédent (direction B, Barlow) : `MASTER-avant-charte.md`.

Sources client : `docs/retourclient/PARC DES EXPOSITIONS D'ABIDJAN_CHARTE GRAPHIQUE.pdf` (la charte prévaut) et `docs/retourclient/Bento DS.fig` (on en reprend les composants et la structure des tokens ; correspondance dans `BENTO-TOKENS.md`).

Secteur : lieu événementiel B2B / MICE (salons, congrès, conventions, concerts). Cible : organisateurs, agences, directions communication, institutions. Objectif de conversion : demande de devis qualifiée.

## 1. Intention

Le site parle comme la signalétique d'un grand parc d'expositions : on lit vite, on sait où aller, on sent l'échelle des lieux.
- **Puissance** : grands chiffres, photos officielles des lieux (Hall, Dôme, parvis).
- **Flux** : flèches, lettres de halls, repères orange qui guident vers l'action.
- **Plan** : grilles visibles en filets de 1px, cellules de tailles inégales, angles vifs (choix PEA : rayons Bento ramenés à 0).

Motif signature : l'**arche** du logo, redessinée fidèlement en deux surfaces SVG pleines et effilées (une cloche haute au-dessus d'un arc plat), utilisée avec parcimonie : héros, bloc CTA, visite 360°, emplacements photo.

## 2. Couleurs (charte p. 10 et kit web p. 17)

Trois couches comme dans Bento : `--brand-*` (thème PEA) → sémantique `--color-*` → composants `--btn-*`, `--footer-bg`… Un composant ne lit jamais une couleur Brand directement.

| Token | Hex | Origine charte | Rôle | Contraste vérifié |
|---|---|---|---|---|
| `--brand-primary-600` = `--color-brand` | #DA5900 | Orange 218-89-0 | Logo, aplats, arche, h1/h2 ≥ 24 px, chiffres sur noir | 3,88 blanc · 3,56 pierre (grand texte) · 5,1 sur noir |
| `--brand-primary-700` = `--color-primary` | #B34900 | ombre de l'orange | Fond des boutons (texte blanc), liens et eyebrows orange sur clair | 5,43 blanc · 4,98 pierre |
| `--brand-primary-800` = `--color-primary-hover`, `--footer-bg` | #9D4015 | Brun 157-64-21 | Survol, fond du pied de page | blanc 6,61 · crème #F8E0CC 5,2 |
| `--brand-primary-900` | #5D120A | Brun foncé 93-18-10 | Texte des encarts, arches sourdes | 12,2 sur #FCF2EA |
| `--brand-primary-300` | #F3931B | Orange clair 243-147-27 | Aplats sans texte, badge « reporté » (texte noir 8,5) | — |
| `--brand-secondary-600` = `--color-secondary` | #006528 | Vert 0-101-40 | Dates, statut « à venir », bouton tertiaire | 7,26 blanc |
| `--brand-secondary-200` | #95C11F | Vert clair 149-193-31 | Aplats sans texte | — |
| `--brand-primary-200`, `--brand-tertiary-200` | #EAD1B8, #D5CEBC | Beige, Pierre | Surfaces d'accompagnement | — |
| `--color-base-200` | #F7F5F1 | Pierre très claire | Fond de page | texte noir 18,2 |
| `--color-dark` | #0A0A0A | Noir (monochrome) | Texte, sections sombres | blanc 19,8 |
| `--color-muted` | #525252 | — | Texte secondaire sur clair | 7,18 pierre · 7,81 blanc |
| `--color-muted-on-dark` | #A1A1A1 | — | Texte secondaire sur noir | 7,66 |
| `--form-border-color` | #737373 | — | Bordure des champs | 4,74 blanc |

**Règle des deux oranges.** #DA5900 (orange PEA) pour le logo, les aplats, l'arche, les titres ≥ 24 px et le texte sur noir ; #B34900 dès qu'un texte orange de petite taille ou un bouton à texte blanc doit être lu sur fond clair.
**Règle du pied brun.** Sur le brun #9D4015, l'orange ne se lit pas (1,7:1) : accents en crème #F8E0CC, logo en version Négatif (blanc), logo GL events en signature grise.
**Logo.** Positif orange sur fond clair, Négatif blanc sur fond couleur ou photo (`filter: brightness(0) invert(1)`), Monochrome noir. Jamais d'autre teinte ni de déformation (charte p. 5).

Interdits : dégradés violets, ombres portées décoratives, toute couleur hors charte pour les aplats.

## 3. Typographie — Poppins seule (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

Charte p. 7 : « L'ensemble des documents de communication utilisent la typographie Poppins ». Barlow et Barlow Condensed sont retirés (archives : `ARCHIVE-TITRES-BARLOW.md`, `MASTER-avant-charte.md`). Variables Bento : `--font-family-base` = `--font-family-display` = Poppins.

| Rôle | Taille | Graisse | Interlignage | Casse / approche |
|---|---|---|---|---|
| Hero (h1 du diaporama) | `clamp(2.125rem, 5vw, 4.25rem)` | 600 | 1.1 | blanc sur photo |
| Display (h1) | `clamp(2rem, 4vw, 3.25rem)` | 600 | 1.1 | blanc sur l'en-tête orange |
| Headline (h2) | `clamp(1.5rem, 2.5vw, 2.125rem)` | 600 | 1.15 | #DA5900 (≥ 24 px, grand texte) |
| Title (h3) | `clamp(1.0625rem, 1.25vw, 1.25rem)` | 600 | 1.3 | noir |
| Figure (chiffres) | `clamp(1.5rem, 2vw + .5rem, 2.125rem)` | 700 | 1 | — |
| Lead | `clamp(1.0625rem, 1.3vw, 1.1875rem)` | 400 | 1.55 | max 60ch |
| Body | 1rem (16px) | 400 | 1.65 | max 68ch |
| Bouton | 15px | 600 | 1.15 | casse normale (Bento `btn/text-transform: none`) |
| Label / eyebrow / badge | .8125rem (13px) | 600 | 1.2 | capitales, .08em |

## 4. Espacements & grille

Échelle (`--s-1` … `--s-10`) : 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 px.
- Sections : `clamp(64px, 9vw, 128px)` vertical.
- Conteneur : `min(1320px, 100% - 2 × gouttière)` ; gouttière 16px (<768) · 32px (≥768) · 64px (≥1280).
- Grilles « plan de hall » : cellules jointives séparées par 1px (`gap:1px` sur fond `--color-border`), pas d'espace blanc entre cartes.
- Points de rupture mobile-first : 480 · 600 · 768 · 1024 · 1120 (menu complet) · 1280.
- En-tête de page intérieure : deux colonnes dès 1024px (titre / chapô aligné en bas).

## 5. Formes & profondeur

- Rayons : 0 par défaut ; 2px pour champs de formulaire. Aucune bordure latérale épaisse sur une carte (« side-tab »).
- Aucune ombre. Profondeur par contraste de surfaces (noir / blanc / pierre claire) et par filets.
- Filet orange de 4px sous le header (repère « signalétique »).

## 6. Composants

- **Bouton** (Bento « Button ») : primaire fond `--btn-primary-bg` (#B34900), texte blanc, Poppins 600 15px en casse normale, min-height 48px, padding 12px 20px, angles vifs, flèche SVG qui glisse de 3px au survol. Variantes : `.btn--secondary` (Default + Outline), `.btn--tertiary` (vert), `.btn--default` (sans fond), `.btn--outline` ; état désactivé à 50 %.
- **Bouton secondaire** : bordure 2px `currentColor`, transparent ; au survol, fond ink / texte blanc (ou inversé sur sombre).
- **Lien flèche** : texte MAJ + flèche, soulignement 2px orange au survol.
- **Cellule chiffre** : chiffre Figure + label ; bande de cellules de largeurs inégales.
- **Carte espace** : visuel + plaque signalétique (lettre de hall A/B/C sur carré orange) + nom + données ; bento asymétrique.
- **Ligne service** : numéro orange · nom MAJ · description ; tableau 2 colonnes sur fond ink.
- **Chips filtres** : `<button aria-pressed>`, bordure 1px, état actif ink plein.
- **Champs** : label visible lié (`for`), bordure 1px #84878D (3,6:1 UI), focus orange-action 2px + anneau.
- **Visite 360°** : façade (arche + bouton) ; l'iframe Matterport n'est chargée qu'au clic (`assets/site.js`), lien direct sans JS.
- **Focus clavier** : `outline: 3px solid var(--color-primary); outline-offset: 3px` (sur sombre : `--color-brand` ; sur le brun du pied de page et l’orange des en-têtes : blanc).
- **Contrôle de défilement** (`.ctrl`, diaporama de l'accueil et carrousel de logos) : compteur « 01 / 08 » (Poppins 600, chiffres tabulaires, lu « Image 01 / 08 » par les lecteurs d'écran) · barre de segments décorative (`aria-hidden` ; piste 2 px, remplissage orange 4 px qui avance pendant `--ctrl-duration`, 7 s ou 5 s ; la navigation se fait par Précédent / Suivant, cibles de 44 px) · Précédent / Pause / Suivant (44 px, sans bordure, chevrons au trait, orange au survol, cadre orange 2 px au focus). La fin du remplissage fait passer à la vue suivante (barre et défilement synchrones) ; pause = bouton, survol ou focus (`.is-paused`). Variante `.ctrl--on-photo` : bandeau encre 72 %, texte blanc ≥ 7:1. Mouvement réduit : segment plein, minuterie.
- **Sous-menu de navigation** (`.nav__sub`) : panneau encre, filet orange 3 px en tête, angles vifs ; liens Poppins 500 + description Poppins 13 px (`--color-muted-on-dark`) ; page courante en orange. Bouton d'ouverture séparé du lien (disclosure, `aria-expanded`), cible 44 px.
- **WhatsApp de l'en-tête fixe** (`.topbar__wa`) : visible seulement quand l'en-tête est blanc (`.is-solid`), icône + numéro dès 1280 px, encre puis orange action au survol.
- **Newsletter** (haut du pied de page, toutes les pages) : intitulé orange, titre, phrase d'accroche ; libellé visible, champ e-mail + bouton primaire « S'inscrire », case de consentement avec lien vers la politique de confidentialité ; erreurs sous les champs (`aria-invalid`, focus sur le premier champ en erreur), confirmation `role="status"` qui reçoit le focus. Maquette : inscription simulée, à brancher sur l'outil d'e-mailing.

## 7. Accessibilité (non négociable)

- Texte ≥ 4,5:1 ; gros texte et composants UI ≥ 3:1.
- Focus visible sur tout élément interactif, lien d'évitement « Aller au contenu ».
- Cibles tactiles ≥ 44 × 44px.
- `aria-current="page"` dans la navigation ; menu mobile `<button aria-expanded aria-controls>`.
- `prefers-reduced-motion` : transitions désactivées.
- Icônes : SVG inline `aria-hidden="true"`, jamais d'emoji.

## 8. Anti-patterns à éviter

- Grilles de cartes toutes identiques (varier : bento, liste, bande, vedette + liste).
- Dégradé violet / néon, glassmorphism, ombres floues.
- Pilules et rayons > 4px (rupture avec la direction).
- Placeholder gris-vert ou rayures en dégradé : utiliser l'aplat `--color-base-300` (#ECE8DF) avec l'arche du logo en ton sourd (#CDC5B3).
- Césure automatique dans les titres (`hyphens: manual`).

## 9. Arche — motif et composants

Planche de référence (règles, variantes, propositions) : [L'arche du Parc](https://claude.ai/artifact/3NKB1kd9hXu4pcyu4AbF8W). Choix retenus le 7 octobre 2026 : en-tête **E2** (ajusté : photo sous filtre orange, arche à la couleur de la section suivante), usages **2, 3, 6, 7, 10, 11, 12**.

### Règles
- Deux tracés exacts du logo, `viewBox="16 -1 360 68"` : l'arche (`M20 61C70 54 120 25.5 150 12…Z`) et la base (`M36 64.8C100 54 150 47 200 47…Z`).
- **Jamais étirée** : mise à l'échelle uniforme uniquement. Toute boîte qui porte l'arche a le même rapport largeur / hauteur (`aspect-ratio: 360 / 62.5` pour la silhouette, `332 / 28` pour la base) ; elle peut être recadrée par un bord, jamais déformée.
- Les deux traits à partir de 56 px de large ; en dessous (icônes, puces, repères), la **silhouette pleine du dôme**.
- Couleurs : orange `#DA5900` sur noir ou pierre, blanc sur l'orange, noir, blanc ou pierre quand l'arche découpe une section.

### Tokens (`styles.css`, `:root`)
| Token | Contenu | Usage |
|---|---|---|
| `--arch` / `--arch-mute` | les deux traits, orange #DA5900 / pierre `#CDC5B3` | filigranes, fonds d'attente |
| `--placeholder` | pierre `#ECE8DF` + `--arch-mute` à 56 % | image en attente (11) |
| `--arch-dome` | silhouette pleine, 360 × 62,5 (masque) | en-têtes de page, bas de section, cartes, accueil |
| `--arch-base-line` | trait de base, 332 × 28 (masque, épaissi de 5 unités) | page active du menu (6) |

### Composants retenus
- **En-tête des pages intérieures** (`.page-hero--bg`, issu de E2 puis ajusté) : la photo de la page (`PAGE_BG` dans `tools/pages/generer.py`) en fond, désaturée et fondue en produit à 60 % dans `--page-header-bg` = orange action `#B34900` (le produit ne peut que foncer : texte blanc ≥ 5,43:1 ; fil d'Ariane en graisse 500). En bas à droite, la silhouette exacte de l'arche (`width: clamp(560px, 64vw, 1100px)`, coupée par le bord droit) prend la couleur de la section suivante (`--arch-next` : blanc, encre ou papier, via `:has`), qui monte ainsi dans l'en-tête. Texte à 52 % à gauche. Sous 1024 px : arche sous le texte (`150vw`).
- **2. Bas de section en arche** : une section sombre suivie d'une section claire se termine par la silhouette de la section suivante, centrée (`min(100%, 1000px)`), à plat. Accueil : la section suivante monte dans le diaporama (`.hero__arch`, dès 1024 px), la souris de défilement s'y loge.
- **Haut du pied de page** : l'arche encre (`min(100vw, 640px)`) monte dans la dernière section ; la bande autour reprend sa couleur (blanc, papier ou encre, via `:has`), percée de la silhouette par un masque composite (`mask-composite: exclude`).
- **3. Cartes « espaces »** : le bandeau du nom porte la silhouette ; au repos seul le sommet dépasse (`translateY(72%)`), au survol ou au focus l'arche monte dans la photo.
- **6. Page active du menu** : soulignée par le trait de base (masque `--arch-base-line`), qui se déploie au survol.
- **7. Chiffres clés** : l'arche se trace au-dessus du chiffre à son apparition et à chaque survol (`.figure__arch`, ajouté par `assets/site.js`).
- **10. Chargement** : l'arche et sa base se tracent en boucle (`.arch-loader`, `role="status"`) pendant le chargement de la carte, du fil Facebook et de la visite 360°, et lors du passage d'une page à l'autre (voile papier `.page-loader`, affiché après 150 ms).
- **11. Image en attente** : `--placeholder` sur galeries, carte, mur d'actualités, encadré contact.
- **12. Retour en haut** : icône = silhouette du dôme.
- **Parallaxe** : la photo du diaporama de l'accueil (14 % du défilement) et celle de l'en-tête des pages (18 %) descendent plus lentement que la page, dans une marge prévue en CSS (`--plx`, `assets/site.js`) : jamais de vide visible.
- **Diaporama** : plus de couleur par image ; indicateur actif et molette en orange.
- Animations (3, 7, 10) et parallaxe figées si « réduire les animations » est activé.
