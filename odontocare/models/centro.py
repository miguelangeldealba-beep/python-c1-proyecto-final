from extensions import db

class Centro(db.Model):
    __tablename__ = "centro"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    direccion = db.Column(db.String(200), nullable=False)