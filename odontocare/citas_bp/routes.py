from flask import jsonify, request
from flask_jwt_extended import jwt_required

from extensions import db
from models.cita import Cita
from . import citas_bp
from utils.roles import role_required

import os
import requests


@citas_bp.route("/citas", methods=["POST"])
@jwt_required()
@role_required("admin", "secretaria")
def create_cita():

    data = request.get_json()

    admin_url = os.getenv("ADMIN_SERVICE_URL", "http://127.0.0.1:5000")
    print("ADMIN URL:", admin_url)

    headers = {
        "Authorization": request.headers.get("Authorization")
    }

    paciente_response = requests.get(
        f"{admin_url}/admin/pacientes/{data['paciente_id']}",
        headers=headers
    )

    if paciente_response.status_code != 200:
        return jsonify({
            "error": "Paciente no encontrado en admin-service"
        }), 404

    paciente_data = paciente_response.json()

    if paciente_data.get("estado") != "ACTIVO":
        return jsonify({
            "error": "Paciente inactivo"
        }), 400

    doctor_response = requests.get(
        f"{admin_url}/admin/doctores/{data['doctor_id']}",
        headers=headers
    )

    if doctor_response.status_code != 200:
        return jsonify({
            "error": "Doctor no encontrado en admin-service"
        }), 404

    centro_response = requests.get(
        f"{admin_url}/admin/centros/{data['centro_id']}",
        headers=headers
    )

    if centro_response.status_code != 200:
        return jsonify({
            "error": "Centro no encontrado en admin-service"
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


@citas_bp.route("/citas", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria", "medico")
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


@citas_bp.route("/citas/<int:id>", methods=["GET"])
@jwt_required()
@role_required("admin", "secretaria", "medico", "paciente")
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


@citas_bp.route("/citas/<int:id>", methods=["PUT"])
@jwt_required()
@role_required("admin", "secretaria")
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


@citas_bp.route("/citas/<int:id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
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