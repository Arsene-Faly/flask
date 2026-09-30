--Initialiser les migration
flask --app app db init

flask --app app db migrate -m "Create contact table"
flask --app app db upgrade

Faker est une bibliothèque Python qui permet de générer automatiquement des données fictives.

pip install Faker

python -m seed.categories_seed

| Catégorie        | Méthode Faker                    | Utilisation           | Exemple                      |
| ---------------- | -------------------------------- | --------------------- | ---------------------------- |
| 👤 Personne      | `fake.name()`                    | Nom complet           | `Jean Dupont`                |
| 👤 Personne      | `fake.first_name()`              | Prénom                | `Jean`                       |
| 👤 Personne      | `fake.last_name()`               | Nom                   | `Dupont`                     |
| 👤 Personne      | `fake.name_male()`               | Nom masculin          | `Jean Dupont`                |
| 👤 Personne      | `fake.name_female()`             | Nom féminin           | `Marie Martin`               |
| 📧 Contact       | `fake.email()`                   | Email                 | `jean@example.com`           |
| 📧 Contact       | `fake.safe_email()`              | Email de test         | `jean@example.org`           |
| 📧 Contact       | `fake.company_email()`           | Email professionnel   | `jean@entreprise.fr`         |
| 📱 Contact       | `fake.phone_number()`            | Numéro téléphone      | `01 45 67 89 12`             |
| 📍 Adresse       | `fake.address()`                 | Adresse complète      | `12 rue Victor Hugo...`      |
| 📍 Adresse       | `fake.street_address()`          | Adresse/rue           | `12 rue Victor Hugo`         |
| 📍 Adresse       | `fake.city()`                    | Ville                 | `Paris`                      |
| 📍 Adresse       | `fake.country()`                 | Pays                  | `France`                     |
| 📍 Adresse       | `fake.country_code()`            | Code pays             | `FR`                         |
| 📍 Adresse       | `fake.postcode()`                | Code postal           | `75001`                      |
| 📍 Adresse       | `fake.latitude()`                | Latitude              | `48.8566`                    |
| 📍 Adresse       | `fake.longitude()`               | Longitude             | `2.3522`                     |
| 📝 Texte         | `fake.word()`                    | Un mot                | `ordinateur`                 |
| 📝 Texte         | `fake.words()`                   | Plusieurs mots        | `["ordinateur", "maison"]`   |
| 📝 Texte         | `fake.sentence()`                | Une phrase            | `Le produit est disponible.` |
| 📝 Texte         | `fake.sentences()`               | Plusieurs phrases     | `[...]`                      |
| 📝 Texte         | `fake.paragraph()`               | Un paragraphe         | `Lorem ipsum...`             |
| 📝 Texte         | `fake.paragraphs()`              | Plusieurs paragraphes | `[...]`                      |
| 📝 Texte         | `fake.text()`                    | Texte aléatoire       | `Lorem ipsum...`             |
| 📝 Texte         | `fake.text(max_nb_chars=200)`    | Texte limité          | `Lorem ipsum...`             |
| 📝 Texte         | `fake.slug()`                    | Slug URL              | `ordinateur-portable`        |
| 🔢 Nombre        | `fake.random_int()`              | Entier aléatoire      | `57`                         |
| 🔢 Nombre        | `fake.random_int(min=1,max=100)` | Entier dans une plage | `42`                         |
| 🔢 Nombre        | `fake.random_number()`           | Nombre aléatoire      | `8342`                       |
| 🔢 Nombre        | `fake.pyint()`                   | Entier Python         | `25`                         |
| 🔢 Nombre        | `fake.pyfloat()`                 | Nombre décimal        | `25.73`                      |
| 🔢 Nombre        | `fake.pydecimal()`               | Decimal               | `1250.50`                    |
| 🎲 Aléatoire     | `fake.random_element()`          | Choisir un élément    | `"Rouge"`                    |
| 🎲 Aléatoire     | `fake.random_elements()`         | Plusieurs éléments    | `["Rouge", "Bleu"]`          |
| 🎲 Aléatoire     | `fake.random_choices()`          | Choix avec répétition | `["Rouge", "Rouge"]`         |
| 🎲 Aléatoire     | `fake.random_sample()`           | Choix sans répétition | `["Rouge", "Bleu"]`          |
| 📅 Date          | `fake.date()`                    | Date                  | `2026-09-28`                 |
| 📅 Date          | `fake.date_time()`               | Date + heure          | `2026-09-28 10:30:00`        |
| 📅 Date          | `fake.date_of_birth()`           | Date naissance        | `2000-05-12`                 |
| 📅 Date          | `fake.year()`                    | Année                 | `2020`                       |
| ⏰ Heure          | `fake.time()`                    | Heure                 | `14:35:20`                   |
| ⏰ Heure          | `fake.timezone()`                | Fuseau horaire        | `Europe/Paris`               |
| 🏢 Entreprise    | `fake.company()`                 | Nom entreprise        | `Dupont SARL`                |
| 🏢 Entreprise    | `fake.company_suffix()`          | Suffixe entreprise    | `SARL`                       |
| 💼 Travail       | `fake.job()`                     | Profession            | `Développeur web`            |
| 💼 Travail       | `fake.catch_phrase()`            | Slogan                | `Solutions innovantes`       |
| 🌐 Internet      | `fake.url()`                     | URL                   | `https://example.com`        |
| 🌐 Internet      | `fake.domain_name()`             | Domaine               | `example.com`                |
| 🌐 Internet      | `fake.domain_word()`             | Nom domaine           | `example`                    |
| 🌐 Internet      | `fake.user_name()`               | Nom utilisateur       | `jeandupont`                 |
| 🔐 Sécurité      | `fake.password()`                | Mot de passe fictif   | `xK8@pL92`                   |
| 🌐 Réseau        | `fake.ipv4()`                    | Adresse IPv4          | `192.168.1.25`               |
| 🌐 Réseau        | `fake.ipv6()`                    | Adresse IPv6          | `2001:db8::1`                |
| 🆔 Identifiant   | `fake.uuid4()`                   | UUID                  | `550e8400-e29b...`           |
| 💳 Identifiant   | `fake.credit_card_number()`      | Numéro carte fictif   | `...`                        |
| 💳 Identifiant   | `fake.credit_card_expire()`      | Expiration fictive    | `10/30`                      |
| 💳 Identifiant   | `fake.credit_card_provider()`    | Type carte            | `VISA`                       |
| 🖼️ Image        | `fake.image_url()`               | URL image             | `https://...`                |
| 🎨 Couleur       | `fake.color_name()`              | Nom couleur           | `Blue`                       |
| 🎨 Couleur       | `fake.hex_color()`               | Couleur HEX           | `#3A7BD5`                    |
| 🎨 Couleur       | `fake.rgb_color()`               | Couleur RGB           | `123,45,200`                 |
| 📦 Produit       | `fake.ean()`                     | Code-barres EAN       | `5901234123457`              |
| 📦 Produit       | `fake.isbn13()`                  | ISBN 13               | `9781234567890`              |
| 📚 Livre         | `fake.isbn10()`                  | ISBN 10               | `1234567890`                 |
| 🗣️ Langue       | `fake.language_code()`           | Code langue           | `fr`                         |
| 🗣️ Langue       | `fake.language_name()`           | Nom langue            | `French`                     |
| 🌍 Localisation  | `fake.locale()`                  | Locale                | `fr_FR`                      |
| ⚖️ Unité         | `fake.pybool()`                  | Booléen               | `True` / `False`             |
| ⚖️ Unité         | `fake.boolean()`                 | Booléen               | `True` / `False`             |
| 📂 Fichier       | `fake.file_name()`               | Nom fichier           | `document.pdf`               |
| 📂 Fichier       | `fake.file_extension()`          | Extension             | `pdf`                        |
| 💻 Informatique  | `fake.file_path()`               | Chemin fictif         | `/home/user/file.txt`        |
| 💻 Informatique  | `fake.unix_path()`               | Chemin Unix           | `/tmp/test.txt`              |
| 🖥️ Informatique | `fake.unix_device()`             | Périphérique Unix     | `/dev/sda1`                  |


ORM BASIQUE
| ORM                                              | Signification                    |
| ------------------------------------------------ | -------------------------------- |
| `Category.query.all()`                           | Toutes les catégories            |
| `Category.query.first()`                         | Première catégorie               |
| `Category.query.get(1)`                          | Catégorie avec `id = 1`          |
| `Category.query.filter_by(name="Sport").all()`   | Catégories dont le nom est Sport |
| `Category.query.filter_by(name="Sport").first()` | Première catégorie Sport         |
| `Category.query.count()`                         | Nombre de catégories             |
| `Category.query.order_by(Category.name).all()`   | Trier par nom                    |
| `Category.query.delete()`                        | Supprimer des catégories         |


pip install flask-sqlalchemy
pip install Flask-Migrate
pip install pymysql

🐬 MySQL, c’est quoi ?
MySQL est un système de gestion de base de données relationnelle (SGBDR).

Il sert à stocker, organiser, rechercher et modifier des données dans une base de données.

Tu installes MySQL parce que ton application Flask a besoin d’un serveur de base de données pour stocker les informations.

🖥️ phpMyAdmin, c’est quoi ?
phpMyAdmin est une interface web qui permet de gérer MySQL/MariaDB plus facilement.

https://github.com/Arsene-Faly/flask