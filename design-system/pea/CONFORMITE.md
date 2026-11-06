# Conformité : charte graphique PEA + Bento DS

Dernier contrôle : 6 novembre 2026, commande `node tools/verif/conformite.mjs`. Le script ouvre chaque page dans Chrome headless, en mouvement réduit pour que les blocs apparaissant au défilement soient visibles, et contrôle les styles **calculés**. Rapport détaillé page par page : `RAPPORT-INTEGRATION.md`, généré par `python3 tools/verif/rapport.py`.

| Contrôle | Pages | Largeurs | Écarts | Éléments contrôlés |
|---|---|---|---|---|
| Toutes les pages FR + 3 pages EN | 40 | 375, 768, 1024, 1440 | **0** | 13 380 textes, 2 004 titres, 1 092 boutons, 13 484 écarts entre sous-éléments |

À titre de comparaison :
- l’état du commit `c714ec6` comptait **3 529 écarts** : 1 982 graisses hors kit web, 400 titres en 600, 368 composants Bento absents, 232 fonds noirs, 172 boutons hors spec, 159 contrastes, 32 chargements de police, 6 rayons et 6 couleurs de titre ;
- le premier contrôle des espacements a relevé **220 écarts**. Après tri des faux positifs (espace libre d’alignement, cellules de tableau), il restait 13 vrais défauts, tous corrigés :
  - héros 136 → 128 px ;
  - arche des chiffres-clés 30 → 32 px ;
  - dates de l’agenda 6 → 8 px ;
  - titre et date des cartes d’agenda collés ;
  - réserve de 50vw de la photo du CTA sur mobile ;
  - infos pratiques collées aux raisons, à cause d’un conflit de cascade qui touchait aussi les fiches événement ;
  - cases à cocher sans gap ;
  - liste RSE étirée à 1024 px ;
  - meta d’en-tête irrégulière ;
  - étiquette PDF à 6 px ;
  - marges de section fluides ;
  - gap des encarts à 12 px au lieu de 16 ;
  - padding de l’en-tête de page et du CTA hors token Bento.

Hors périmètre : `planches.html`, une planche d’index interne sans en-tête ni pied de page. `accueil.html` et `fiche-evenement.html` sont de simples redirections.

## 1. Règles contrôlées automatiquement

| Règle | Source | Contrôle |
|---|---|---|
| Poppins seule | charte p. 7 | famille calculée de chaque texte visible |
| Graisses 100 / 400 / 700 | kit web p. 17 | graisse calculée de chaque texte ; graisses chargées depuis Google Fonts |
| Angles vifs | choix PEA (06/11) | aucun `border-radius`, sauf les champs (≤ 2 px) et le logo GL events |
| Pas de fond noir | charte (noir = logo monochrome) | aucun fond de luminance < 0,02 sur plus de 1 500 px², hors voiles sur photo |
| Titres | Bento Title + choix PEA | Bold 700 ; ≥ 24 px sur fond clair en #DA5900 ; < 24 px jamais en orange |
| Boutons | Bento Button | 16 px, Regular, bordure 2 px |
| Topbar et Site header | Bento `topbar/height`, `site-header/height` | 48 px ; 64 px (72 px dès 1120 px) |
| Contraste | WCAG 2.2 AA | ≥ 4,5:1, ou ≥ 3:1 pour le grand texte, pour chaque texte visible sur son fond réel |
| Composants présents | Bento | `data-bento` attendu par page (Topbar, Site header, Menu, Footer, Newsletter form, puis selon la page) |
| Pas de débordement | — | `scrollWidth` ≤ largeur de fenêtre |
| Échelle d’espacement | Bento `space/*` | chaque padding, marge verticale et gap calculé ∈ {4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96, 128} (1–3 px tolérés pour les filets) ; marges `auto` et réserves de l’arche exclues |
| Écarts entre sous-éléments | Bento `space/*` | écart rendu entre voisins (même colonne ou même ligne) : sur l’échelle en flux de blocs, ≥ gap en flex / grille, jamais négatif, jamais < 4 px posés entre deux blocs de texte |
| Logo jamais déformé | charte p. 5 | rapport largeur/hauteur affiché = rapport du fichier (± 2 %) |

