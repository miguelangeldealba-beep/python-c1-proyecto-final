from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from extensions import db
from models.patient import Patient
from models.user import User
from models.doctor import Doctor
from models.centro import Centro
from models.cita import Cita

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.route("/usuario", methods=["POST"])
@jwt_required()
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
def get_patients():

    patients = Patient.query.all()

    return jsonify([
        patient.to_dict()
        for patient in patients
    ])


@admin_bp.route("/pacientes/<int:id>", methods=["GET"])
@jwt_required()
def get_patient(id):

    patient = Patient.query.get(id)

    if not patient:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    return jsonify(patient.to_dict())


@admin_bp.route("/pacientes/<int:id>", methods=["PUT"])
@jwt_required()
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


@admin_bp.route("/citas", methods=["POST"])
@jwt_required()
def create_cita():

    data = request.get_json()

    paciente = Patient.query.get(data["paciente_id"])

    if not paciente:
        return jsonify({
            "error": "Paciente no encontrado"
        }), 404

    if paciente.estado != "ACTIVO":
        return jsonify({
            "error": "Paciente inactivo"
        }), 400

    doctor = Doctor.query.get(data["doctor_id"])

    if not doctor:
        return jsonify({
            "error": "Doctor no encontrado"
        }), 404

    centro = Centro.query.get(data["centro_id"])

    if not centro:
        return jsonify({
            "error": "Centro no encontrado"
        }), 404


    cita_existente = Cita.query.filter(
        Cita.doctor_id == data["doctor_id"],
        Cita.fecha == data["fecha"]
    ).first()

    if cita_existente:
        return jsonify({
            "error": "El doctor ya tiene una cita en esa fecha"
        }), 400

    nueva_cita = Cita(
        paciente_id=data["paciente_id"],
        doctor_id=data["doctor_id"],
        centro_id=data["centro_id"],
        fecha=data["fecha"],
        motivo=data["motivo"],
        estado=data["estado"]
    )

    db.session.add(nueva_cita)
    db.session.commit()

    return jsonify({
        "message": "Cita creada correctamente"
    }), 201


@admin_bp.route("/citas", methods=["GET"])
@jwt_required()
def get_citas():

    citas = Cita.query.all()

    result = []

    for cita in citas:
        result.append({
            "id": cita.id,
            "paciente_id": cita.paciente_id,
            "doctor_id": cita.doctor_id,
            "centro_id": cita.centro_id,
            "fecha": cita.fecha,
            "motivo": cita.motivo,
            "estado": cita.estado
        })

    return jsonify(result)


@admin_bp.route("/citas/<int:id>", methods=["GET"])
@jwt_required()
def get_cita(id):

    cita = Cita.query.get(id)

    if not cita:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    return jsonify({
        "id": cita.id,
        "paciente_id": cita.paciente_id,
        "doctor_id": cita.doctor_id,
        "centro_id": cita.centro_id,
        "fecha": cita.fecha,
        "motivo": cita.motivo,
        "estado": cita.estado
    })


@admin_bp.route("/citas/<int:id>", methods=["PUT"])
@jwt_required()
def update_cita(id):

    cita = Cita.query.get(id)

    if not cita:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    data = request.get_json()

    cita.paciente_id = data.get("paciente_id", cita.paciente_id)
    cita.doctor_id = data.get("doctor_id", cita.doctor_id)
    cita.centro_id = data.get("centro_id", cita.centro_id)
    cita.fecha = data.get("fecha", cita.fecha)
    cita.motivo = data.get("motivo", cita.motivo)
    cita.estado = data.get("estado", cita.estado)

    db.session.commit()

    return jsonify({
        "message": "Cita actualizada correctamente"
    })


@admin_bp.route("/citas/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_cita(id):

    cita = Cita.query.get(id)

    if not cita:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    db.session.delete(cita)
    db.session.commit()

    return jsonify({
        "message": "Cita eliminada correctamente"
    })