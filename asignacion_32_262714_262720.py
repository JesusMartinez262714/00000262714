"""
Una universidad desea desarrollar un sistema para almacenar y gestionar los datos académicos de sus estudiantes. El sistema debe permitir que los usuarios registren estudiantes con información básica y calificaciones, además de facilitar la consulta y organización de estos registros. Para cumplir con estos objetivos, el sistema debe incluir las siguientes funcionalidades:

En primer lugar, el sistema debe permitir registrar cada estudiante con un ID único, un nombre y tres calificaciones. A partir de las calificaciones ingresadas, se debe calcular automáticamente el promedio del estudiante y guardarlo como un dato adicional. Cada estudiante registrado debe aparecer en una lista de alumnos almacenada en el sistema.

Además, el sistema debe contar con una opción para imprimir el listado de estudiantes de forma ordenada. El usuario podrá elegir el criterio de ordenamiento de la lista, ya sea por ID, nombre o promedio. También podrá seleccionar el orden, que puede ser ascendente o descendente. Al mostrar la lista, el sistema debe presentar todos los detalles de cada estudiante: ID, nombre, tres calificaciones y promedio. También se debe incluir un resumen al final del listado, que indique el total de estudiantes aprobados y reprobados, además del promedio general de todos los estudiantes registrados.

Finalmente, el sistema debe contar con un menú de opciones que permita al usuario seleccionar entre agregar un nuevo estudiante, imprimir el listado de estudiantes o salir del programa. En caso de ingresar una opción inválida, el sistema debe notificar al usuario y pedirle que seleccione una opción válida. El objetivo es que el sistema sea fácil de usar y permita a los usuarios acceder y gestionar la información de los estudiantes de manera efectiva.

Restricciones:

Se considera que un estudiante está aprobado si su promedio es de 7.0 o superior; de lo contrario, está reprobado.
Las calificaciones se registran con valores decimales para una mayor precisión en el cálculo del promedio.
El sistema no debe cerrar hasta que el usuario elija la opción de salir del menú.

"""
# Definimos un diccionario vacío para almacenar la información de los estudiantes.
alumnos = {}


"""
opcionalmente podemos añadir esto...
def obtener_calificacion():
    while True:
        # Solicita la calificación y convierte la entrada a flotante.
        calificacion = float(input("Ingrese la calificación (0 - 10): "))          
        # Comprueba que la calificación esté en el rango de 0 a 10.
        if 0 <= calificacion <= 10:
            return calificacion
        else:
            print("La calificación debe estar entre 0 y 10.")
        """

# Definimos una función para agregar un estudiante al diccionario "alumnos".
def agregar_estudiante(alumnos:dict):
    # Solicitamos el nombre del estudiante y el ID.
     # Solicita el ID y verifica si ya existe en el diccionario "alumnos".
    while True:
        id = input("Ingrese el ID: ")
        if id in alumnos:
            print("Este ID ya está registrado. Ingrese un ID diferente.")
        else:
            break
    nombre = input("Ingrese el nombre del alumno: ")
    # Solicitamos tres calificaciones, que serán números decimales.

    """ Solicita tres calificaciones usando la función obtener_calificacion.
    calificacion1 = obtener_calificacion()
    calificacion2 = obtener_calificacion()
    calificacion3 = obtener_calificacion()"""
    # Creamos una lista vacía para almacenar las calificaciones
    calificaciones = []

        # Solicitamos y validamos tres calificaciones
    for i in range(3):
        while True:
            calificacion = input(f"Ingrese la calificación {i + 1} (0 - 10): ")
            
            # Intenta convertir la entrada a flotante y verifica que esté en rango
            if calificacion.replace(".", "", 1).isdigit() and 0 <= float(calificacion) <= 10:
                calificaciones.append(float(calificacion))
                break
            else:
                print("Ingrese un valor numérico entre 0 y 10.")


    # Convertimos la lista de calificaciones en una tupla
    calificaciones = tuple(calificaciones)

    # Calculamos el promedio
    promedio = sum(calificaciones) / len(calificaciones)

    print("Calificaciones ingresadas:", calificaciones)
    print("Promedio:", promedio)

    
    # Creamos un diccionario para el estudiante usando su ID como clave.
    alumnos[id] = {
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio
    }
    
    print("Estudiante agregado con éxito.")


    
def eliminarEstudiante(alumnos:dict):
    AlumnoEliminado=input("Ingrese el ID del alumno que desea eliminar: ")
    encontrado=False
    if AlumnoEliminado in alumnos:
        del alumnos[AlumnoEliminado]
        print("Alumno Eliminado")
        encontrado=True

    if not encontrado:
        print("Ese estudiante no existe")
    print("")

