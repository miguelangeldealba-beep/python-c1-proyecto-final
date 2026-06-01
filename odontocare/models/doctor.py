from extensions import db

class Doctor(db.Model):
    __tablename__ = "doctores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100))
    estado = db.Column(db.String(20), default="ACTIVO")
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "estado": self.estado
        }