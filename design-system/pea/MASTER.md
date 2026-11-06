# PEA — Design System MASTER

**Charte graphique officielle (novembre 2026) + composants Bento DS (GL events)**

Ce fichier est la source de vérité pour les maquettes du Parc des Expositions d’Abidjan. Les règles d’une page décrites dans `pages/<page>.md` (s’il existe) priment sur lui.

Fichiers associés :
- `DESIGN.md` : couleurs, typographie et composants.
- `BENTO-TOKENS.md` : valeurs à appliquer dans Bento.
- `CONFORMITE.md` : matrices et preuves.
- `MASTER-avant-charte.md` : état précédent (direction B, Barlow).

Sources client : `docs/retourclient/PARC DES EXPOSITIONS D'ABIDJAN_CHARTE GRAPHIQUE.pdf` (la charte prévaut) et `docs/retourclient/Bento DS.fig` (composants et structure des tokens).

Contexte :
- Secteur : lieu événementiel B2B / MICE (salons, congrès, conventions, concerts).
- Cible : organisateurs, agences, directions de la communication, institutions.
- Objectif de conversion : une demande de devis qualifiée.

## 1. Intention

Le site prolonge les supports officiels du Parc :
- un fond blanc ;
- de grandes photos des lieux ;
- des panneaux en couleurs d’accompagnement ;
- des chiffres mis en avant en orange ;
- le logo intact.

Chaque élément visible est un composant Bento DS (`data-bento`). L’arche du logo est le seul motif propre au Parc.

## 2. Couleurs

Trois couches, comme dans Bento : `--brand-*` (thème PEA) → `--color-*` (sémantique) → tokens de composants. Détail et contrastes : `DESIGN.md` § Colors.

| Rôle | Valeur | Contraste |
|---|---|---|
| Orange PEA (marque, titres ≥ 24 px, chiffres) | #DA5900 | 3,88:1 sur blanc (grand texte) |
| Orange action (boutons, liens, sur-titres, en-tête de page) | #B34900 | blanc dessus : 5,43:1 |
| Brun (Topbar, vidéo, pied de page, survols) | #9D4015 | blanc dessus : 6,61:1 ; crème dessus : 5,2:1 |
| Vert (services, bouton tertiaire) | #006528 | blanc dessus : 7,26:1 |
| Brun foncé (CTA, cookies, visite 360°) | #5D120A | blanc dessus : 13,5:1 |
| Crème (newsletter, chiffres-clés, accordéon) | #FCF2EA | orange dessus : 3,55:1 (grand texte) ; noir dessus : 18:1 |
| Texte | #0A0A0A sur blanc | 19,8:1 |
| Texte secondaire | #525252 | 7,2:1 sur pierre |

Le noir n’est jamais un fond. Il ne sert qu’au texte et au logo monochrome.

## 3. Typographie

Poppins seule, en 100, 400 et 700 (kit web de la charte). Les titres suivent le composant Bento Title :
- Bold, interligne 1,2 ;
- L1 48 px, L2 30 px, L3 24 px en orange ;
- L4 20 px, L5 18 px et L6 16 px en noir.

Le reste du texte :
- texte courant 16 px, chapô 18 px ;
- boutons 16 px Regular ;
- badges 14 px Bold en capitales.

## 4. Espacements et grille

- Échelle : 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 px.
- Sections : `clamp(48px, 7vw, 96px)`.
- Conteneur : 1320 px. Gouttière : 16 px, puis 32 px, puis 64 px.
- Collections de cartes : 1 à 3 colonnes, espacement de 24 px.
- Points de rupture : 480 · 600 · 768 · 1024 · 1120 (menu complet) · 1280.

## 5. Formes et profondeur

- Rayons à 0. Les champs gardent 2 px.
- Ombres Bento :
  - `shadow-md` au survol des cartes ;
  - `0 2px 8px rgba(0,0,0,.12)` sur l’en-tête collé ;
  - `shadow-lg` sur le sous-menu et le menu mobile ;
  - `shadow-xl` sur la modale et le bandeau cookies.