def consultarEstudiante(alumnos):
    id_buscar = input("Ingrese el ID del alumno a consultar: ")
    
    # Verifica si el ID está en el diccionario
    if id_buscar in alumnos:
        estudiante = alumnos[id_buscar]
        print(f"""+{"":-^10}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+""")
        print(f"""|{"ID":^10}|{"Nombre":^15}|{"Calificación 1":^15}|{"Calificación 2":^15}|{"Calificación 3":^15}|{"Promedio":^15}|""")
        print(f"""+{"":-^10}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+""")
        
        print(f"""|{id_buscar:^10}|{estudiante["nombre"]:^15}|{estudiante["calificaciones"][0]:^15.2f}|{estudiante["calificaciones"][1]:^15.2f}|{estudiante["calificaciones"][2]:^15.2f}|{estudiante["promedio"]:^15.2f}|""")
        
        print(f"""+{"":-^10}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+{"":-^15}+""")
    else:
        print("El estudiante con el ID proporcionado no existe.")



# Definimos una función para imprimir el listado de estudiantes, ordenado por algún criterio.
def imprimir_listado(alumnos):
    # Solicitamos el criterio de ordenamiento: ID, nombre o promedio.
    # Validación del campo de ordenamiento
    while True:
        # Solicita al usuario que indique el campo por el que desea ordenar (ID, nombre o promedio)
        campo = input("Indique el campo por el que desea ordenar (0=id, 1=nombre, 2=promedio): ")
        
        # Verifica que la entrada sea un número (dígito) y esté en los valores permitidos (0, 1 o 2)
        if campo.isdigit() and int(campo) in [0, 1, 2]:
            campo = int(campo)  # Convierte la entrada en un entero, ya que se ha validado su formato
            break  # Sale del ciclo, ya que la entrada es válida
        else:
            # Muestra un mensaje de error si la entrada no es válida y vuelve a solicitarla
            print("Opción no válida. Seleccione 0, 1 o 2.")

    # Validación del orden de clasificación
    while True:
        # Solicita al usuario que indique el orden de clasificación, eliminando espacios y convirtiendo a minúsculas
        orden = input("Indique el orden (ascendente o descendente): ").strip().lower()
        
        # Verifica que la entrada sea 'ascendente' o 'descendente'
        if orden in ["ascendente", "descendente"]:
            # Establece 'ascendente' en True si el usuario elige 'ascendente', de lo contrario, será False
            ascendente = (orden == "ascendente")
            break  # Sale del ciclo, ya que la entrada es válida
        else:
            # Muestra un mensaje de error si la entrada no es válida y vuelve a solicitarla
            print("Opción no válida. Ingrese 'ascendente' o 'descendente'.")

    ascendente = True if orden == "ascendente" else False

    # Ordenamos los estudiantes según el criterio seleccionado.
    if campo == 0:
        estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[0], reverse=not ascendente)
    elif campo == 1:
        estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[1]["nombre"], reverse=not ascendente)
    elif campo == 2:
        estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[1]["promedio"], reverse=not ascendente)

    print("\nListado de Estudiantes\n")
    print("ID      Nombre         Calificación1   Calificación2   Calificación3   Promedio")
    print("------  -------------  -------------   -------------   -------------   --------")

    aprobados = 0
    reprobados = 0
    promedio_general = 0

    for id_, datos in estudiantes_ordenados:
        nombre = datos["nombre"]
        c1, c2, c3 = datos["calificaciones"]
        promedio = datos["promedio"]
        
        print(f"{id_:<6}  {nombre:<13}  {c1:>13.2f}   {c2:>13.2f}   {c3:>13.2f}   {promedio:>8.2f}")
        
        if promedio >= 7:
            aprobados += 1
        else:
            reprobados += 1
        
        promedio_general += promedio

    if len(alumnos) > 0:
        promedio_general /= len(alumnos)

    print("------  -------------  -------------   -------------   -------------   --------")
    print(f"Alumnos aprobados: {aprobados}   -   Alumnos reprobados: {reprobados}   -   Promedio General: {promedio_general:.2f} ")

# Definimos una función para mostrar un menú de opciones y gestionar el flujo del programa.
def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar estudiante")
        print("2.-eliminar estudiante")
        print("3.-Consultar estudiante")
        print("4. Imprimir listado")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_estudiante(alumnos)
        elif opcion=="2":
            eliminarEstudiante(alumnos)
        elif opcion=="3":
            consultarEstudiante(alumnos)
        elif opcion == "4":
            imprimir_listado(alumnos)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

# Iniciamos el programa llamando a la función "menu".
menu()
