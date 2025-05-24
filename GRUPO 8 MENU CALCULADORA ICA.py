"""
Calculadora del Índice de Calidad del Aire (ICA) para PM 2.5
Este programa permite calcular el ICA basado en concentraciones de PM 2.5, mostrar información sobre las categorías del ICA y proporcionar enlaces a recursos útiles.
"""

def main():
    """
    # Función principal que maneja el flujo del programa
    # Muestra el menú principal y gestiona la navegación entre opciones
    """
    continuar = True

    while continuar:
        # Muestra el menú principal con opciones para el usuario
        print("=========================================================================")
        print("         CALCULADORA DE ÍNDICE DE CALIDAD DEL AIRE PARA PM 2.5")
        print("=========================================================================")
        print("1. Calcular ICA para PM 2.5")
        print("2. Ver información sobre categorías de ICA")
        print("3. Sugerencias de páginas web sobre el ICA")
        print("4. Salir")

        # Validación de entrada para asegurar que el usuario seleccione una opción válida
        while True:
            opcion = input("Seleccione una opción (1-4): ").strip()
            if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, ingrese una de las opciones disponibles.")

        # Procesar la selección del usuario
        if opcion == "1":
            # Opción 1: Calcular el ICA basado en concentración de PM 2.5
            calcular_y_mostrar_ica()
            # Preguntar si quiere continuar usando el programa
            continuar = preguntar_continuar()
        elif opcion == "2":
            # Opción 2: Mostrar información sobre las categorías del ICA
            mostrar_info_categorias()
            # Preguntar si quiere continuar usando el programa
            continuar = preguntar_continuar()
        elif opcion == "3":
            # Opción 3: Mostrar enlaces a recursos web sobre calidad del aire
            links()
            # No preguntar si quiere continuar usando el programa (contenido en la función links)
            continue
        elif opcion == "4":
            # Opción 4: Salir del programa
            print("¡Gracias por usar la calculadora de ICA para PM 2.5!")
            continuar = False

def preguntar_continuar():
  """
  # Pregunta al usuario si desea continuar usando el programa.
  # Devuelve True si desea continuar, False si desea salir.
  """
  while True:
    seguir = input("¿Desea seguir usando el menú? (sí/no): ").strip().lower()
    if seguir == "sí" or seguir == "si":
      return True  # Vuelve al menú principal
    elif seguir == "no":
      print("¡Gracias por usar la calculadora de ICA para PM 2.5!")
      return False
      break
    else:
      print("Respuesta no válida. Escriba 'sí' o 'no'.")

def obtener_concentracion_valida():
    """
    # Solicita y valida la entrada de concentración de PM 2.5
    # Asegura que el valor ingresado sea un número positivo
    # Permite al usuario cancelar la operación
    # Retorna: float (concentración válida) o None (si se cancela)
    """
    while True:
        entrada = input("Ingrese la concentración de PM 2.5 (µg/m³) o 'cancelar' para volver: ")

        if entrada.lower() == "cancelar":
            print("Operación cancelada.")
            return None
        try:
            concentracion = float(entrada)
            if concentracion < 0:
                print("Error: La concentración debe ser un valor positivo. Intente nuevamente.")
            else:
                return concentracion
        except ValueError:
            print("Error: Debe ingresar un valor numérico. Intente nuevamente.")

def calcular_y_mostrar_ica():
    """
    # Gestiona el proceso de cálculo y visualización del ICA
    # Solicita la concentración, calcula el ICA y muestra los resultados
    """
    concentracion = obtener_concentracion_valida()

    if concentracion is not None:
        # Calcular el ICA y obtener información relacionada
        ica, categoria, color, recomendacion = calcular_ica_pm25(concentracion)

        # Mostrar resultados al usuario
        print(f"Resultados para concentración de PM 2.5 = {concentracion} µg/m³:")
        print(f"Índice de Calidad del Aire (ICA): {int(ica)}")
        print(f"Categoría: {categoria}")
        print(f"Color asociado: {color}")
        print(f"Recomendación: {recomendacion}")

