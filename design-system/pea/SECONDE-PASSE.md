# Seconde passe — validation du design (7 octobre 2026)

Sources : impeccable « document » (DESIGN.md mis à jour), détecteur impeccable (28 pages FR + EN), audit automatique navigateur (375 / 768 / 1024 / 1440 px), mesures de pages, recommandation ui-ux-pro-max (`design-system/parc-des-expositions-abidjan/MASTER.md`, secteur lieu événementiel B2B/MICE : orange événementiel + bleu, Outfit / Work Sans, ombres — conservée comme référence, non appliquée).

État de base vérifié : aucun débordement, aucun contraste sous 4,5:1 (3:1 gros texte), cibles ≥ 44 px, focus visible, 0 image sans `alt`, sur les 28 pages et 4 largeurs.

## Les 10 problèmes, du plus grave au moins grave

1. **Agenda trop long et trop dense sur mobile** (lisibilité, responsive) — 10,5 écrans à 375 px ; 20 cartes répétant image + type + titre + date + actions ; 24 liens « Détails » et 8 boutons « Réserver » ; 56 textes sous 15 px.
2. **Accueil trop long sur mobile** (espacements, hiérarchie) — 9,9 écrans avant le passage du diaporama à 90vh (≈ 10,1 désormais), 7 sections à 64–128 px de marge ; le devis n'est proposé qu'en tête et au 6e bloc.
3. **Deux couleurs d'action dans le héros** (boutons, hiérarchie) — les teintes calculées (bleu, rouge, violet #5e67e6…) colorent titre et bouton principal, à côté du logo, de l'arche et du CTA d'en-tête orange : la règle du signal unique est rompue sur l'écran le plus vu, et une teinte est violette.
4. **Labels de 13 px en capitales espacées** (lisibilité) — eyebrows, dates, types, compteurs : nombreux et petits ; depuis la suppression du marqueur, ils flottent au-dessus des titres.
5. **En-tête lourd sur mobile** (responsive) — 120 px de chrome (barre utilitaire 44 px + en-tête 76 px) ; la barre utilitaire cumule WhatsApp, FR | EN et 3 réseaux.
6. **Affiches officielles recadrées en 16:9** (lisibilité) — vignettes de la frise, fenêtre de détails et cartes de l'accueil coupent le texte et les visages des affiches.
7. **Éléments flottants en bas d'écran** (boutons) — retour en haut, bandeau cookies, contrôles du diaporama, indicateur « souris » : le retour en haut passe sous le bandeau cookies au premier passage.
8. **Hiérarchie des boutons diluée** (boutons) — primaire (orange ou teinte), secondaire, lien fléché, petit bouton ; « Site officiel » en bouton primaire au même rang que « Réserver ».
9. **Rythme vertical inégal** (hiérarchie, espacements) — titres réduits (28–44 px) dans des sections toujours hautes ; les chiffres-clés (jusqu'à 72 px) dominent désormais les titres de section.
10. **Cohérence de la version anglaise** (lisibilité) — casse hétérogène, PDF et textes légaux en français, logo en français à côté de « Abidjan Exhibition Center ».

## Deux directions de consolidation (direction B conservée)

**B1 — « Signalétique stricte »**
Une seule couleur d'action : l'orange partout, y compris dans le diaporama (les teintes d'image ne colorent plus que les indicateurs et le filet du titre).
Labels à 14 px avec un trait orange de 2 px ; sections resserrées (48–96 px) ; agenda en liste compacte (vignette carrée 72 px, actions regroupées dans la fenêtre).
En-tête mobile allégé (réseaux déplacés dans le menu), boutons ramenés à deux niveaux.

**B2 — « Signalétique photographique »**
Les teintes d'image deviennent un système assumé : chaque section photo emprunte la teinte de son image (filtrée des violets), l'orange restant réservé au logo et au devis.
Affiches en portrait 4:5 jamais recadrées ; agenda en grille d'affiches par mois, détails au clic sur l'affiche ; cartes espaces et galeries plus grandes.
Rythme magazine : sections pleine largeur alternées photo / texte, labels 14 px, CTA devis flottant discret sur mobile.

**Choix utilisateur : B1 — « Signalétique stricte ».**

## Étape 3 — Application de B1
Orange seule couleur d’action (diaporama compris : la teinte d’image ne colore plus que l’indicateur actif) ; labels 14 px avec trait orange de 2 px en bordure ; sections 48–96 px ; chiffres-clés ≤ titres ; agenda compact (vignette carrée 72 px, un seul « Détails », actions dans la fenêtre) ; affiches entières (`contain`) ; en-tête mobile allégé (réseaux dans le menu) ; retour en haut au-dessus du bandeau cookies ; deux niveaux de boutons ; fiche technique PDF anglaise.

## Étape 4 — Critique impeccable (deux évaluations indépendantes) puis polish
**Score de santé : 19/36 → 26/36 (« bon »).** Détecteur : seuls restent les faux positifs connus (filet d’en-tête, blanc chaud, gouttières par `.wrap`, eyebrow de la planche interne).

Polish appliqué après critique : comparatif des 3 espaces + bloc devis sur « Nos espaces » ; accueil terminé par le bloc devis (après le mur) ; voile du héros mobile éclairci en haut ; boutons « Afficher… », « Itinéraire », « Lancer la visite » en secondaire ; chiffres-clés ramenés sous les titres ; sur-titre de 17 px corrigé ; teintes violettes exclues du diaporama ; bouton Fermer en tête de la fenêtre événement ; récapitulatif de la demande dans le message de succès ; illustration contact en bandeau sous 1024 px ; paragraphes limités à 60ch ; « Plan du site » → « Plan du Parc ».

Restent ouverts (informations à fournir par le Parc) : adresse e-mail de contact, délai de réponse chiffré, hauteur du Dôme, capacité du Hall en personnes / stands, logo en version anglaise, textes juridiques, plan du Parc en anglais.

## Avant / après (seconde passe)
| Point | Avant la seconde passe | Après |
|---|---|---|
| Score heuristique | 19/36 | 26/36 |
| Couleur d’action du héros | Teinte de l’image (bleu, rouge, violet) | Orange ; la teinte n’anime que l’indicateur actif |
| Agenda à 375 px | 10,5 écrans, 24 « Détails » + 8 « Réserver » visibles | ≈ 7 écrans, 1 « Détails » par carte, actions dans la fenêtre |
| Affiches | Recadrées en 16:9 | Entières (`contain`) dans cartes, frise et fenêtre |
| Labels | 13 px, sans repère | 14 px, trait orange 2 px |
| Rythme | Sections 64–128 px ; chiffres 72 px > titres 44 px | Sections 48–96 px ; chiffres ≤ titres |
| En-tête mobile | WhatsApp + FR/EN + 3 réseaux dans la barre | WhatsApp + FR/EN ; réseaux dans le menu |
| Boutons | 4 styles, « Site officiel » primaire | 2 niveaux ; liens fléchés = liens |
| Nos espaces | Cartes seules | Cartes + comparatif (surface, hauteur, capacité, usages, documents, devis) + bloc devis |
| Fin de l’accueil | Mur social | Bloc « Parlez-nous de votre projet » |
| Version anglaise | PDF français | PDF anglais, chaînes 100 % traduites (hors noms propres) |

