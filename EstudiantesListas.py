'''
Desarrollador:Jesus Manuel Martinez Cortez 262714
asignacion:Calificaciones con listas
objetivo:capturar calificacion y promedios de estudiantes y el promedio general y numero de aprobados,todo esto sin saber cuantos estudiantes seran,utilizando listas
'''

import math
listaGlobal=[]
promedioTotal=0
aprobado=0
promedioGeneral=0
i=0

while True:
    print("1.- Agregar estudiante")
    print("2.-Imprimir lista")
    print("3.-Imprimir promedio mas alto")
    print("4.-Imprimir promedio mas bajo")
    print("5.-Imprimir estudiantes con promedio particular")
    print("6.-Ordenar")
    print("7.-Salir")
    opcion=int(input("Ingrese una de estas opciones "))

    if opcion==7:
        break

    if opcion==1:
        calificaciones=[]

        for i in range (1,4):
            cal=float(input(f"ingrese la calificacion {i}: "))
            while cal <0 or cal >10:
                cal=float(input(f"ingrese la calificacion {i} nuevamente (0-10): "))

            calificaciones.append(cal)

        promedio_individual=round(sum(calificaciones)/3,2)  
        calificaciones.append(promedio_individual)
        listaGlobal.append(calificaciones)
        promedioTotal+=promedio_individual

        if promedio_individual >=7:
                aprobado+=1
                

    elif opcion==2:
        contador_alumnos=0
        for estudiante in listaGlobal:
            contador_alumnos+=1
            print(f"estudiante {contador_alumnos} parcial 1 {estudiante[0]} parcial 2 {estudiante[1]} parcial 3 {estudiante[2]} promedio {estudiante[3]} ")
        
        promedioGeneral=round(promedioTotal/len(listaGlobal),2)
        print(f"promedio general {promedioGeneral}")
        print(f"cantidad de aprobados {aprobado}")

    elif opcion==3:
        calificaciones=[]
        for i in range(len(listaGlobal)):
            calificaciones.append(listaGlobal[i][3])
        listaGlobal.sort(reverse=True)
        print(f"El promedio mas alto es {calificaciones[0]}")

    elif opcion==4:
        calificaciones=[]
        for i in range(len(listaGlobal)):
            calificaciones.append(listaGlobal[i][3])
        listaGlobal.sort(reverse=False)
        print(f"El promedio mas alto es {calificaciones[0]}")

    elif opcion==5:
        promedios=[]
        particular=(input('Ingrese el promedio particular: '))
        for i in range(len(listaGlobal)):

            if particular == listaGlobal[i][3]:
                promedios.append(listaGlobal[i])
                i+=1
        print(f'Los estudiantes con el promedio {particular} son {promedios}')





    elif opcion==6:
        print("")
        


    else:
        print("Porfavor ingrese una opcion valida")
        print(" ")