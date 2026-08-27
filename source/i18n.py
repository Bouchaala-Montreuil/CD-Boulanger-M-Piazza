# -*- coding: utf-8 -*-
"""
CD Boulangerie — traductions FR / EN / PL.

Chaque langue contient exactement les mêmes clés.
Pour corriger un texte : modifiez-le ici puis relancez `python3 build-website.py`.
"""

LANGS = [
    ("fr", "Français", "FR", ""),      # préfixe vide = racine du site
    ("en", "English",  "EN", "en"),
    ("pl", "Polski",   "PL", "pl"),
]

T = {}

# ===========================================================================
#  FRANÇAIS
# ===========================================================================
T["fr"] = {
    "html_lang": "fr",
    "locale": "fr_FR",

    # --- navigation / chrome ------------------------------------------------
    "nav_home": "Accueil",
    "nav_products": "Produits",
    "nav_house": "La Maison",
    "nav_bakeries": "Nos boulangeries",
    "nav_contact": "Contact",
    "nav_order": "Commander",
    "brand_sub": "Artisan · Var",
    "skip": "Aller au contenu",
    "menu_label": "Menu",
    "lang_label": "Langue",
    "follow": "Nous suivre",
    "top": "Haut de page",
    "close": "Fermer",
    "prev": "Précédent",
    "next": "Suivant",
    "gallery": "Galerie",
    "loading": "Chargement",
    "scroll": "Défiler",
    "up_next": "Suite",
    "back": "Retour",

    # --- loader -------------------------------------------------------------
    "load_where": "Montferrat &amp; Figanières",
    "load_who": "Artisan boulanger",
    "load_steps": ["Pétrissage", "Pointage", "Façonnage", "Enfournement", "Sortie du four"],

    # --- footer -------------------------------------------------------------
    "f_tagline": "Pains, viennoiseries et pâtisseries façonnés chaque jour sur place, au cœur du Var.",
    "f_nav": "Navigation",
    "f_find": "Nous trouver",
    "f_contact": "Contact",
    "f_rights": "Tous droits réservés",
    "f_craft": "Fabrication artisanale · Var",

    # --- accueil ------------------------------------------------------------
    "h_eyebrow": "Est. Montferrat · Var",
    "h_title_1": "Le goût du vrai,",
    "h_title_2": "chaque jour.",
    "h_lead": "Pains au levain, viennoiseries pur beurre et pâtisseries façonnées sur place. "
              "Une maison ancrée dans le Var, engagée pour le local et l'anti-gaspillage.",
    "h_cta1": "Découvrir nos produits",
    "h_cta2": "Horaires &amp; accès",
    "h_img_hero": "Vitrine du matin — pains au levain",

    "mq_home": ["Levain naturel", "Farines françaises", "Cuit sur place",
                "Produits locaux", "Anti-gaspillage", "Montferrat &amp; Figanières"],

    "h_s1_eyebrow": "01 — La sélection",
    "h_s1_title": "Nos pains de caractère",
    "h_s1_lead": "Des pâtes fermentées lentement, façonnées à la main et cuites chaque matin. "
                 "Le temps fait le reste.",
    "h_c1_t": "Le Grand Levain", "h_c1_n": "36 H",
    "h_c1_d": "Croûte épaisse, mie alvéolée, fermentation longue sur levain naturel.",
    "h_c2_t": "La Tradition", "h_c2_n": "24 H",
    "h_c2_d": "Farine française sélectionnée, pointage lent, façonnage main.",
    "h_c3_t": "Viennoiseries", "h_c3_n": "07 H",
    "h_c3_d": "Pur beurre, tourées et cuites sur place, sorties de four du matin.",
    "h_all": "Voir toute la carte",
    "h_tag_sig": "Signature", "h_tag_morning": "Le matin",
    "h_img_levain": "Pain au levain tranché, mie alvéolée",
    "h_img_trad": "Baguettes tradition françaises",
    "h_img_croissants": "Croissants pur beurre",

    "h_q_eyebrow": "Notre philosophie",
    "h_quote": "Rien ne se presse. Un bon pain demande du temps, de la patience "
               "et la main d'un artisan.",
    "h_q_by": "CD Boulangerie — Montferrat",
    "h_img_fournil": "Le fournil à 5 h du matin",
    "h_st1": "De fermentation", "h_st2": "Boulangeries",
    "h_st3": "Langues du site", "h_st4": "Fait sur place",

    "h_s2_eyebrow": "02 — La maison",
    "h_s2_title_1": "Artisans,", "h_s2_title_2": "pas industriels",
    "h_s2_text": "Tout est fabriqué dans notre fournil : pétrissage, pointage, façonnage, cuisson. "
                 "Nous choisissons des farines françaises et travaillons avec les producteurs du Var.",
    "h_s2_link": "Notre histoire",
    "h_img_faconnage": "Façonnage du pain à la main",

    "h_s3_eyebrow": "03 — Nos adresses",
    "h_s3_title_1": "Deux villages,", "h_s3_title_2": "un même fournil",
    "h_s3_text": "Retrouvez-nous à Montferrat et à Figanières, du mardi au dimanche. "
                 "Commandes spéciales et gâteaux sur réservation.",
    "h_s3_link": "Horaires &amp; itinéraires",
    "h_img_devanture": "Devanture de la boulangerie de Montferrat",

    "h_s4_eyebrow": "04 — Engagements",
    "h_s4_title": "Des gestes concrets",
    "h_e1_t": "Too Good To Go",
    "h_e1_d": "Paniers à prix réduit en fin de journée pour lutter contre le gaspillage alimentaire.",
    "h_e2_t": "Bière au pain recyclé",
    "h_e2_d": "Le pain de la veille est valorisé en brassage plutôt que jeté. Rien ne se perd.",
    "h_e3_t": "Livraisons de proximité",
    "h_e3_d": "Associations et personnes à mobilité réduite, selon conditions. Demandez-nous.",

    # --- produits -----------------------------------------------------------
    "p_eyebrow": "La carte",
    "p_title_1": "Pains, viennoiseries", "p_title_2": "&amp; pâtisseries",
    "p_lead": "Le pain d'abord : c'est notre métier. Le reste suit la saison et l'envie du fournil.",
    "mq_prod": ["Cuit ce matin", "Levain naturel", "Pur beurre", "Fait maison", "Farines françaises"],

    "p_s1_eyebrow": "01 — Les pains",
    "p_s1_title": "Le fournil",
    "p_rows": [
        ("Le Grand Levain", "Fermentation 36 h, croûte épaisse, mie alvéolée.", "Signature"),
        ("La Tradition", "Farine française, pointage lent, façonnage main.", "Tous les jours"),
        ("Pain de campagne", "Blé et seigle, mie dense, longue conservation.", "Tous les jours"),
        ("Céréales &amp; graines", "Tournesol, lin, sésame, pavot.", "Tous les jours"),
        ("Pain complet", "Farine T110, riche en fibres.", "Sur commande"),
        ("Fougasse provençale", "Huile d'olive, herbes du Var, olives.", "Selon four"),
    ],

    "p_s2_eyebrow": "02 — Le reste de la carte",
    "p_s2_title": "Chaque jour au comptoir",
    "p_cat1_t": "Viennoiseries",
    "p_cat1_d": "Croissants, pains au chocolat, chaussons aux pommes, brioches. "
                "Pur beurre, tourés et cuits sur place.",
    "p_cat2_t": "Pâtisseries",
    "p_cat2_d": "Tartes de saison, éclairs, entremets. Gâteaux d'anniversaire et de fête sur commande.",
    "p_cat3_t": "Snacking &amp; burgers",
    "p_cat3_d": "Sandwichs sur notre pain, quiches, pizzas et burgers maison le midi.",
    "p_cat4_t": "Produits locaux",
    "p_cat4_d": "Miel, confitures, huile d'olive et produits de producteurs du Var, sélectionnés par nos soins.",
    "p_img_vienn": "Plateau de viennoiseries",
    "p_img_patis": "Vitrine de pâtisseries et tartes",
    "p_img_snack": "Sandwich artisanal sur pain maison",
    "p_img_local": "Miel et produits locaux du Var",

    "p_s3_eyebrow": "03 — Galerie",
    "p_s3_title": "En images",
    "p_s3_lead": "Cliquez sur une photo pour l'agrandir.",
    "p_f_all": "Tout", "p_f_breads": "Pains", "p_f_vienn": "Viennoiseries",
    "p_f_patis": "Pâtisseries", "p_f_snack": "Snacking", "p_f_local": "Produits locaux",
    "p_zoom": "Agrandir",
    "p_gal": ["Pain au levain", "Tradition française", "Pain de campagne",
              "Croissant pur beurre", "Pain au chocolat", "Chausson aux pommes",
              "Tarte aux fruits", "Éclair", "Gâteau de fête",
              "Sandwich du jour", "Burger maison", "Miel &amp; produits du Var"],

    "p_cta_title": "Une commande spéciale ?",
    "p_cta_lead": "Gâteaux d'anniversaire, buffets, événements, pains en grande quantité. "
                  "Prévenez-nous 48 h à l'avance.",
    "p_cta_btn": "Nous contacter",

    # --- la maison ----------------------------------------------------------
    "m_eyebrow": "La maison",
    "m_title_1": "Le temps", "m_title_2": "comme ingrédient",
    "m_lead": "L'artisanat n'est pas un argument de vente. C'est notre quotidien : des gestes, "
              "des heures et une exigence qui ne se négocie pas.",
    "m_img_fournil": "Le fournil au petit matin",
    "mq_maison": ["36 heures de fermentation", "Levain naturel", "Façonné à la main",
                  "Cuit sur place", "Farines françaises"],

    "m_s1_eyebrow": "01 — Le geste",
    "m_s1_title": "Du grain au comptoir",
    "m_rows": [
        ("Sélection", "Farines françaises choisies chez des meuniers partenaires, produits locaux du Var.", "Amont"),
        ("Levain", "Un levain naturel entretenu chaque jour, jamais remplacé par un raccourci.", "Vivant"),
        ("Fermentation", "Pointage long, jusqu'à 36 heures. C'est là que le goût se construit.", "36 heures"),
        ("Façonnage", "À la main, pièce par pièce, sans machine de formage.", "Main"),
        ("Cuisson", "Sur place, chaque matin, en plusieurs fournées pour du pain toujours frais.", "Sur place"),
    ],

    "m_s2_eyebrow": "02 — Notre engagement",
    "m_s2_title_1": "Local,", "m_s2_title_2": "vraiment",
    "m_s2_text": "Nous travaillons avec les mairies, les écoles, les crèches et l'EHPAD de nos villages. "
                 "Nos produits complémentaires viennent de producteurs du Var, pas d'une centrale d'achat.",
    "m_img_petrissage": "Pétrissage de la pâte",
    "m_a1_t": "Anti-gaspillage",
    "m_a1_d": "Paniers Too Good To Go en fin de journée, valorisation du pain de la veille en brassage "
              "de bière, dons aux associations locales.",
    "m_a2_t": "Circuits courts",
    "m_a2_d": "Miel, confitures et huile d'olive de producteurs varois. Nous privilégions les "
              "fournisseurs situés à moins de cinquante kilomètres.",
    "m_a3_t": "Services de proximité",
    "m_a3_d": "Livraisons pour les associations et les personnes à mobilité réduite selon conditions. "
              "Un dépôt UPS est prévu prochainement.",

    "m_s3_eyebrow": "03 — Confiance",
    "m_s3_title": "Ils travaillent avec nous",
    "m_s3_lead": "Collectivités, écoles, structures de santé et professionnels de la restauration.",
    "m_partners": ["Mairie de Montferrat", "Mairie de Figanières", "Mairie de Châteaudouble",
                   "EHPAD de Figanières", "Crèche de Figanières", "Crèche de Montferrat",
                   "École de Montferrat", "Restaurant La Bastide", "Associations locales",
                   "Producteurs du Var", "Too Good To Go", "Brasseurs partenaires"],
    "m_quote": "Un pain honnête, tous les jours, pour les gens d'ici.",

    # --- boulangeries -------------------------------------------------------
    "b_eyebrow": "Nos adresses",
    "b_title_1": "Deux villages,", "b_title_2": "un même fournil",
    "b_lead": "Retrouvez CD Boulangerie à Montferrat et à Figanières, au cœur du Var.",
    "b_badge": "Boulangerie",
    "b_addr": "Adresse", "b_tue_sat": "Mar — Sam", "b_sun": "Dimanche",
    "b_mon": "Lundi", "b_closed": "Fermé", "b_phone": "Téléphone",
    "b_route": "Itinéraire", "b_contact": "Contact",
    "b_note": "Les horaires peuvent varier les jours fériés. En cas de doute, appelez-nous au ",
    "b_img_1": "Boulangerie de Montferrat", "b_img_2": "Boulangerie de Figanières",
    "mq_boul": ["Ouvert du mardi au dimanche", "Cuit sur place", "Commandes 48 h à l'avance"],
    "b_s2_eyebrow": "Bon à savoir",
    "b_s2_title": "Avant de venir",
    "b_k1_t": "Sortie de four",
    "b_k1_d": "Première fournée à 7 h, seconde en fin d'après-midi. "
              "Les viennoiseries partent vite le week-end.",
    "b_k2_t": "Commandes",
    "b_k2_d": "Gâteaux, buffets et grandes quantités : prévenez-nous 48 h à l'avance par téléphone.",
    "b_k3_t": "Paniers anti-gaspi",
    "b_k3_d": "Disponibles en fin de journée via Too Good To Go, selon les invendus du jour.",

    # --- contact ------------------------------------------------------------
    "c_eyebrow": "Contact",
    "c_title_1": "Parlons de", "c_title_2": "votre commande",
    "c_lead": "Une question, un gâteau sur mesure, un événement à organiser ? "
              "Écrivez-nous ou appelez directement le fournil.",
    "mq_contact": ["Commandes 48 h à l'avance", "Gâteaux sur mesure",
                   "Buffets &amp; événements", "Montferrat &amp; Figanières"],
    "c_form": "Formulaire",
    "c_name": "Votre nom *", "c_name_ph": "Prénom et nom",
    "c_tel": "Téléphone", "c_tel_ph": "06 00 00 00 00",
    "c_msg": "Votre message *",
    "c_msg_ph": "Décrivez votre demande, la date souhaitée et le nombre de personnes.",
    "c_send": "Envoyer le message",
    "c_note": "Le formulaire ouvre votre messagerie avec le message pré-rempli. "
              "Pour une réponse immédiate, appelez-nous.",
    "c_err": "Merci de renseigner votre nom et votre message.",
    "c_opening": "Ouverture de votre messagerie…",
    "c_subject": "Demande de",
    "c_direct": "Direct",
    "c_qa_phone": "Téléphone", "c_qa_mail": "E-mail",
    "c_qa_fb": "Facebook", "c_qa_ig": "Instagram", "c_qa_route": "Itinéraire",
    "c_qa_wa": "WhatsApp", "wa_msg": "Bonjour, je vous contacte depuis votre site.",
    "c_hours": "Horaires",
    "c_faq_eyebrow": "Questions fréquentes",
    "c_faq_title": "Vous vous demandez…",
    "c_faq": [
        ("Combien de temps à l'avance commander un gâteau ?",
         "Comptez 48 heures pour un gâteau d'anniversaire classique, et une semaine pour une "
         "pièce montée ou une commande de plus de vingt personnes."),
        ("Livrez-vous ?",
         "Nous livrons les associations et les personnes à mobilité réduite de Montferrat et "
         "Figanières, selon conditions. Appelez-nous pour en discuter."),
        ("Proposez-vous des produits sans gluten ?",
         "Notre fournil travaille la farine de blé en permanence : nous ne pouvons pas garantir "
         "une absence de traces. Demandez-nous conseil pour les alternatives."),
        ("Travaillez-vous avec les professionnels ?",
         "Oui : restaurants, collectivités, écoles, crèches et EHPAD. Contactez-nous pour établir "
         "un devis adapté à votre volume."),
    ],


    # --- événements ---------------------------------------------------------
    "nav_events": "Événements",
    "e_eyebrow": "La vie du village",
    "e_title_1": "Nos rendez-vous,", "e_title_2": "toute l'année",
    "e_lead": "Fêtes du village, jours fériés, marchés de Noël : nous sommes de "
              "toutes les occasions. Une fournée spéciale, un stand, un coup de main — "
              "la boulangerie fait partie de la vie d'ici.",
    "e_img_hero": "Stand de la boulangerie à la fête du village",
    "mq_events": ["Fêtes du village", "Jours fériés", "Marchés de Noël",
                  "Commandes spéciales", "Suivez-nous sur Facebook"],

    "e_s1_eyebrow": "01 — Le calendrier",
    "e_s1_title": "Ce qui nous anime",
    "e_s1_lead": "Les dates exactes changent chaque année. Le plus sûr est de nous "
                 "suivre sur Facebook : tout y est annoncé en premier.",
    "e_rows": [
        ("Épiphanie", "Galettes des rois à la frangipane et à la pomme, tout le mois de janvier.", "Janvier"),
        ("Chandeleur", "Crêpes et beignets préparés le jour même.", "Février"),
        ("Pâques", "Chocolats, brioches de Pâques et agneaux pascals sur commande.", "Avril"),
        ("Fête du village", "Notre stand sur la place : fougasses, pizzas et pain cuit devant vous.", "Été"),
        ("Marchés nocturnes", "Présents sur les marchés d'été de Montferrat et Figanières.", "Juillet — Août"),
        ("Marché de Noël", "Bûches, pains d'épices et chocolats. Commandes à passer tôt.", "Décembre"),
    ],

    "e_s2_eyebrow": "02 — Sur demande",
    "e_s2_title_1": "Vos événements,", "e_s2_title_2": "nous suivons",
    "e_s2_text": "Mariage, baptême, communion, repas d'association ou pot de départ : "
                 "nous préparons buffets sucrés et salés, pièces montées et grandes "
                 "quantités de pain. Prévenez-nous une à deux semaines à l'avance selon la taille.",
    "e_img_buffet": "Buffet préparé pour un événement",
    "e_c1_t": "Fêtes de famille",
    "e_c1_d": "Pièces montées, gâteaux personnalisés, buffets sucrés-salés pour vos grandes occasions.",
    "e_c2_t": "Associations & écoles",
    "e_c2_d": "Goûters, viennoiseries en nombre et pain pour vos manifestations locales.",
    "e_c3_t": "Professionnels",
    "e_c3_d": "Petits-déjeuners d'entreprise, séminaires, inaugurations. Devis rapide.",

    "e_s3_eyebrow": "03 — Ne rien rater",
    "e_s3_title": "Suivez-nous sur Facebook",
    "e_s3_text": "Nous annonçons chaque événement, chaque fournée spéciale et chaque "
                 "nouveauté sur nos réseaux. C'est le moyen le plus simple de rester informé.",
    "e_cta_fb": "Voir notre page Facebook",
    "e_cta_ig": "Nous suivre sur Instagram",
    "e_cta_wa": "Écrire sur WhatsApp",
    "e_note": "Une idée d'événement ? Appelez-nous, on en parle.",

    # --- métadonnées --------------------------------------------------------

    # --- Pages légales ------------------------------------------------------
    # Les valeurs entre crochets [ ] doivent être remplacées par les vraies
    # informations du client avant la mise en ligne. Voir ../docs/CLIENT-HANDOFF.md
    "nav_legal": "Mentions légales",
    "nav_cgv": "Conditions générales",
    "nav_privacy": "Confidentialité",

    "lg_eyebrow": "Informations légales",
    "lg_title_1": "Mentions",
    "lg_title_2": "légales",
    "lg_lead": "Informations relatives à l'éditeur du site, à son hébergeur et aux droits applicables.",
    "lg_updated": "Dernière mise à jour",

    "lg_s1_t": "Éditeur du site",
    "lg_s1_b": [
        ("Dénomination sociale", "CD Boulangerie"),
        ("Forme juridique", "Société par actions simplifiée (SAS)"),
        ("Capital social", "[À COMPLÉTER] €"),
        ("Siège social", "6 Rue du Dr Rayol, 83131 Montferrat, France"),
        ("Immatriculation", "RCS Draguignan — SIREN 918 964 834"),
        ("N° TVA intracommunautaire", "[À COMPLÉTER]"),
        ("Téléphone", "09 78 80 63 06"),
        ("Directeur de la publication", "[À CONFIRMER]"),
    ],
    "lg_s2_t": "Hébergement",
    "lg_s2_b": [
        ("Hébergeur", "[NOM DE L'HÉBERGEUR]"),
        ("Adresse", "[ADRESSE COMPLÈTE]"),
        ("Téléphone", "[TÉLÉPHONE]"),
    ],
    "lg_s3_t": "Propriété intellectuelle",
    "lg_s3_p": "L'ensemble de ce site — structure, textes, photographies, logo et éléments graphiques — est protégé par le droit d'auteur. Toute reproduction, représentation ou adaptation, totale ou partielle, sans autorisation écrite préalable est interdite.\n\nLes photographies présentées sont la propriété de CD Boulangerie. Les logos des partenaires et les blasons communaux restent la propriété de leurs détenteurs respectifs et sont affichés avec leur accord.",
    "lg_s4_t": "Responsabilité",
    "lg_s4_p": "Les informations publiées sur ce site (produits, horaires, tarifs, événements) sont données à titre indicatif et peuvent évoluer. Les horaires sont susceptibles de varier les jours fériés et pendant les congés annuels. En cas de doute, nous vous invitons à nous appeler avant de vous déplacer.\n\nCD Boulangerie ne saurait être tenue responsable des dommages résultant d'une interruption du service ou de la présence d'un virus informatique.",
    "lg_s5_t": "Liens vers d'autres sites",
    "lg_s5_p": "Ce site contient des liens vers des sites tiers (Facebook, Instagram, WhatsApp, Google Maps). CD Boulangerie n'exerce aucun contrôle sur ces sites et décline toute responsabilité quant à leur contenu.",
    "lg_s6_t": "Droit applicable",
    "lg_s6_p": "Le présent site est soumis au droit français. Tout litige relève de la compétence des tribunaux du ressort de Draguignan.",
    "lg_s7_t": "Nous contacter",
    "lg_s7_p": "Pour toute question relative à ces mentions légales, vous pouvez nous joindre par téléphone, par e-mail ou directement en boutique.",

    # --- Conditions générales -----------------------------------------------
    "cg_eyebrow": "Nos conditions",
    "cg_title_1": "Conditions",
    "cg_title_2": "générales",
    "cg_lead": "Les règles qui s'appliquent à nos ventes en boutique et à vos commandes sur mesure. Rien de compliqué : ce sont nos habitudes de travail, mises par écrit.",
    "cg_intro_t": "En deux mots",
    "cg_intro_p": "CD Boulangerie est une boulangerie artisanale. Nous vendons nos produits directement en boutique, à Montferrat et à Figanières. Ce site est une vitrine : il ne permet pas de payer en ligne. Les commandes se font par téléphone, par message ou en boutique.",

    "cg_s1_t": "1. Champ d'application",
    "cg_s1_p": "Les présentes conditions s'appliquent à toutes les ventes réalisées dans nos boutiques ainsi qu'aux commandes passées par téléphone, par e-mail, par WhatsApp ou sur place. Toute commande vaut acceptation de ces conditions.",
    "cg_s2_t": "2. Nos produits",
    "cg_s2_p": "Nos produits sont fabriqués artisanalement, chaque jour, dans notre fournil. Ce sont des produits vivants : l'aspect, le poids et la coloration peuvent légèrement varier d'une fournée à l'autre. C'est la marque du fait main, pas un défaut.\n\nLa disponibilité dépend de la production du jour. Certains produits sont proposés uniquement en saison ou sur commande.",
    "cg_s3_t": "3. Allergènes",
    "cg_s3_p": "Nos produits sont préparés dans un fournil où sont manipulés notamment : gluten, œufs, lait, fruits à coque, soja et sésame. Malgré notre vigilance, nous ne pouvons pas garantir l'absence totale de traces.\n\nSi vous avez une allergie, signalez-le nous avant toute commande : nous vous indiquerons précisément la composition de chaque produit.",
    "cg_s4_t": "4. Prix",
    "cg_s4_p": "Les prix sont affichés en boutique, en euros, toutes taxes comprises. Ils peuvent être modifiés à tout moment, notamment en fonction du cours des matières premières. Le prix applicable est celui affiché au moment de la commande.\n\nPour les commandes sur mesure, un devis est établi avant validation.",
    "cg_s5_t": "5. Commandes sur mesure",
    "cg_s5_p": "Nous réalisons des pièces montées, gâteaux personnalisés, buffets et commandes en volume pour les particuliers, les associations et les professionnels.",
    "cg_s5_b": [
        ("Délai de commande", "48 heures minimum pour un gâteau classique, une semaine pour une pièce montée ou un buffet."),
        ("Confirmation", "Une commande n'est ferme qu'après notre confirmation explicite, par téléphone ou par écrit."),
        ("Acompte", "Un acompte peut être demandé pour les commandes importantes. Il est déduit du montant final."),
        ("Retrait", "Les commandes sont à retirer en boutique, aux jour et heure convenus."),
    ],
    "cg_s6_t": "6. Annulation",
    "cg_s6_p": "Une commande peut être annulée sans frais jusqu'à 48 heures avant la date de retrait. Passé ce délai, la fabrication étant engagée, l'acompte versé reste acquis.\n\nEn cas d'annulation de notre fait — panne, force majeure, indisponibilité d'une matière première — vous êtes prévenu au plus vite et intégralement remboursé.",
    "cg_s7_t": "7. Paiement",
    "cg_s7_p": "Le paiement s'effectue en boutique, au moment du retrait : espèces, carte bancaire ou tout autre moyen accepté en caisse. Aucun paiement n'est encaissé via ce site.",
    "cg_s8_t": "8. Retrait et conservation",
    "cg_s8_p": "Nos produits sont frais et sans conservateur. Ils sont à consommer rapidement : le jour même pour les viennoiseries et les pâtisseries, sous deux à trois jours pour les pains au levain.\n\nÀ compter de la remise, la bonne conservation relève de votre responsabilité. Les produits à base de crème doivent être maintenus au frais.",
    "cg_s9_t": "9. Droit de rétractation",
    "cg_s9_p": "Conformément à l'article L221-28 du code de la consommation, le droit de rétractation ne s'applique pas aux denrées alimentaires périssables ni aux produits confectionnés selon les spécifications du consommateur.",
    "cg_s10_t": "10. Réclamations",
    "cg_s10_p": "Une remarque, un souci sur une commande ? Parlez-nous-en le jour même, en boutique ou par téléphone. Nous trouverons une solution : c'est plus simple et plus rapide que n'importe quelle procédure.",
    "cg_s11_t": "11. Médiation",
    "cg_s11_p": "En cas de litige non résolu à l'amiable, le consommateur peut recourir gratuitement à un médiateur de la consommation. Les coordonnées du médiateur compétent sont disponibles sur demande en boutique.",
    "cg_s12_t": "12. Droit applicable",
    "cg_s12_p": "Les présentes conditions sont soumises au droit français. En cas de litige, les tribunaux du ressort de Draguignan sont seuls compétents.",

    # --- Confidentialité ----------------------------------------------------
    "pv_eyebrow": "Vos données",
    "pv_title_1": "Politique de",
    "pv_title_2": "confidentialité",
    "pv_lead": "Ce que nous faisons — et surtout ne faisons pas — de vos informations personnelles.",
    "pv_hl_t": "L'essentiel en une phrase",
    "pv_hl_p": "Ce site ne dépose aucun cookie, n'utilise aucun outil de mesure d'audience et ne transmet vos données à personne. Les seules informations que nous recevons sont celles que vous nous envoyez volontairement.",
    "pv_s1_t": "Qui traite vos données",
    "pv_s1_p": "CD Boulangerie, 6 Rue du Dr Rayol, 83131 Montferrat, est responsable du traitement des données collectées sur ce site.",
    "pv_s2_t": "Quelles données, et pourquoi",
    "pv_s2_b": [
        ("Formulaire de contact", "Nom, téléphone et contenu du message. Uniquement pour répondre à votre demande."),
        ("Appel ou WhatsApp", "Votre numéro apparaît, comme pour n'importe quel appel. Nous ne le conservons pas au-delà du traitement de votre demande."),
        ("Navigation", "Aucune donnée n'est collectée. Pas de cookie, pas de statistiques, pas de traqueur."),
    ],
    "pv_s3_t": "Pas de cookies",
    "pv_s3_p": "Ce site ne dépose aucun cookie sur votre appareil. C'est pour cette raison qu'aucun bandeau de consentement ne vous est présenté : il n'y a rien à accepter.\n\nLes polices de caractères sont hébergées sur notre propre serveur : votre adresse IP n'est transmise à aucun service tiers lors de l'affichage des pages.",
    "pv_s4_t": "Services extérieurs",
    "pv_s4_p": "Les boutons Facebook, Instagram, WhatsApp et Google Maps sont de simples liens. Aucun contenu de ces services n'est chargé tant que vous ne cliquez pas. Si vous cliquez, vous quittez notre site et ce sont les règles de confidentialité de ces services qui s'appliquent.",
    "pv_s5_t": "Durée de conservation",
    "pv_s5_p": "Les messages reçus sont conservés le temps nécessaire au traitement de votre demande, puis pendant trois ans au maximum à des fins de suivi commercial. Les données liées à une commande sont conservées dix ans, comme l'impose la réglementation comptable.",
    "pv_s6_t": "Vos droits",
    "pv_s6_p": "Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition sur vos données. Pour l'exercer, écrivez-nous ou passez en boutique : nous répondons sous un mois.\n\nSi la réponse ne vous satisfait pas, vous pouvez saisir la CNIL (cnil.fr).",
    "pv_s7_t": "Sécurité",
    "pv_s7_p": "Le site est diffusé en HTTPS. Les messages que vous nous envoyez arrivent dans notre boîte e-mail professionnelle, à laquelle seule la direction a accès.",

    "meta": {
        "mentions": ("Mentions légales — CD Boulangerie",
                     "Informations légales de CD Boulangerie : éditeur, hébergeur, propriété intellectuelle et droit applicable."),
        "cgv": ("Conditions générales — CD Boulangerie",
                "Nos conditions de vente : commandes sur mesure, allergènes, délais, annulation et paiement."),
        "confidentialite": ("Politique de confidentialité — CD Boulangerie",
                            "Aucun cookie, aucun traqueur. Ce que nous faisons de vos données et comment exercer vos droits."),
        "index": ("CD Boulangerie — Boulangerie artisanale à Montferrat &amp; Figanières",
                  "Boulangerie artisanale dans le Var : pains au levain, viennoiseries pur beurre "
                  "et pâtisseries faites sur place. Montferrat et Figanières."),
        "produits": ("Nos produits — CD Boulangerie",
                     "Pains au levain, viennoiseries pur beurre, pâtisseries, snacking et produits "
                     "locaux du Var."),
        "maison": ("La Maison — CD Boulangerie",
                   "Notre savoir-faire : levain naturel, fermentation longue, façonnage à la main "
                   "et engagement local dans le Var."),
        "boulangeries": ("Nos boulangeries — CD Boulangerie",
                         "Horaires, adresses et itinéraires de nos boulangeries de Montferrat et "
                         "Figanières dans le Var."),
        "contact": ("Contact — CD Boulangerie",
                    "Contactez CD Boulangerie pour vos commandes, gâteaux sur mesure et événements."),
        "evenements": ("Événements — CD Boulangerie",
                       "Fêtes du village, jours fériés, marchés de Noël et buffets sur mesure. Suivez CD Boulangerie pour ne rien rater."),
    },
}

