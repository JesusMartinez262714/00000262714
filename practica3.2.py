"""
Ejercicio:practica 3.2
Desarrollador: Jesus Manuel Martinez Cortez 00000262714
Objetivo:Calcular la velocidad,la altura maxima,tiempo de vuelo,distancia de un proyectil
"""
import math
GRAVEDAD=9.81
IMPULSO_POR_BOMBEO=2.5
RESISTENCIA=0.2
velocidadInicial=0
alturaMaxima=0
tiempoVuelo=0
Distancia=0


#Velocidad inicial

masa=float(input("Ingrese la masa total de el proyectil en kg: "))
angulo=float(input("Ingrese el angulo de lanzamiento: "))
bombeos=int(input("Ingrese cuantos bombeos se hicieron"))

angulo=math.radians(angulo)

velocidadInicial=IMPULSO_POR_BOMBEO*bombeos-RESISTENCIA*masa

#Altura maxima
alturaMaxima=(math.pow(velocidadInicial,2)*math.pow(math.sin(angulo),2))/(2*GRAVEDAD)

#Tiempo de vuelo
tiempoVuelo=(2*velocidadInicial*math.sin(angulo))/GRAVEDAD

#Distancia Horizontal
Distancia=(math.pow(velocidadInicial,2)*math.sin(2*angulo))/GRAVEDAD

print(f"La velocidad inicial alcanzada es de: {velocidadInicial}")
print(f"La altura maxima alcanzada es de: {alturaMaxima}")
print(f"El tiempo de vuelo alcanzado es de: {tiempoVuelo}")
print(f"La distancia horizontal alcanzada es de: {Distancia}")




