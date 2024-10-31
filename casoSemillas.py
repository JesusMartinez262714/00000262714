import math as tilin

# Inicialización de variables
semilla = ""
calidad_semilla = ""
cantidad_hectareas = 0
tipoTerreno = ""
semestre = 0
precio_recipiente_fertilizante = 0
precio_costal_semillas = 0
semillam2 = 0
fertilizante_por_gramos = 0
costo_Total_Costales = 0
costo_Total_Fertilizate = 0


# Datos de entrada
semilla = input("Tipo de semilla maiz/trigo: ")
calidad_semilla = input("La calidad premium/basico: ")
semestre = int(input("Ingrese en que semestre del año se realiza el cultivo (enero-junio=1, julio-diciembre=2): "))
tipoTerreno = input("Tipo de terreno pedregoso/suave: ")
cantidad_hectareas = int(input("Ingrese cuantas hectareas desea plantar: "))
precio_costal_semillas = float(input("Ingrese el costo del costal de semillas: "))
precio_recipiente_fertilizante = float(input("Ingrese el costo del recipiente: "))


# Ternarios y seteados
semillam2 = 100 if semilla == "trigo" and tipoTerreno == "pedregoso" else \
             130 if semilla == "maiz" and tipoTerreno == "pedregoso" else \
             80 if semilla == "trigo" and tipoTerreno == "suave" else \
             115 if semilla == "maiz" and tipoTerreno == "suave" else 0

cantidad_semillas_hectarea = (semillam2 * 10000)

# Ajuste por calidad y semestre
cantidad_semillas_hectarea = ((cantidad_semillas_hectarea * 100) / 125) if calidad_semilla == "premium" and semestre == 1 and semilla == "trigo"  else \
                             ((cantidad_semillas_hectarea * 100) / 130) if calidad_semilla == "premium" and semestre == 1 and semilla == "maiz"   else \
                             ((cantidad_semillas_hectarea * 100) / 120) if calidad_semilla == "premium" and semestre == 2 and semilla == "trigo"  else \
                             ((cantidad_semillas_hectarea * 100) / 125) if calidad_semilla == "premium" and semestre == 2 and semilla == "maiz"   else \
                             cantidad_semillas_hectarea

cantidad_total_semillas = (cantidad_semillas_hectarea * cantidad_hectareas)

# Cálculo de la cantidad de fertilizante
porCada = cantidad_semillas_hectarea / 100 if tipoTerreno == "pedregoso" and semilla == "trigo" else \
          cantidad_semillas_hectarea / 130 if tipoTerreno == "pedregoso" and semilla == "maiz"  else \
          cantidad_semillas_hectarea / 90 if  tipoTerreno == "suave"     and semilla == "trigo" else \
          cantidad_semillas_hectarea / 110 if tipoTerreno == "suave"     and semilla == "maiz"  else 0

ml = 10 if tipoTerreno == "pedregoso" and semilla == "trigo" else \
     15 if tipoTerreno == "pedregoso" and semilla == "maiz"  else \
     7  if tipoTerreno == "suave"     and semilla == "trigo" else \
     10 if tipoTerreno == "suave"     and semilla == "maiz"  else 0

cantidad_fertilizante_hectarea = (ml * porCada)

#  calidad de semilla
cantidad_fertilizante_hectarea = cantidad_fertilizante_hectarea * 0.5 if calidad_semilla == "premium" else cantidad_fertilizante_hectarea

cantidad_total_fertilizante = (cantidad_fertilizante_hectarea * cantidad_hectareas)

# Cálculo de costales y recipientes
hectarea_costales = (cantidad_semillas_hectarea/1000) / 300
total_costales = (cantidad_total_semillas/1000) / 300
hectarea_recipiente = (cantidad_fertilizante_hectarea/1000) / 19
total_recipientes = (cantidad_total_fertilizante/1000) / 19

total_recipientes = tilin.ceil(total_recipientes)
total_costales = tilin.ceil(total_costales)

# Cálculo de costos
costo_Total_Costales = total_costales * precio_costal_semillas
costo_Total_Fertilizate = total_recipientes * precio_recipiente_fertilizante
total_Final = costo_Total_Fertilizate + costo_Total_Costales

# Redondeo de resultados
cantidad_total_semillas = round(cantidad_total_semillas/1000, 3)
cantidad_total_fertilizante = round(cantidad_total_fertilizante/1000, 3)
costo_Total_Costales = round(costo_Total_Costales, 3)
costo_Total_Fertilizate = round(costo_Total_Fertilizate, 3)
total_Final = round(total_Final, 3)


#Formateo
print(f"""
{"Datos de cotización":-^46}
{"Concepto":<30}Valor
{"":-^46}
{"Tipo semilla:":<30}{semilla}
{"Calidad:":<30}{calidad_semilla}
{"Terreno:":<30}{tipoTerreno}
{"Semestre:":<30}{semestre}

+{"":-^28}+{"":-^30}+{"":-^30}+{"":-^28}+
|{" Cantidad de semilla total":<28}|{" Cantidad de fertilizante ":<30}|{" Cantidad de sacos de semilla ":<28}|{" Cantidad de recipientes ":<28}|
|{" (kg)":<28}|{" total (litros)":<30}|{"":<30}|{" de fertilizante ":<28}|
+{"":-^28}+{"":-^30}+{"":-^30}+{"":-^28}+
|{cantidad_total_semillas:^28}|{cantidad_total_fertilizante:^30}|{total_costales:^30}|{total_recipientes:^28}|
+{"":-^28}+{"":-^30}+{"":-^30}+{"":-^28}+
+{"":-^28}+{"":-^30}+{"":-^28}+
|{" Costo total de la semilla ":<28}|{" Costo total del fertilizante ":<28}|{" Costo total de los insumos ":<27}|
+{"":-^28}+{"":-^30}+{"":-^28}+
|{costo_Total_Costales:^28}|{costo_Total_Fertilizate:^30}|{total_Final:^28}|
+{"":-^28}+{"":-^30}+{"":-^28}+
""")
