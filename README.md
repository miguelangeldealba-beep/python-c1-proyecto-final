# OdontoCare

Proyecto Final Python C1

## Descripción

OdontoCare es una API REST desarrollada con Flask para la gestión de clínicas dentales.

El sistema permite administrar:

- Pacientes
- Doctores
- Centros médicos
- Citas médicas

La aplicación incorpora autenticación JWT, persistencia mediante SQLite y SQLAlchemy, arquitectura modular basada en Blueprints, cliente externo para consumo de servicios REST y despliegue mediante Docker.

---

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Requests
- Docker

---

## Arquitectura del proyecto

```
odontocare/
│
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
├── app.py
├── cliente.py
├── carga_inicial.py
├── datos.csv
├── requirements.txt
└── Dockerfile
```

---

## Funcionalidades implementadas

### Autenticación

- Registro de usuarios
- Login
- Generación de tokens JWT
- Protección de endpoints

### Gestión de Pacientes

- Crear paciente
- Consultar paciente
- Actualizar paciente
- Eliminar paciente

### Gestión de Doctores

- Crear doctor
- Consultar doctor
- Actualizar doctor
- Eliminar doctor

### Gestión de Centros

- Crear centro
- Consultar centro
- Actualizar centro
- Eliminar centro

### Gestión de Citas

- Crear cita
- Consultar cita
- Actualizar cita
- Eliminar cita
- Validación de conflictos de agenda

### Cliente Externo

- Consumo de la API mediante requests
- Comunicación cliente-servidor

### Docker

- Construcción de imagen Docker
- Ejecución del sistema dentro de contenedor

### Microservicios

- Servicio administrativo
- Servicio de citas
- Comunicación REST entre servicios

---

## Instalación

Clonar el repositorio:

```bash
git clone <url-del-repositorio>
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución local

```bash
python app.py
```

Servidor disponible en:

```text
http://127.0.0.1:5000
```

---

## Ejecución mediante Docker

Construir imagen:

```bash
docker build -t odontocare-api .
```

Ejecutar contenedor:

```bash
docker run -p 5000:5000 odontocare-api
```

---

## Endpoints principales

### Autenticación

```http
POST /register
POST /login
```

### Pacientes

```http
GET    /admin/pacientes
GET    /admin/pacientes/<id>
POST   /admin/pacientes
PUT    /admin/pacientes/<id>
DELETE /admin/pacientes/<id>
```

### Doctores

```http
GET    /admin/doctores
GET    /admin/doctores/<id>
POST   /admin/doctores
PUT    /admin/doctores/<id>
DELETE /admin/doctores/<id>
```

### Centros

```http
GET    /admin/centros
GET    /admin/centros/<id>
POST   /admin/centros
PUT    /admin/centros/<id>
DELETE /admin/centros/<id>
```

### Citas

```http
GET    /admin/citas
GET    /admin/citas/<id>
POST   /admin/citas
PUT    /admin/citas/<id>
DELETE /admin/citas/<id>
```

---

## Archivo de carga inicial

El proyecto incluye:

```text
datos.csv
```

y el script:

```text
carga_inicial.py
```

para automatizar la creación de registros iniciales.

---

## Autor

Miguel Ángel de Alba y Pérez
Proyecto Final Python C1 – OdontoCare