États vérifiés à la main dans Chrome headless (`interact`) :
- menu mobile ouvert, en panneau blanc ;
- sous-menu blanc avec ombre ;
- en-tête collé avec ombre ;
- fenêtre d’événement ouverte, à surface blanche ;
- vidéo : le clic charge `presentation-pea-1080.mp4`, `readyState` 4, lecture en cours.

## 2. Composants Bento

| Bento | Spec relevée dans le .fig | Site | État |
|---|---|---|---|
| Topbar | 48 px ; `topbar/bg` primary/800 ; capitales Regular | brun #9D4015, 48 px, téléphone et lieu en capitales, langues et réseaux | ✅ |
| Site header (Stuck) | 64 px, fond clair, ombre une fois collé | blanc, 64/72 px, `0 2px 8px rgba(0,0,0,.12)` | ✅ (logo de 48 px : écart assumé) |
| Menu / Submenu / Menu/Mobile | items 8/16 ; actif primary/800 ; sous-menu blanc, padding 16, ombre ; panneau mobile blanc de 384 px | conforme ; soulignement en arche gardé | ✅ |
| Breadcrumb | 14 px, neutral/600, « › », courant en gras | conforme ; blanc sur l’en-tête orange | ✅ |
| Page header | Background=image, Color=primary ; meta, titre, summary, addons | conforme ; meta et addons sur les pages événement | ✅ |
| Block/Hero | contenu ≤ 768 px ; lead 18 ; boutons fill/invert | conforme | ✅ |
| Carousel | boutons 57,6 px, puces | boutons 56 px, puces 10 px (rayon 0) | ✅ |
| Title | Bold 700, interligne 1,2, L1 48 · L2 30 · L3 24 · L4 20 · L5 18 · L6 16 | conforme ; L1–L3 orange (choix PEA) | ✅ |
| Button | 16 px Regular, 12/16, bordure 2 ; primary, tertiary, default, outline, invert | conforme | ✅ |
| Link | primary, souligné au survol, gap 8 | conforme | ✅ |
| Badge | 14 px Bold capitales, 4/12, bordure 1 | conforme : espaces, dates, types, usages, équipements, lieu | ✅ |
| Card | fond base-100, bordure 1, padding 24, gap 16, image 240 / affiche 400 | conforme : espaces, événements, mur, encarts | ✅ |
| Collection | gap md 24, 1 à 3 colonnes | conforme | ✅ |
| Block/Key figures | centré, valeur 36 Bold, description 16, gap 24, Background=light | conforme ; valeur en orange (charte p. 16) | ✅ |
| Block/Video | titre, 16:9, lecture 64 px centrée blanche ombrée | conforme ; section brune | ✅ |
| Cta | padding 48/32, image, boutons | conforme ; aplat brun foncé | ✅ |
| Block/Partners | tuiles 150 px, logos ≤ 100 px, carrousel | conforme | ✅ |
| Block/Agenda list · Block/Events | titre d’item, bouton primary, filtres | conforme ; badge de type, bouton « Détails » | ✅ |
| Modal | voile 60 %, surface blanche, padding 24, fermeture 32+, ombre | conforme (fenêtre d’événement) ; visionneuse en variante « bare » | ✅ |
| Accordion | fond primary/50, bordure 1, titre Bold primary/950, icône primary/500 | conforme (FAQ) | ✅ |
| Image gallery | gap 16, voile 30 % et icône au survol | conforme | ✅ |
| Form/Field | label en gras, requis en primary, focus 2 px décalé de 2 | conforme ; bordure et hauteur : écarts assumés | ✅ |
| Newsletter form | champ et bouton primary | bloc crème avant le pied de page | ✅ |
| Contact details · Block/Map | gap 8 ; carte de 400 px | conforme | ✅ |
| Footer (Columns=3) | `footer/bg` primary/800 ; colonnes titre + menu ; barre légale | conforme | ✅ |
| Tabs | padding 12/16, filet 2 | sous-navigation des fiches espace | ✅ |
| Item list · Block/Icons text · Table · Divider | — | services, raisons, comparatif | ✅ |

