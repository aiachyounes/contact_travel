# contact_travel
J'ai eu l'occasion de créer un module Odoo "Contact Travel" pour gérer les voyages. Voici comment cela s'est passé :

Tout d'abord, j'ai veillé à avoir Odoo correctement installé et configuré sur mon serveur. C'était une étape essentielle pour démarrer ce projet.

Ensuite, j'ai structuré mon dossier de module "Contact Travel". J'ai créé un dossier principal, auquel j'ai ajouté un fichier "init.py", un sous-dossier "models" pour mes modèles, un autre sous-dossier "views" pour mes vues, et j'ai pensé à inclure un dossier "security" pour gérer les autorisations.

Dans le dossier "security", j'ai créé des fichiers XML pour établir les règles de sécurité de mon module. Ces règles étaient cruciales pour restreindre l'accès à certaines fonctionnalités en fonction des groupes d'utilisateurs.

Ensuite, j'ai défini les détails de base de mon module, comme son nom, sa version, et l'auteur, dans un fichier "manifest.py" situé dans le dossier de mon module. C'était une manière de présenter mon module aux utilisateurs.

Pour stocker les informations sur les voyages, j'ai développé un modèle appelé "Voyage". J'ai créé des champs tels que le nom du voyage, une description, et d'autres champs selon les besoins spécifiques du projet.

Pour afficher les informations sur les voyages, j'ai conçu une vue en utilisant un fichier XML que j'ai placé dans le dossier "views". Cette vue a été cruciale pour définir comment les détails des voyages seraient affichés dans l'interface d'Odoo.

Une fois mon module prêt, je suis allé dans Odoo, j'ai recherché mon module dans la section "Paramètres techniques" > "Modules" > "Modules" et je l'ai installé. Ensuite, j'ai mis à jour la liste des modules pour m'assurer qu'il était actif.

Enfin, j'ai personnalisé davantage mon module en créant des vues pour les étapes des voyages, des relations, des menus, etc., selon les besoins spécifiques de mon application. J'ai testé le module dans un environnement de développement pour m'assurer que tout fonctionnait correctement. 

