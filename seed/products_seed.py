from faker import Faker

from config import db
from app import app

# Importer les modèles Category et Product
from models import Category, Product

fake = Faker("fr_FR")

with app.app_context():

    categories = Category.query.all()

    # Vérifier qu'il existe des catégories
    if not categories:

        print("Aucune catégorie trouvée.")
        print("Lancez d'abord : python -m seed.categories_seed")

    else:

        # Répéter l'opération 50 fois
        for i in range(50):

            # Choisir une catégorie aléatoire
            category = fake.random_element(categories)

            # Création produit
            product = Product(

                # Générer un nom de produit
                name=fake.catch_phrase(),

                # Générer une description
                description=fake.text(
                    max_nb_chars=300
                ),

                # Générer un prix entre 10 et 1000
                price=fake.pydecimal(
                    left_digits=4,
                    right_digits=2,
                    positive=True
                ),

                # Associer le produit à une catégorie
                category_id=category.id
            )

            # Ajouter le produit à la session SQLAlchemy
            db.session.add(product)

        # Enregistrer tous les produits
        db.session.commit()

        # Afficher un message
        print("50 produits créés avec succès !")