def calcular_ica_pm25(concentracion):
    """
    # Calcula el Índice de Calidad del Aire basado en la concentración de PM 2.5
    # Utiliza rangos y fórmulas estándar para determinar el ICA
    # Parámetros:
    #   concentracion (float): Concentración de PM 2.5 en µg/m³
    # Retorna:
    #   tupla: (ica, categoria, color, recomendacion)
    """
    # Categoría BUENA: 0-50
    if concentracion <= 9.0:
        # Fórmula de interpolación lineal para calcular el ICA
        ica = ((50 - 0) / (9.0 - 0)) * (concentracion - 0) + 0
        categoria = "Buena"
        color = "Verde"
        recomendacion = "La calidad del aire es satisfactoria, la contaminación \npresenta poco o ningún riesgo."
    # Categoría MODERADA: 51-100
    elif concentracion <= 35.4:
        ica = ((100 - 51) / (35.4 - 9.1)) * (concentracion - 9.1) + 51
        categoria = "Moderada"
        color = "Amarillo"
        recomendacion = "La calidad del aire es aceptable, pero puede haber riesgo \npara personas muy sensibles."
    # Categoría DAÑINA PARA GRUPOS SENSIBLES: 101-150
    elif concentracion <= 55.4:
        ica = ((150 - 101) / (55.4 - 35.5)) * (concentracion - 35.5) + 101
        categoria = "Dañina para grupos sensibles"
        color = "Naranja"
        recomendacion = "Los grupos sensibles pueden experimentar efectos en la \nsalud. El público en general no suele verse afectado."
    # Categoría DAÑINA: 151-200
    elif concentracion <= 125.4:
        ica = ((200 - 151) / (125.4 - 55.5)) * (concentracion - 55.5) + 151
        categoria = "Dañina"
        color = "Rojo"
        recomendacion = "Todos pueden comenzar a experimentar efectos en la salud. \nLos grupos sensibles pueden experimentar efectos más graves."
    # Categoría MUY DAÑINA: 201-300
    elif concentracion <= 225.4:
        ica = ((300 - 201) / (225.4 - 125.5)) * (concentracion - 125.5) + 201
        categoria = "Muy dañina"
        color = "Púrpura"
        recomendacion = "Advertencias sanitarias de condiciones de emergencia. \nLa población completa tiene más probabilidades de verse afectada."
    # Categoría PELIGROSA: 301-500
    else:
        ica = ((500 - 301) / (500.4 - 225.5)) * (concentracion - 225.5) + 301
        categoria = "Peligrosa"
        color = "Marrón"
        recomendacion = "¡Alerta de salud! Todos pueden experimentar efectos \ngraves en la salud."

    return ica, categoria, color, recomendacion

def mostrar_info_categorias():
    """
    # Muestra información detallada sobre las categorías del ICA
    # Incluye rangos de valores, colores asociados y recomendaciones
    # Presenta la información de una manera visual y amigable para el usuario
    """
    print("==========================================================================")
    print("              CATEGORÍAS DEL ÍNDICE DE CALIDAD DEL AIRE")
    print("==========================================================================")

    # Definimos las categorías y sus características con formato de lista de diccionarios
    categorias = [
        {"nombre": "Buena", "rango": "0-50", "color": "Verde",
         "recomendacion": "No hay restricciones, puede hacer sus actividades al aire \n  libre con normalidad."},
        {"nombre": "Moderada", "rango": "51-100", "color": "Amarillo",
         "recomendacion": "Por favor, realice actividades cortas y no tan intensas \n  al aire libre."},
        {"nombre": "Dañina para grupos sensibles", "rango": "101-150", "color": "Naranja",
         "recomendacion": "Por favor, realice actividades cortas y no tan intensas \n  al aire libre."},
        {"nombre": "Dañina", "rango": "151-200", "color": "Rojo",
         "recomendacion": "Por favor, considere reprogramar sus actividades al \n  aire libre."},
        {"nombre": "Muy dañina", "rango": "201-300", "color": "Púrpura",
         "recomendacion": "Por favor, no realizar cualquier tipo de actividad \n  física al aire libre."},
        {"nombre": "Peligrosa", "rango": "301-500", "color": "Marrón",
         "recomendacion": "Por favor, quédese en casa hasta que la calidad del \n  aire mejore."}
    ]

    # Mostramos cada categoría con su información
    for categoria in categorias:
        print(f"• {categoria['nombre']} ({categoria['rango']}) - Color: {categoria['color']}")
        print(f"  Recomendación: {categoria['recomendacion']}")
        print("")  # Línea en blanco para separar categorías

