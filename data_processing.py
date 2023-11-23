
def calcular_promedio(datos):
    casos_hoy = datos.get('todayCases', 0)
    casos_recuperados = datos.get('todayRecovered', 0)

    try:
        promedio = (casos_hoy + casos_recuperados) / 2
        return promedio
    except (KeyError, TypeError) as e:
        raise ValueError(f"Error al calcular el promedio: {e}")

def calcular_suma(datos):
    try:
        suma_casos = sum([datos[tipo] for tipo in ['todayCases', 'active', 'critical', 'recovered', 'casesPerOneMillion']])
        return suma_casos
    except (KeyError, TypeError) as e:
        raise ValueError(f"Error al calcular la suma: {e}")



    






