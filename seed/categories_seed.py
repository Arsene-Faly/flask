# pip install Faker

# Importer Faker pour générer des données fictives
from faker import Faker

# Importer notre application Flask et SQLAlchemy
from config import db
from app import app

# Importer le modèle Category
from models import Category


# fr_FR permet de générer des données adaptées au français
fake = Faker("fr_FR")


# Il permet d'utiliser la base de données en dehors d'une route Flask
with app.app_context():

    # Répéter l'opération 10 fois
    for i in range(10):

        # Créer une nouvelle catégorie
        category = Category(
            # Générer un nom de catégorie aléatoire
            name=fake.word(),

            # max_nb_chars limite la longueur du texte à 200 caractères
            description=fake.text(max_nb_chars=200)
        )

        # Ajouter la catégorie à la session SQLAlchemy
        db.session.add(category)

    # Enregistrer toutes les catégories dans la base de données
    db.session.commit()

    # Afficher un message après l'insertion
    print("10 catégories créées avec succès !")

    # python -m seed.categories_seed