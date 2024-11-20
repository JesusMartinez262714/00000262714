# Definimos un diccionario vacío para almacenar la información de los estudiantes.
alumnos = {}

# Bucle para el menú de opciones
while True:
    print("\nMenú de Opciones:")
    print("1. Agregar estudiante")
    print("2. Imprimir listado")
    print("3. Salir")
    
    # Solicita una opción al usuario
    opcion = input("Seleccione una opción (1-3): ")

    # Opción para agregar un estudiante
    if opcion == "1":
        # Solicita un ID único para el estudiante
        while True:
            id = input("Ingrese el ID: ")
            if id in alumnos:
                print("Este ID ya está registrado. Ingrese un ID diferente.")
            else:
                break

        # Solicita el nombre del estudiante
        nombre = input("Ingrese el nombre del alumno: ")

        # Creamos una lista para almacenar las tres calificaciones
        calificaciones = []

        # Solicita y valida tres calificaciones
        for i in range(3):
            while True:
                calificacion = input(f"Ingrese la calificación {i + 1} (0 - 10): ")
                
                # Verifica si la entrada es numérica y está en el rango 0-10
                if calificacion.replace(".", "", 1).isdigit() and 0 <= float(calificacion) <= 10:
                    calificaciones.append(float(calificacion))  # Agrega la calificación a la lista
                    break
                else:
                    print("Ingrese un valor numérico entre 0 y 10.")

        # Convierte la lista de calificaciones a una tupla para hacerla inmutable
        calificaciones = tuple(calificaciones)

        # Calcula el promedio de las calificaciones
        promedio = sum(calificaciones) / len(calificaciones)

        # Agrega al estudiante al diccionario `alumnos` usando el ID como clave
        alumnos[id] = {
            "nombre": nombre,
            "calificaciones": calificaciones,
            "promedio": promedio
        }
        
        print("Estudiante agregado con éxito.")

    # Opción para imprimir el listado de estudiantes
    elif opcion == "2":
        # Validación del campo de ordenamiento (ID, nombre o promedio)
        while True:
            campo = input("Indique el campo por el que desea ordenar (0=id, 1=nombre, 2=promedio): ")
            
            # Verifica que la entrada sea un número válido y esté en el conjunto de opciones
            if campo.isdigit() and int(campo) in [0, 1, 2]:
                campo = int(campo)  # Convierte el campo en un entero para su uso en el ordenamiento
                break
            else:
                print("Opción no válida. Seleccione 0, 1 o 2.")

        # Validación del orden de clasificación (ascendente o descendente)
        while True:
            orden = input("Indique el orden (ascendente o descendente): ").strip().lower()
            
            # Verifica que la entrada sea "ascendente" o "descendente"
            if orden in ["ascendente", "descendente"]:
                ascendente = (orden == "ascendente")  # True para ascendente, False para descendente
                break
            else:
                print("Opción no válida. Ingrese 'ascendente' o 'descendente'.")

        # Ordena los estudiantes en función del campo seleccionado y el orden especificado
        if campo == 0:
            estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[0], reverse=not ascendente)
        elif campo == 1:
            estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[1]["nombre"], reverse=not ascendente)
        elif campo == 2:
            estudiantes_ordenados = sorted(alumnos.items(), key=lambda x: x[1]["promedio"], reverse=not ascendente)

        # Encabezado del listado
        print("\nListado de Estudiantes\n")
        print("ID      Nombre         Calificación1   Calificación2   Calificación3   Promedio")
        print("------  -------------  -------------   -------------   -------------   --------")

        # Variables para el conteo de aprobados, reprobados y el promedio general
        aprobados = 0
        reprobados = 0
        # Variables para el conteo de aprobados, reprobados y el promedio general
        promedio_general = 0

        # Recorre la lista ordenada de estudiantes y muestra sus datos
        for id_, datos in estudiantes_ordenados:
            nombre = datos["nombre"]
            c1, c2, c3 = datos["calificaciones"]
            promedio = datos["promedio"]
            
            # Imprime los datos de cada estudiante en el formato especificado
            print(f"{id_:<6}  {nombre:<13}  {c1:>13.2f}   {c2:>13.2f}   {c3:>13.2f}   {promedio:>8.2f}")
            
            # Actualiza los contadores de aprobados y reprobados según el promedio
            if promedio >= 7:
                aprobados += 1
            else:
                reprobados += 1
            
            # Suma los promedios individuales para calcular el promedio general
            promedio_general += promedio

        # Calcula el promedio general de todos los estudiantes
        if len(alumnos) > 0:
            promedio_general /= len(alumnos)

        # Imprime el resumen final con el total de aprobados, reprobados y el promedio general
        print("------  -------------  -------------   -------------   -------------   --------")
        print(f"Alumnos aprobados: {aprobados}   -   Alumnos reprobados: {reprobados}   -   Promedio General: {promedio_general:.2f} ")

    # Opción para salir del programa
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Finaliza el bucle y cierra el programa

    # Mensaje de error si la opción seleccionada no es válida
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

