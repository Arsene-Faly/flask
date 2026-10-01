from config import db


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text, nullable=False)

    price = db.Column(db.Numeric(10, 2), nullable=False)

    category_id = db.Column(
        db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False
    )

    category = db.relationship("Category", back_populates="products")

    # Date et heure de création
    created_at = db.Column(db.DateTime, default=db.func.now())
