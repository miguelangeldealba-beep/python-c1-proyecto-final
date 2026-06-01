import requests

# LOGIN
login_url = "http://127.0.0.1:5000/login"

login_data = {
    "username": "admin1",
    "password": "1234"
}

login_response = requests.post(login_url, json=login_data)

token = login_response.json()["token"]

print("TOKEN:")
print(token)

# OBTENER DOCTORES
headers = {
    "Authorization": f"Bearer {token}"
}

doctores_url = "http://127.0.0.1:5000/admin/doctores"

response = requests.get(doctores_url, headers=headers)

print("\nDOCTORES:")
print(response.json())