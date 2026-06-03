# theme_aws

Module Odoo 15 qui ajoute au site web une section dynamique présentant un catalogue de services AWS, alimentée depuis le back-office.

## Description

`theme_aws` est un module pour la plateforme Odoo 15 (partie Website). Il permet de gérer une liste de services Amazon Web Services dans l'interface d'administration, puis de les afficher sur le site public via un bloc (snippet) réutilisable dans l'éditeur de pages.

Le contenu n'est pas codé en dur dans la page : les services sont stockés en base, exposés par une route HTTP au format JSON, et injectés côté navigateur par un widget JavaScript. Ajouter ou modifier un service dans le back-office se répercute donc directement sur le site, sans toucher au code.

Le module personnalise également l'en-tête et le pied de page du site, et fournit une traduction française (fr_BE).

## Fonctionnalités principales

- Modèle de données `aws.services` pour décrire un service : nom, identifiant de service, catégorie, description et image.
- Catégories prédéfinies pour classer les services : Storage, Serverless, Compute, ML ou AI (champ de type sélection).
- Vues back-office (liste et formulaire) et menu dédié sous la configuration du site web, pour la saisie et la gestion des services.
- Route HTTP publique `/services/` (type JSON, méthode POST) qui renvoie le nom, l'image et la catégorie de chaque service enregistré.
- Snippet de site web "AWS services - Dynamic" disponible dans l'éditeur, qui affiche les services sous forme de cartes (image, nom, catégorie).
- Widget JavaScript public (`publicWidget`) qui interroge la route `/services/` via RPC et construit le rendu côté client.
- En-tête et pied de page personnalisés, surchargeant le gabarit `website.layout`.
- Règle d'accès (`ir.model.access.csv`) pour le modèle `aws.services`.
- Traduction française des libellés (`i18n/fr_BE.po`).

## Pile technique

- Odoo 15 (framework web et ORM Python)
- Python pour les modèles et le contrôleur HTTP
- XML pour les vues, gabarits QWeb et définitions de snippet
- JavaScript (module `web.public.widget` d'Odoo) pour le rendu dynamique côté client
- Bootstrap (classes de mise en page fournies par le thème Odoo)
- Dépendances Odoo : modules `website` et `web`

## Prérequis

- Une instance Odoo 15 fonctionnelle, avec le module `website` installé
- Python 3 (fourni avec Odoo)

## Installation

1. Copier le dossier `aws` dans un répertoire d'addons reconnu par votre instance Odoo (par exemple le dossier référencé dans `addons_path`).

2. Redémarrer le serveur Odoo en mettant à jour la liste des applications :

   ```bash
   ./odoo-bin -c odoo.conf -u all -d <nom_de_la_base>
   ```

   ou, depuis l'interface, activer le mode développeur puis cliquer sur "Mettre à jour la liste des applications".

3. Dans le menu Applications, rechercher "theme_aws" et l'installer.

4. Renseigner les services : menu **Site Web > Configuration > AWS services > services**, puis ajouter un ou plusieurs enregistrements (nom, identifiant, catégorie, description, image).

5. Éditer une page du site, ouvrir le panneau des blocs, et glisser le snippet **AWS services - Dynamic** à l'endroit voulu. Les services saisis s'affichent automatiquement.

## Structure du projet

```
aws/
├── __manifest__.py              # Declaration du module (dependances, donnees, assets)
├── __init__.py                  # Importe models et controllers
├── models/
│   ├── __init__.py
│   └── services.py              # Modele aws.services
├── controllers/
│   ├── __init__.py
│   └── explore_services.py      # Route JSON /services/
├── views/
│   ├── aws_services.xml         # Vues liste/formulaire, action et menus back-office
│   ├── header.xml               # En-tete personnalise (surcharge website.layout)
│   ├── footer.xml               # Pied de page personnalise (surcharge website.layout)
│   └── snippets/
│       ├── snippets.xml         # Enregistrement du snippet dans l'editeur
│       └── explore-services.xml # Gabarit QWeb du snippet
├── static/
│   └── src/
│       ├── js/
│       │   └── explore-services.js   # Widget public qui rend les services
│       └── img/
│           └── snippets/
│               └── city1.png         # Vignette du snippet
├── security/
│   └── ir.model.access.csv      # Droits d'acces sur aws.services
└── i18n/
    └── fr_BE.po                 # Traduction francaise
```

## Modèle de données

Modèle `aws.services` :

| Champ                 | Type      | Description                                                        |
|-----------------------|-----------|-------------------------------------------------------------------|
| `name`                | Char      | Nom du service (obligatoire)                                       |
| `service_id`          | Char      | Identifiant du service (obligatoire)                              |
| `description`         | Selection | Catégorie : Storage, Serverless, Compute, ML ou AI (obligatoire)  |
| `description_service` | Text      | Texte libre de description                                         |
| `image`               | Binary    | Image du service (obligatoire)                                     |

## API HTTP

- `POST /services/` (type JSON, accès public) : renvoie la liste des services enregistrés, avec les champs `name`, `image` et `description`. Cette route est consommée par le widget JavaScript du snippet.

## Remarques

- Les gabarits d'en-tête et de pied de page référencent un logo situé à `/theme_yourhome/static/src/img/logo.png`, chemin qui n'est pas fourni par ce module. Adapter ce chemin vers une image de votre choix (par exemple un fichier placé sous `aws/static/src/img/`) pour afficher correctement le logo.
- Certains libellés du pied de page et du snippet sont des textes de remplissage (placeholders) à personnaliser selon le contenu réel du site.
