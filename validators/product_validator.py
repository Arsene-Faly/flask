from models import Product


def validate_product(name, description, price, category_id, product_id=None):

    errors = []

    # Vérification du nom
    if not name:
        errors.append("Le nom du produit est obligatoire.")

    # Vérification de la description
    if not description:
        errors.append("La description du produit est obligatoire.")

    # Vérification du prix
    if not price:
        errors.append("Le prix du produit est obligatoire.")
    else:
        try:
            price = float(price)

            if price < 0:
                errors.append("Le prix ne peut pas être négatif.")

        except ValueError:
            errors.append("Le prix doit être un nombre valide.")

    # Vérification de la catégorie
    if not category_id:
        errors.append("La catégorie est obligatoire.")

    # Vérification du nom du produit
    if name:

        query = Product.query.filter_by(name=name)

        # Pour la modification :
        # on exclut le produit actuel
        if product_id:
            query = query.filter(Product.id != product_id)

        product_existant = query.first()

        if product_existant:
            errors.append("Ce produit existe déjà.")

    return errors
