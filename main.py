
import api_handler
import file_handler
import excel_handler
import json
import data_processing
from datetime import datetime

def menu():
    while True:
        print("\n--- Menú ---")
        print("1) Información de todo el mundo")
        print("2) Información por continente (Asia)")
        print("3) Información por continente (América del Norte)")
        print("4) Información por continente (América del Sur)")
        print("5) Información de México")
        print("6) Calcular el promedio de casos en México")
        print("7) Calcular la suma de casos a nivel mundial")
        print("8) Escribe los datos en un archivo Excel")
        print("9) Lee los datos desde un archivo Excel")
        print("10) Salir del menú")

        opcion = input("Selecciona una opción (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ").lower()

        if opcion == '1':
            datos_mundo = api_handler.consultar_api("https://disease.sh/v3/covid-19/all")
            mostrar_datos(datos_mundo)
            guardar_preguntar(datos_mundo, "Información de todo el mundo")

        elif opcion == '2':
            url_asia = "https://disease.sh/v3/covid-19/continents/asia?strict=true"
            datos_asia = api_handler.consultar_api(url_asia)
            mostrar_datos(datos_asia)
            guardar_preguntar(datos_asia, "Información por continente (Asia)")

        elif opcion == '3':
            url_america_norte = "https://disease.sh/v3/covid-19/continents/North%20America?strict=true"
            datos_america_norte = api_handler.consultar_api(url_america_norte)
            mostrar_datos(datos_america_norte)
            guardar_preguntar(datos_america_norte, "Información por continente (América del Norte)")

        elif opcion == '4':
            url_america_sur = "https://disease.sh/v3/covid-19/continents/South%20America?strict=true"
            datos_america_sur = api_handler.consultar_api(url_america_sur)
            mostrar_datos(datos_america_sur)
            guardar_preguntar(datos_america_sur, "Información por continente (América del Sur)")

        elif opcion == '5':
            datos_mexico = api_handler.consultar_api("https://disease.sh/v3/covid-19/countries/Mexico")
            mostrar_datos(datos_mexico)
            guardar_preguntar(datos_mexico, "Información de México")

        elif opcion == '6':
            calcular_promedio_mexico()

        elif opcion == '7':
            calcular_suma_mundial()

        elif opcion == '8':
            escribir_datos_excel()

        elif opcion == '9':
            leer_datos_excel()

        elif opcion == '10':
            print("Saliendo del menú. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige de nuevo.")

def calcular_promedio_mexico():
    datos_mundo = api_handler.consultar_api("https://disease.sh/v3/covid-19/all")
    promedio_casos_mexico = data_processing.calcular_promedio(datos_mundo)
    print(f"\nEl promedio de casos en México es: {promedio_casos_mexico}\n")

def calcular_suma_mundial():
    datos_mundo = api_handler.consultar_api("https://disease.sh/v3/covid-19/all")
    suma_casos_mundial = data_processing.calcular_suma(datos_mundo)
    print(f"\nLa suma de casos a nivel mundial es: {suma_casos_mundial}\n")

def escribir_datos_excel():
    datos_excel = api_handler.consultar_api("https://disease.sh/v3/covid-19/all")
    excel_handler.escribir_excel("datos_mundo.xlsx", datos_excel)
    print("Datos guardados en el archivo Excel 'datos_mundo.xlsx'")

def leer_datos_excel():
    try:
        datos_desde_excel = excel_handler.leer_excel("datos_mundo.xlsx")
        mostrar_datos(datos_desde_excel)
    except FileNotFoundError:
        print("Error: El archivo Excel 'datos_mundo.xlsx' no encontrado.")

def mostrar_datos(datos):
    if datos:
        print("\nDatos:")
        print(json.dumps(datos, indent=2))
    else:
        print("Error al obtener los datos.")

def guardar_preguntar(datos, nombre_predeterminado=None):
    respuesta = input("¿Quieres guardar estos datos? (s/n):")
    if respuesta.lower() == 's':
        guardar_archivo(datos, nombre_predeterminado)

def guardar_archivo(datos, nombre_predeterminado=None):
    if nombre_predeterminado:
        nombre_archivo = nombre_predeterminado
    else:
        # Si no se proporciona un nombre específico, usa la fecha y hora actual
        nombre_archivo = f"datos_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    file_handler.escribir_archivo_txt(nombre_archivo, datos)
    print(f"Datos guardados en {nombre_archivo}.txt")

if __name__ == "__main__":
    menu()