## 3. Charte

| Règle (page) | Application | État |
|---|---|---|
| Poppins pour toute la communication (p. 7) | seule police chargée et calculée | ✅ |
| Kit web : Thin, Regular, Bold (p. 17) | graisses 100 / 400 / 700 uniquement | ✅ |
| Orange 218-89-0, couleur principale (p. 10) | #DA5900 : logo, arche, titres, chiffres | ✅ |
| Couleurs secondaires et d’accompagnement (p. 11, 17) | aplats brun, vert, brun foncé, crème ; tokens beige, pierre, terracotta, orange clair, vert clair | ✅ |
| Supports : fond blanc + panneaux de couleur + grandes photos (p. 16, 19) | fond blanc, aplats, photos officielles | ✅ |
| Mots-clés et chiffres mis en avant en orange (p. 16) | chiffres-clés en orange | ✅ |
| Logo Positif / Négatif / Monochrome (p. 4) | Positif dans l’en-tête ; Négatif sur l’en-tête orange, dans le pied de page et le favicon | ✅ (fichiers vectoriels à fournir) |
| Ne pas modifier les couleurs ni déformer le logo (p. 5) | contrôle automatique du rapport | ✅ |
| Logo GL events en signature (p. 17–18) | couleurs d’origine, dans la barre légale (choix de l’utilisateur ; le kit web le montre en gris) | ✅ |
| Accroche « Le plus grand parc exposition d’Afrique de l’Ouest » (p. 16, 19) | sur-titre du héros (FR et EN) | ✅ à valider par le client |

## 4. Écarts assumés avec Bento

| Écart | Bento | PEA | Raison |
|---|---|---|---|
| Rayons | 2 à 8 px, pilules | 0 (champs : 2 px) | choix de l’utilisateur (06/11) |
| Couleur des titres L1–L3 | primary/800 (brun) | #DA5900 | choix de l’utilisateur |
| Hauteur du logo | 32 px | 40 px (mobile) / 48 px | logo PEA sur trois lignes, illisible à 32 px |
| Bordure des champs | neutral/300 (#D4D4D4, 1,5:1) | #737373 (4,7:1) | WCAG 1.4.11 : 3:1 minimum |
| Hauteur et police des champs | 40 px, 14 px | 48 px, 16 px | cible tactile ; pas de zoom automatique sur iOS |
| Erreurs de formulaire | neutral/950 | neutral/950 précédé de « ! » | conforme Bento ; repère non coloré ajouté |
| Filtres pressés | `tags-filter-bg-checked` base-content (noir) | orange action | pas de fond noir (charte) |
| Onglet actif | primary/500 (3,4:1 sur blanc) | texte #B34900, filet #DA5900 | contraste du texte |

## 5. Points à remonter au client

1. Kit web p. 17 : le libellé « RVB 243-147-27 » est posé sous un aplat d’orange foncé. Le site applique 218-89-0 (p. 10).
2. Logo : fournir les versions Négatif et Monochrome en SVG. Le site les obtient aujourd’hui par filtre CSS sur le PNG positif.
3. Accroche « Le plus grand parc exposition d’Afrique de l’Ouest » utilisée en sur-titre du héros : à confirmer.
4. La vidéo de présentation n’a pas de sous-titres.
5. `6C2A7050 - Copie.jpg` est un doublon de `6C2A7050.jpg` (ignoré par la conversion).
6. Le dossier `espalanafes` est vide : la galerie du Parvis & Esplanades n’a que 2 photos du Dôme vu du parvis. Les photos déposées dans ce dossier rejoindront la galerie à la prochaine conversion.
