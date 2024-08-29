# Ynov Basket

Projet compensatoire B2 dans lequel il fallait trier et afficher les données de cette [api](./https://www.balldontlie.io).

# Comment utiliser le projet

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

Une fois le projet installé, veuillez sauvegarder votre clée pour l'API (que vous pouvez obtenir [ici](./https://www.balldontlie.io) en vous créant un compte) dans le fichier `key.txt` à la racine de ce projet. Par exemple :

```console
$ pwd
/Ynov_Basket
$ echo "INSERT-YOUR-API-KEY" > key.txt
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
