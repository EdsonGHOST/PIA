
import json

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en el archivo '{nombre_archivo}'.")
        return None



def escribir_archivo_txt(nombre_archivo, datos):
    try:
        with open(f"{nombre_archivo}.txt", "w", encoding="utf-8") as archivo:
            archivo.write(json.dumps(datos, indent=2))
        return True
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
        return False
