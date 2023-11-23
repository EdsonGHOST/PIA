
import requests

def consultar_api(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            datos = response.json()
            print("Datos de la API recibidos:", datos) 
            return datos
        else:
            print(f"Error en consultar la API. Código de estado: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
        return None








