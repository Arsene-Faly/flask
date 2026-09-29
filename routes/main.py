from flask import Blueprint, render_template, request
import time

# Déclaration BluePrint
main = Blueprint("main", __name__, url_prefix="/")

# Un décorateur est une fonction qui enveloppe une autre fonction pour lui ajouter un comportement.
@main.route("/")
def home_view():
    context = {"page": "home"}

    return render_template("pages/index.html", **context)


@main.route("/service")
def service_view():
    liste_services = [
        {
            "name": "Développement python",
            "description": "Création de sites web modernes et adaptés aux besoins des utilisateurs.",
        },
        {
            "name": "Développement Flask",
            "description": "Développement d'applications web avec le framework Flask.",
        },
        {
            "name": "API",
            "description": "Création et intégration d'API pour communiquer avec différentes applications.",
        },
    ]

    context = {
        "page": "service",
        "liste_services": liste_services
    }

    return render_template("pages/service.html", **context)


@main.route("/about")
def about_view():
    technologies = ["HTML", "CSS", "JS", "PYTHON"]
    
    context = {
        "page": "about",
        "technologies" : technologies
        }
    return render_template("pages/about.html", **context)


@main.route("/contact", methods=["GET", "POST"])
def contact_view():
    context = {"page": "contact"}

    if request.method == "POST":

        # Simulation d'un traitement long
        time.sleep(3)

        print("Nom :", request.form["name"])
        print("Email :", request.form["email"])
        print("Message :", request.form["message"])

    return render_template("pages/contact.html", **context)
