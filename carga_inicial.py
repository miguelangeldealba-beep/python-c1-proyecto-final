import csv
import requests

BASE_URL = "http://127.0.0.1:5000"


def mostrar_respuesta(titulo, response):
    print(f"\n--- {titulo} ---")
    print("Status:", response.status_code)

    try:
        print(response.json())
    except Exception:
        print(response.text)


# 1. LOGIN
login_data = {
    "username": "admin",
    "password": "admin"
}

login_response = requests.post(
    f"{BASE_URL}/login",
    json=login_data
)

mostrar_respuesta("LOGIN", login_response)

if login_response.status_code != 200:
    raise SystemExit("Error: no se pudo hacer login")

token = login_response.json().get("token")

headers = {
    "Authorization": f"Bearer {token}"
}


# 2. LEER CSV Y CARGAR DATOS
with open("datos.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        tipo = fila["tipo"]

        if tipo == "paciente":
            data = {
                "nombre": fila["nombre"],
                "telefono": fila["telefono"],
                "estado": fila["estado"]
            }

            response = requests.post(
                f"{BASE_URL}/admin/pacientes",
                json=data,
                headers=headers
            )

            mostrar_respuesta("CREAR PACIENTE", response)

        elif tipo == "doctor":
            data = {
                "nombre": fila["nombre"],
                "especialidad": fila["especialidad"]
            }

            response = requests.post(
                f"{BASE_URL}/admin/doctores",
                json=data,
                headers=headers
            )

            mostrar_respuesta("CREAR DOCTOR", response)

        elif tipo == "centro":
            data = {
                "nombre": fila["nombre"],
                "direccion": fila["direccion"]
            }

            response = requests.post(
                f"{BASE_URL}/admin/centros",
                json=data,
                headers=headers
            )

            mostrar_respuesta("CREAR CENTRO", response)


# 3. CREAR CITA FINAL
cita_data = {
    "paciente_id": 1,
    "doctor_id": 1,
    "centro_id": 1,
    "fecha": "2025-06-15",
    "motivo": "Limpieza dental",
    "estado": "PENDIENTE"
}

response = requests.post(
    f"{BASE_URL}/admin/citas",
    json=cita_data,
    headers=headers
)

mostrar_respuesta("CREAR CITA", response)


# 4. MOSTRAR CITAS
response = requests.get(
    f"{BASE_URL}/admin/citas",
    headers=headers
)

mostrar_respuesta("LISTAR CITAS", response)
print("\nCLIENTE EXTERNO EJECUTADO CORRECTAMENTE")