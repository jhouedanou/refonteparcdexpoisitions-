# PEA — Design System MASTER

**Direction B — « Signalétique & architecture »**
Source de vérité globale pour les maquettes du Parc des Expositions d'Abidjan. Les règles d'une page dans `pages/<page>.md` (s'il existe) priment sur ce fichier.

Secteur : lieu événementiel B2B / MICE (salons, congrès, conventions, concerts). Cible : organisateurs, agences, directions communication, institutions. Objectif de conversion : demande de devis qualifiée.

## 1. Intention

Le site parle comme la signalétique d'un grand parc d'expositions : on lit vite, on sait où aller, on sent l'échelle des lieux.
- **Puissance** : grands chiffres, titres condensés en capitales.
- **Flux** : flèches, numéros de halls, bandeaux orange qui guident vers l'action.
- **Plan** : grilles visibles en filets de 1px, cellules de tailles inégales, angles vifs.

Motif signature : l'**arche** du logo, redessinée fidèlement en deux surfaces SVG pleines et effilées (une cloche haute au-dessus d'un arc plat), utilisée avec parcimonie : héros, bloc CTA, visite 360°, emplacements photo.

## 2. Couleurs

| Token | Hex | Rôle | Contraste vérifié |
|---|---|---|---|
| `--ink` | #111217 | Texte, fonds sombres (héros, services, footer) | blanc dessus 18,7:1 |
| `--ink-2` | #1A1C21 | Cellules sur fond sombre | orange dessus 5,58:1 |
| `--paper` | #F5F3EE | Fond de page chaud | — |
| `--white` | #FFFFFF | Sections claires, cellules | — |
| `--muted` | #55595F | Texte secondaire sur clair | 6,35 (paper) · 7,05 (blanc) |
| `--muted-dark` | #B9BBC0 | Texte secondaire sur sombre | 9,74 (ink) |
| `--line` | #D9D7D1 | Filets de grille sur clair | décoratif |
| `--line-dark` | #2E3138 | Filets de grille sur sombre | décoratif |
| `--orange` | #F36A00 | **Marque** : logo, bandeaux, gros chiffres, accents sur fond sombre | 6,12 sur ink · **3,06 sur blanc → jamais pour du texte sur clair** |
| `--orange-action` | #C2410C | **Action** : fond des CTA (texte blanc), eyebrows et liens sur clair | 5,18 (blanc) · 4,67 (paper) |
| `--orange-action-hover` | #9A3412 | Survol / pressé | 7,31 |
| `--green` | #0E6F54 | Dates, statut « à venir » | 6,14 (blanc) |

**Règle du signal unique.** L'orange n'est jamais décoratif « pour remplir » : il indique une direction, un repère ou une action.
**Règle des deux oranges.** #F36A00 sur fond sombre ou en aplat sans texte ; #C2410C dès qu'un texte doit être lisible sur fond clair.

Interdits : dégradés violets, dégradés « placeholder » gris-vert, ombres portées décoratives.

## 3. Typographie — 100 % Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Barlow+Condensed:wght@600;700;800&family=Barlow:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

- **Poppins** (600) : titres h1–h3, police du logo ; casse normale ; h2 en #DB5913, h1 blanc sur l’en-tête orange. Ancienne police des titres archivée : `ARCHIVE-TITRES-BARLOW.md`.
- **Barlow Condensed** (600/700/800) : eyebrows, navigation, boutons, chiffres-clés, en capitales.
- **Barlow** (400/500/600) : texte courant, formulaires, légendes.
- Repli : `sans-serif` générique uniquement.

| Rôle | Police | Taille | Graisse | Interlignage | Casse / approche |
|---|---|---|---|---|---|
| Display (h1) | Poppins | `clamp(2rem, 4.2vw, 3.5rem)` | 600 | 1.1 | casse normale, blanc sur en-tête orange |
| Headline (h2) | Poppins | `clamp(1.5rem, 2.6vw, 2.25rem)` | 600 | 1.15 | casse normale, #DB5913 |
| Title (h3) | Poppins | `clamp(1.125rem, 1.3vw, 1.3125rem)` | 600 | 1.3 | casse normale, encre |
| Figure (chiffres) | Barlow Condensed | `clamp(2.5rem, 5vw, 4.5rem)` | 800 | .9 | — |
| Lead | Barlow | `clamp(1.0625rem, 1.4vw, 1.25rem)` | 400 | 1.55 | max 60ch |
| Body | Barlow | 1.0625rem (17px) | 400 | 1.6 | max 68ch |
| Label | Barlow Condensed | .8125rem (13px) min | 700 | 1.2 | MAJ, .12em |

## 4. Espacements & grille

Échelle (`--s-1` … `--s-10`) : 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 px.
- Sections : `clamp(64px, 9vw, 128px)` vertical.
- Conteneur : `min(1320px, 100% - 2 × gouttière)` ; gouttière 16px (<768) · 32px (≥768) · 64px (≥1280).
- Grilles « plan de hall » : cellules jointives séparées par 1px (`gap:1px` sur fond `--line`), pas d'espace blanc entre cartes.
- Points de rupture mobile-first : 480 · 600 · 768 · 1024 · 1120 (menu complet) · 1280.
- En-tête de page intérieure : deux colonnes dès 1024px (titre / chapô aligné en bas).

## 5. Formes & profondeur

- Rayons : 0 par défaut ; 2px pour champs de formulaire. Aucune bordure latérale épaisse sur une carte (« side-tab »).
- Aucune ombre. Profondeur par contraste de surfaces (ink / white / paper) et par filets.
- Filet orange de 4px sous le header (repère « signalétique »).

## 6. Composants