def links():
    """
    # Muestra información sobre páginas web relacionadas con la calidad del aire
    # Permite al usuario seleccionar una opción para ver detalles específicos
    # Después de cada opción, pregunta si desea ver otra página
    """
    while True:
        print("=========================================================================")
        print("                PÁGINAS WEB SOBRE CALIDAD DEL AIRE ")
        print("=========================================================================")
        print("1. AirNow")
        print("2. AirNow Fire and Smoke Map")
        print("3. AirNow Mobile App")
        print("4. AirNow EnviroFlash")
        print("5. AirNow Widget Website")
        print("6. AirData Website")
        print("7. AirCompare Website")
        print("8. Volver al menú principal")

        opcion_web = input("Seleccione una opción (1-8): ").strip()

        if opcion_web == "1":
            print("\nAirNow:")
            print("El sitio web AirNow.gov proporciona datos sobre la calidad del aire\na nivel local, estatal, nacional e internacional. Su función principal\nes permitir a los usuarios verificar rápidamente el estado de la calidad\ndel aire mediante el AirNow Dial y acceder a recursos sobre salud y\ncalidad del aire.")
            print("Enlace: https://www.airnow.gov/\n")
        elif opcion_web == "2":
            print("\nAirNow Fire and Smoke Map:")
            print("El Mapa de Incendios y Humo de AirNow muestra información sobre la\ncalidad del aire relacionada con incendios, incluyendo datos de partículas\nfinas (PM2.5) y la ubicación de incendios. Ayuda a los usuarios a proteger\nsu salud con recomendaciones y actualizaciones sobre la calidad del aire.")
            print("Enlace: https://fire.airnow.gov/\n")
        elif opcion_web == "3":
            print("\nAirNow Mobile App:")
            print("La aplicación AirNow de la EPA permite consultar de forma rápida y\nsencilla la calidad del aire actual y pronosticada, ayudando en la\nplanificación de actividades y en la protección de la salud. Muestra el\nÍndice de Calidad del Aire (ICA) local y ofrece mapas interactivos de\ncalidad del aire y de incendios.")
            print("Enlace: https://play.google.com/store/apps/details?id=com.saic.airnow&hl=en_US&gl=US&pli=1\n")
        elif opcion_web == "4":
            print("\nAirNow EnviroFlash:")
            print("EnviroFlash de AirNow envía alertas sobre la calidad del aire a correos\nelectrónicos o teléfonos móviles, informando sobre pronósticos y condiciones\nen la ubicación seleccionada. Esto ayuda a los usuarios a planificar\nactividades al aire libre considerando la calidad del aire.")
            print("Enlace: https://m.enviroflash.info/\n")
        elif opcion_web == "5":
            print("\nAirNow Widget Website:")
            print("AirNow Widget Website permite a las organizaciones mostrar información\nsobre la calidad del aire en sus sitios web, facilitando el acceso a datos\nrelevantes y concienciando a la comunidad sobre la contaminación del aire.")
            print("Enlace: https://www.airnow.gov/aqi-widgets/\n")
        elif opcion_web == "6":
            print("\nAirData Website:")
            print("AirData proporciona datos de calidad del aire recopilados a partir de\nmonitores exteriores en Estados Unidos, Puerto Rico y las Islas Vírgenes\nEstadounidenses. Los usuarios tienen la opción de descargar, generar, ver\no visualizar estos datos, facilitando el acceso a información crucial\nsobre la contaminación del aire.")
            print("Enlace: https://www.epa.gov/outdoor-air-quality-data\n")
        elif opcion_web == "7":
            print("\nAirCompare Website:")
            print("La página web de AirCompare ofrece mapas interactivos que muestran la\ncalidad del aire en los condados de EE. UU., proporcionando datos históricos\nsobre la contaminación. Además, resalta a los grupos más vulnerables,\npromoviendo la concienciación sobre los riesgos asociados con la\ncontaminación del aire.")
            print("Enlace: https://www3.epa.gov/aircompare/\n")
        elif opcion_web == "8":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.\n")
            continue

        # Preguntar si quiere ver otra página
        while True:
            otra = input("¿Desea ver otra página? (sí/no): ").strip().lower()
            if otra == "sí" or otra == "si":
                break
            elif otra == "no":
                print("Volviendo al menú principal...\n")
                return
            else:
                print("Respuesta no válida. Por favor, escriba 'sí' o 'no'.")


# Ejecutar el programa
main()