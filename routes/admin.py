from flask import Blueprint, render_template

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/dashboard"
)


@admin.route("/")
def dashboard_view():

    return render_template(
        "pages/admin/index.html"
    )