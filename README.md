# TO_DO_List_project



## Liste des Chemins URL

### Routes de l'application publique (Frontend)

| Méthode | Chemin                | Description                             |
|---------|-----------------------|-----------------------------------------|
| GET     | /                     | Page d'accueil                          |
| GET     | /register/            | Page d'inscription                      |
| POST    | /register/            | Soumettre le formulaire d'inscription   |
| GET     | /login/               | Page de connexion                       |
| POST    | /login/               | Soumettre le formulaire de connexion    |
| GET     | /logout/              | Déconnexion                             |
| GET     | /tasks/               | Liste des tâches de l'utilisateur       |
| POST    | /tasks/               | Ajouter une nouvelle tâche              |
| GET     | /tasks/<id>/          | Détails d'une tâche spécifique          |
| PUT     | /tasks/<id>/          | Mettre à jour une tâche                 |
| DELETE  | /tasks/<id>/          | Supprimer une tâche                     |

### Routes de l'API

| Méthode | Chemin                | Description                             |
|---------|-----------------------|-----------------------------------------|
| GET     | /api/tasks/           | Récupérer la liste des tâches           |
| POST    | /api/tasks/           | Créer une nouvelle tâche                |
| GET     | /api/tasks/<id>/      | Récupérer une tâche spécifique          |
| PUT     | /api/tasks/<id>/      | Mettre à jour une tâche                 |
| DELETE  | /api/tasks/<id>/      | Supprimer une tâche                     |



## Questions

### Fonctionnement de Django

1. **Affichage d'une page HTML `index.html` à l'URL `/` via l'application `public`** :
   - Lorsqu'un utilisateur accède à l'URL `/`, Django traite la requête en suivant ces étapes :
     1. La requête est dirigée vers l'application `public` par le routeur de Django.
     2. La vue associée à l'URL `/` est exécutée, généralement définie dans `public/views.py`.
     3. La vue renvoie le rendu du template `index.html`, situé dans `public/templates/public/index.html`.
   - **Arborescence des répertoires** :
     ```
     DJANGO_PROJECT/
     └── public/
         └── templates/
             └── public/
                 └── index.html
     ```

2. **Configuration de la base de données** :
   - La base de données est configurée dans le fichier `settings.py`, situé dans le répertoire racine de l'application Django.

3. **Fichiers de paramètres** :
   - Les fichiers à mentionner sont :
     - `settings.py` : contient les configurations générales, y compris la base de données, les applications installées, etc.
     - `urls.py` : définit les URL et les vues associées.
     - `wsgi.py` : utilisé pour le déploiement, indique l'application WSGI à utiliser.
     - `asgi.py` : utilisé pour le déploiement ASGI.

4. **Exécution des commandes `makemigrations` et `migrate`** :
   - `python manage.py makemigrations` : crée de nouveaux fichiers de migration basés sur les modifications apportées aux modèles (fichiers `models.py`).
   - `python manage.py migrate` : applique ces migrations à la base de données, créant ainsi les tables correspondantes.

### Fonctionnement de Docker

1. **Commandes Dockerfile** :
   - `FROM` : spécifie l'image de base à utiliser pour créer le conteneur.
   - `RUN` : exécute une commande dans le conteneur au moment de la construction.
   - `WORKDIR` : définit le répertoire de travail pour les instructions suivantes.
   - `EXPOSE` : indique le port sur lequel le conteneur écoute.
   - `CMD` : définit la commande par défaut à exécuter lors du démarrage du conteneur.

2. **Mentions dans `docker-compose.yml`** :
   - `ports: - "80:80"` : redirige le port 80 de la machine hôte vers le port 80 du conteneur.
   - `build: context: . dockerfile: Dockerfile.api` : définit le contexte de construction pour le service `api`.
   - `depends_on: - web - api` : assure que les services `web` et `api` démarrent avant ce service.
   - `environment: ...` : définit des variables d'environnement à utiliser dans le conteneur.

3. **Définir des variables d'environnement** :
   - Une méthode est d'utiliser un fichier `.env` pour stocker les variables, qui peuvent être référencées dans `docker-compose.yml`.

4. **Adresser un serveur web dans un conteneur** :
   - Tu peux utiliser le nom du service défini dans `docker-compose.yml` pour accéder au serveur. Par exemple, dans le conteneur `nginx`, tu peux accéder au conteneur `web` avec `http://web:8000`.