# ===========================================================================
#  ENGLISH
# ===========================================================================
T["en"] = {
    "html_lang": "en",
    "locale": "en_GB",

    "nav_home": "Home",
    "nav_products": "Products",
    "nav_house": "Our Craft",
    "nav_bakeries": "Our bakeries",
    "nav_contact": "Contact",
    "nav_order": "Order",
    "brand_sub": "Artisan · Var",
    "skip": "Skip to content",
    "menu_label": "Menu",
    "lang_label": "Language",
    "follow": "Follow us",
    "top": "Back to top",
    "close": "Close",
    "prev": "Previous",
    "next": "Next",
    "gallery": "Gallery",
    "loading": "Loading",
    "scroll": "Scroll",
    "up_next": "Up next",
    "back": "Back",

    "load_where": "Montferrat &amp; Figanières",
    "load_who": "Artisan baker",
    "load_steps": ["Kneading", "First rise", "Shaping", "Into the oven", "Out of the oven"],

    "f_tagline": "Breads, viennoiseries and pastries shaped fresh every day on the premises, "
                 "in the heart of the Var.",
    "f_nav": "Navigation",
    "f_find": "Find us",
    "f_contact": "Contact",
    "f_rights": "All rights reserved",
    "f_craft": "Artisan baked · Var, France",

    "h_eyebrow": "Est. Montferrat · Var",
    "h_title_1": "The taste of real,",
    "h_title_2": "every single day.",
    "h_lead": "Sourdough breads, all-butter viennoiseries and pastries shaped on site. "
              "A house rooted in the Var, committed to local sourcing and zero waste.",
    "h_cta1": "Discover our products",
    "h_cta2": "Opening hours &amp; directions",
    "h_img_hero": "Morning window display — sourdough loaves",

    "mq_home": ["Natural sourdough", "French flours", "Baked on site",
                "Local produce", "Zero waste", "Montferrat &amp; Figanières"],

    "h_s1_eyebrow": "01 — The selection",
    "h_s1_title": "Breads with character",
    "h_s1_lead": "Slowly fermented doughs, shaped by hand and baked every morning. "
                 "Time does the rest.",
    "h_c1_t": "The Grand Levain", "h_c1_n": "36 H",
    "h_c1_d": "Thick crust, open crumb, long fermentation on natural sourdough.",
    "h_c2_t": "The Tradition", "h_c2_n": "24 H",
    "h_c2_d": "Selected French flour, slow first rise, shaped entirely by hand.",
    "h_c3_t": "Viennoiseries", "h_c3_n": "07 H",
    "h_c3_d": "All butter, laminated and baked on site, straight from the morning oven.",
    "h_all": "See the full range",
    "h_tag_sig": "Signature", "h_tag_morning": "Mornings",
    "h_img_levain": "Sliced sourdough loaf with open crumb",
    "h_img_trad": "French tradition baguettes",
    "h_img_croissants": "All-butter croissants",

    "h_q_eyebrow": "Our philosophy",
    "h_quote": "Nothing is rushed. Good bread takes time, patience and the hand of a craftsman.",
    "h_q_by": "CD Boulangerie — Montferrat",
    "h_img_fournil": "The bakehouse at 5 in the morning",
    "h_st1": "Of fermentation", "h_st2": "Bakeries",
    "h_st3": "Site languages", "h_st4": "Made on site",

    "h_s2_eyebrow": "02 — Our craft",
    "h_s2_title_1": "Craftsmen,", "h_s2_title_2": "not a factory",
    "h_s2_text": "Everything is made in our own bakehouse: kneading, rising, shaping, baking. "
                 "We choose French flours and work with producers from the Var.",
    "h_s2_link": "Our story",
    "h_img_faconnage": "Shaping bread dough by hand",

    "h_s3_eyebrow": "03 — Our addresses",
    "h_s3_title_1": "Two villages,", "h_s3_title_2": "one bakehouse",
    "h_s3_text": "Find us in Montferrat and Figanières, Tuesday through Sunday. "
                 "Special orders and cakes by reservation.",
    "h_s3_link": "Hours &amp; directions",
    "h_img_devanture": "Shopfront of the Montferrat bakery",

    "h_s4_eyebrow": "04 — Commitments",
    "h_s4_title": "Concrete actions",
    "h_e1_t": "Too Good To Go",
    "h_e1_d": "Discounted baskets at the end of the day to fight food waste.",
    "h_e2_t": "Beer from surplus bread",
    "h_e2_d": "Yesterday's bread is brewed into beer rather than binned. Nothing is lost.",
    "h_e3_t": "Local deliveries",
    "h_e3_d": "For associations and people with reduced mobility, conditions apply. Just ask us.",

    "p_eyebrow": "The range",
    "p_title_1": "Breads, viennoiseries", "p_title_2": "&amp; pastries",
    "p_lead": "Bread first: that is our trade. The rest follows the season and the mood of the bakehouse.",
    "mq_prod": ["Baked this morning", "Natural sourdough", "All butter", "Homemade", "French flours"],

    "p_s1_eyebrow": "01 — The breads",
    "p_s1_title": "The bakehouse",
    "p_rows": [
        ("The Grand Levain", "36-hour fermentation, thick crust, open crumb.", "Signature"),
        ("The Tradition", "French flour, slow rise, hand shaped.", "Every day"),
        ("Country loaf", "Wheat and rye, dense crumb, keeps for days.", "Every day"),
        ("Cereals &amp; seeds", "Sunflower, linseed, sesame, poppy.", "Every day"),
        ("Wholemeal bread", "T110 flour, rich in fibre.", "To order"),
        ("Provençal fougasse", "Olive oil, herbs from the Var, olives.", "Oven permitting"),
    ],

    "p_s2_eyebrow": "02 — The rest of the range",
    "p_s2_title": "Every day at the counter",
    "p_cat1_t": "Viennoiseries",
    "p_cat1_d": "Croissants, pains au chocolat, apple turnovers, brioches. "
                "All butter, laminated and baked on site.",
    "p_cat2_t": "Pastries",
    "p_cat2_d": "Seasonal tarts, éclairs, entremets. Birthday and celebration cakes to order.",
    "p_cat3_t": "Snacks &amp; burgers",
    "p_cat3_d": "Sandwiches on our own bread, quiches, pizzas and homemade burgers at lunchtime.",
    "p_cat4_t": "Local produce",
    "p_cat4_d": "Honey, jams, olive oil and goods from Var producers, selected by us.",
    "p_img_vienn": "Tray of viennoiseries",
    "p_img_patis": "Display of pastries and tarts",
    "p_img_snack": "Artisan sandwich on homemade bread",
    "p_img_local": "Honey and local produce from the Var",

    "p_s3_eyebrow": "03 — Gallery",
    "p_s3_title": "In pictures",
    "p_s3_lead": "Click a photo to enlarge it.",
    "p_f_all": "All", "p_f_breads": "Breads", "p_f_vienn": "Viennoiseries",
    "p_f_patis": "Pastries", "p_f_snack": "Snacks", "p_f_local": "Local produce",
    "p_zoom": "Enlarge",
    "p_gal": ["Sourdough bread", "French tradition", "Country loaf",
              "All-butter croissant", "Pain au chocolat", "Apple turnover",
              "Fruit tart", "Éclair", "Celebration cake",
              "Sandwich of the day", "Homemade burger", "Honey &amp; Var produce"],

    "p_cta_title": "A special order?",
    "p_cta_lead": "Birthday cakes, buffets, events, bread in large quantities. "
                  "Please give us 48 hours' notice.",
    "p_cta_btn": "Get in touch",

    "m_eyebrow": "Our craft",
    "m_title_1": "Time", "m_title_2": "as an ingredient",
    "m_lead": "Craftsmanship is not a sales pitch. It is our daily routine: gestures, hours "
              "and a standard that is never negotiable.",
    "m_img_fournil": "The bakehouse at first light",
    "mq_maison": ["36 hours of fermentation", "Natural sourdough", "Hand shaped",
                  "Baked on site", "French flours"],

    "m_s1_eyebrow": "01 — The craft",
    "m_s1_title": "From grain to counter",
    "m_rows": [
        ("Selection", "French flours from partner millers, local produce from the Var.", "Upstream"),
        ("Sourdough", "A natural starter fed every single day, never replaced by a shortcut.", "Living"),
        ("Fermentation", "A long rise, up to 36 hours. That is where the flavour is built.", "36 hours"),
        ("Shaping", "By hand, piece by piece, with no moulding machine.", "By hand"),
        ("Baking", "On site, every morning, in several batches so the bread is always fresh.", "On site"),
    ],

    "m_s2_eyebrow": "02 — Our commitment",
    "m_s2_title_1": "Local,", "m_s2_title_2": "genuinely",
    "m_s2_text": "We work with the town halls, schools, nurseries and care home of our villages. "
                 "Our additional products come from Var producers, not from a central purchasing group.",
    "m_img_petrissage": "Kneading the dough",
    "m_a1_t": "Zero waste",
    "m_a1_d": "Too Good To Go baskets at the end of the day, yesterday's bread brewed into beer, "
              "donations to local associations.",
    "m_a2_t": "Short supply chains",
    "m_a2_d": "Honey, jams and olive oil from Var producers. We favour suppliers located less than "
              "fifty kilometres away.",
    "m_a3_t": "Neighbourhood services",
    "m_a3_d": "Deliveries for associations and people with reduced mobility, conditions apply. "
              "A UPS drop-off point is planned shortly.",

    "m_s3_eyebrow": "03 — Trust",
    "m_s3_title": "They work with us",
    "m_s3_lead": "Local authorities, schools, care facilities and catering professionals.",
    "m_partners": ["Montferrat Town Hall", "Figanières Town Hall", "Châteaudouble Town Hall",
                   "Figanières care home", "Figanières nursery", "Montferrat nursery",
                   "Montferrat school", "La Bastide restaurant", "Local associations",
                   "Var producers", "Too Good To Go", "Partner brewers"],
    "m_quote": "Honest bread, every day, for the people who live here.",

    "b_eyebrow": "Our addresses",
    "b_title_1": "Two villages,", "b_title_2": "one bakehouse",
    "b_lead": "Find CD Boulangerie in Montferrat and Figanières, in the heart of the Var.",
    "b_badge": "Bakery",
    "b_addr": "Address", "b_tue_sat": "Tue — Sat", "b_sun": "Sunday",
    "b_mon": "Monday", "b_closed": "Closed", "b_phone": "Phone",
    "b_route": "Directions", "b_contact": "Contact",
    "b_note": "Hours may vary on public holidays. If in doubt, call us on ",
    "b_img_1": "Montferrat bakery", "b_img_2": "Figanières bakery",
    "mq_boul": ["Open Tuesday to Sunday", "Baked on site", "Orders 48 hours ahead"],
    "b_s2_eyebrow": "Good to know",
    "b_s2_title": "Before you visit",
    "b_k1_t": "Out of the oven",
    "b_k1_d": "First batch at 7 am, second in the late afternoon. "
              "Viennoiseries go quickly at the weekend.",
    "b_k2_t": "Orders",
    "b_k2_d": "Cakes, buffets and large quantities: please call us 48 hours ahead.",
    "b_k3_t": "Anti-waste baskets",
    "b_k3_d": "Available at the end of the day via Too Good To Go, depending on what is left.",

    "c_eyebrow": "Contact",
    "c_title_1": "Let's talk about", "c_title_2": "your order",
    "c_lead": "A question, a bespoke cake, an event to organise? "
              "Write to us or call the bakehouse directly.",
    "mq_contact": ["Orders 48 hours ahead", "Bespoke cakes",
                   "Buffets &amp; events", "Montferrat &amp; Figanières"],
    "c_form": "Form",
    "c_name": "Your name *", "c_name_ph": "First name and surname",
    "c_tel": "Phone", "c_tel_ph": "+33 6 00 00 00 00",
    "c_msg": "Your message *",
    "c_msg_ph": "Describe your request, the date you need and the number of people.",
    "c_send": "Send message",
    "c_note": "The form opens your email app with the message pre-filled. "
              "For an immediate answer, please call us.",
    "c_err": "Please fill in your name and your message.",
    "c_opening": "Opening your email app…",
    "c_subject": "Enquiry from",
    "c_direct": "Direct",
    "c_qa_phone": "Phone", "c_qa_mail": "Email",
    "c_qa_fb": "Facebook", "c_qa_ig": "Instagram", "c_qa_route": "Directions",
    "c_qa_wa": "WhatsApp", "wa_msg": "Hello, I am contacting you from your website.",
    "c_hours": "Opening hours",
    "c_faq_eyebrow": "Frequently asked",
    "c_faq_title": "You may be wondering…",
    "c_faq": [
        ("How far ahead should I order a cake?",
         "Allow 48 hours for a standard birthday cake, and one week for a tiered cake or an order "
         "for more than twenty people."),
        ("Do you deliver?",
         "We deliver to associations and people with reduced mobility in Montferrat and Figanières, "
         "conditions apply. Call us to discuss it."),
        ("Do you offer gluten-free products?",
         "Our bakehouse works with wheat flour constantly, so we cannot guarantee the absence of "
         "traces. Ask us for advice on alternatives."),
        ("Do you work with businesses?",
         "Yes: restaurants, local authorities, schools, nurseries and care homes. Contact us for a "
         "quote suited to your volume."),
    ],


    # --- événements ---------------------------------------------------------
    "nav_events": "Events",
    "e_eyebrow": "Village life",
    "e_title_1": "Our gatherings,", "e_title_2": "all year round",
    "e_lead": "Village fairs, public holidays, Christmas markets: we are part of every "
              "occasion. A special batch, a market stall, a helping hand — the bakery "
              "belongs to the life of this place.",
    "e_img_hero": "The bakery stall at the village fair",
    "mq_events": ["Village fairs", "Public holidays", "Christmas markets",
                  "Special orders", "Follow us on Facebook"],

    "e_s1_eyebrow": "01 — The calendar",
    "e_s1_title": "What keeps us busy",
    "e_s1_lead": "Exact dates change every year. The safest way is to follow us on "
                 "Facebook: everything is announced there first.",
    "e_rows": [
        ("Epiphany", "King cakes with frangipane and apple, all through January.", "January"),
        ("Candlemas", "Crêpes and doughnuts made fresh on the day.", "February"),
        ("Easter", "Chocolates, Easter brioches and paschal lambs to order.", "April"),
        ("Village fair", "Our stall on the square: fougasse, pizza and bread baked in front of you.", "Summer"),
        ("Night markets", "Present at the summer markets in Montferrat and Figanières.", "July — August"),
        ("Christmas market", "Yule logs, gingerbread and chocolates. Order early.", "December"),
    ],

    "e_s2_eyebrow": "02 — On request",
    "e_s2_title_1": "Your events,", "e_s2_title_2": "we follow",
    "e_s2_text": "Wedding, christening, communion, club dinner or farewell party: we "
                 "prepare sweet and savoury buffets, tiered cakes and bread in large "
                 "quantities. Give us one to two weeks' notice depending on the size.",
    "e_img_buffet": "Buffet prepared for an event",
    "e_c1_t": "Family celebrations",
    "e_c1_d": "Tiered cakes, custom cakes, sweet and savoury buffets for your big occasions.",
    "e_c2_t": "Clubs & schools",
    "e_c2_d": "Snacks, viennoiseries in quantity and bread for your local events.",
    "e_c3_t": "Businesses",
    "e_c3_d": "Corporate breakfasts, seminars, openings. Quick quote.",

    "e_s3_eyebrow": "03 — Miss nothing",
    "e_s3_title": "Follow us on Facebook",
    "e_s3_text": "We announce every event, every special batch and every new product on "
                 "our social pages. It is the simplest way to stay informed.",
    "e_cta_fb": "Visit our Facebook page",
    "e_cta_ig": "Follow us on Instagram",
    "e_cta_wa": "Message us on WhatsApp",
    "e_note": "Got an event in mind? Call us and let's talk it through.",


    # --- Legal pages --------------------------------------------------------
    "nav_legal": "Legal notice",
    "nav_cgv": "Terms & conditions",
    "nav_privacy": "Privacy",

    "lg_eyebrow": "Legal information",
    "lg_title_1": "Legal",
    "lg_title_2": "notice",
    "lg_lead": "Information about the publisher of this website, its host and the applicable rights.",
    "lg_updated": "Last updated",

    "lg_s1_t": "Website publisher",
    "lg_s1_b": [
        ("Company name", "CD Boulangerie"),
        ("Legal form", "Simplified joint-stock company (SAS)"),
        ("Share capital", "[TO BE COMPLETED] €"),
        ("Registered office", "6 Rue du Dr Rayol, 83131 Montferrat, France"),
        ("Registration", "Draguignan Trade Register — SIREN 918 964 834"),
        ("VAT number", "[TO BE COMPLETED]"),
        ("Telephone", "+33 9 78 80 63 06"),
        ("Publication director", "[TO BE CONFIRMED]"),
    ],
    "lg_s2_t": "Hosting",
    "lg_s2_b": [
        ("Host", "[HOST NAME]"),
        ("Address", "[FULL ADDRESS]"),
        ("Telephone", "[TELEPHONE]"),
    ],
    "lg_s3_t": "Intellectual property",
    "lg_s3_p": "This entire website — structure, texts, photographs, logo and graphic elements — is protected by copyright. Any reproduction, representation or adaptation, in whole or in part, without prior written permission is prohibited.\n\nThe photographs shown are the property of CD Boulangerie. Partner logos and municipal coats of arms remain the property of their respective owners and are displayed with their consent.",
    "lg_s4_t": "Liability",
    "lg_s4_p": "The information published on this site (products, opening hours, prices, events) is given for guidance only and may change. Opening hours may vary on public holidays and during annual closures. If in doubt, please call us before travelling.\n\nCD Boulangerie cannot be held liable for damage resulting from a service interruption or the presence of a computer virus.",
    "lg_s5_t": "Links to other sites",
    "lg_s5_p": "This site contains links to third-party sites (Facebook, Instagram, WhatsApp, Google Maps). CD Boulangerie has no control over these sites and accepts no responsibility for their content.",
    "lg_s6_t": "Applicable law",
    "lg_s6_p": "This website is governed by French law. Any dispute falls within the jurisdiction of the courts of Draguignan.",
    "lg_s7_t": "Contact us",
    "lg_s7_p": "For any question regarding this legal notice, you can reach us by telephone, by e-mail or directly in the shop.",

    # --- Terms & conditions -------------------------------------------------
    "cg_eyebrow": "Our terms",
    "cg_title_1": "Terms &",
    "cg_title_2": "conditions",
    "cg_lead": "The rules that apply to our in-shop sales and to your custom orders. Nothing complicated: these are simply our working habits, written down.",
    "cg_intro_t": "In short",
    "cg_intro_p": "CD Boulangerie is an artisan bakery. We sell our products directly in our shops in Montferrat and Figanières. This website is a showcase: it does not allow online payment. Orders are placed by telephone, by message or in person.",

    "cg_s1_t": "1. Scope",
    "cg_s1_p": "These terms apply to all sales made in our shops as well as to orders placed by telephone, e-mail, WhatsApp or in person. Any order implies acceptance of these terms.",
    "cg_s2_t": "2. Our products",
    "cg_s2_p": "Our products are made by hand, every day, in our own bakehouse. They are living products: appearance, weight and colour may vary slightly from one batch to the next. That is the mark of handmade work, not a defect.\n\nAvailability depends on the day's production. Some products are offered seasonally or to order only.",
    "cg_s3_t": "3. Allergens",
    "cg_s3_p": "Our products are prepared in a bakehouse where gluten, eggs, milk, nuts, soya and sesame are handled. Despite our care, we cannot guarantee the complete absence of traces.\n\nIf you have an allergy, please tell us before ordering: we will give you the exact composition of each product.",
    "cg_s4_t": "4. Prices",
    "cg_s4_p": "Prices are displayed in the shop, in euros, including all taxes. They may change at any time, particularly according to raw material costs. The applicable price is the one displayed at the time of the order.\n\nFor custom orders, a quotation is issued before confirmation.",
    "cg_s5_t": "5. Custom orders",
    "cg_s5_p": "We make tiered cakes, personalised cakes, buffets and bulk orders for individuals, associations and businesses.",
    "cg_s5_b": [
        ("Lead time", "48 hours minimum for a standard cake, one week for a tiered cake or a buffet."),
        ("Confirmation", "An order is only firm once we have explicitly confirmed it, by telephone or in writing."),
        ("Deposit", "A deposit may be requested for large orders. It is deducted from the final amount."),
        ("Collection", "Orders are collected in the shop, on the agreed day and time."),
    ],
    "cg_s6_t": "6. Cancellation",
    "cg_s6_p": "An order may be cancelled free of charge up to 48 hours before the collection date. After that, as production has begun, any deposit paid is retained.\n\nIf we have to cancel — breakdown, force majeure, unavailable ingredient — you will be informed as soon as possible and fully refunded.",
    "cg_s7_t": "7. Payment",
    "cg_s7_p": "Payment is made in the shop, on collection: cash, card or any other means accepted at the till. No payment is taken through this website.",
    "cg_s8_t": "8. Collection and storage",
    "cg_s8_p": "Our products are fresh and free of preservatives. They should be eaten quickly: the same day for viennoiseries and pastries, within two to three days for sourdough breads.\n\nFrom the moment of collection, proper storage is your responsibility. Cream-based products must be kept refrigerated.",
    "cg_s9_t": "9. Right of withdrawal",
    "cg_s9_p": "In accordance with article L221-28 of the French Consumer Code, the right of withdrawal does not apply to perishable foodstuffs or to products made to the consumer's specifications.",
    "cg_s10_t": "10. Complaints",
    "cg_s10_p": "A remark, a problem with an order? Tell us the same day, in the shop or by telephone. We will find a solution: it is simpler and faster than any formal procedure.",
    "cg_s11_t": "11. Mediation",
    "cg_s11_p": "If a dispute cannot be settled amicably, consumers may refer the matter free of charge to a consumer mediator. The details of the competent mediator are available on request in the shop.",
    "cg_s12_t": "12. Applicable law",
    "cg_s12_p": "These terms are governed by French law. In the event of a dispute, the courts of Draguignan have sole jurisdiction.",

    # --- Privacy ------------------------------------------------------------
    "pv_eyebrow": "Your data",
    "pv_title_1": "Privacy",
    "pv_title_2": "policy",
    "pv_lead": "What we do — and above all do not do — with your personal information.",
    "pv_hl_t": "The essentials in one sentence",
    "pv_hl_p": "This website sets no cookies, uses no analytics tools and passes your data to no one. The only information we receive is what you send us voluntarily.",
    "pv_s1_t": "Who processes your data",
    "pv_s1_p": "CD Boulangerie, 6 Rue du Dr Rayol, 83131 Montferrat, France, is responsible for processing the data collected on this site.",
    "pv_s2_t": "What data, and why",
    "pv_s2_b": [
        ("Contact form", "Name, telephone and message content. Solely to answer your enquiry."),
        ("Call or WhatsApp", "Your number appears, as with any call. We do not keep it beyond handling your request."),
        ("Browsing", "No data is collected. No cookies, no statistics, no trackers."),
    ],
    "pv_s3_t": "No cookies",
    "pv_s3_p": "This site places no cookies on your device. That is why no consent banner is shown: there is nothing to accept.\n\nThe fonts are hosted on our own server: your IP address is not passed to any third-party service when pages are displayed.",
    "pv_s4_t": "External services",
    "pv_s4_p": "The Facebook, Instagram, WhatsApp and Google Maps buttons are plain links. No content from these services is loaded until you click. If you do click, you leave our site and the privacy rules of those services apply.",
    "pv_s5_t": "Retention period",
    "pv_s5_p": "Messages received are kept for as long as needed to handle your request, then for a maximum of three years for commercial follow-up. Order-related data is kept for ten years, as required by accounting rules.",
    "pv_s6_t": "Your rights",
    "pv_s6_p": "You have the right to access, correct, erase, restrict and object to the processing of your data. To exercise it, write to us or come into the shop: we reply within one month.\n\nIf our answer does not satisfy you, you may contact the CNIL, the French data protection authority (cnil.fr).",
    "pv_s7_t": "Security",
    "pv_s7_p": "The site is served over HTTPS. The messages you send us arrive in our professional mailbox, to which only management has access.",

    "meta": {
        "mentions": ("Legal notice — CD Boulangerie",
                     "Legal information for CD Boulangerie: publisher, host, intellectual property and applicable law."),
        "cgv": ("Terms & conditions — CD Boulangerie",
                "Our terms of sale: custom orders, allergens, lead times, cancellation and payment."),
        "confidentialite": ("Privacy policy — CD Boulangerie",
                            "No cookies, no trackers. What we do with your data and how to exercise your rights."),
        "index": ("CD Boulangerie — Artisan bakery in Montferrat &amp; Figanières",
                  "Artisan bakery in the Var, France: sourdough breads, all-butter viennoiseries "
                  "and pastries made on site. Montferrat and Figanières."),
        "produits": ("Our products — CD Boulangerie",
                     "Sourdough breads, all-butter viennoiseries, pastries, snacks and local "
                     "produce from the Var."),
        "maison": ("Our Craft — CD Boulangerie",
                   "Our know-how: natural sourdough, long fermentation, hand shaping and a local "
                   "commitment in the Var."),
        "boulangeries": ("Our bakeries — CD Boulangerie",
                         "Opening hours, addresses and directions for our bakeries in Montferrat "
                         "and Figanières."),
        "contact": ("Contact — CD Boulangerie",
                    "Contact CD Boulangerie for orders, bespoke cakes and events."),
        "evenements": ("Events — CD Boulangerie",
                       "Village fairs, public holidays, Christmas markets and bespoke buffets. Follow CD Boulangerie so you never miss a thing."),
    },
}

