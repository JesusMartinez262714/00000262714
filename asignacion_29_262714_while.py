'''
Desarrollador: Jesus Manuel Martinez Cortez 262714
Asignación: Calificaciones con listas y tuplas usando solo while
Objetivo: Capturar calificación y promedios de estudiantes, el promedio general y el número de aprobados.
          Todo esto sin saber cuántos estudiantes serán, utilizando listas y tuplas y únicamente bucles while.
'''

import math

# Lista global para almacenar los datos de los estudiantes
listaGlobal = []
# Inicialización de variables para almacenar promedios y contadores
promedioTotal = 0
aprobado = 0
promedioGeneral = 0

# Ciclo principal del programa
while True:
    print("1.- Agregar estudiante")
    print("2.- Imprimir lista")
    print("3.- Imprimir promedio más alto")
    print("4.- Imprimir promedio más bajo")
    print("5.- Imprimir estudiantes con promedio particular")
    print("6.- Ordenar")
    print("7.- Salir")
    opcion = int(input("Ingrese una de estas opciones: "))

    # Opción para salir del programa
    if opcion == 7:
        break

    # Opción para agregar un nuevo estudiante
    if opcion == 1:
        calificaciones = []
        nombre = input('Ingrese el nombre del estudiante: ')
        i = 1  # Contador para las calificaciones
        # Ciclo para capturar tres calificaciones
        while i <= 3:
            cal = float(input(f"Ingrese la calificación {i}: "))
            # Validar que la calificación esté en el rango adecuado
            while cal < 0 or cal > 10:
                cal = float(input(f"Ingrese la calificación {i} nuevamente (0-10): "))
            calificaciones.append(cal)  # Agregar calificación a la lista
            i += 1  # Incrementar el contador

        # Calcular el promedio individual del estudiante
        promedio_individual = round(sum(calificaciones) / 3, 2)
        alumno = (nombre, calificaciones, promedio_individual)  # Tupla con datos del estudiante
        listaGlobal.append(alumno)  # Agregar el estudiante a la lista global
        promedioTotal += promedio_individual  # Acumular el promedio total

        # Contar estudiantes aprobados
        if promedio_individual >= 7:
            aprobado += 1

    # Opción para imprimir la lista de estudiantes y sus promedios
    elif opcion == 2:
        print(f"""
{"Nombre":^14}|{"Calificación 1":^18}|{"Calificación 2":^18}|{"Calificación 3":^18}|{"Promedio":^18}
{"":-^90}""")
        
        i = 0  # Contador para iterar sobre la lista de estudiantes
        while i < len(listaGlobal):
            estudiante = listaGlobal[i]
            print(f"""{estudiante[0]:^14} {estudiante[1][0]:^18}  {estudiante[1][1]:^18}  {estudiante[1][2]:^18} {estudiante[2]:^18}
{"":-^90}""")
            i += 1  # Incrementar el contador

        # Calcular y mostrar el promedio general y la cantidad de aprobados
        if listaGlobal:  # Verificar que la lista no esté vacía
            promedioGeneral = round(promedioTotal / len(listaGlobal), 2)
            print(f"Promedio general: {promedioGeneral}")
            print(f"Cantidad de aprobados: {aprobado}")

    # Opción para imprimir el promedio más alto
    elif opcion == 3:
        if listaGlobal:  # Verificar que haya estudiantes en la lista
            calificaciones = []
            i = 0
            while i < len(listaGlobal):
                calificaciones.append(listaGlobal[i][2])  # Agregar promedios a la lista
                i += 1  # Incrementar el contador
            listaGlobal.sort(reverse=False, key=lambda estudiante: estudiante[2])  # Ordenar por promedio ascendente
            print(f"El promedio más alto es {listaGlobal[-1][0]} con {listaGlobal[-1][2]}")  # Mostrar el estudiante con el promedio más alto

    # Opción para imprimir el promedio más bajo
    elif opcion == 4:
        if listaGlobal:  # Verificar que haya estudiantes en la lista
            calificaciones = []
            i = 0
            while i < len(listaGlobal):
                calificaciones.append(listaGlobal[i][2])  # Agregar promedios a la lista
                i += 1  # Incrementar el contador
            listaGlobal.sort(reverse=True, key=lambda estudiante: estudiante[2])  # Ordenar por promedio descendente
            print(f"El promedio más bajo es {listaGlobal[-1][0]} con {listaGlobal[-1][2]}")  # Mostrar el estudiante con el promedio más bajo

    # Opción para buscar estudiantes por un promedio particular
    elif opcion == 5:
        promedios = []
        particular = float(input('Ingrese el promedio particular: '))
        i = 0
        while i < len(listaGlobal):
            # Comparar el promedio particular con los promedios de los estudiantes
            if listaGlobal[i][2] == particular:
                promedios.append(listaGlobal[i])  # Agregar a la lista de promedios
            i += 1  # Incrementar el contador
        print(f"Los estudiantes con el promedio {particular} son: {promedios}")

    # Opción para ordenar estudiantes por nombre o promedio
    elif opcion == 6:
        while True:
            print('1.- Organizar por nombre')
            print('2.- Organizar por promedio')
            print('3.- Salir')
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                print('1.- En orden ascendente (A a Z)')
                print('2.- En orden descendente (Z a A)')
                sub_opcion = int(input('Ingrese una opción: '))
                if sub_opcion == 1:
                    estudiantes_ordenados = sorted(listaGlobal, key=lambda estudiante: estudiante[0])  # Ordenar por nombre ascendente
                elif sub_opcion == 2:
                    estudiantes_ordenados = sorted(listaGlobal, key=lambda estudiante: estudiante[0], reverse=True)  # Ordenar por nombre descendente
                
                print('Estudiantes ordenados por nombre:')
                i = 0
                while i < len(estudiantes_ordenados):
                    print(estudiantes_ordenados[i])  # Imprimir estudiantes ordenados
                    i += 1  # Incrementar el contador

            elif opcion == 2:
                print('1.- En orden ascendente (menor a mayor)')
                print('2.- En orden descendente (mayor a menor)')
                sub_opcion = int(input('Ingrese una opción: '))
                if sub_opcion == 1:
                    estudiantes_ordenados = sorted(listaGlobal, key=lambda estudiante: estudiante[2])  # Ordenar por promedio ascendente
                elif sub_opcion == 2:
                    estudiantes_ordenados = sorted(listaGlobal, key=lambda estudiante: estudiante[2], reverse=True)  # Ordenar por promedio descendente
                
                print('Estudiantes ordenados por promedio:')
                i = 0
                while i < len(estudiantes_ordenados):
                    print(estudiantes_ordenados[i])  # Imprimir estudiantes ordenados
                    i += 1  # Incrementar el contador

            elif opcion == 3:
                break  # Salir del menú de ordenación

    else:
        print("Por favor ingrese una opción válida")
        print(" ")