- Profondeur : alternance blanc, pierre et aplats.

## 6. Composants

Voir `CONFORMITE.md` § 2 : spec Bento, application et état de chaque composant.

## 7. Accessibilité (non négociable)

Toutes ces règles sont contrôlées par `node tools/verif/conformite.mjs` (contraste calculé sur le fond réel de chaque texte) :
- Texte ≥ 4,5:1 ; gros texte et composants d’interface ≥ 3:1.
- Focus visible : 2 px noir décalé de 2 px (Bento `form/focus-outline`). Il est blanc sur photo, sur aplat et dans le pied de page.
- Lien d’évitement « Aller au contenu ».
- Cibles tactiles ≥ 44 × 44 px.
- `aria-current="page"` dans la navigation. Menu mobile en `<button aria-expanded aria-controls>`, avec un libellé « Menu » lisible par les lecteurs d’écran.
- `prefers-reduced-motion` : transitions, diaporama, parallaxe et apparitions désactivés.
- Icônes : SVG inline `aria-hidden="true"`, jamais d’emoji.

## 8. Anti-patterns à éviter

- Fonds noirs, graisses 500 et 600, autre police que Poppins, rayons.
- Texte orange de moins de 24 px sur fond clair ; orange sur un aplat sombre.
- Logo recoloré ou déformé.
- Dégradés violets ou néon, glassmorphism.
- Retour des éléments retirés : grilles jointives de 1 px, filet orange sous l’en-tête, lettres de hall.
- Composant sans `data-bento`.

## 9. Arche : motif et composants

### Règles
- Les deux tracés exacts du logo, dans un `viewBox="16 -1 360 68"` : l’arche (`M20 61C70 54 120 25.5 150 12…Z`) et la base (`M36 64.8C100 54 150 47 200 47…Z`).
- **Jamais étirée** : uniquement une mise à l’échelle uniforme (`aspect-ratio: 360 / 62.5`, ou `332 / 28` pour la base). On peut la recadrer, jamais la déformer.
- Couleurs :
  - orange #DA5900 sur fond clair, sur photo ou dans le héros ;
  - quand l’arche découpe une section, elle prend la couleur de la section suivante (blanc, pierre, crème ou aplat).

### Tokens (`styles.css`, section 1)

| Token | Contenu | Usage |
|---|---|---|
| `--arch` / `--arch-mute` | les deux traits, en orange / en pierre | héros, visite 360°, fonds d’attente |
| `--placeholder` | pierre très claire + `--arch-mute` | image en attente |
| `--arch-dome` | silhouette pleine, 360 × 62,5 (masque) | en-têtes de page, bas d’aplat, haut du pied de page, héros |
| `--arch-base-line` | trait de base, 332 × 28 (masque) | page active du menu |

### Usages retenus
- **En-tête de page** (Bento Page header) : la photo de la page, désaturée et fondue à 60 % dans l’orange action. En bas à droite, l’arche prend la couleur de la section suivante.
- **Bas des aplats** (brun, vert, brun foncé) : la section claire suivante monte dans l’aplat, en suivant la silhouette.
- **Accueil** : la section suivante monte dans le diaporama (`.hero__arch`, à partir de 1280 px).
- **Haut du pied de page** : l’arche brune monte dans le bloc newsletter crème.
- **Menu** : la page active est soulignée par le trait de base.
- **Chiffres-clés** : l’arche se trace au-dessus de chaque valeur (`.figure__arch`, `assets/site.js`).
- **Chargement** : `.arch-loader` (carte, fil Facebook, visite 360°) et `.page-loader` entre deux pages.
- **Retour en haut** : silhouette du dôme sur un carré brun.

Retiré le 6 novembre 2026 : l’arche dans les cartes « espaces ». Le composant Bento Card place l’image à l’intérieur de son padding.
