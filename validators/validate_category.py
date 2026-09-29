from models import Category


def validate_category(name, description, category_id=None):

    errors = []

    # Vérification du nom
    if not name:
        errors.append(
            "Le nom de la catégorie est obligatoire."
        )

    # Vérifier si le nom existe déjà
    if name:

        query = Category.query.filter_by(
            name=name
        )

        # Pour la modification :
        # on exclut la catégorie que l'on est en train de modifier
        if category_id:
            query = query.filter(
                Category.id != category_id
            )

        category_existante = query.first()

        if category_existante:
            errors.append(
                "Cette catégorie existe déjà."
            )

    return errors