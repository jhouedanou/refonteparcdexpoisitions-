# Offre de service – Refonte du site du Parc des Expositions d'Abidjan

Oct 1, 2026 · @Social Media

Nous proposons une refonte en 5 phases sur 6 semaines, sur le socle Drupal 10 existant, avec une mise en ligne prioritaire de la homepage, du formulaire de devis et de la version anglaise dès la fin de la semaine 4.

## Contexte et compréhension du besoin

Le site actuel ([parcdesexpositionsabidjan.com](https://www.parcdesexpositionsabidjan.com/fr)) tourne sous Drupal 10 avec le thème Bento. Il présente les espaces mais ne répond pas à la question centrale du cahier des charges : « Pourquoi organiser mon événement au PEA ? ».

Le site doit devenir un outil commercial : générer des demandes de devis, porter l'image premium et internationale du PEA, et se positionner sur les requêtes MICE d'Abidjan et d'Afrique de l'Ouest.

Contraintes retenues :

- Drupal 10 conservé ; le thème Bento est remplacé par un thème enfant ou un thème sur mesure (Twig + SDC), pour éviter de reconstruire le back-office.
- Bilingue FR/EN avec URLs traduites (déjà en place, à fiabiliser).
- Priorité 1 : homepage, formulaire de devis, SEO, CTA commerciaux, version anglaise.

Maquette (accueil desktop et mobile, page espace, formulaire de devis) : [PEA – Maquette refonte homepage](https://claude.ai/artifact/Fiqri2r85JgrshEa6c2EZu).

## Audit SEO de l'existant

Le site est techniquement sain (Drupal 10, canonicals, URLs traduites, images WebP) mais quasi invisible sur les mots-clés du cahier des charges : sur « salle événementielle Abidjan centre de conférence », les premiers résultats sont la presse, GL events et des annuaires, pas le site du PEA. Constats relevés le 1er octobre 2026 sur la homepage et la page espaces :

| Constat | Impact | Amélioration proposée |
| --- | --- | --- |
| Title homepage « Page d'accueil \| Parc des Expositions d'Abidjan » | Fort | Title ciblé : « Parc des Expositions d'Abidjan – Convention center & salons en Côte d'Ivoire » |
| Aucune meta description détectée | Fort | Meta description unique par page via Metatag, rédigée FR et EN |
| H1 « Bienvenue au Parc des Expositions d'Abidjan », sans mot-clé métier | Fort | H1 orienté requête : convention center, salons, congrès, Abidjan |
| Chiffres clés affichés « 0 m² », « 0 places » dans le HTML (compteurs JS) | Fort | Valeurs réelles en HTML, animation en amélioration progressive |
| Contenu très court, 3 espaces sur une seule page | Fort | Une page par espace (Dôme, Hall, Parvis), une page par type d'événement, une page par service |
| Pas de page services, photothèque ni contact/devis dans le menu | Fort | Arborescence du CDC en 6 rubriques, CTA devis sur chaque page |
| Logo avec alt « Imported image » | Moyen | Alts descriptifs, convention de nommage des médias |
| Plan du site en PDF seul | Moyen | Fiches techniques en HTML indexable + PDF téléchargeable |
| Pas d'Open Graph sur la homepage | Moyen | OG/Twitter Cards sur toutes les pages |
| Données structurées non visibles | Moyen | Schema.org : EventVenue, Place, Event (agenda), FAQPage, Organization, BreadcrumbList |
| Concurrence de gl-events.com sur la marque (page « Abidjan Exhibition Centre ») | Moyen | Coordination avec GL events : lien vers le site PEA, cohérence des contenus |

Points à vérifier en phase d'audit (accès Search Console et serveur requis) : robots.txt, sitemap XML, hreflang FR/EN, Core Web Vitals, profil Google Business, backlinks, pages indexées.

Améliorations structurantes :

- **Pages d'atterrissage par intention** : « Salon professionnel Abidjan », « Congrès Abidjan », « Événement corporate », « Concert », avec leurs équivalents EN (« Exhibition center Abidjan », « Conference venue Abidjan », « MICE West Africa »).
- **Agenda indexable** : une page par événement avec Schema Event, source de trafic récurrent.
- **Contenus destination** : venir à Abidjan, hôtels, visas, pour capter la recherche internationale.
- **Netlinking local** : CCI, ministères, offices du tourisme, organisateurs hébergés (SARA, MIVA, Archibat).
- **Suivi** : Search Console, GA4, événements de conversion sur devis, appel et WhatsApp.

## Benchmark des sites de référence

Les quatre références partagent trois choix que nous reprenons : l'image avant le texte, un accès direct aux espaces par capacité, et un CTA commercial toujours visible.

| Site | Ce qu'on retient pour le PEA |
| --- | --- |
| [GL events](https://www.gl-events.com/fr) | Cohérence avec le groupe exploitant, fiches lieux normalisées (capacités, plans) |
| [The Seed](https://www.theseed.com.tr/en/home-page/) | Référence principale : pages lieux épurées, photo plein cadre, capacités par configuration, CTA devis sur chaque page |
| [Hungexpo](https://hungexpo.hu/) | Parc d'expositions comparable : halls, agenda des salons, location d'espaces |
| [Metropolitan Santiago](https://metropolitansantiago.cl/en/) | Convention center : recherche d'espace par type et capacité, version anglaise au même niveau |

Traduction dans la maquette : photo plein cadre en ouverture, les 6 rubriques du cahier des charges dans l'ordre sur l'accueil, une page par espace sur le modèle de The Seed (chiffres clés, capacités par configuration, équipements, visite 360°, galerie, autres espaces), formulaire de devis en 3 étapes, barre d'appel fixe sur mobile.

## Proposition

### Arborescence

1. Qui sommes-nous ? (PEA, GL events, RSE, chiffres)
2. Nos espaces : Dôme, Hall, Parvis & esplanades, visite virtuelle, comparateur de capacités, fiches techniques
3. Nos services : audiovisuel, restauration, mobilier, sécurité, nettoyage, hébergement
4. Photothèque (photos, vidéos, kit presse)
5. Agenda (page par événement)
6. Contact / Réserver / Demander un service (devis en 3 étapes, accès, FAQ)

Plus des pages d'atterrissage SEO par type d'événement et une page destination Abidjan.

### Design

Direction inspirée de The Seed : fond blanc, grandes photos plein cadre, typographie Poppins (celle du logo), palette issue du logo du PEA : orange PEA #DA5914 pour le logo et les grands chiffres, orange foncé #B8470C pour les boutons et liens (contraste AA), brun nuit #2B1D16 pour les titres et bandeaux sombres, gris chaud #F5F2EF pour les fonds. Design system livré sous forme de composants Drupal (SDC) réutilisables par l'équipe.

### Technique Drupal 10

- Thème enfant de Bento avec composants SDC pour les nouveaux blocs, sans reconstruire le thème de zéro.
- Modules : Metatag, Schema.org Metatag, Simple XML Sitemap, Redirect, Pathauto, Webform (devis + CRM/e-mail), Content Translation, Image styles WebP/AVIF, Responsive Image.
- Formulaire de devis : Webform multi-étapes, envoi au service commercial, export CSV, connecteur CRM si disponible, anti-spam (Antibot/Honeypot).
- Performance : cache, lazy-loading, CDN, objectif Core Web Vitals « bon » sur mobile.
- Visite virtuelle : intégration d'une solution 360° existante ou à produire (hors périmètre si non fournie).

### SEO

Architecture sémantique sur les 18 mots-clés du CDC, une page cible par groupe de mots-clés, plan de redirections 301 exhaustif, balisage Schema.org, hreflang, suivi des positions mensuel pendant 3 mois après la mise en ligne.

## Livrables par phase

| Phase | Semaines | Livrables | Validation client |
| --- | --- | --- | --- |
| 1. Audit express | S1 (3 j) | Audits UX, technique, SEO, contenus ; plan de mots-clés et mapping URL | Note d'audit |
| 2. Design | S1 à S2 | Maquettes Priorité 1 (déjà prêtes), puis pages espace, service, agenda, page SEO ; design system | Maquettes finales |
| 3. Développement & contenus | S2 à S5 | Thème enfant Drupal, Webform devis, contenus FR/EN, fiches techniques | Recette sur préprod |
| 4. Tests | S4 (Priorité 1), S5 (site complet) | Tests desktop, mobile, navigateurs, formulaires, SEO, vitesse | PV de recette |
| 5. Mise en ligne | S6 | Migration, redirections 301, sauvegarde, mise en production, formation | PV de mise en ligne |

Après mise en ligne : 3 mois de suivi SEO (rapport mensuel de positions et de demandes de devis).

## Planning

&#91;embedded content: planning · 6 semaines, 1 jalon Priorité 1\]

La Priorité 1 passe en ligne fin S4, le site complet fin S6, puis 3 mois de suivi SEO. Tenir 6 semaines suppose les leviers suivants :

- **Équipe** : 2 personnes à plein temps (1 développeur Drupal, 1 designer-intégrateur SEO), design et développement en parallèle dès S2.
- **Technique** : thème enfant de Bento plutôt que thème sur mesure ; modules contrib uniquement, aucun module custom.
- **Périmètre** : 6 pages d'atterrissage SEO au lancement, les autres après ; visite 360° en lien externe ; photothèque sur la médiathèque existante.
- **Client** : un décideur unique, validation sous 48 h, contenus et traductions EN livrés fin S2 au plus tard.

Risque principal : un retard de contenus ou de validation décale la mise en ligne d'autant, sans marge.

## Conditions

Prestation réalisée à titre gracieux (pro bono) : aucun montant n'est facturé au PEA. Charge estimée, pour information : environ 55 jours-homme sur 6 semaines.

Hypothèses :

- Textes, traductions EN, photos et vidéos fournis par le PEA ; rédaction SEO et traduction hors périmètre.
- Visite virtuelle 360° fournie par le PEA.
- Accès fournis dès S1 : serveur, Drupal admin, Search Console, Analytics, DNS.
- Hébergement, licences et connecteur CRM hors périmètre.
- Deux allers-retours de corrections par livrable.

Questions ouvertes :

- [ ] Date de démarrage (S1) et décideur unique côté PEA ?
- [ ] Un CRM est-il utilisé par le service commercial ?
- [ ] Validation de la charte (logo, couleurs) par GL events requise ?
- [ ] Visite virtuelle existante ?
