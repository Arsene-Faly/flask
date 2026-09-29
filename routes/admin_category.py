from flask import Blueprint, render_template, request, redirect, url_for

from models import Category
from config import db

from validators import validate_category

admin_category = Blueprint(
    "admin_category",
    __name__,
    url_prefix="/dashboard/category"
)


@admin_category.route("/")
def category_list():

    categories = Category.query.all()

    nombre_categories = Category.query.count()

    context = {
        "categories": categories,
        "nombre_categories": nombre_categories
    }

    return render_template(
        "pages/admin/categories/list.html",
        **context
    )


@admin_category.route("/create", methods=["GET", "POST"])
def category_create():

    errors = []
    success = []

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        # Validation
        errors = validate_category(
            name,
            description
        )

        # Si aucune erreur
        if not errors:

            category = Category(
                name=name,
                description=description
            )

            db.session.add(category)
            db.session.commit()

            success.append("La catégorie a été ajoutée avec succès.")

    context = {
        "errors": errors,
        "success": success
    }

    return render_template(
        "pages/admin/categories/create.html",
        **context
    )


@admin_category.route("/detail/<int:id>")
def category_detail(id):
    # sert à récupérer une catégorie dans la base de données grâce à son id.
    category = Category.query.get_or_404(id)

    context = {
        'category' : category
    }
    return render_template(
        "pages/admin/categories/detail.html",
        **context
    )


@admin_category.route("/edit/<int:id>", methods=["GET", "POST"])
def category_edit(id):

    category = Category.query.get_or_404(id)

    errors = []
    success = []

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        # Validation
        errors = validate_category(
            name,
            description,
            category.id
        )

        # Si aucune erreur
        if not errors:

            category.name = name

            category.description = description

            db.session.commit()

            success.append(
                "La catégorie a été modifiée avec succès."
            )

    context = {
        "category": category,
        "errors": errors,
        "success": success
    }
    
    return render_template(
        "pages/admin/categories/edit.html",
        **context
    )

@admin_category.route("/delete/<int:id>", methods=["POST"])
def category_delete(id):

    category = Category.query.get_or_404(id)

    db.session.delete(category)

    db.session.commit()

    return redirect(
        url_for("admin_category.category_list")
    )