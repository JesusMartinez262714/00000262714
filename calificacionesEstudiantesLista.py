import math as tilin
listaGlobal=[]
promedioTotal=0
aprobado=0


for i in range(1, 11, 1):
    print(f"Alumno {i}")
    calif1=float(input("Ingrese Calificacion 1: "))
    print("")

    calif2=float(input("Ingrese Calificacion 2: "))
    print("")

    calif3=float(input("Ingrese Calificacion 3: "))
    print("")

    promedio=tilin.ceil((calif1+calif2+calif3)/3)

    listaGlobal+=[[calif1,calif2,calif3,promedio]]

    if promedio>=7:
        aprobado+=1



promedioTotal=tilin.ceil((listaGlobal[0][3]+listaGlobal[1][3]+listaGlobal[2][3]+listaGlobal[3][3]+listaGlobal[4][3]+listaGlobal[5][3]+listaGlobal[6][3]+listaGlobal[7][3]+listaGlobal[8][3]+listaGlobal[9][3])/10)





print(f"""
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"Estudiante":^16}|{"Calificacion 1":^21}|{"Calificacion 2":^21}|{"Calificacion 3":^21}|{"Promedio":^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"1":^16}|{listaGlobal[0][0]:^21}|{listaGlobal[0][1]:^21}|{listaGlobal[0][2]:^21}|{listaGlobal[0][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"2":^16}|{listaGlobal[1][0]:^21}|{listaGlobal[1][1]:^21}|{listaGlobal[1][2]:^21}|{listaGlobal[1][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"3":^16}|{listaGlobal[2][0]:^21}|{listaGlobal[2][1]:^21}|{listaGlobal[2][2]:^21}|{listaGlobal[2][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"4":^16}|{listaGlobal[3][0]:^21}|{listaGlobal[3][1]:^21}|{listaGlobal[3][2]:^21}|{listaGlobal[3][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"5":^16}|{listaGlobal[4][0]:^21}|{listaGlobal[4][1]:^21}|{listaGlobal[4][2]:^21}|{listaGlobal[4][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"6":^16}|{listaGlobal[5][0]:^21}|{listaGlobal[5][1]:^21}|{listaGlobal[5][2]:^21}|{listaGlobal[5][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"7":^16}|{listaGlobal[6][0]:^21}|{listaGlobal[6][1]:^21}|{listaGlobal[6][2]:^21}|{listaGlobal[6][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"8":^16}|{listaGlobal[7][0]:^21}|{listaGlobal[7][1]:^21}|{listaGlobal[7][2]:^21}|{listaGlobal[7][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"9":^16}|{listaGlobal[8][0]:^21}|{listaGlobal[8][1]:^21}|{listaGlobal[8][2]:^21}|{listaGlobal[8][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+
|{"10":^16}|{listaGlobal[9][0]:^21}|{listaGlobal[9][1]:^21}|{listaGlobal[9][2]:^21}|{listaGlobal[9][3]:^21}|
+{"":_^16}+{"":_^21}+{"":_^21}+{"":_^21}+{"":_^21}+

PROMEDIO GRUPAL: {promedioTotal}

NUMERO DE ESTUDIANTES APROBADOS: {aprobado}
      
""")