- **Bouton primaire** : fond `--orange-action`, texte blanc, Barlow Condensed 700 MAJ 15px, .08em, min-height 48px, padding 8px 24px, flèche SVG à droite qui glisse de 3px au survol.
- **Bouton secondaire** : bordure 2px `currentColor`, transparent ; au survol, fond ink / texte blanc (ou inversé sur sombre).
- **Lien flèche** : texte MAJ + flèche, soulignement 2px orange au survol.
- **Cellule chiffre** : chiffre Figure + label ; bande de cellules de largeurs inégales.
- **Carte espace** : visuel + plaque signalétique (lettre de hall A/B/C sur carré orange) + nom + données ; bento asymétrique.
- **Ligne service** : numéro orange · nom MAJ · description ; tableau 2 colonnes sur fond ink.
- **Chips filtres** : `<button aria-pressed>`, bordure 1px, état actif ink plein.
- **Champs** : label visible lié (`for`), bordure 1px #84878D (3,6:1 UI), focus orange-action 2px + anneau.
- **Visite 360°** : façade (arche + bouton) ; l'iframe Matterport n'est chargée qu'au clic (`assets/site.js`), lien direct sans JS.
- **Focus clavier** : `outline: 3px solid var(--orange-action); outline-offset: 3px` (sur sombre : `--orange`).

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
- Placeholder gris-vert ou rayures en dégradé : utiliser l'aplat `--paper-2` (#EBE8E1) avec l'arche du logo en ton sourd (#C4C0B7).
- Césure automatique dans les titres (`hyphens: manual`).

## 9. Arche — motif et composants

Planche de référence (règles, variantes, propositions) : [L'arche du Parc](https://claude.ai/artifact/3NKB1kd9hXu4pcyu4AbF8W). Choix retenus le 7 octobre 2026 : en-tête **E2** (ajusté : photo sous filtre orange, arche à la couleur de la section suivante), usages **2, 3, 6, 7, 10, 11, 12**.

### Règles
- Deux tracés exacts du logo, `viewBox="16 -1 360 68"` : l'arche (`M20 61C70 54 120 25.5 150 12…Z`) et la base (`M36 64.8C100 54 150 47 200 47…Z`).
- **Jamais étirée** : mise à l'échelle uniforme uniquement. Toute boîte qui porte l'arche a le même rapport largeur / hauteur (`aspect-ratio: 360 / 62.5` pour la silhouette, `332 / 28` pour la base) ; elle peut être recadrée par un bord, jamais déformée.
- Les deux traits à partir de 56 px de large ; en dessous (icônes, puces, repères), la **silhouette pleine du dôme**.
- Couleurs : orange `#F36A00` sur encre ou papier, blanc sur l'orange, encre ou papier quand l'arche découpe une section.

### Tokens (`styles.css`, `:root`)
| Token | Contenu | Usage |
|---|---|---|
| `--arch` / `--arch-mute` | les deux traits, orange / gris `#C4C0B7` | filigranes, fonds d'attente |
| `--placeholder` | papier `#EBE8E1` + `--arch-mute` à 56 % | image en attente (11) |
| `--arch-dome` | silhouette pleine, 360 × 62,5 (masque) | en-têtes de page, bas de section, cartes, accueil |
| `--arch-base-line` | trait de base, 332 × 28 (masque, épaissi de 5 unités) | page active du menu (6) |

### Composants retenus
- **En-tête des pages intérieures** (`.page-hero--bg`, issu de E2 puis ajusté) : la photo de la page (`PAGE_BG` dans `tools/pages/generer.py`) en fond, désaturée et fondue en produit à 60 % dans l'orange `#BF4F14` (texte blanc ≥ 4,85:1). En bas à droite, la silhouette exacte de l'arche (`width: clamp(560px, 64vw, 1100px)`, coupée par le bord droit) prend la couleur de la section suivante (`--arch-next` : blanc, encre ou papier, via `:has`), qui monte ainsi dans l'en-tête. Texte à 52 % à gauche. Sous 1024 px : arche sous le texte (`150vw`).
- **2. Bas de section en arche** : une section sombre suivie d'une section claire se termine par la silhouette de la section suivante, centrée (`min(100%, 1000px)`), à plat. Accueil : la section suivante monte dans le diaporama (`.hero__arch`, dès 1024 px), la souris de défilement s'y loge.
- **3. Cartes « espaces »** : le bandeau du nom porte la silhouette ; au repos seul le sommet dépasse (`translateY(72%)`), au survol ou au focus l'arche monte dans la photo.
- **6. Page active du menu** : soulignée par le trait de base (masque `--arch-base-line`), qui se déploie au survol.
- **7. Chiffres clés** : l'arche se trace au-dessus du chiffre à son apparition et à chaque survol (`.figure__arch`, ajouté par `assets/site.js`).
- **10. Chargement** : l'arche et sa base se tracent en boucle (`.arch-loader`, `role="status"`) pendant le chargement de la carte, du fil Facebook et de la visite 360°, et lors du passage d'une page à l'autre (voile papier `.page-loader`, affiché après 150 ms).
- **11. Image en attente** : `--placeholder` sur galeries, carte, mur d'actualités, encadré contact.
- **12. Retour en haut** : icône = silhouette du dôme.
- **Parallaxe** : la photo du diaporama de l'accueil (14 % du défilement) et celle de l'en-tête des pages (18 %) descendent plus lentement que la page, dans une marge prévue en CSS (`--plx`, `assets/site.js`) : jamais de vide visible.
- **Diaporama** : plus de couleur par image ; indicateur actif et molette en orange.
- Animations (3, 7, 10) et parallaxe figées si « réduire les animations » est activé.
