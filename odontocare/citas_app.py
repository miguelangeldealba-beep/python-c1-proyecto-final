from flask import Flask
from extensions import db, jwt
from citas_bp import citas_bp
from models.cita import Cita
from models.user import User
from models.patient import Patient
from models.doctor import Doctor
from models.centro import Centro

def create_citas_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///citas.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "mi_clave_super_segura_123456789"

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(citas_bp)

    @app.route("/")
    def home():
        return {
            "message": "Microservicio de citas funcionando correctamente"
        }

    return app

app = create_citas_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)