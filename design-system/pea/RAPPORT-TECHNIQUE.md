# Annexe technique : mesures de l’intégration charte PEA + Bento DS, page par page

Site de démonstration : <https://pae-orpin.vercel.app/>. Chaque titre de page ci-dessous est un lien direct vers la page sur ce site.

Généré le 06/11/2026 par `tools/verif/rapport.py`, à partir des mesures de `node tools/verif/conformite.mjs` (Chrome headless, styles **calculés**, mouvement réduit pour que tout soit visible). Version illustrée (captures) : publiée avec ce rapport.

## Synthèse

| Indicateur | Valeur |
|---|---|
| Pages contrôlées | 40 (toutes les pages FR + 3 pages EN) |
| Largeurs | 375 · 768 · 1024 · 1440 px |
| Combinaisons page × largeur | 160 |
| **Écarts restants** | **0** |
| Textes contrôlés (police, graisse, contraste) | 13 380 |
| Titres contrôlés (composant Title) | 2 004 |
| Boutons contrôlés (composant Button) | 1 092 |
| Écarts entre sous-éléments mesurés | 13 484 |

### Règles contrôlées sur chaque page et chaque largeur

- **Charte** : Poppins seule ; graisses 100 / 400 / 700 (kit web p. 17) ; aucun fond noir ; logo jamais déformé ; titres ≥ 24 px en orange #DA5900, jamais d’orange sous 24 px.
- **Bento** : Button 16 px Regular bordure 2 ; Title Bold ; Topbar 48 px ; Site header 64 / 72 px ; composants attendus présents (`data-bento`) ; angles vifs (rayons à 0, champs 2 px).
- **Accessibilité** : contraste ≥ 4,5:1 (≥ 3:1 pour le grand texte) de chaque texte sur son fond réel ; aucun débordement horizontal.
- **Espacements** : chaque padding, marge verticale et gap sur l’échelle Bento (4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64, plus 96 · 128 pour la mise en page) ; l’écart rendu entre deux sous-éléments voisins sur l’échelle, jamais négatif, jamais nul entre deux blocs de texte. Seules exceptions : les réserves de l’arche du logo (hauteur proportionnelle à la largeur) et l’espace libre d’alignement (liens de cartes alignés en bas).

### Écarts verticaux mesurés entre sous-éléments (toutes pages, toutes largeurs)

| Écart | 0 px | 1 px | 4 px | 8 px | 12 px | 16 px | 20 px | 24 px | 32 px | 34 px | 48 px | 49 px | 56 px | 62 px | 64 px |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Occurrences | 856 | 2 | 352 | 3084 | 956 | 1595 | 4 | 297 | 872 | 8 | 434 | 1 | 16 | 1 | 40 |

Les valeurs hors échelle restantes (si présentes) sont des espaces libres d’alignement en flex / grille, listés page par page.

### Composants Bento par page

| Composant | Pages | Spec Bento contrôlée |
|---|---|---|
| Button | 40 / 40 | btn 16 px Regular · padding 12 / 16 · bordure 2 |
| Contact details | 40 / 40 | contact-details/gap 8 |
| Footer | 40 / 40 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale |
| Menu | 40 / 40 | menu/item-padding 8 / 16 · menu/fg neutral/950 |
| Modal | 40 / 40 | modal/padding 24 · surface blanche · voile 60 % |
| Newsletter form | 40 / 40 | newsletter-form : champ + bouton primary |
| Site header | 40 / 40 | site-header/height 64 · fond clair · ombre une fois collé |
| Title | 40 / 40 | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 |
| Topbar | 40 / 40 | topbar/height 48 · topbar/bg primary/800 (brun) |
| Breadcrumb | 38 / 40 | breadcrumb/font-size 14 · séparateur « › » · courant en gras |
| Page header | 38 / 40 | page-header/padding-block 128 · Background=image, Color=primary |
| Card | 35 / 40 | card/padding 24 · card/gap 16 · bordure 1 base-300 |
| Badge | 34 / 40 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 |
| Link | 34 / 40 | link/color primary · souligné au survol · gap 8 |
| Collection | 27 / 40 | collection/gap-md 24 · 1 à 3 colonnes |
| Cta | 8 / 40 | cta/padding 48 / 32 · Background=image |
| Block/Key figures | 7 / 40 | block-key-figures/gap 24 · valeur 36 Bold · centré |
| Image gallery | 7 / 40 | image-gallery/gap 16 · voile 30 % au survol |
| Block/Icons text | 5 / 40 | block-icons-text : 3 colonnes, Divider |
| Block/Video | 4 / 40 | block-youtube : cadre 16:9 · lecture 64 px centrée |
| Tabs | 4 / 40 | tab/padding 12 / 16 · filet 2 |
| Block/Agenda list | 2 / 40 | block-events : titre d’item, bouton primary |
| Block/Hero | 2 / 40 | block-hero : contenu ≤ 768 · lead 18 · voile sur photo |
| Block/Partners | 2 / 40 | block-partners/tile-height 150 · logo ≤ 100 |
| Carousel | 2 / 40 | carousel/btn-size 57,6 · puces |
| Accordion | 1 / 40 | accordion/gap 16 · item 8 / 16 · fond primary/50 |
| Block/Map | 1 / 40 | block-map/height 400 |
| Form/Field | 1 / 40 | form : label Bold · gap 8 · focus 2 px |
| Item list | 1 / 40 | item-list : liste de services |

## Pages

### [Parc des Expositions d’Abidjan – Convention center & salons en Côte d’Ivoire](https://pae-orpin.vercel.app/)

Site de démonstration : <https://pae-orpin.vercel.app/>

