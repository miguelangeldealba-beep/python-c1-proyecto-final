# OdontoCare

Proyecto Final Python C1

## Descripción

OdontoCare es una API REST desarrollada con Flask para la gestión de clínicas dentales.

El sistema permite administrar:

* Pacientes
* Doctores
* Centros médicos
* Citas médicas

La aplicación incorpora autenticación JWT, persistencia mediante SQLite y SQLAlchemy, arquitectura modular basada en Blueprints, comunicación entre microservicios mediante REST y despliegue mediante Docker.

---

## Tecnologías utilizadas

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* SQLite
* Requests
* Docker
* Docker Compose

---

## Arquitectura del proyecto

```text
odontocare/

├── admin_bp/
│   └── routes.py
│
├── auth_bp/
│   └── routes.py
│
├── citas_bp/
│   └── routes.py
│
├── models/
│   ├── user.py
│   ├── patient.py
│   ├── doctor.py
│   ├── centro.py
│   └── cita.py
│
├── utils/
│   └── roles.py
│
├── config/
│
├── instance/
│   └── odontocare.db
│
├── admin_app.py
├── citas_app.py
├── app.py
├── cliente.py
├── extensions.py
├── carga_inicial.py
├── datos.csv
├── docker-compose.yml
├── requirements.txt
└── README.md