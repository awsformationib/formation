
# ✅ Fiche Solution – CRUD `Vol` avec **Flask + SQLAlchemy**

## 📦 Structure des fichiers recommandée

```
vols_flask_app/
│
├── app.py               ← point d’entrée Flask
├── models.py            ← définition SQLAlchemy du modèle Vol
├── database.py          ← config DB + session
└── routes.py            ← routes Flask pour CRUD
```

---

## 1️⃣ `models.py` – Définition du modèle `Vol`

```
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Vol(db.Model):
    __tablename__ = 'vols'

    numero = db.Column(db.String(10), primary_key=True)
    destination = db.Column(db.String(50))
    avion = db.Column(db.String(50))
    statut = db.Column(db.String(20))
    heure_creation = db.Column(db.DateTime, default=datetime.utcnow)
    heure_decollage = db.Column(db.DateTime, nullable=True)
    heure_arrivee = db.Column(db.DateTime, nullable=True)
```

---

## 2️⃣ `database.py` – Configuration de la base de données

```
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import db

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:motdepasse@localhost/formation"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
```

---

## 3️⃣ `routes.py` – Routes Flask pour CRUD

```
from flask import Blueprint, request, jsonify
from models import db, Vol
from datetime import datetime

bp = Blueprint('vols', __name__)

@bp.route('/vols', methods=['POST'])
def creer_vol():
    data = request.get_json()
    vol = Vol(**data)
    db.session.add(vol)
    db.session.commit()
    return jsonify({"message": "Vol créé"}), 201

@bp.route('/vols', methods=['GET'])
def lister_vols():
    vols = Vol.query.all()
    return jsonify([v.__dict__ for v in vols])

@bp.route('/vols/<numero>', methods=['GET'])
def get_vol(numero):
    vol = Vol.query.get(numero)
    if vol:
        return jsonify(vol.__dict__)
    return jsonify({"error": "Vol introuvable"}), 404

@bp.route('/vols/<numero>', methods=['PUT'])
def update_statut(numero):
    vol = Vol.query.get(numero)
    if not vol:
        return jsonify({"error": "Vol non trouvé"}), 404
    data = request.get_json()
    if 'statut' in data:
        vol.statut = data['statut']
        db.session.commit()
    return jsonify({"message": "Mise à jour effectuée"})

@bp.route('/vols/<numero>', methods=['DELETE'])
def delete_vol(numero):
    vol = Vol.query.get(numero)
    if vol:
        db.session.delete(vol)
        db.session.commit()
        return jsonify({"message": "Vol supprimé"})
    return jsonify({"error": "Vol introuvable"}), 404
```

---

## 4️⃣ `app.py` – Point d’entrée Flask

```
from flask import Flask
from database import init_db
from models import db
from routes import bp

app = Flask(__name__)
init_db(app)
app.register_blueprint(bp)

with app.app_context():
    db.create_all()  # Création des tables si besoin

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🧪 Exemple de test via `curl` ou Postman

```
curl -X POST http://localhost:5000/vols \
     -H "Content-Type: application/json" \
     -d '{"numero": "AF001", "destination": "Tokyo", "avion": "Airbus A350", "statut": "prévu"}'
```

---

## ✅ Extensions possibles

| Option                    | Description                                   |
| ------------------------- | --------------------------------------------- |
| Pagination                | via `.paginate()` de SQLAlchemy               |
| Recherche par destination | `Vol.query.filter(Vol.destination.like(...))` |
| Validation                | via `marshmallow` ou `pydantic` avec Flask    |
| Swagger UI                | via `flasgger` ou `flask-restx`               |

---

## 🚀 Commande pour lancer le serveur Flask

Depuis le dossier racine (`vols_flask_app/`), exécutez dans le terminal :

```
python app.py
```

Le serveur démarrera sur `http://localhost:5000/`.

> Vous pouvez ajouter un fichier `.env` ou utiliser `python-dotenv` si vous voulez externaliser la configuration (mot de passe, URI, etc.).
