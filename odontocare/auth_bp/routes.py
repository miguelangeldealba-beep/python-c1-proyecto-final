from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from extensions import db

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        username=data["username"]
    ).first()

    if not user:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    if user.password != data["password"]:
        return jsonify({
            "error": "Password incorrecta"
        }), 401

    access_token = create_access_token(
        identity=user.username,
        additional_claims={
            "role": user.role
        }
    )

    return jsonify({
        "token": access_token,
        "role": user.role
    })


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    existing_user = User.query.filter_by(
        username=data["username"]
    ).first()

    if existing_user:
        return jsonify({
            "error": "El usuario ya existe"
        }), 400

    new_user = User(
        username=data["username"],
        password=data["password"],
        role=data.get("role", "paciente")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Usuario creado correctamente"
    }), 201