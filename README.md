# PEA — proposition 1 / base The Seed

Pack de maquettes HTML statiques pour transmission à Codex / développeur.

- 1 fichier HTML par page
- CSS partagé `styles.css`
- contenu structuré selon le cahier des charges PEA
- identité visuelle orange / noir / blanc chaud
- images présentes à titre de maquette uniquement

Pages : Accueil, Qui sommes-nous, Nos espaces, Fiche espace, Nos services, Photothèque, Agenda, Fiche événement, Contact/Devis, Visite virtuelle.

## Proposition actuelle inspirée de Salvador

[Ouvrir la maquette](design/proposition-salvador.html) · [Voir l’aperçu ordinateur](design/apercu-salvador.png) · [Voir l’aperçu mobile](design/apercu-salvador-mobile.png).

La proposition reprend le rythme du [Centro de Convenções Salvador](https://ccs-salvador.com.br/) : photographie immersive en ouverture, navigation superposée, présentation du lieu, agenda, destination et accompagnement. L’identité du Parc repose sur son logo, ses photographies et les couleurs orange `#F36A00`, noir `#111217` et blanc chaud `#F7F5F0`.

Le menu reste : **Qui sommes-nous ? · Nos espaces · Nos services · Photothèque · Agenda**, avec **Demander un devis** à droite. Les dix pages et leurs URL restent celles du projet initial. La maquette ajoute des raccourcis dans le contenu, sans créer de rubrique.

### Recommandations de design

- **Donner la première place au lieu.** Une photo d’architecture en ouverture, puis des vues d’événements et de configurations. Le visuel peut changer à la demande ; le nom du Parc et les actions restent stables. Une photo fixe suffit pour la première version. Prévoir ensuite une prise de vue extérieure haute définition, adaptée aux cadrages ordinateur et mobile.
- **Se rapprocher de la typographie de Salvador.** Une sans empattement accueillante, des titres de 48 à 72 px sur ordinateur et de 34 à 48 px sur mobile. Réserver les caractères spectaculaires à l’identité du lieu ; viser 16 à 18 px pour les textes de lecture en production. La nouvelle proposition remplace les grandes italiques de la piste précédente.
- **Créer le rythme par la composition.** Alterner image pleine largeur, texte en deux colonnes, agenda en trois colonnes et section photo/texte. Réserver les cartes aux contenus répétables, notamment les événements. Privilégier les aplats et des angles discrets.
- **Hiérarchiser la couleur.** Utiliser l’orange pour l’action principale et quelques repères. Le blanc chaud porte les sections de lecture. Le noir sert aux textes et au bandeau final. Garder les couleurs originales des photographies et des affiches.
- **Protéger la lisibilité du logo.** Le logo orange fourni reste entier sur une réserve blanche dans l’en-tête superposé. Après défilement, l’en-tête devient blanc. Garder un dégagement autour du logo et utiliser un original vectoriel en production.
- **Montrer les affiches entières.** Leur contenu utile ne doit pas disparaître dans un recadrage. Présenter aussi le titre et la date en texte HTML, indépendamment de l’affiche.

### Recommandations UX par parcours

| Parcours ou page existante | Recommandation prioritaire |
| --- | --- |
| Accueil | Sous l’image, deux accès explicites : trouver un espace et consulter le programme. L’agenda et le devis restent accessibles sans parcourir toute la page. |
| Nos espaces | Comparer les lieux par usage, surface et capacité selon la configuration. Distinguer clairement les m² et le nombre de personnes. Prévoir des filtres simples uniquement si le catalogue le justifie. |
| Fiche espace | Présenter immédiatement photos, plans, configurations assises/debout, équipements inclus et prestations possibles. Préremplir l’espace dans le devis. N’afficher un téléchargement que si le document existe. |
| Agenda | Afficher les dates lisibles et les événements à venir. Proposer un filtre par date et type, avec remise à zéro et état vide. Archiver automatiquement les événements passés. |
| Fiche événement | Afficher date, horaires, lieu précis, organisateur, conditions d’accès, informations PMR et lien de billetterie confirmé. Adapter le bouton au cas réel : réserver, s’inscrire ou obtenir des informations. |
| Contact et devis | Conserver la page et ses champs ; rendre indispensables seulement les informations nécessaires au premier échange. Regrouper coordonnées et projet, permettre une date encore inconnue, afficher les erreurs près des champs et une confirmation explicite après envoi. |
| Nos services | Expliquer ce qui est inclus, optionnel ou à chiffrer. Relier chaque prestation au besoin de l’organisateur et au devis, en gardant un vocabulaire concret. |
| Photothèque et visite virtuelle | Légender les espaces et les configurations. Lancer la visite immersive à la demande, avec une alternative en photos et plans. |
| Qui sommes-nous ? | Présenter le lieu, son opérateur et la destination. Conserver les informations sur Abidjan dans cette rubrique ; utiliser Contact/Devis et les fiches événements pour les informations pratiques. |

Pour le devis, privilégier un formulaire court, des libellés persistants et un retour clair après chaque erreur ou succès, conformément aux [recommandations du W3C sur les formulaires](https://www.w3.org/WAI/tutorials/forms/).

### Mobile, accessibilité et chargement

- Garder le devis visible dans l’en-tête mobile et ouvrir le menu au toucher. Viser des zones tactiles de 44 px minimum comme objectif de confort. Vérifier les petits écrans, le clavier et le zoom à 200 %.
- Vérifier le contraste du texte sur chaque image et chaque aplat. Le texte courant vise au moins 4,5:1 ; les grands caractères, 3:1. L’orange est conservé : privilégier un texte sombre sur le bouton orange. [Référence W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- Garder les animations discrètes et respecter la réduction des mouvements. Si un diaporama automatique est ajouté, proposer pause/reprise et commande au clavier. La maquette utilise un changement manuel. [Référence W3C](https://www.w3.org/WAI/tutorials/carousels/).
- Optimiser les photographies et charger en différé les images sous la première section. Charger en priorité l’image d’accueil. La vidéo et la visite 360° ne doivent pas retarder l’accès aux informations.

### Contenus et périmètre de la maquette

Les informations, coordonnées et photographies proviennent du [site officiel du Parc](https://www.parcdesexpositionsabidjan.com/fr), de sa [présentation](https://www.parcdesexpositionsabidjan.com/fr/qui-sommes-nous) et de sa page [espaces et services](https://www.parcdesexpositionsabidjan.com/fr/nos-espaces-services). Les trois visuels et dates correspondent à l’[agenda officiel consulté le 7 octobre 2026](https://www.parcdesexpositionsabidjan.com/fr/liste-des-agendas).

Le contenu événementiel de cette maquette est un instantané : les dates devront être alimentées par le CMS en production. Les trois fiches événement ouvrent le site officiel ; les autres liens ouvrent les pages existantes du projet. Les recommandations de filtrage, de préremplissage du devis et d’archivage restent à implémenter sur ces pages. La version présentée est une maquette d’accueil.

### Ordre de réalisation recommandé

1. Retenir l’accueil, l’en-tête et les règles de photographie/typographie de cette direction.
2. Décliner en priorité Nos espaces, Fiche espace, Contact/Devis et les fiches événements pour terminer les deux parcours essentiels.
3. Décliner les autres pages, brancher les contenus officiels et vérifier les états vides, erreurs, succès et affichages mobiles.
4. Mesurer les demandes de devis abouties, les clics vers la billetterie et les demandes d’itinéraire pour guider les ajustements.

Les pistes précédentes (`design/maquette-accueil.html` et `design/proposition-editoriale.html`) sont conservées pour comparaison. La Page créée lors de la première proposition correspond à cette ancienne piste.

## Refonte — direction B « Signalétique & architecture »

Les dix pages et `styles.css` ont été refondus (textes et structure conservés) :

- Système de design : [`DESIGN.md`](DESIGN.md) (format impeccable) et [`design-system/pea/MASTER.md`](design-system/pea/MASTER.md). L'état d'avant refonte est archivé dans `design-system/pea/DESIGN-avant-refonte.md`.
- Page d’accueil : `index.html` (l’ancienne adresse `accueil.html` redirige vers elle) ; la planche des sous-pages est désormais `planches.html`.
- Polices Google Fonts : Poppins 600 en capitales (titres, police du logo, #DB5913), Barlow Condensed (labels, boutons, chiffres) et Barlow (texte). Ancienne police des titres archivée dans `design-system/pea/ARCHIVE-TITRES-BARLOW.md`.
- Accueil : carrousel « Ils nous ont fait confiance » ; ajouter un logo dans `images/logos/`, puis relancer `tools/optimiser-images.py` et l’ajouter à la liste `LOGOS` de `tools/pages/generer.py`. Pages intérieures : en-tête orange logo avec photo fondue, choisie dans `PAGE_BG` ; en-tête du site transparent sur toutes les pages, blanc au défilement.
- Logo officiel : `assets/logo-pea.webp` (en-tête, pied de page) ; favicon `assets/favicon.svg` (arche du logo).
- Visite virtuelle Matterport intégrée sur `visite-virtuelle.html` : chargée au clic sur « Lancer la visite 360° ».
- Comportements (menu mobile, filtres, visite) : `assets/site.js`.
- Passage impeccable « critique » puis « polish » : textes de cahier des charges réécrits pour les visiteurs (les textes d'origine sont conservés en commentaires `<!-- Note de maquette … -->`), formulaire de devis complet avec validation et état de succès, filtres fonctionnels, navigation et pied de page complétés.
- À brancher côté Drupal : envoi réel du formulaire (simulé dans `assets/site.js`), données des filtres (usages par espace déduits des légendes, à confirmer), vraie fiche technique (PDF provisoire `assets/fiche-technique-hall-exposition.pdf`), dates réelles des événements (dates d'exemple marquées « Exemple »), photos réelles, version anglaise.
- Agenda en frise chronologique : 20 événements (octobre–décembre 2026) relevés le 7 octobre 2026 sur [l’agenda officiel](https://www.parcdesexpositionsabidjan.com/fr/liste-des-agendas), avec les liens de réservation publiés (Brands Licensing Africa, concerts Molière et Serge Beynaud) et le site officiel d’Auto Expo. Les types (salon, concert, forum…) sont déduits des intitulés. La page Facebook n’est pas lisible sans connexion : aucun événement n’en a été repris. La fiche événement présente Auto Expo ; les autres événements renvoient vers leur fiche du site actuel en attendant leurs pages Drupal.
- En-tête : barre avec le numéro en lien WhatsApp (`wa.me`, message pré-rempli), Instagram, Facebook et LinkedIn. Pied de page : logo GL events (`assets/logo-gl-events.png`, lien vers gl-events.com) et liens légaux. Contact : carte Google Maps du Parc avec liens « Itinéraire » et « Ouvrir dans Google Maps ».
- Événements : chaque « Détails » ouvre une fenêtre (`<dialog>`) avec description, date, lieu, organisateur, liens de réservation ou site officiel et ajout à l’agenda (.ics). Lien direct possible : `agenda.html#concert-tayc`. Descriptions reformulées depuis les fiches du site officiel (relevé du 7 octobre 2026).
- Accueil : mur d’actualité hybride avant le pied de page. Le fil Facebook vient du Page Plugin officiel de Meta (la page `profile.php?id=61572597774113` est une Page au nouveau format, compatible). Instagram et LinkedIn n’ont pas de fil intégrable sans jeton : tuiles reliées aux comptes, à alimenter en production via un agrégateur (Curator.io, Juicer, Walls.io…) ou les API Meta Graph / LinkedIn depuis Drupal. Une tuile « Prochainement au Parc » complète le mur.
- Cookies : bandeau (« Tout refuser » / « Tout accepter », même poids) qui conditionne la carte Google Maps et le fil Facebook ; choix mémorisé dans le navigateur, modifiable via « Gérer les cookies » en pied de page. Page `informations-legales.html` : mentions légales, politique cookies, confidentialité, CGU, éthique et conformité (textes juridiques à fournir).
- Images : photos sources dans `images/`, converties en WebP par `python3 tools/optimiser-images.py --agenda` (deux largeurs, 1600 et 800 px, jamais agrandies, ≤ 380 Ko ; visuels de l’agenda téléchargés depuis le site officiel). 16 Mo de JPEG → 9 Mo de WebP.
- Pages espaces dédiées : `hall-exposition.html`, `le-dome.html`, `parvis-esplanades.html` (données officielles, galeries avec visionneuse), remplaçant `fiche-espace.html`.
- Accueil : diaporama Ken Burns de 8 images (90vh), titre et boutons accordés à la couleur dominante de chaque image (contraste vérifié), indicateur de défilement, chiffres-clés animés ; mur d’actualité avec les 6 dernières publications Instagram (`images/instagram/`, liens vers les vraies publications).
- Photothèque : photos réelles, filtres Espace / Type, visionneuse au clavier. Contact : illustration signalétique. Services : accompagnement, bâtiment administratif et engagements RSE repris du site officiel.
- Version anglaise : `en/` (générée depuis `tools/i18n/en.json` ; `python3 tools/i18n/extraire.py` liste les chaînes à traduire), sélecteur FR | EN dans l’en-tête et le pied de page. Retour en haut sur toutes les pages.
- Seconde passe de validation : `design-system/pea/SECONDE-PASSE.md`.
- À confirmer par le Parc : adresse e-mail de contact, délai de réponse annoncé (« dans les meilleurs délais » pour l'instant), disponibilité de WhatsApp sur le +225 27 21 71 09 97 (numéro fixe : nécessite WhatsApp Business), textes juridiques.

## Régénérer la maquette

Les pages HTML (FR à la racine, EN dans `en/`) sont générées ; ne pas les modifier à la main.

Photos : les dossiers `images/Hall d’Exposition`, `images/dome`, `images/parvis&esplanades` et `images/abidjan` sont **pilotés** — toute image déposée dans le dossier apparaît dans la galerie de la page correspondante après les étapes 1 et 3 (ajouter son texte alternatif dans `ALTS` de `tools/pages/generer.py`, sinon un texte générique est utilisé et signalé). Une photo retirée ou déplacée disparaît de la page à la régénération.

1. `python3 tools/optimiser-images.py --agenda` — convertit `images/` en WebP dans `assets/img/` (et télécharge les visuels de l’agenda).
2. `python3 tools/i18n/en.py` — régénère `tools/i18n/en.json` après modification des traductions ; `python3 tools/i18n/extraire.py` liste les chaînes françaises.
3. `python3 tools/pages/generer.py` — écrit toutes les pages FR et EN (contenus, événements, diaporama et calcul des teintes dans ce fichier).

Prérequis : Python 3, `cwebp`, `ffmpeg`, `sips` (macOS). Styles : `styles.css` ; comportements : `assets/site.js`.