# ===========================================================================
#  POLSKI
# ===========================================================================
T["pl"] = {
    "html_lang": "pl",
    "locale": "pl_PL",

    "nav_home": "Strona główna",
    "nav_products": "Produkty",
    "nav_house": "Nasze rzemiosło",
    "nav_bakeries": "Nasze piekarnie",
    "nav_contact": "Kontakt",
    "nav_order": "Zamów",
    "brand_sub": "Rzemiosło · Var",
    "skip": "Przejdź do treści",
    "menu_label": "Menu",
    "lang_label": "Język",
    "follow": "Obserwuj nas",
    "top": "Do góry",
    "close": "Zamknij",
    "prev": "Poprzednie",
    "next": "Następne",
    "gallery": "Galeria",
    "loading": "Ładowanie",
    "scroll": "Przewiń",
    "up_next": "Dalej",
    "back": "Powrót",

    "load_where": "Montferrat &amp; Figanières",
    "load_who": "Piekarz rzemieślnik",
    "load_steps": ["Wyrabianie", "Fermentacja", "Formowanie", "Do pieca", "Z pieca"],

    "f_tagline": "Chleby, wypieki maślane i ciasta formowane codziennie na miejscu, "
                 "w sercu regionu Var.",
    "f_nav": "Nawigacja",
    "f_find": "Znajdź nas",
    "f_contact": "Kontakt",
    "f_rights": "Wszelkie prawa zastrzeżone",
    "f_craft": "Wypiek rzemieślniczy · Var, Francja",

    "h_eyebrow": "Od zawsze Montferrat · Var",
    "h_title_1": "Smak prawdziwy,",
    "h_title_2": "każdego dnia.",
    "h_lead": "Chleby na zakwasie, maślane wypieki i ciasta formowane na miejscu. "
              "Piekarnia zakorzeniona w regionie Var, oddana lokalnym dostawcom i zero waste.",
    "h_cta1": "Poznaj nasze produkty",
    "h_cta2": "Godziny &amp; dojazd",
    "h_img_hero": "Poranna witryna — chleby na zakwasie",

    "mq_home": ["Naturalny zakwas", "Francuskie mąki", "Pieczone na miejscu",
                "Lokalne produkty", "Zero waste", "Montferrat &amp; Figanières"],

    "h_s1_eyebrow": "01 — Wybór",
    "h_s1_title": "Chleby z charakterem",
    "h_s1_lead": "Ciasta fermentowane powoli, formowane ręcznie i wypiekane każdego ranka. "
                 "Resztę robi czas.",
    "h_c1_t": "Wielki Zakwas", "h_c1_n": "36 H",
    "h_c1_d": "Gruba skórka, otwarty miękisz, długa fermentacja na naturalnym zakwasie.",
    "h_c2_t": "Tradycja", "h_c2_n": "24 H",
    "h_c2_d": "Wyselekcjonowana francuska mąka, powolna fermentacja, ręczne formowanie.",
    "h_c3_t": "Wypieki maślane", "h_c3_n": "07 H",
    "h_c3_d": "Czyste masło, ciasto laminowane i pieczone na miejscu, prosto z porannego pieca.",
    "h_all": "Zobacz pełną ofertę",
    "h_tag_sig": "Sygnaturowy", "h_tag_morning": "Rano",
    "h_img_levain": "Krojony chleb na zakwasie z otwartym miękiszem",
    "h_img_trad": "Francuskie bagietki tradycyjne",
    "h_img_croissants": "Maślane rogaliki",

    "h_q_eyebrow": "Nasza filozofia",
    "h_quote": "Nic się nie spieszy. Dobry chleb wymaga czasu, cierpliwości i ręki rzemieślnika.",
    "h_q_by": "CD Boulangerie — Montferrat",
    "h_img_fournil": "Piekarnia o piątej nad ranem",
    "h_st1": "Fermentacji", "h_st2": "Piekarnie",
    "h_st3": "Języki strony", "h_st4": "Robione na miejscu",

    "h_s2_eyebrow": "02 — Nasze rzemiosło",
    "h_s2_title_1": "Rzemieślnicy,", "h_s2_title_2": "nie fabryka",
    "h_s2_text": "Wszystko powstaje w naszej piekarni: wyrabianie, fermentacja, formowanie, wypiek. "
                 "Wybieramy francuskie mąki i współpracujemy z producentami z regionu Var.",
    "h_s2_link": "Nasza historia",
    "h_img_faconnage": "Ręczne formowanie chleba",

    "h_s3_eyebrow": "03 — Nasze adresy",
    "h_s3_title_1": "Dwie wsie,", "h_s3_title_2": "jedna piekarnia",
    "h_s3_text": "Znajdziesz nas w Montferrat i Figanières, od wtorku do niedzieli. "
                 "Zamówienia specjalne i torty na rezerwację.",
    "h_s3_link": "Godziny &amp; dojazd",
    "h_img_devanture": "Witryna piekarni w Montferrat",

    "h_s4_eyebrow": "04 — Zobowiązania",
    "h_s4_title": "Konkretne działania",
    "h_e1_t": "Too Good To Go",
    "h_e1_d": "Paczki w obniżonej cenie pod koniec dnia, by walczyć z marnowaniem żywności.",
    "h_e2_t": "Piwo z chleba",
    "h_e2_d": "Wczorajszy chleb trafia do warzenia piwa, a nie do kosza. Nic się nie marnuje.",
    "h_e3_t": "Dostawy lokalne",
    "h_e3_d": "Dla stowarzyszeń i osób o ograniczonej mobilności, na określonych warunkach. Zapytaj nas.",

    "p_eyebrow": "Oferta",
    "p_title_1": "Chleby, wypieki maślane", "p_title_2": "&amp; ciasta",
    "p_lead": "Najpierw chleb — to nasz zawód. Reszta podąża za sezonem i rytmem piekarni.",
    "mq_prod": ["Pieczone dziś rano", "Naturalny zakwas", "Czyste masło",
                "Domowe", "Francuskie mąki"],

    "p_s1_eyebrow": "01 — Chleby",
    "p_s1_title": "Piekarnia",
    "p_rows": [
        ("Wielki Zakwas", "Fermentacja 36 h, gruba skórka, otwarty miękisz.", "Sygnaturowy"),
        ("Tradycja", "Francuska mąka, powolna fermentacja, ręczne formowanie.", "Codziennie"),
        ("Chleb wiejski", "Pszenica i żyto, zwarty miękisz, długa świeżość.", "Codziennie"),
        ("Zboża &amp; ziarna", "Słonecznik, len, sezam, mak.", "Codziennie"),
        ("Chleb pełnoziarnisty", "Mąka T110, bogata w błonnik.", "Na zamówienie"),
        ("Fougasse prowansalska", "Oliwa z oliwek, zioła z Var, oliwki.", "Zależnie od pieca"),
    ],

    "p_s2_eyebrow": "02 — Reszta oferty",
    "p_s2_title": "Codziennie na ladzie",
    "p_cat1_t": "Wypieki maślane",
    "p_cat1_d": "Rogaliki, pains au chocolat, ciastka z jabłkiem, brioche. "
                "Czyste masło, laminowane i pieczone na miejscu.",
    "p_cat2_t": "Ciasta",
    "p_cat2_d": "Sezonowe tarty, eklery, entremets. Torty urodzinowe i okolicznościowe na zamówienie.",
    "p_cat3_t": "Przekąski &amp; burgery",
    "p_cat3_d": "Kanapki na naszym chlebie, quiche, pizze i domowe burgery w porze lunchu.",
    "p_cat4_t": "Produkty lokalne",
    "p_cat4_d": "Miód, dżemy, oliwa i wyroby producentów z Var, starannie przez nas wybrane.",
    "p_img_vienn": "Taca wypieków maślanych",
    "p_img_patis": "Witryna z ciastami i tartami",
    "p_img_snack": "Rzemieślnicza kanapka na domowym chlebie",
    "p_img_local": "Miód i produkty lokalne z Var",

    "p_s3_eyebrow": "03 — Galeria",
    "p_s3_title": "W obrazach",
    "p_s3_lead": "Kliknij zdjęcie, aby je powiększyć.",
    "p_f_all": "Wszystko", "p_f_breads": "Chleby", "p_f_vienn": "Wypieki maślane",
    "p_f_patis": "Ciasta", "p_f_snack": "Przekąski", "p_f_local": "Produkty lokalne",
    "p_zoom": "Powiększ",
    "p_gal": ["Chleb na zakwasie", "Tradycja francuska", "Chleb wiejski",
              "Maślany rogalik", "Pain au chocolat", "Ciastko z jabłkiem",
              "Tarta owocowa", "Ekler", "Tort okolicznościowy",
              "Kanapka dnia", "Domowy burger", "Miód &amp; produkty z Var"],

    "p_cta_title": "Zamówienie specjalne?",
    "p_cta_lead": "Torty urodzinowe, bufety, imprezy, chleb w dużych ilościach. "
                  "Prosimy o zgłoszenie 48 h wcześniej.",
    "p_cta_btn": "Skontaktuj się",

    "m_eyebrow": "Nasze rzemiosło",
    "m_title_1": "Czas", "m_title_2": "jako składnik",
    "m_lead": "Rzemiosło to nie hasło reklamowe. To nasza codzienność: gesty, godziny "
              "i wymagania, które nie podlegają negocjacji.",
    "m_img_fournil": "Piekarnia o świcie",
    "mq_maison": ["36 godzin fermentacji", "Naturalny zakwas", "Formowane ręcznie",
                  "Pieczone na miejscu", "Francuskie mąki"],

    "m_s1_eyebrow": "01 — Gest",
    "m_s1_title": "Od ziarna do lady",
    "m_rows": [
        ("Selekcja", "Francuskie mąki od zaprzyjaźnionych młynarzy, lokalne produkty z Var.", "Początek"),
        ("Zakwas", "Naturalny zakwas dokarmiany każdego dnia, nigdy zastępowany skrótem.", "Żywy"),
        ("Fermentacja", "Długie leżakowanie, do 36 godzin. Tam buduje się smak.", "36 godzin"),
        ("Formowanie", "Ręcznie, sztuka po sztuce, bez maszyny formującej.", "Ręcznie"),
        ("Wypiek", "Na miejscu, każdego ranka, w kilku partiach — chleb zawsze świeży.", "Na miejscu"),
    ],

    "m_s2_eyebrow": "02 — Nasze zobowiązanie",
    "m_s2_title_1": "Lokalnie,", "m_s2_title_2": "naprawdę",
    "m_s2_text": "Współpracujemy z urzędami, szkołami, żłobkami i domem opieki w naszych wsiach. "
                 "Nasze produkty uzupełniające pochodzą od producentów z Var, nie z centrali zakupowej.",
    "m_img_petrissage": "Wyrabianie ciasta",
    "m_a1_t": "Zero waste",
    "m_a1_d": "Paczki Too Good To Go pod koniec dnia, wczorajszy chleb wykorzystany do warzenia "
              "piwa, darowizny dla lokalnych stowarzyszeń.",
    "m_a2_t": "Krótkie łańcuchy dostaw",
    "m_a2_d": "Miód, dżemy i oliwa od producentów z Var. Wybieramy dostawców oddalonych "
              "o mniej niż pięćdziesiąt kilometrów.",
    "m_a3_t": "Usługi sąsiedzkie",
    "m_a3_d": "Dostawy dla stowarzyszeń i osób o ograniczonej mobilności, na określonych warunkach. "
              "Wkrótce planowany punkt odbioru UPS.",

    "m_s3_eyebrow": "03 — Zaufanie",
    "m_s3_title": "Oni z nami pracują",
    "m_s3_lead": "Samorządy, szkoły, placówki opiekuńcze i profesjonaliści z branży gastronomicznej.",
    "m_partners": ["Urząd w Montferrat", "Urząd w Figanières", "Urząd w Châteaudouble",
                   "Dom opieki Figanières", "Żłobek Figanières", "Żłobek Montferrat",
                   "Szkoła w Montferrat", "Restauracja La Bastide", "Lokalne stowarzyszenia",
                   "Producenci z Var", "Too Good To Go", "Zaprzyjaźnieni piwowarzy"],
    "m_quote": "Uczciwy chleb, każdego dnia, dla ludzi stąd.",

    "b_eyebrow": "Nasze adresy",
    "b_title_1": "Dwie wsie,", "b_title_2": "jedna piekarnia",
    "b_lead": "Znajdź CD Boulangerie w Montferrat i Figanières, w sercu regionu Var.",
    "b_badge": "Piekarnia",
    "b_addr": "Adres", "b_tue_sat": "Wt — Sob", "b_sun": "Niedziela",
    "b_mon": "Poniedziałek", "b_closed": "Zamknięte", "b_phone": "Telefon",
    "b_route": "Dojazd", "b_contact": "Kontakt",
    "b_note": "Godziny mogą się różnić w dni świąteczne. W razie wątpliwości zadzwoń: ",
    "b_img_1": "Piekarnia w Montferrat", "b_img_2": "Piekarnia w Figanières",
    "mq_boul": ["Otwarte od wtorku do niedzieli", "Pieczone na miejscu",
                "Zamówienia 48 h wcześniej"],
    "b_s2_eyebrow": "Warto wiedzieć",
    "b_s2_title": "Zanim przyjdziesz",
    "b_k1_t": "Prosto z pieca",
    "b_k1_d": "Pierwsza partia o 7:00, druga późnym popołudniem. "
              "W weekendy wypieki maślane znikają szybko.",
    "b_k2_t": "Zamówienia",
    "b_k2_d": "Torty, bufety i duże ilości: prosimy o telefon 48 h wcześniej.",
    "b_k3_t": "Paczki anti-waste",
    "b_k3_d": "Dostępne pod koniec dnia przez Too Good To Go, w zależności od tego, co zostało.",

    "c_eyebrow": "Kontakt",
    "c_title_1": "Porozmawiajmy o", "c_title_2": "Twoim zamówieniu",
    "c_lead": "Pytanie, tort na miarę, impreza do zorganizowania? "
              "Napisz do nas albo zadzwoń bezpośrednio do piekarni.",
    "mq_contact": ["Zamówienia 48 h wcześniej", "Torty na miarę",
                   "Bufety &amp; imprezy", "Montferrat &amp; Figanières"],
    "c_form": "Formularz",
    "c_name": "Twoje imię i nazwisko *", "c_name_ph": "Imię i nazwisko",
    "c_tel": "Telefon", "c_tel_ph": "+33 6 00 00 00 00",
    "c_msg": "Twoja wiadomość *",
    "c_msg_ph": "Opisz swoje życzenie, wybraną datę i liczbę osób.",
    "c_send": "Wyślij wiadomość",
    "c_note": "Formularz otwiera Twój program pocztowy z gotową wiadomością. "
              "Aby uzyskać natychmiastową odpowiedź, zadzwoń do nas.",
    "c_err": "Prosimy podać imię i wiadomość.",
    "c_opening": "Otwieranie programu pocztowego…",
    "c_subject": "Zapytanie od",
    "c_direct": "Bezpośrednio",
    "c_qa_phone": "Telefon", "c_qa_mail": "E-mail",
    "c_qa_fb": "Facebook", "c_qa_ig": "Instagram", "c_qa_route": "Dojazd",
    "c_qa_wa": "WhatsApp", "wa_msg": "Dzień dobry, piszę do Państwa ze strony internetowej.",
    "c_hours": "Godziny otwarcia",
    "c_faq_eyebrow": "Częste pytania",
    "c_faq_title": "Być może zastanawiasz się…",
    "c_faq": [
        ("Z jakim wyprzedzeniem zamówić tort?",
         "Na klasyczny tort urodzinowy potrzebujemy 48 godzin, a na tort piętrowy lub zamówienie "
         "dla ponad dwudziestu osób — tygodnia."),
        ("Czy dowozicie?",
         "Dowozimy do stowarzyszeń i osób o ograniczonej mobilności w Montferrat i Figanières, "
         "na określonych warunkach. Zadzwoń, aby to omówić."),
        ("Czy macie produkty bezglutenowe?",
         "W naszej piekarni stale pracujemy z mąką pszenną, więc nie możemy zagwarantować braku "
         "śladowych ilości. Chętnie doradzimy alternatywy."),
        ("Czy współpracujecie z firmami?",
         "Tak: restauracje, samorządy, szkoły, żłobki i domy opieki. Skontaktuj się z nami, "
         "przygotujemy wycenę dopasowaną do Twojej skali."),
    ],


    # --- événements ---------------------------------------------------------
    "nav_events": "Wydarzenia",
    "e_eyebrow": "Życie wsi",
    "e_title_1": "Nasze spotkania,", "e_title_2": "przez cały rok",
    "e_lead": "Święta wsi, dni wolne, jarmarki bożonarodzeniowe — jesteśmy przy każdej "
              "okazji. Specjalny wypiek, stoisko, pomocna dłoń: piekarnia jest częścią "
              "życia tego miejsca.",
    "e_img_hero": "Stoisko piekarni na święcie wsi",
    "mq_events": ["Święta wsi", "Dni świąteczne", "Jarmarki bożonarodzeniowe",
                  "Zamówienia specjalne", "Obserwuj nas na Facebooku"],

    "e_s1_eyebrow": "01 — Kalendarz",
    "e_s1_title": "Co nas zajmuje",
    "e_s1_lead": "Dokładne daty zmieniają się co roku. Najpewniej jest śledzić nas na "
                 "Facebooku: tam ogłaszamy wszystko w pierwszej kolejności.",
    "e_rows": [
        ("Trzech Króli", "Ciasta królewskie z frangipane i jabłkiem, przez cały styczeń.", "Styczeń"),
        ("Matki Boskiej Gromnicznej", "Naleśniki i pączki przygotowywane tego samego dnia.", "Luty"),
        ("Wielkanoc", "Czekoladki, wielkanocne brioche i baranki na zamówienie.", "Kwiecień"),
        ("Święto wsi", "Nasze stoisko na placu: fougasse, pizza i chleb pieczony na miejscu.", "Lato"),
        ("Targi wieczorne", "Obecni na letnich targach w Montferrat i Figanières.", "Lipiec — Sierpień"),
        ("Jarmark świąteczny", "Bûche, pierniki i czekoladki. Zamówienia z wyprzedzeniem.", "Grudzień"),
    ],

    "e_s2_eyebrow": "02 — Na życzenie",
    "e_s2_title_1": "Twoje wydarzenia,", "e_s2_title_2": "jesteśmy z Tobą",
    "e_s2_text": "Wesele, chrzciny, komunia, kolacja stowarzyszenia albo pożegnanie: "
                 "przygotowujemy bufety słodkie i słone, torty piętrowe oraz chleb w "
                 "dużych ilościach. Prosimy o zgłoszenie na tydzień lub dwa wcześniej.",
    "e_img_buffet": "Bufet przygotowany na wydarzenie",
    "e_c1_t": "Uroczystości rodzinne",
    "e_c1_d": "Torty piętrowe, torty na zamówienie, bufety słodko-słone na wielkie okazje.",
    "e_c2_t": "Stowarzyszenia i szkoły",
    "e_c2_d": "Poczęstunki, wypieki maślane w większych ilościach i chleb na lokalne imprezy.",
    "e_c3_t": "Firmy",
    "e_c3_d": "Śniadania firmowe, seminaria, otwarcia. Szybka wycena.",

    "e_s3_eyebrow": "03 — Nic nie przegap",
    "e_s3_title": "Obserwuj nas na Facebooku",
    "e_s3_text": "Ogłaszamy każde wydarzenie, każdy specjalny wypiek i każdą nowość w "
                 "naszych mediach społecznościowych. To najprostszy sposób, by być na bieżąco.",
    "e_cta_fb": "Zobacz naszą stronę na Facebooku",
    "e_cta_ig": "Obserwuj nas na Instagramie",
    "e_cta_wa": "Napisz na WhatsAppie",
    "e_note": "Masz pomysł na wydarzenie? Zadzwoń, porozmawiajmy.",


    # --- Strony prawne ------------------------------------------------------
    "nav_legal": "Nota prawna",
    "nav_cgv": "Regulamin",
    "nav_privacy": "Prywatność",

    "lg_eyebrow": "Informacje prawne",
    "lg_title_1": "Nota",
    "lg_title_2": "prawna",
    "lg_lead": "Informacje o wydawcy strony, jej dostawcy hostingu i obowiązujących prawach.",
    "lg_updated": "Ostatnia aktualizacja",

    "lg_s1_t": "Wydawca strony",
    "lg_s1_b": [
        ("Nazwa firmy", "CD Boulangerie"),
        ("Forma prawna", "Uproszczona spółka akcyjna (SAS)"),
        ("Kapitał zakładowy", "[DO UZUPEŁNIENIA] €"),
        ("Siedziba", "6 Rue du Dr Rayol, 83131 Montferrat, Francja"),
        ("Rejestracja", "Rejestr handlowy Draguignan — SIREN 918 964 834"),
        ("Numer VAT UE", "[DO UZUPEŁNIENIA]"),
        ("Telefon", "+33 9 78 80 63 06"),
        ("Dyrektor publikacji", "[DO POTWIERDZENIA]"),
    ],
    "lg_s2_t": "Hosting",
    "lg_s2_b": [
        ("Dostawca hostingu", "[NAZWA DOSTAWCY]"),
        ("Adres", "[PEŁNY ADRES]"),
        ("Telefon", "[TELEFON]"),
    ],
    "lg_s3_t": "Własność intelektualna",
    "lg_s3_p": "Cała ta strona — struktura, teksty, zdjęcia, logo i elementy graficzne — jest chroniona prawem autorskim. Wszelkie powielanie, przedstawianie lub adaptacja, w całości lub w części, bez uprzedniej pisemnej zgody jest zabronione.\n\nPrezentowane zdjęcia są własnością CD Boulangerie. Logotypy partnerów i herby gmin pozostają własnością ich właścicieli i są prezentowane za ich zgodą.",
    "lg_s4_t": "Odpowiedzialność",
    "lg_s4_p": "Informacje publikowane na tej stronie (produkty, godziny otwarcia, ceny, wydarzenia) mają charakter orientacyjny i mogą ulec zmianie. Godziny mogą się różnić w dni świąteczne i podczas urlopów. W razie wątpliwości prosimy o telefon przed przyjazdem.\n\nCD Boulangerie nie ponosi odpowiedzialności za szkody wynikające z przerwy w działaniu serwisu lub obecności wirusa komputerowego.",
    "lg_s5_t": "Linki do innych stron",
    "lg_s5_p": "Ta strona zawiera linki do serwisów zewnętrznych (Facebook, Instagram, WhatsApp, Mapy Google). CD Boulangerie nie sprawuje nad nimi kontroli i nie ponosi odpowiedzialności za ich treść.",
    "lg_s6_t": "Prawo właściwe",
    "lg_s6_p": "Niniejsza strona podlega prawu francuskiemu. Wszelkie spory podlegają jurysdykcji sądów w Draguignan.",
    "lg_s7_t": "Kontakt",
    "lg_s7_p": "W sprawie tej noty prawnej można się z nami skontaktować telefonicznie, mailowo lub bezpośrednio w piekarni.",

    # --- Regulamin ----------------------------------------------------------
    "cg_eyebrow": "Nasze zasady",
    "cg_title_1": "Regulamin",
    "cg_title_2": "sprzedaży",
    "cg_lead": "Zasady dotyczące sprzedaży w piekarni i zamówień na miarę. Nic skomplikowanego: to po prostu nasze zwyczaje pracy, spisane na papierze.",
    "cg_intro_t": "W skrócie",
    "cg_intro_p": "CD Boulangerie to piekarnia rzemieślnicza. Sprzedajemy nasze produkty bezpośrednio w piekarniach w Montferrat i Figanières. Ta strona jest wizytówką: nie umożliwia płatności online. Zamówienia składa się telefonicznie, wiadomością lub na miejscu.",

    "cg_s1_t": "1. Zakres stosowania",
    "cg_s1_p": "Niniejszy regulamin dotyczy wszystkich sprzedaży realizowanych w naszych piekarniach oraz zamówień składanych telefonicznie, mailowo, przez WhatsApp lub na miejscu. Złożenie zamówienia oznacza akceptację regulaminu.",
    "cg_s2_t": "2. Nasze produkty",
    "cg_s2_p": "Nasze produkty powstają ręcznie, każdego dnia, w naszej piekarni. To produkty żywe: wygląd, waga i kolor mogą się nieznacznie różnić między wypiekami. To znak pracy ręcznej, a nie wada.\n\nDostępność zależy od dziennej produkcji. Niektóre produkty oferujemy sezonowo lub wyłącznie na zamówienie.",
    "cg_s3_t": "3. Alergeny",
    "cg_s3_p": "Nasze produkty przygotowywane są w piekarni, gdzie używa się między innymi: glutenu, jaj, mleka, orzechów, soi i sezamu. Mimo naszej staranności nie możemy zagwarantować całkowitego braku śladów.\n\nJeśli masz alergię, poinformuj nas przed złożeniem zamówienia: podamy dokładny skład każdego produktu.",
    "cg_s4_t": "4. Ceny",
    "cg_s4_p": "Ceny są podane w piekarni, w euro, z wszystkimi podatkami. Mogą ulec zmianie w każdej chwili, zwłaszcza w zależności od cen surowców. Obowiązuje cena widoczna w momencie składania zamówienia.\n\nDla zamówień na miarę przygotowujemy wycenę przed potwierdzeniem.",
    "cg_s5_t": "5. Zamówienia na miarę",
    "cg_s5_p": "Wykonujemy torty piętrowe, torty personalizowane, bufety i zamówienia hurtowe dla osób prywatnych, stowarzyszeń i firm.",
    "cg_s5_b": [
        ("Czas realizacji", "Minimum 48 godzin na klasyczny tort, tydzień na tort piętrowy lub bufet."),
        ("Potwierdzenie", "Zamówienie jest wiążące dopiero po naszym wyraźnym potwierdzeniu, telefonicznie lub pisemnie."),
        ("Zaliczka", "Przy dużych zamówieniach możemy poprosić o zaliczkę. Jest ona odliczana od kwoty końcowej."),
        ("Odbiór", "Zamówienia odbiera się w piekarni, w ustalonym dniu i o ustalonej godzinie."),
    ],
    "cg_s6_t": "6. Anulowanie",
    "cg_s6_p": "Zamówienie można anulować bezpłatnie do 48 godzin przed datą odbioru. Po tym terminie, gdy produkcja już się rozpoczęła, wpłacona zaliczka nie podlega zwrotowi.\n\nJeśli to my musimy anulować — awaria, siła wyższa, brak surowca — informujemy jak najszybciej i zwracamy całość wpłaty.",
    "cg_s7_t": "7. Płatność",
    "cg_s7_p": "Płatność następuje w piekarni, przy odbiorze: gotówka, karta lub inny sposób akceptowany w kasie. Przez tę stronę nie pobieramy żadnych płatności.",
    "cg_s8_t": "8. Odbiór i przechowywanie",
    "cg_s8_p": "Nasze produkty są świeże i bez konserwantów. Należy je szybko spożyć: tego samego dnia w przypadku wypieków maślanych i ciast, w ciągu dwóch–trzech dni w przypadku chlebów na zakwasie.\n\nOd momentu odbioru za właściwe przechowywanie odpowiada klient. Produkty na bazie śmietany należy przechowywać w chłodzie.",
    "cg_s9_t": "9. Prawo odstąpienia",
    "cg_s9_p": "Zgodnie z artykułem L221-28 francuskiego kodeksu konsumenckiego prawo odstąpienia nie ma zastosowania do łatwo psujących się artykułów spożywczych ani do produktów wykonanych według specyfikacji konsumenta.",
    "cg_s10_t": "10. Reklamacje",
    "cg_s10_p": "Masz uwagę albo problem z zamówieniem? Powiedz nam tego samego dnia, w piekarni lub telefonicznie. Znajdziemy rozwiązanie: to prostsze i szybsze niż jakakolwiek formalna procedura.",
    "cg_s11_t": "11. Mediacja",
    "cg_s11_p": "W przypadku sporu nierozwiązanego polubownie konsument może bezpłatnie zwrócić się do mediatora konsumenckiego. Dane właściwego mediatora są dostępne na życzenie w piekarni.",
    "cg_s12_t": "12. Prawo właściwe",
    "cg_s12_p": "Niniejszy regulamin podlega prawu francuskiemu. W przypadku sporu wyłącznie właściwe są sądy w Draguignan.",

    # --- Prywatność ---------------------------------------------------------
    "pv_eyebrow": "Twoje dane",
    "pv_title_1": "Polityka",
    "pv_title_2": "prywatności",
    "pv_lead": "Co robimy — a przede wszystkim czego nie robimy — z Twoimi danymi osobowymi.",
    "pv_hl_t": "Najważniejsze w jednym zdaniu",
    "pv_hl_p": "Ta strona nie zapisuje żadnych plików cookie, nie korzysta z narzędzi analitycznych i nikomu nie przekazuje Twoich danych. Jedyne informacje, jakie otrzymujemy, to te, które sam nam wysyłasz.",
    "pv_s1_t": "Kto przetwarza Twoje dane",
    "pv_s1_p": "CD Boulangerie, 6 Rue du Dr Rayol, 83131 Montferrat, Francja, jest administratorem danych zbieranych na tej stronie.",
    "pv_s2_t": "Jakie dane i po co",
    "pv_s2_b": [
        ("Formularz kontaktowy", "Imię i nazwisko, telefon oraz treść wiadomości. Wyłącznie po to, by odpowiedzieć na Twoje zapytanie."),
        ("Telefon lub WhatsApp", "Twój numer jest widoczny, jak przy każdym połączeniu. Nie przechowujemy go dłużej niż to konieczne."),
        ("Przeglądanie", "Nie zbieramy żadnych danych. Bez cookies, bez statystyk, bez trackerów."),
    ],
    "pv_s3_t": "Brak plików cookie",
    "pv_s3_p": "Ta strona nie zapisuje żadnych plików cookie na Twoim urządzeniu. Dlatego nie wyświetlamy banera zgody: nie ma czego akceptować.\n\nKroje pisma są hostowane na naszym własnym serwerze: Twój adres IP nie jest przekazywany żadnej usłudze zewnętrznej podczas wyświetlania stron.",
    "pv_s4_t": "Usługi zewnętrzne",
    "pv_s4_p": "Przyciski Facebook, Instagram, WhatsApp i Mapy Google to zwykłe linki. Żadna treść z tych usług nie jest ładowana, dopóki nie klikniesz. Po kliknięciu opuszczasz naszą stronę i obowiązują zasady prywatności tych serwisów.",
    "pv_s5_t": "Okres przechowywania",
    "pv_s5_p": "Otrzymane wiadomości przechowujemy tak długo, jak to potrzebne do obsługi zapytania, a następnie maksymalnie przez trzy lata w celach handlowych. Dane związane z zamówieniem przechowujemy dziesięć lat, zgodnie z przepisami księgowymi.",
    "pv_s6_t": "Twoje prawa",
    "pv_s6_p": "Masz prawo dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania oraz sprzeciwu. Aby z niego skorzystać, napisz do nas lub przyjdź do piekarni: odpowiadamy w ciągu miesiąca.\n\nJeśli odpowiedź Cię nie zadowoli, możesz zwrócić się do francuskiego organu ochrony danych CNIL (cnil.fr).",
    "pv_s7_t": "Bezpieczeństwo",
    "pv_s7_p": "Strona działa w protokole HTTPS. Wiadomości, które nam wysyłasz, trafiają do naszej firmowej skrzynki e-mail, do której dostęp ma wyłącznie kierownictwo.",

    "meta": {
        "mentions": ("Nota prawna — CD Boulangerie",
                     "Informacje prawne CD Boulangerie: wydawca, hosting, własność intelektualna i prawo właściwe."),
        "cgv": ("Regulamin — CD Boulangerie",
                "Nasz regulamin sprzedaży: zamówienia na miarę, alergeny, terminy, anulowanie i płatność."),
        "confidentialite": ("Polityka prywatności — CD Boulangerie",
                            "Bez cookies, bez trackerów. Co robimy z Twoimi danymi i jak korzystać ze swoich praw."),
        "index": ("CD Boulangerie — Piekarnia rzemieślnicza w Montferrat &amp; Figanières",
                  "Piekarnia rzemieślnicza w regionie Var we Francji: chleby na zakwasie, maślane "
                  "wypieki i ciasta robione na miejscu. Montferrat i Figanières."),
        "produits": ("Nasze produkty — CD Boulangerie",
                     "Chleby na zakwasie, maślane wypieki, ciasta, przekąski i produkty lokalne z Var."),
        "maison": ("Nasze rzemiosło — CD Boulangerie",
                   "Nasze know-how: naturalny zakwas, długa fermentacja, ręczne formowanie "
                   "i lokalne zaangażowanie."),
        "boulangeries": ("Nasze piekarnie — CD Boulangerie",
                         "Godziny otwarcia, adresy i dojazd do naszych piekarni w Montferrat "
                         "i Figanières."),
        "contact": ("Kontakt — CD Boulangerie",
                    "Skontaktuj się z CD Boulangerie w sprawie zamówień, tortów na miarę i imprez."),
        "evenements": ("Wydarzenia — CD Boulangerie",
                       "Święta wsi, dni świąteczne, jarmarki bożonarodzeniowe i bufety na zamówienie. Obserwuj CD Boulangerie, by nic nie przegapić."),
    },
}


def check():
    """Vérifie que les 3 langues ont exactement les mêmes clés."""
    ref = set(T["fr"].keys())
    problems = []
    for code in ("en", "pl"):
        missing = ref - set(T[code].keys())
        extra = set(T[code].keys()) - ref
        if missing:
            problems.append(f"{code}: clés manquantes {sorted(missing)}")
        if extra:
            problems.append(f"{code}: clés en trop {sorted(extra)}")
    for key in ("p_rows", "m_rows", "p_gal", "m_partners", "c_faq",
                "load_steps", "mq_home", "mq_prod", "mq_maison", "mq_boul", "mq_contact"):
        n = len(T["fr"][key])
        for code in ("en", "pl"):
            if len(T[code][key]) != n:
                problems.append(f"{code}.{key}: {len(T[code][key])} éléments au lieu de {n}")
    return problems


if __name__ == "__main__":
    p = check()
    print("\n".join(p) if p else "✓ Les 3 langues sont cohérentes.")
