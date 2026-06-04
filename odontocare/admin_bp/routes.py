from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from extensions import db
from models.patient import Patient
from models.user import User
from models.doctor import Doctor
from models.centro import Centro
from utils.roles import role_required

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/usuario", methods=["POST"])
@jwt_required()
@role_required("admin", "secretaria")
def create_user():

    data = request.get_json()

    new_user = User(
        username=data["username"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Usuario creado correctamente"
    }), 201


@admin_bp.route("/pacientes", methods=["POST"])
@jwt_required()
@role_required("admin", "secretaria")
def create_patient():

    data = request.get_json()

    patient = Patient(
        nombre=data["nombre"],
        telefono=data.get("telefono"),
        estado=data.get("estado", "ACTIVO")
    )

    db.session.add(patient)
    db.session.commit()

    return jsonify({
        "message": "Paciente creado",
        "patient": patient.to_dict()
    }), 201


@admin_bp.route("/pacientes", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_patients():

    patients = Patient.query.all()

    return jsonify([
        patient.to_dict()
        for patient in patients
    ])


@admin_bp.route("/pacientes/<int:id>", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_paciente(id):

    patient = Patient.query.get(id)

    if not patient:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    return jsonify(patient.to_dict())


@admin_bp.route("/pacientes/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("admin", "secretaria")
def update_patient(id):

    patient = Patient.query.get(id)

    if not patient:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    data = request.get_json()

    patient.nombre = data.get("nombre", patient.nombre)
    patient.telefono = data.get("telefono", patient.telefono)
    patient.estado = data.get("estado", patient.estado)

    db.session.commit()

    return jsonify({
        "message": "Paciente actualizado",
        "patient": patient.to_dict()
    })


@admin_bp.route("/pacientes/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin", "secretaria")
def delete_patient(id):

    patient = Patient.query.get(id)

    if not patient:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({
        "message": "Paciente eliminado"
    })


@admin_bp.route("/doctores", methods=["POST"])
@jwt_required()
@role_required("admin", "secretaria")
def create_doctor():

    data = request.get_json()

    new_doctor = Doctor(
        nombre=data["nombre"],
        especialidad=data["especialidad"]
    )

    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({
        "message": "Doctor creado correctamente"
    }), 201


@admin_bp.route("/doctores", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_doctores():

    doctors = Doctor.query.all()

    result = []

    for doctor in doctors:
        result.append({
            "id": doctor.id,
            "nombre": doctor.nombre,
            "especialidad": doctor.especialidad
        })

    return jsonify(result)


@admin_bp.route("/doctores/<int:id>", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_doctor(id):

    doctor = Doctor.query.get(id)

    if not doctor:
        return jsonify({
            "error": "Doctor no encontrado"
        }), 404

    return jsonify({
        "id": doctor.id,
        "nombre": doctor.nombre,
        "especialidad": doctor.especialidad
    })


@admin_bp.route("/doctores/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("admin", "secretaria")
def update_doctor(id):

    doctor = Doctor.query.get(id)

    if not doctor:
        return jsonify({
            "error": "Doctor no encontrado"
        }), 404

    data = request.get_json()

    doctor.nombre = data.get("nombre", doctor.nombre)
    doctor.especialidad = data.get("especialidad", doctor.especialidad)

    db.session.commit()

    return jsonify({
        "message": "Doctor actualizado correctamente"
    })


@admin_bp.route("/doctores/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin", "secretaria")
def delete_doctor(id):

    doctor = Doctor.query.get(id)

    if not doctor:
        return jsonify({
            "error": "Doctor no encontrado"
        }), 404

    db.session.delete(doctor)
    db.session.commit()

    return jsonify({
        "message": "Doctor eliminado correctamente"
    })


@admin_bp.route("/centros", methods=["POST"])
@jwt_required()
@role_required("admin", "secretaria")
def create_centro():

    data = request.get_json()

    new_centro = Centro(
        nombre=data["nombre"],
        direccion=data["direccion"]
    )

    db.session.add(new_centro)
    db.session.commit()

    return jsonify({
        "message": "Centro creado correctamente"
    }), 201


@admin_bp.route("/centros", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_centros():

    centros = Centro.query.all()

    result = []

    for centro in centros:
        result.append({
            "id": centro.id,
            "nombre": centro.nombre,
            "direccion": centro.direccion
        })

    return jsonify(result)


@admin_bp.route("/centros/<int:id>", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria")
def get_centro(id):

    centro = Centro.query.get(id)

    if not centro:
        return jsonify({
            "error": "Centro no encontrado"
        }), 404

    return jsonify({
        "id": centro.id,
        "nombre": centro.nombre,
        "direccion": centro.direccion
    })


@admin_bp.route("/centros/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("admin", "secretaria")
def update_centro(id):

    centro = Centro.query.get(id)

    if not centro:
        return jsonify({
            "error": "Centro no encontrado"
        }), 404

    data = request.get_json()

    centro.nombre = data.get("nombre", centro.nombre)
    centro.direccion = data.get("direccion", centro.direccion)

    db.session.commit()

    return jsonify({
        "message": "Centro actualizado correctamente"
    })


@admin_bp.route("/centros/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin", "secretaria")
def delete_centro(id):

    centro = Centro.query.get(id)

    if not centro:
        return jsonify({
            "error": "Centro no encontrado"
        }), 404

    db.session.delete(centro)
    db.session.commit()

    return jsonify({
        "message": "Centro eliminado correctamente"
    })