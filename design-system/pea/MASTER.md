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
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

- **Barlow Condensed** (600/700/800) : titres, eyebrows, navigation, boutons, chiffres-clés. Capitales pour h1/h2, eyebrows, boutons.
- **Barlow** (400/500/600) : texte courant, formulaires, légendes.
- Repli : `sans-serif` générique uniquement.

| Rôle | Police | Taille | Graisse | Interlignage | Casse / approche |
|---|---|---|---|---|---|
| Display (h1) | Barlow Condensed | `clamp(2.75rem, 7vw, 6rem)` | 800 | .92 | MAJ, -0.01em |
| Headline (h2) | Barlow Condensed | `clamp(2rem, 4.5vw, 3.75rem)` | 800 | .95 | MAJ |
| Title (h3) | Barlow Condensed | `clamp(1.375rem, 2vw, 1.75rem)` | 700 | 1.05 | MAJ, .01em |
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
