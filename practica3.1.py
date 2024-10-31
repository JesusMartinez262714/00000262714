"""
Ejercicio:practica 3.1
Desarrollador: Jesus Manuel Martinez Cortez 00000262714
Objetivo:Calcular el tiempo de subida y bajada de un objeto en base a su velocidad inicial y su altura deseada
"""

import math
GRAVEDAD=9.81
TiempoSubida=0
TiempoBajada=0


VelocidadIncial=float(input("Ingrese la velocidad inicial metros/segundo:  "))
AlturaDeseada=float(input("Ingrese la altura deseada en metros:   "))

TiempoSubida=(VelocidadIncial+(math.sqrt(math.pow(VelocidadIncial,2)-2*GRAVEDAD*AlturaDeseada*-1)))/GRAVEDAD

TiempoBajada=math.fabs((VelocidadIncial-(math.sqrt(math.pow(VelocidadIncial,2)-2*GRAVEDAD*AlturaDeseada*-1)))/GRAVEDAD)

print(f"El tiempo de subida es de: {TiempoSubida}")

print(f"El tiempo de bajada es de: {TiempoBajada}")

