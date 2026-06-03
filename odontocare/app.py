from flask import Flask
from extensions import db
from models.patient import Patient
from admin_bp.routes import admin_bp
from models.user import User
from extensions import jwt
from auth_bp.routes import auth_bp
from citas_bp import citas_bp
from models.doctor import Doctor
from models.centro import Centro
from models.cita import Cita

def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///odontocare.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "mi_clave_super_segura_123456789"

    db.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp)
    app.register_blueprint(citas_bp)

    @app.route("/")
    def home():
        return {
            "message": "OdontoCare API funcionando correctamente"
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)