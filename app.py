from flask import Flask, render_template, redirect, url_for
 
from flask_migrate import Migrate 
   
from config import Config, db
# from routes.main import main
# from routes.auth import auth

# Importation models
from models import Category

from routes import main, auth, admin, admin_category


# __name__ → Variable speciale pour indiquer à Flask où se trouve notre application.
app = Flask(__name__)

# Charger la configuration depuis config.py
app.config.from_object(Config)
# Connecter SQLAlchemy à notre application Flask
db.init_app(app)

# Initialiser Flask-Migrate
migrate = Migrate(app, db)

# Enregistrer
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(admin_category)

# Variable globale : variable accessible dans l'application
@app.context_processor
def global_variables():
    return {"site_name": "My Blog", "author": "Arsène"}

@app.errorhandler(404)
def page_not_found(error):
    # return render_template('404.html')
    return redirect(url_for("main.home_view"))


# Si notre fichier est executer notre serveur marche
if __name__ == "__main__":
    app.run(debug=True, port=5000)
