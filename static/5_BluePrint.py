"""
Dans **Flask**, un **Blueprint** sert à organiser ton application en plusieurs parties (authentification, produits, utilisateurs, etc.).

Par exemple, au lieu d'avoir un seul gros `app.py`, tu peux faire :

```text
mon_projet/
│
├── app.py
│
├── routes/
│   ├── __init__.py
│   ├── home.py
│   └── users.py
│
└── templates/
    ├── home.html
    └── users.html
```

### 1. Créer un Blueprint

Dans `routes/home.py` :

```python
from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return "Page d'accueil"
```

Ici :

```python
home = Blueprint("home", __name__)
```

crée le Blueprint.

Et :

```python
@home.route("/")
```

définit une route qui appartient au Blueprint.

---

### 2. Enregistrer le Blueprint

Dans `app.py` :

```python
from flask import Flask
from routes.home import home

app = Flask(__name__)

app.register_blueprint(home)


if __name__ == "__main__":
    app.run(debug=True)
```

Maintenant :

```text
http://127.0.0.1:5000/
```

affiche :

```text
Page d'accueil
```

---

## 3. Avec plusieurs Blueprints

Supposons que tu développes une application avec :

* `home`
* `users`
* `products`

Tu peux organiser comme ceci :

```text
mon_projet/
│
├── app.py
│
├── routes/
│   ├── __init__.py
│   ├── home.py
│   ├── users.py
│   └── products.py
│
└── templates/
```

### `routes/users.py`

```python
from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/")
def index():
    return "Liste des utilisateurs"


@users.route("/profile")
def profile():
    return "Profil utilisateur"
```

### `routes/products.py`

```python
from flask import Blueprint

products = Blueprint("products", __name__, url_prefix="/products")


@products.route("/")
def index():
    return "Liste des produits"
```

### `app.py`

```python
from flask import Flask

from routes.home import home
from routes.users import users
from routes.products import products


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(products)


if __name__ == "__main__":
    app.run(debug=True)
```

Tu obtiens alors :

```text
/                   → Accueil
/users/             → Utilisateurs
/users/profile      → Profil
/products/          → Produits
```

### Pourquoi utiliser `url_prefix` ?

Avec :

```python
users = Blueprint("users", __name__, url_prefix="/users")
```

tu peux écrire simplement :

```python
@users.route("/")
def index():
    ...
```

Flask comprend automatiquement :

```text
/users/
```

Donc le Blueprint est particulièrement utile pour faire une structure Flask propre, un peu comme les **apps Django**.

"""
