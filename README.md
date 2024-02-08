# Yenega Framework

Bienvenue dans le framework Yenega ! Ce framework python exploite la librairie tkinter pour construire facilement et rapidement des applications desktop multiplateforme.

## Prérequis

Avant d'utiliser le framework Yenega, assurez-vous d'avoir les éléments suivants installés sur votre système :

- [Python 3](https://www.python.org/downloads)
- [Git](https://git-scm.com/downloads)

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