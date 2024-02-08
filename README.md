# Yenega Framework

Bienvenue dans le framework Yenega ! Ce framework python exploite la librairie tkinter pour construire facilement et rapidement des applications desktop multiplateforme.

## Prérequis

Avant d'utiliser le framework Yenega, assurez-vous d'avoir les éléments suivants installés sur votre système :

- [Python 3](https://www.python.org/downloads)
- [Git](https://git-scm.com/downloads)

## Configuration du Projet

Avant de commencer à utiliser le framework Yenega, assurez-vous de configurer les paramètres appropriés dans le fichier `env.py`. Ces paramètres définissent des configurations essentielles pour le bon fonctionnement de l'application.

## Fichier `env.py`

Assurez-vous de définir correctement les valeurs des paramètres suivants dans le fichier `env.py` de votre projet :

### Description des Paramètres :

- `LANG`: Langue par défaut de l'application.
- `APP_NAME`: Nom de l'application.
- `DATABASE`: Type de base de données utilisé.
- `DATABASE_HOST`: Adresse du serveur de base de données.
- `DATABASE_NAME`: Nom de la base de données.
- `DATABASE_USER`: Nom d'utilisateur de la base de données. *(Par défaut: "root")*
- `DATABASE_PASSWORD`: Mot de passe de la base de données. *(Par défaut: "root")*

**Remarque:** Assurez-vous que `DATABASE_USER` et `DATABASE_PASSWORD` correspondent à l'utilisateur et au mot de passe de votre installation MySQL. Par défaut, le nom d'utilisateur est 'root' et le mot de passe est vide. Cependant, cela peut varier en fonction de votre configuration.

- `LOGO_ICO`: Chemin vers le fichier ICO du logo de l'application. *(Placez l'image dans le dossier "resource/image/logo/")*
- `LOGO_PNG`: Chemin vers le fichier PNG du logo de l'application. *(Placez l'image dans le dossier "resource/image/logo/")*
  
N'oubliez pas de mettre à jour ces valeurs en fonction de votre configuration spécifique.

### Exemple d'Utilisation :

```python
# Exemple pour une application en français avec une base de données MySQL

LANG = "fr"
APP_NAME = "APP"

DATABASE = "mysql"
DATABASE_HOST = "localhost"
DATABASE_NAME = "yenega"
DATABASE_USER = "root"
DATABASE_PASSWORD = "root"

LOGO_ICO = "\\resource\\image\\logo\\logo.ico"
LOGO_PNG = "\\resource\\image\\logo\\logo.png"

PRIMARY_COLOR = "#fc5914"
SECONDARY_COLOR = "black"
BACKGROUND_COLOR = "white"
```

Assurez-vous que ces configurations correspondent à votre environnement et à vos préférences. Pour plus d'informations sur la configuration, consultez la documentation du framework Yenega.

## Commandes Disponibles

Le framework Yenega propose les commandes suivantes :

- `migrate`: Gère la migration de la base de données.
```bash
python path/vers/yenega.py migrate
```

  Options:
  - `--refresh`: Rafraîchit la base de données en supprimant toutes les tables avant la migration.
```bash
python path/vers/yenega.py migrate --refresh
```
  - `--reset`: Supprime toutes les tables de la base de données.
```bash
python path/vers/yenega.py migrate --reset
```

- `seed`: Gère l'initialisation des données dans la base de données.

  Options :
- `--admin`: Crée un accès administrateur avec les identifiants "admin" et le mot de passe haché de "admin".
```bash
python yenega.py seed --admin
```
  - `--force`: Force la recréation de l'accès administrateur s'il existe déjà.
```bash
python yenega.py seed --force
```

## Problèmes Connus

Si vous rencontrez des problèmes lors de l'utilisation du framework Yenega, veuillez consulter les sections "Problèmes Courants" ou "Contributions" dans le fichier [CONTRIBUTING.md]() pour obtenir de l'aide.

## Contributions

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md]() pour obtenir des informations sur la manière de contribuer au projet.

***

&copy; 2024 [**B. Tanguy KABORE**](https://www.linkedin.com/in/kabore-tanguy-96ab94298/)