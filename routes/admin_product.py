from flask import Blueprint, render_template, request, redirect, url_for

from models import Product, Category

from config import db

from validators.product_validator import validate_product

admin_product = Blueprint("admin_product", __name__, url_prefix="/dashboard/product")

# ==========================================================

# LISTE DES PRODUITS

# ==========================================================


@admin_product.route("/")
def product_list():

    products = Product.query.all()

    nombre_produits = Product.query.count()

    context = {"products": products, "nombre_produits": nombre_produits}

    return render_template("pages/admin/products/list.html", **context)


# ==========================================================

# AJOUTER UN PRODUIT

# ==========================================================


@admin_product.route("/create", methods=["GET", "POST"])
def product_create():

    errors = []
    success = []

    categories = Category.query.all()

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        description = request.form.get("description", "").strip()

        price = request.form.get("price", "").strip()

        category_id = request.form.get("category_id", "").strip()

        # Validation
        errors = validate_product(name, description, price, category_id)

        # Si aucune erreur
        if not errors:

            product = Product(
                name=name, description=description, price=price, category_id=category_id
            )

            db.session.add(product)

            db.session.commit()

            success.append("Le produit a été ajouté avec succès.")

    context = {"errors": errors, "success": success, "categories": categories}

    return render_template("pages/admin/products/create.html", **context)


# ==========================================================

# DÉTAIL D'UN PRODUIT

# ==========================================================


@admin_product.route("/detail/<int:id>")
def product_detail(id):

    product = Product.query.get_or_404(id)

    context = {"product": product}

    return render_template("pages/admin/products/detail.html", **context)


# ==========================================================

# MODIFIER UN PRODUIT

# ==========================================================


@admin_product.route("/edit/<int:id>", methods=["GET", "POST"])
def product_edit(id):

    product = Product.query.get_or_404(id)

    categories = Category.query.all()

    errors = []
    success = []

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        description = request.form.get("description", "").strip()

        price = request.form.get("price", "").strip()

        category_id = request.form.get("category_id", "").strip()

        # Validation
        errors = validate_product(name, description, price, category_id, product.id)

        # Si aucune erreur
        if not errors:

            product.name = name

            product.description = description

            product.price = price

            product.category_id = category_id

            db.session.commit()

            success.append("Le produit a été modifié avec succès.")

    context = {
        "product": product,
        "categories": categories,
        "errors": errors,
        "success": success,
    }

    return render_template("pages/admin/products/edit.html", **context)


# ==========================================================

# SUPPRIMER UN PRODUIT

# ==========================================================


@admin_product.route("/delete/<int:id>", methods=["POST"])
def product_delete(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)

    db.session.commit()

    return redirect(url_for("admin_product.product_list"))
