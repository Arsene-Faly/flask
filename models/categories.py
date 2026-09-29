from config import db

class Category(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    # nom category
    name = db.Column(
        db.String(100),
        nullable=False
    )
    
    description = db.Column(
        db.Text,
        nullable=True
    )
     
    # Date et heure de création
    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )