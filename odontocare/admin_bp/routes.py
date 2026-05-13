from flask import Blueprint, jsonify, request
from models.patient import Patient

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/patients", methods=["GET"])
def get_patients():

    patients = Patient.query.all()

    result = []

    for patient in patients:
        result.append({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age
        })

    return jsonify(result)

@admin_bp.route("/patients", methods=["POST"])
def create_patient():

    data = request.get_json()

    new_patient = Patient(
        name=data["name"],
        age=data["age"]
    )

    from extensions import db

    db.session.add(new_patient)
    db.session.commit()

    return jsonify({
        "message": "Paciente creado correctamente"
    })