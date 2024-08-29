# Ynov Basket

Projet compensatoire B2 dans lequel il fallait trier et afficher les données de cette [api](./https://www.balldontlie.io).

# Comment utiliser le projet

Clonez et déplacez à la racine du projet :

```console
$ git clone git@github.com:geoffrey-diederichs/Ynov_Basket.git
$ cd Ynov_Basket/
```

Vous pouvez lancer ce projet dans un environnement virtuel Python sous Linux à l'aide des commandes suivantes :

```console
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Sous Windows (powershell) :

```console
$ python3 -m venv venv
$ venv\Scripts\Activate.ps1
$ pip install -r requirements.txt
```

Veuillez maintenant sauvegarder votre clée pour l'API (que vous pouvez obtenir [ici](./https://www.balldontlie.io) en vous créant un compte) dans le fichier `key.txt` à la racine de ce projet. Par exemple :

```console
$ pwd
/Ynov_Basket
$ echo -n "INSERT-YOUR-API-KEY" > key.txt
```

Vous pouvez maintenant lancer le projet :

```console
python3 main.py 
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Et y accéder dans votre navigateur à l'addresse donné par le programme (dont le cas de notre exemple : `http://127.0.0.1:5000`).

# Fonctionnalités

## `/home`

Page d'acceuil vous indiquant de vous connecter si vous ne l'êtes pas, autrement il vous redirige vers `/players`.

## `/singup`, `/login`, `/logout`

Pages permettant de vous créer un compte, de vous connecter et de vous déconnecter.

## `/players`, `/teams`, `/games`

Une fois connecté vous pouvez accéder à ces trois pages listant respectivements : les joueurs, équipes et matchs. En cliquant sur un élément en particulier, vous accèderez à une page le détaillant.
Par exemple en cliquant sur `Alex Abrines` dans `/players`, nous arrivons sur `player/1` détaillant ce joueur.