`index.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 133 textes, 23 titres, 11 boutons, 19 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Salons, congrès et grands événements à Abidjan. | brun foncé (#5D120A) | 0 / 0 | 780 | Carousel, Title, Button, Block/Hero |
| 4 | Un lieu conçu pour faire grandir les événements. | pierre claire (#F7F5F1) | 96 / 96 | 566 | Title, Block/Key figures, Button |
| 5 | Découvrez le Parc en 1 min 37. | brun (#9D4015) | 96 / 269.6 | 1252 | Title, Block/Video |
| 6 | À chaque projet, son espace. | blanc (#FFFFFF) | 96 / 96 | 712 | Title, Collection, Card, Badge |
| 7 | Votre événement commence à Abidjan. | pierre claire (#F7F5F1) | 96 / 96 | 648 | Badge, Title, Button |
| 8 | Prochainement au Parc | blanc (#FFFFFF) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 9 | Le Parc en direct | blanc (#FFFFFF) | 96 / 96 | 935 | Title, Collection, Card, Button, Link |
| 10 | Parlez-nous de votre projet. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 11 | Ils nous ont fait confiance | blanc (#FFFFFF) | 96 / 96 | 439 | Title, Carousel, Block/Partners |
| 12 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 13 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 7 | 97×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Hero | 1 | 1440×780 · padding 0 0 0 0 · gap 0 / 0 · Poppins 400 16px · fond brun foncé (#5D120A) | block-hero : contenu ≤ 768 · lead 18 · voile sur photo | ✅ |
| Block/Key figures | 1 | 1312×192 · padding 32 32 32 32 · gap 24 / 24 · Poppins 400 16px · fond crème (#FCF2EA) · écarts internes 24, 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Block/Partners | 1 | 1440×439 · padding 96 0 96 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | block-partners/tile-height 150 · logo ≤ 100 | ✅ |
| Block/Video | 1 | 1440×1252 · padding 96 0 269.6 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | block-youtube : cadre 16:9 · lecture 64 px centrée | ✅ |
| Button | 11 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 10 | 421×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Carousel | 2 | 344×56 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 16, 8, 8 | carousel/btn-size 57,6 · puces | ✅ boutons de 56 px (rayon 0) — écart assumé |
| Collection | 3 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 2 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 23 | 768×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 8 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 10 (#0A0A0A, #FFFFFF) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 9, 8 px × 24, 12 px × 13, 16 px × 18, 24 px × 3, 32 px × 7, 48 px × 4, 56 px × 1, 64 px × 1. Hors échelle : 56 px (espace libre d’alignement).

Espaces libres d’alignement (voulus) : 34px (gap 8) dans div.card__content  : p.card__desc  → span.card__link ; 49px (gap 16) dans article.card.wall__tile  : p  → a.link-arrow ; 56px (gap 16) dans article.card.wall__tile  : p  → a.link-arrow

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 113.1, 48 / 48 · 0 écart.

### [Qui sommes-nous ? Le Parc des Expositions d’Abidjan, exploité par GL events](https://pae-orpin.vercel.app/qui-sommes-nous.html)

Site de démonstration : <https://pae-orpin.vercel.app/qui-sommes-nous.html>

`qui-sommes-nous.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 65 textes, 9 titres, 4 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Un équipement majeur au service des grands événe | orange action (#B34900) | 128 / 128 | 605 | Breadcrumb, Title, Page header |
| 4 | Faire d’Abidjan un point de rencontre régional. | blanc (#FFFFFF) | 96 / 96 | 648 | Title, Block/Key figures |
| 5 | Découvrez le Parc en 1 min 37. | brun (#9D4015) | 96 / 269.6 | 1252 | Title, Block/Video |
| 6 | Abidjan, ville d’affaires et d’expériences. | pierre claire (#F7F5F1) | 96 / 96 | 733 | Title, Image gallery, Link |
| 7 | Un savoir-faire événementiel international. | brun foncé (#5D120A) | 96 / 96 | 389 | Title |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Block/Key figures | 1 | 608×110 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Block/Video | 1 | 1440×1252 · padding 96 0 269.6 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | block-youtube : cadre 16:9 · lecture 64 px centrée | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 4 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×316 · padding 0 0 0 0 · gap 16 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 1 | 310×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 733×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×605 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 9 | 735×173 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 4 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 8 px × 12, 12 px × 9, 16 px × 4, 32 px × 5, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 113.1, 48 / 48, 64 / 121.7 · 0 écart.

### [Espaces événementiels à Abidjan : Hall, Dôme, Esplanades](https://pae-orpin.vercel.app/nos-espaces.html)

Site de démonstration : <https://pae-orpin.vercel.app/nos-espaces.html>

`nos-espaces.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 112 textes, 11 titres, 9 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Des espaces à la hauteur de vos ambitions. | orange action (#B34900) | 128 / 128 | 676 | Breadcrumb, Title, Page header |
| 4 | Hall d’Exposition | blanc (#FFFFFF) | 96 / 96 | 733 | Collection, Card, Badge, Title |
| 5 | Nos espaces en un coup d’œil | blanc (#FFFFFF) | 96 / 96 | 581 | Title, Button |
| 6 | Explorez les espaces avant votre visite. | pierre claire (#F7F5F1) | 96 / 96 | 648 | Title, Button, Badge |
| 7 | Un espace vous intéresse ? | pierre claire (#F7F5F1) | 96 / 96 | 550 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 97×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 9 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 3 | 421×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×358 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Menu | 1 | 730×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×676 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 3 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 3 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 7, 1 px × 1, 8 px × 18, 12 px × 7, 16 px × 8, 32 px × 6, 48 px × 2. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 34px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Hall d’exposition à Abidjan – 6 500 m², 17 m sous plafond](https://pae-orpin.vercel.app/hall-exposition.html)

Site de démonstration : <https://pae-orpin.vercel.app/hall-exposition.html>

`hall-exposition.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 75 textes, 9 titres, 7 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Hall d’Exposition | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 64 / 96 | 736 | Tabs, Block/Key figures, Image gallery |
| 5 | Un espace pensé pour les événements de grande am | pierre claire (#F7F5F1) | 96 / 96 | 574 | Title, Badge, Card, Button, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 199×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond transparent · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Key figures | 1 | 1312×110 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 6 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 340×358 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×302 · padding 0 0 0 0 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 1 | 290×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 730×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Tabs | 1 | 1312×52 · padding 0 0 0 0 · gap 0 / 8 · Poppins 400 16px · fond transparent · écarts internes 8, 8, 8, 8 | tab/padding 12 / 16 · filet 2 | ✅ |
| Title | 9 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 1 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 3 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 13, 12 px × 4, 16 px × 10, 32 px × 2, 48 px × 3, 64 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 48 / 48, 64 / 121.7 · 0 écart.

### [Le Dôme, convention center d’Abidjan – 5 023 places assises](https://pae-orpin.vercel.app/le-dome.html)

Site de démonstration : <https://pae-orpin.vercel.app/le-dome.html>

`le-dome.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 10 titres, 6 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Le Dôme | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 64 / 96 | 1642 | Tabs, Block/Key figures, Image gallery |
| 5 | Une salle de prestige pour les grands rendez-vou | pierre claire (#F7F5F1) | 96 / 96 | 686 | Title, Badge, Card, Button, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 7 | 255×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond transparent · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Key figures | 1 | 1312×110 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 340×296 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×1208 · padding 0 0 0 0 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, 16, 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 1 | 290×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 730×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Tabs | 1 | 1312×52 · padding 0 0 0 0 · gap 0 / 8 · Poppins 400 16px · fond transparent · écarts internes 8, 8, 8, 8, 8 | tab/padding 12 / 16 · filet 2 | ✅ |
| Title | 10 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 1 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 13, 12 px × 4, 16 px × 11, 32 px × 2, 48 px × 4, 64 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 48 / 48, 64 / 121.7 · 0 écart.

### [Esplanades événementielles à Abidjan – 67 000 m² en plein air](https://pae-orpin.vercel.app/parvis-esplanades.html)

Site de démonstration : <https://pae-orpin.vercel.app/parvis-esplanades.html>

`parvis-esplanades.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 73 textes, 9 titres, 6 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Parvis & Esplanades | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 64 / 96 | 816 | Tabs, Block/Key figures, Image gallery |
| 5 | De grands espaces extérieurs, à l’échelle de vos | pierre claire (#F7F5F1) | 96 / 96 | 547 | Title, Badge, Card, Button, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 206×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond transparent · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Key figures | 1 | 1312×110 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 340×320 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×382 · padding 0 0 0 0 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 1 | 290×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 730×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Tabs | 1 | 1312×52 · padding 0 0 0 0 · gap 0 / 8 · Poppins 400 16px · fond transparent · écarts internes 8, 8, 8, 8 | tab/padding 12 / 16 · filet 2 | ✅ |
| Title | 9 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 1 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 3 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 13, 12 px × 4, 16 px × 9, 32 px × 2, 48 px × 3, 64 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 48 / 48, 64 / 121.7 · 0 écart.

### [Visite virtuelle 360° du Parc des Expositions d’Abidjan](https://pae-orpin.vercel.app/visite-virtuelle.html)

Site de démonstration : <https://pae-orpin.vercel.app/visite-virtuelle.html>

`visite-virtuelle.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 54 textes, 5 titres, 4 boutons, 13 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Explorez le Parc à distance. | orange action (#B34900) | 128 / 128 | 462 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 64 / 96 | 946 | Block/Video, Badge |
| 5 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 6 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 171×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond transparent · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Video | 1 | 1312×738 · padding 0 0 0 0 · gap 0 / 0 · Poppins 400 16px · fond brun foncé (#5D120A) | block-youtube : cadre 16:9 · lecture 64 px centrée | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 4 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Menu | 1 | 730×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×462 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 5 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L3 24px 700 × 1 (#DA5900) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 2, 8 px × 12, 12 px × 4, 16 px × 4, 24 px × 2, 32 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 64 / 121.7 · 0 écart.

### [Services événementiels à Abidjan : audiovisuel, restauration, sécurité](https://pae-orpin.vercel.app/nos-services.html)

Site de démonstration : <https://pae-orpin.vercel.app/nos-services.html>

`nos-services.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 101 textes, 17 titres, 5 boutons, 13 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Tout ce qu’il faut pour faire fonctionner votre  | orange action (#B34900) | 128 / 128 | 605 | Breadcrumb, Title, Page header |
| 4 | Audiovisuel | vert (#006528) | 96 / 269.6 | 755 | Item list, Title |
| 5 | Une équipe à vos côtés, de la préparation au jou | pierre claire (#F7F5F1) | 96 / 96 | 600 | Title, Card |
| 6 | Des événements plus responsables. | blanc (#FFFFFF) | 96 / 96 | 465 | Title |
| 7 | Composez les services adaptés à votre événement. | pierre claire (#F7F5F1) | 96 / 96 | 648 | Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 553×408 · padding 24 24 24 24 · gap — · Poppins 400 16px · fond vert (#006528) · écarts internes 8, 24 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Item list | 1 | 1312×390 · padding 0 0 0 0 · gap 24 / 64 · Poppins 400 16px · fond transparent · écarts internes 64, 24, 64, 24, 64 | item-list : liste de services | ✅ |
| Menu | 1 | 733×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×605 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 17 | 735×173 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 3 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 9 (#FFFFFF) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 4 px × 8, 8 px × 13, 12 px × 7, 16 px × 7, 24 px × 1, 32 px × 4, 48 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 113.1, 48 / 48, 64 / 121.7 · 0 écart.

### [Photothèque – salons, concerts et événements](https://pae-orpin.vercel.app/phototheque.html)

Site de démonstration : <https://pae-orpin.vercel.app/phototheque.html>

`phototheque.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 58 textes, 5 titres, 5 boutons, 12 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Le Parc en images. | orange action (#B34900) | 128 / 128 | 622 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 96 / 96 | 2050 | Image gallery |
| 5 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 6 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 4 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×1816 · padding 0 0 0 0 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, -1312, 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Menu | 1 | 732×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×622 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 5 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L3 24px 700 × 1 (#DA5900) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 2, 8 px × 12, 12 px × 5, 16 px × 5, 32 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Agenda des salons, concerts et événements à Abidjan](https://pae-orpin.vercel.app/agenda.html)

Site de démonstration : <https://pae-orpin.vercel.app/agenda.html>

`agenda.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 178 textes, 29 titres, 27 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Les prochains événements au Parc. | orange action (#B34900) | 128 / 128 | 624 | Breadcrumb, Title, Page header |
| 4 | Octobre 2026 | blanc (#FFFFFF) | 96 / 96 | 3039 | Block/Agenda list, Title, Card, Badge, Link, Button, Modal |
| 5 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 6 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 21 | 76×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Agenda list | 1 | 1312×2804 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent · écarts internes 0, 0, 0, 0, 0 | block-events : titre d’item, bouton primary | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 27 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 20 | 1136×115 · padding 16 16 16 16 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 8, 4, 347 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ padding 16 : carte compacte d’agenda |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 24 | masqué à cette largeur | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×624 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 29 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L3 24px 700 × 4 (#DA5900) · L4 20px 700 × 20 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 22, 4 px × 40, 8 px × 32, 12 px × 4, 16 px × 5, 32 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Demander un devis pour votre événement à Abidjan](https://pae-orpin.vercel.app/contact-devis.html)

Site de démonstration : <https://pae-orpin.vercel.app/contact-devis.html>

`contact-devis.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 99 textes, 8 titres, 9 boutons, 14 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Parlez-nous de votre projet. | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | Demande envoyée | blanc (#FFFFFF) | 64 / 96 | 1600 | Form/Field, Button, Title, Card, Contact details |
| 5 | Venir au Parc | pierre claire (#F7F5F1) | 96 / 96 | 592 | Title, Button, Block/Map |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Block/Map | 1 | 748×400 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | block-map/height 400 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 9 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 340×477 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 2 | 290×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Form/Field | 12 | 372×87 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | form : label Bold · gap 8 · focus 2 px | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 8 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 1 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 1 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 23, 12 px × 7, 16 px × 11, 20 px × 1, 32 px × 8. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 48 / 48, 64 / 121.7 · 0 écart.

### [Salon professionnel à Abidjan – Hall de 6 500 m²](https://pae-orpin.vercel.app/salons-professionnels.html)

Site de démonstration : <https://pae-orpin.vercel.app/salons-professionnels.html>

`salons-professionnels.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 88 textes, 17 titres, 5 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Votre salon professionnel à Abidjan. | orange action (#B34900) | 128 / 128 | 548 | Breadcrumb, Title, Page header |
| 4 | Trois raisons de choisir le Parc. | blanc (#FFFFFF) | 96 / 96 | 455 | Title, Block/Icons text |
| 5 | Les espaces adaptés. | pierre claire (#F7F5F1) | 96 / 96 | 804 | Title, Collection, Card, Badge |
| 6 | Prochainement au Parc | blanc (#FFFFFF) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 7 | Parlez-nous de votre salon. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 5 | 97×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Icons text | 1 | 1312×150 · padding 0 0 0 0 · gap 32 / 32 · Poppins 400 16px · fond transparent · écarts internes 32, 32 | block-icons-text : 3 colonnes, Divider | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 5 | 644×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 2 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×548 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 17 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 4 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 8 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 8 px × 22, 12 px × 11, 16 px × 9, 32 px × 4, 48 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Congrès et conférences à Abidjan – Le Dôme, 5 023 places](https://pae-orpin.vercel.app/congres-conferences.html)

Site de démonstration : <https://pae-orpin.vercel.app/congres-conferences.html>

`congres-conferences.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 15 titres, 5 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Congrès et conférences à Abidjan. | orange action (#B34900) | 128 / 128 | 548 | Breadcrumb, Title, Page header |
| 4 | Trois raisons de choisir le Parc. | blanc (#FFFFFF) | 96 / 96 | 455 | Title, Block/Icons text |
| 5 | Les espaces adaptés. | pierre claire (#F7F5F1) | 96 / 96 | 804 | Title, Collection, Card, Badge |
| 6 | Prochainement au Parc | blanc (#FFFFFF) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 7 | Parlez-nous de votre congrès. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 3 | 96×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Icons text | 1 | 1312×150 · padding 0 0 0 0 · gap 32 / 32 · Poppins 400 16px · fond transparent · écarts internes 32, 32 | block-icons-text : 3 colonnes, Divider | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 3 | 644×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 2 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×548 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 15 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 4 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 6 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 8 px × 18, 12 px × 11, 16 px × 7, 32 px × 4, 48 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Événement d’entreprise à Abidjan – conventions, lancements, galas](https://pae-orpin.vercel.app/evenements-entreprise.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenements-entreprise.html>

`evenements-entreprise.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 88 textes, 17 titres, 5 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Vos événements d’entreprise à Abidjan. | orange action (#B34900) | 128 / 128 | 548 | Breadcrumb, Title, Page header |
| 4 | Trois raisons de choisir le Parc. | blanc (#FFFFFF) | 96 / 96 | 455 | Title, Block/Icons text |
| 5 | Les espaces adaptés. | pierre claire (#F7F5F1) | 96 / 96 | 804 | Title, Collection, Card, Badge |
| 6 | Prochainement au Parc | blanc (#FFFFFF) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 7 | Parlez-nous de votre événement d’entreprise. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 5 | 96×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Icons text | 1 | 1312×150 · padding 0 0 0 0 · gap 32 / 32 · Poppins 400 16px · fond transparent · écarts internes 32, 32 | block-icons-text : 3 colonnes, Divider | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 5 | 421×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 2 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×548 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 17 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 4 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 8 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 8 px × 22, 12 px × 11, 16 px × 9, 32 px × 4, 48 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Salle de concert à Abidjan – le Dôme, jusqu’à 9 588 spectateurs](https://pae-orpin.vercel.app/concerts-spectacles.html)

Site de démonstration : <https://pae-orpin.vercel.app/concerts-spectacles.html>

`concerts-spectacles.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 88 textes, 17 titres, 5 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concerts et spectacles à Abidjan. | orange action (#B34900) | 128 / 128 | 548 | Breadcrumb, Title, Page header |
| 4 | Trois raisons de choisir le Parc. | blanc (#FFFFFF) | 96 / 96 | 429 | Title, Block/Icons text |
| 5 | Les espaces adaptés. | pierre claire (#F7F5F1) | 96 / 96 | 804 | Title, Collection, Card, Badge |
| 6 | Prochainement au Parc | blanc (#FFFFFF) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 7 | Parlez-nous de votre concert. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 5 | 96×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Icons text | 1 | 1312×124 · padding 0 0 0 0 · gap 32 / 32 · Poppins 400 16px · fond transparent · écarts internes 32, 32 | block-icons-text : 3 colonnes, Divider | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 5 | 644×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 2 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×548 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 17 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 4 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 8 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 5, 8 px × 20, 12 px × 11, 16 px × 9, 32 px × 6, 48 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Venir à Abidjan : accès, hôtels et visas](https://pae-orpin.vercel.app/venir-a-abidjan.html)

Site de démonstration : <https://pae-orpin.vercel.app/venir-a-abidjan.html>

`venir-a-abidjan.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 84 textes, 11 titres, 5 boutons, 16 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Venir à Abidjan. | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | Rejoindre le Parc | blanc (#FFFFFF) | 96 / 96 | 605 | Block/Icons text, Title, Link |
| 5 | Questions fréquentes | pierre claire (#F7F5F1) | 96 / 96 | 599 | Title, Accordion |
| 6 | Abidjan, ville d’affaires et d’expériences. | blanc (#FFFFFF) | 96 / 96 | 657 | Title, Image gallery |
| 7 | Parlez-nous de votre événement. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 8 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 9 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Accordion | 1 | 1312×294 · padding 0 0 0 0 · gap 16 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, 16, 16 | accordion/gap 16 · item 8 / 16 · fond primary/50 | ✅ |
| Block/Icons text | 1 | 1312×279 · padding 0 0 0 0 · gap 32 / 32 · Poppins 400 16px · fond transparent · écarts internes 32, 32 | block-icons-text : 3 colonnes, Divider | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×316 · padding 0 0 0 0 · gap 16 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 2 | 190×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 733×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 3 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 3 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 10, 8 px × 12, 12 px × 10, 16 px × 12, 32 px × 3, 48 px × 3. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Mentions légales, cookies et confidentialité](https://pae-orpin.vercel.app/informations-legales.html)

Site de démonstration : <https://pae-orpin.vercel.app/informations-legales.html>

`informations-legales.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 71 textes, 10 titres, 5 boutons, 11 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Informations légales | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | Mentions légales | blanc (#FFFFFF) | 64 / 96 | 1625 | Title, Button |
| 5 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 6 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Menu | 1 | 729×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 10 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 5 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 6, 8 px × 14, 12 px × 4, 16 px × 7, 24 px × 1, 32 px × 6, 64 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 64 / 121.7 · 0 écart.

### [Abidjan Border Forum – 20–22 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-abidjan-border-forum.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-abidjan-border-forum.html>

`evenement-abidjan-border-forum.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Abidjan Border Forum | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1157 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 19, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Agrofood & Plastprintpack West Africa – 8–10 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-agrofood-plastprintpack-west-africa-0.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-agrofood-plastprintpack-west-africa-0.html>

`evenement-agrofood-plastprintpack-west-africa-0.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Agrofood & Plastprintpack West Africa | orange action (#B34900) | 128 / 128 | 631 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1157 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×631 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 21, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Auto Expo – 8–10 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-auto-expo.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-auto-expo.html>

`evenement-auto-expo.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 79 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Auto Expo | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1150 | Title, Link, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 2 | 110×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 3. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Brands Licensing Africa – 15–16 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-brands-licensing-africa.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-brands-licensing-africa.html>

`evenement-brands-licensing-africa.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 11 titres, 7 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Brands Licensing Africa | orange action (#B34900) | 128 / 128 | 621 | Breadcrumb, Title, Button, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1186 | Title, Button, Card |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 7 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×621 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 20, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 3. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Cérémonie PRIMUD – 8 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-ceremonie-primud.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-ceremonie-primud.html>

`evenement-ceremonie-primud.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Cérémonie PRIMUD | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1040 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert 25 ans de carrière de Molière – 5 déc. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-25-ans-de-carriere-de-moliere.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-25-ans-de-carriere-de-moliere.html>

`evenement-concert-25-ans-de-carriere-de-moliere.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 11 titres, 7 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert 25 ans de carrière de Molière | orange action (#B34900) | 128 / 128 | 623 | Breadcrumb, Title, Button, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1102 | Title, Button, Card |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 7 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×623 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 20, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 3. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert 40 ans de carrière Gadji Celi – 31 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-40-ans-de-carriere-gadji-celi.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-40-ans-de-carriere-gadji-celi.html>

`evenement-concert-40-ans-de-carriere-gadji-celi.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert 40 ans de carrière Gadji Celi | orange action (#B34900) | 128 / 128 | 631 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×631 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 20, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Ariel Sheney – 12 déc. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-ariel-sheney.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-ariel-sheney.html>

`evenement-concert-ariel-sheney.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 70 textes, 9 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Ariel Sheney | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 2 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 2 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 9 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 2 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 16, 12 px × 4, 16 px × 8, 24 px × 1, 32 px × 5, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Ismaël Isaac – 7 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-ismael-isaac.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-ismael-isaac.html>

`evenement-concert-ismael-isaac.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Ismaël Isaac | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Kiff No Beat – 28 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-kiff-no-beat.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-kiff-no-beat.html>

`evenement-concert-kiff-no-beat.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Kiff No Beat | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Mary Sy – 1 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-mary-sy.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-mary-sy.html>

`evenement-concert-mary-sy.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Mary Sy | orange action (#B34900) | 128 / 128 | 545 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1058 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×545 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Milo – 24 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-milo.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-milo.html>

`evenement-concert-milo.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Milo | orange action (#B34900) | 128 / 128 | 545 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1058 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×545 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert Serge Beynaud – 5 déc. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-serge-beynaud-0.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-serge-beynaud-0.html>

`evenement-concert-serge-beynaud-0.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 76 textes, 10 titres, 7 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert Serge Beynaud | orange action (#B34900) | 128 / 128 | 565 | Breadcrumb, Title, Button, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1102 | Title, Button, Card |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 3 | 181×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 7 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 3 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×565 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 10 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 3 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 9, 24 px × 1, 32 px × 5, 48 px × 3. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Concert TAYC – 11 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-concert-tayc.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-concert-tayc.html>

`evenement-concert-tayc.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Concert TAYC | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 20, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Foire Europe Afrique d’Abidjan – 16–19 déc. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-foire-europe-afrique-dabidjan.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-foire-europe-afrique-dabidjan.html>

`evenement-foire-europe-afrique-dabidjan.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Foire Europe Afrique d’Abidjan | orange action (#B34900) | 128 / 128 | 631 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1012 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×631 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Food Expo – 8–10 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-food-expo-0.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-food-expo-0.html>

`evenement-food-expo-0.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 79 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Food Expo | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1150 | Title, Link, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×567 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 2 | 110×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 20, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 5, 48 px × 3. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Horeca Expo – 8–10 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-horeca-expo.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-horeca-expo.html>

`evenement-horeca-expo.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 79 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Horeca Expo | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1150 | Title, Link, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 2 | 110×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 3. Hors échelle : aucun.

Espaces libres d’alignement (voulus) : 56px (gap 8) dans div.card__content  : p.card__desc  → span.card__link

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Salon des collectivités territoriales – 15–17 oct. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-salon-des-collectivites-territoriales.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-salon-des-collectivites-territoriales.html>

`evenement-salon-des-collectivites-territoriales.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Salon des collectivités territoriales | orange action (#B34900) | 128 / 128 | 631 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×631 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Salon Equip Auto – 26–28 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-salon-equip-auto.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-salon-equip-auto.html>

`evenement-salon-equip-auto.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 80 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Salon Equip Auto | orange action (#B34900) | 128 / 128 | 573 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1142 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×573 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 19, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Salon ivoirien des ressources extractives & énergétiques – 18–22 nov. 2026 à Abidjan](https://pae-orpin.vercel.app/evenement-salon-ivoirien-des-ressources-extractives-energetiques.html)

Site de démonstration : <https://pae-orpin.vercel.app/evenement-salon-ivoirien-des-ressources-extractives-energetiques.html>

`evenement-salon-ivoirien-des-ressources-extractives-energetiques.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 11 titres, 5 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Salon ivoirien des ressources extractives & éner | orange action (#B34900) | 128 / 128 | 631 | Breadcrumb, Title, Badge, Page header |
| 4 | À propos de l’événement | blanc (#FFFFFF) | 96 / 96 | 1086 | Title, Card, Button |
| 5 | À suivre au Parc | pierre claire (#F7F5F1) | 96 / 96 | 972 | Title, Collection, Card, Badge, Link |
| 6 | Les prochains événements du Parc, dans votre boî | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 573 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 4 | 287×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 193×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 4 | 340×236 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Collection | 1 | 1312×591 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×573 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 1 | 169×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 731×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×631 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 11 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 2 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 18, 12 px × 4, 16 px × 10, 24 px × 1, 32 px × 7, 48 px × 2. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Upcoming trade shows, concerts and events in Abidjan](https://pae-orpin.vercel.app/en/agenda.html)

Site de démonstration : <https://pae-orpin.vercel.app/en/agenda.html>

`en/agenda.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 178 textes, 29 titres, 27 boutons, 15 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Upcoming events at the venue. | orange action (#B34900) | 128 / 128 | 624 | Breadcrumb, Title, Page header |
| 4 | October 2026 | blanc (#FFFFFF) | 96 / 96 | 3039 | Block/Agenda list, Title, Card, Badge, Link, Button, Modal |
| 5 | Upcoming events at the venue, straight to your i | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 6 | Footer | brun (#9D4015) | 159.1 / 24 | 542 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 21 | 125×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond pierre claire (#F7F5F1) · bordure 1px #E7E1D6 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Agenda list | 1 | 1312×2804 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent · écarts internes 0, 0, 0, 0, 0 | block-events : titre d’item, bouton primary | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 27 | 167×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 20 | 1136×115 · padding 16 16 16 16 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 8, 4, 347 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ padding 16 : carte compacte d’agenda |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×542 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 24 | masqué à cette largeur | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 615×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×624 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 29 | 735×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L3 24px 700 × 4 (#DA5900) · L4 20px 700 × 20 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 22, 4 px × 40, 8 px × 31, 12 px × 4, 16 px × 5, 32 px × 4. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 48 / 48, 64 / 121.7 · 0 écart.

### [Abidjan Exhibition Center – Convention center & trade shows in Côte d’Ivoire](https://pae-orpin.vercel.app/en/)

Site de démonstration : <https://pae-orpin.vercel.app/en/>

`en/index.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 133 textes, 23 titres, 11 boutons, 19 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | Trade shows, congresses and major events in Abid | brun foncé (#5D120A) | 0 / 0 | 780 | Carousel, Title, Button, Block/Hero |
| 4 | A venue built to help events grow. | pierre claire (#F7F5F1) | 96 / 96 | 548 | Title, Block/Key figures, Button |
| 5 | Discover the venue in 1 min 37. | brun (#9D4015) | 96 / 269.6 | 1252 | Title, Block/Video |
| 6 | The right venue for every project. | blanc (#FFFFFF) | 96 / 96 | 712 | Title, Collection, Card, Badge |
| 7 | Your event starts in Abidjan. | pierre claire (#F7F5F1) | 96 / 96 | 648 | Badge, Title, Button |
| 8 | Coming up at the venue | blanc (#FFFFFF) | 96 / 96 | 948 | Title, Collection, Card, Badge, Link |
| 9 | Live from the venue | blanc (#FFFFFF) | 96 / 96 | 935 | Title, Collection, Card, Button, Link |
| 10 | Tell us about your project. | pierre claire (#F7F5F1) | 96 / 96 | 632 | Cta, Title, Button |
| 11 | They trusted us | blanc (#FFFFFF) | 96 / 96 | 439 | Title, Carousel, Block/Partners |
| 12 | Upcoming events at the venue, straight to your i | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 13 | Footer | brun (#9D4015) | 159.1 / 24 | 542 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 7 | 89×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond orange action (#B34900) · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Hero | 1 | 1440×780 · padding 0 0 0 0 · gap 0 / 0 · Poppins 400 16px · fond brun foncé (#5D120A) | block-hero : contenu ≤ 768 · lead 18 · voile sur photo | ✅ |
| Block/Key figures | 1 | 1312×192 · padding 32 32 32 32 · gap 24 / 24 · Poppins 400 16px · fond crème (#FCF2EA) · écarts internes 24, 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Block/Partners | 1 | 1440×439 · padding 96 0 96 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | block-partners/tile-height 150 · logo ≤ 100 | ✅ |
| Block/Video | 1 | 1440×1252 · padding 96 0 269.6 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | block-youtube : cadre 16:9 · lecture 64 px centrée | ✅ |
| Button | 11 | 167×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 10 | 421×407 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Carousel | 2 | 344×56 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 16, 8, 8 | carousel/btn-size 57,6 · puces | ✅ boutons de 56 px (rayon 0) — écart assumé |
| Collection | 3 | 1312×407 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | collection/gap-md 24 · 1 à 3 colonnes | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Cta | 1 | 1312×440 · padding 48 32 48 32 · gap — · Poppins 400 16px · fond brun foncé (#5D120A) · écarts internes 12, 32, 32 | cta/padding 48 / 32 · Background=image | ✅ |
| Footer | 1 | 1440×542 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Link | 2 | 248×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 612×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 1 | masqué à cette largeur | modal/padding 24 · surface blanche · voile 60 % | ✅ |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Title | 23 | 768×115 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 8 (#DA5900, #FFFFFF) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 10 (#0A0A0A, #FFFFFF) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 9, 8 px × 23, 12 px × 13, 16 px × 18, 24 px × 3, 32 px × 7, 48 px × 4, 56 px × 1, 64 px × 1. Hors échelle : 56 px (espace libre d’alignement).

Espaces libres d’alignement (voulus) : 34px (gap 8) dans div.card__content  : p.card__desc  → span.card__link ; 56px (gap 16) dans article.card.wall__tile  : p  → a.link-arrow ; 62px (gap 16) dans article.card.wall__tile  : p  → a.link-arrow

**Mobile (375 px)** : en-tête 64 px · titre L1 36px 700 × 1 (#FFFFFF) · padding des sections 48 / 113.1, 48 / 48 · 0 écart.

### [The Dome, Abidjan’s convention center – 5,023 seats](https://pae-orpin.vercel.app/en/le-dome.html)

Site de démonstration : <https://pae-orpin.vercel.app/en/le-dome.html>

`en/le-dome.html` — **0 écart à 375 · 768 · 1024 · 1440 px** · 78 textes, 10 titres, 6 boutons, 17 composants Bento · contraste minimal 3.52:1

**Sections (1440 px)**

| # | Section | Fond | Padding haut / bas | Hauteur | Composants |
|---|---|---|---|---|---|
| 1 | Topbar | brun (#9D4015) | 0 / 0 | 48 | Topbar |
| 2 | Site header | blanc (#FFFFFF) | 0 / 0 | 72 | Menu, Button, Site header |
| 3 | The Dome | orange action (#B34900) | 128 / 128 | 490 | Breadcrumb, Title, Page header |
| 4 | section.section.section--white | blanc (#FFFFFF) | 64 / 96 | 1642 | Tabs, Block/Key figures, Image gallery |
| 5 | A prestigious hall for major events. | pierre claire (#F7F5F1) | 96 / 96 | 686 | Title, Badge, Card, Button, Link |
| 6 | Upcoming events at the venue, straight to your i | crème (#FCF2EA) | 64 / 64 | 279 | Title, Button, Newsletter form |
| 7 | Footer | brun (#9D4015) | 159.1 / 24 | 542 | Contact details, Title, Footer |

**Composants (1440 px, première occurrence)**

| Composant | Nb | Mesure | Spec Bento | État |
|---|---|---|---|---|
| Badge | 7 | 247×24 · padding 4 12 4 12 · gap 4 / 4 · Poppins 700 14px · fond transparent · bordure 1px #B34900 | badge 14 px Bold capitales · padding 4 / 12 · bordure 1 | ✅ |
| Block/Key figures | 1 | 1312×110 · padding 0 0 0 0 · gap 24 / 24 · Poppins 400 16px · fond transparent · écarts internes 24, 24 | block-key-figures/gap 24 · valeur 36 Bold · centré | ✅ |
| Breadcrumb | 1 | 735×44 · padding 0 0 0 0 · gap — · Poppins 400 14px · fond transparent | breadcrumb/font-size 14 · séparateur « › » · courant en gras | ✅ |
| Button | 5 | 167×44 · padding 12 16 12 16 · gap 8 / 8 · Poppins 400 16px · fond orange action (#B34900) · bordure 2px #B34900 | btn 16 px Regular · padding 12 / 16 · bordure 2 | ✅ |
| Card | 1 | 340×320 · padding 24 24 24 24 · gap 16 / 16 · Poppins 400 16px · fond blanc (#FFFFFF) · bordure 1px #E7E1D6 · écarts internes 16, 16, 16, 16 | card/padding 24 · card/gap 16 · bordure 1 base-300 | ✅ |
| Contact details | 1 | 420×105 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent · écarts internes 8 | contact-details/gap 8 | ✅ |
| Footer | 1 | 1440×542 · padding 159.1 0 24 0 · gap — · Poppins 400 16px · fond brun (#9D4015) · écarts internes 0 | footer/bg primary/800 (brun) · colonnes titre + menu · barre légale | ✅ |
| Image gallery | 1 | 1312×1208 · padding 0 0 0 0 · gap 0 / 16 · Poppins 400 16px · fond transparent · écarts internes 16, 16, 16, 16, 16 | image-gallery/gap 16 · voile 30 % au survol | ✅ |
| Link | 1 | 290×44 · padding 0 0 0 0 · gap 8 / 8 · Poppins 400 16px · fond transparent | link/color primary · souligné au survol · gap 8 | ✅ |
| Menu | 1 | 615×44 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond transparent | menu/item-padding 8 / 16 · menu/fg neutral/950 | ✅ |
| Modal | 2 | 0×0 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond voile noir (#000000) | modal/padding 24 · surface blanche · voile 60 % | ✅ fermé (dialogue) |
| Newsletter form | 1 | 1440×279 · padding 64 0 64 0 · gap — · Poppins 400 16px · fond crème (#FCF2EA) | newsletter-form : champ + bouton primary | ✅ |
| Page header | 1 | 1440×490 · padding 128 0 128 0 · gap — · Poppins 400 16px · fond orange action (#B34900) | page-header/padding-block 128 · Background=image, Color=primary | ✅ padding 128 px à cette largeur (64 → 96 → 128) |
| Site header | 1 | 1440×72 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond blanc (#FFFFFF) | site-header/height 64 · fond clair · ombre une fois collé | ✅ 72 px dès 1120 px : logo de 48 px (écart assumé) |
| Tabs | 1 | 1312×52 · padding 0 0 0 0 · gap 0 / 8 · Poppins 400 16px · fond transparent · écarts internes 8, 8, 8, 8, 8 | tab/padding 12 / 16 · filet 2 | ✅ |
| Title | 10 | 735×58 · padding 0 0 0 0 · gap — · Poppins 700 48px · fond transparent | title/font-weight 700 · line-height 1,2 · L1 48 → L6 16 | ✅ |
| Topbar | 1 | 1440×48 · padding 0 0 0 0 · gap — · Poppins 400 16px · fond brun (#9D4015) | topbar/height 48 · topbar/bg primary/800 (brun) | ✅ |

**Titres** : L1 48px 700 × 1 (#FFFFFF) · L2 30px 700 × 1 (#DA5900) · L3 24px 700 × 1 (#DA5900) · L4 20px 700 × 4 (#0A0A0A) · L5 18px 700 × 2 (#FFFFFF)

**Espacements (1440 px)** : écarts verticaux entre sous-éléments — 0 px × 3, 8 px × 12, 12 px × 4, 16 px × 11, 32 px × 2, 48 px × 4, 64 px × 1. Hors échelle : aucun.

**Mobile (375 px)** : en-tête 64 px · titre L1 32px 700 × 1 (#FFFFFF) · padding des sections 32 / 48, 48 / 48, 64 / 121.7 · 0 écart.

## Écarts assumés et points client

Voir `design-system/pea/CONFORMITE.md` § 4 et § 5.
