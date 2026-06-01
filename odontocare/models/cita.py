from extensions import db

class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctores.id"),
        nullable=False
    )

    centro_id = db.Column(
        db.Integer,
        db.ForeignKey("centro.id"),
        nullable=False
    )

    fecha = db.Column(db.String(100), nullable=False)
    motivo = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(50), nullable=False, default="PENDIENTE")

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )