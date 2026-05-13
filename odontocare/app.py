from flask import Flask
from extensions import db
from models.patient import Patient
from admin_bp.routes import admin_bp


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///odontocare.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return {
            "message": "OdontoCare API funcionando correctamente"
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)