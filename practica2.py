import math


LADRILLOS_POR_M2=25
KG_CEMENTO_POR_M2=5
KG_YESO_POR_M2=2.5
TABLON_POR_M2=0.5

cant_m2=float(input("ingrese cuantos metros cuadrados son"))
"Prueba 1: 30"

"Prueba 2: 60"

Ladrillo=float(input("ingrese el precio de los ladrillos c/u"))
"Prueba 1: 10"

"Prueba 2: 20"

Cemento=float(input("ingrese el precio de los costales de 50kg de cemento"))
"Prueba 1: 40"

"Prueba 2: 80"

tablon_madera=float(input("ingrese el precio de los tablones de madera c/u"))
"Prueba 1: 5"

"Prueba 2: 10"

yeso=float(input("ingrese el precio de los costales de 20kg de yeso"))
"Prueba 1: 15"

"Prueba 2: 30"

cant_ladrillos_por_m2 =LADRILLOS_POR_M2*cant_m2
"Prueba 1: 25*30=750"

"Prueba 2: 25*60=1500"

cant_cemento_por_m2 =KG_CEMENTO_POR_M2*cant_m2
"Prueba 1: 5*30=150"

"Prueba 2: 5*60=300"

cant_yeso_por_m2 =KG_YESO_POR_M2*cant_m2
"Prueba 1: 2.5*30=75"

"Prueba 2: 2.5*60=150"

cant_tablones_por_m2 =TABLON_POR_M2*cant_m2
"Prueba 1: .5*30=15"

"Prueba 2: .5*60=30"

cant_costales_cemento =math.ceil(cant_cemento_por_m2/50)
"Prueba 1: 150/50=3"

"Prueba 2: 300/50=6"

cant_costales_yeso =math.ceil(cant_yeso_por_m2/20)
"Prueba 1: 75/20=4"

"Prueba 2: 150/20=8"

costo_ladrillos=cant_ladrillos_por_m2*Ladrillo
"Prueba 1: 750*10=7500"

"Prueba 2: 1500*20=30000"

costo_cemento=cant_costales_cemento*Cemento
"Prueba 1: 3*40=120"

"Prueba 2: 6*80=480"

costo_yeso=cant_yeso_por_m2*yeso
"Prueba 1: 75*15=1125"

"Prueba 2: 150*30=4500"

costo_tablones=cant_tablones_por_m2*tablon_madera
"Prueba 1: 15*5=75"

"Prueba 2: 30*10=300"




print(f'Se usaran un total de {cant_ladrillos_por_m2} ladrillos, con un costo de {costo_ladrillos} pesos' )
"Prueba 1: Se usaran un total de 750 ladrillos, con un costo de 7500 pesos"

"Prueba 2: Se usaran un total de 1500 ladrillos, con un costo de 30000 pesos"

print(f'Se usaran un total de {cant_costales_cemento} costales de cemento, con un costo de {costo_cemento} pesos' )
"Prueba 1: Se usaran un total de 3 costales de cemento, con un costo de 120 pesos"

"Prueba 2: Se usaran un total de 6 costales de cemento, con un costo de 480 pesos"

print(f'Se usaran un total de {cant_costales_yeso} costales de yeso, con un costo de {costo_yeso} pesos' )
"Prueba 1: Se usaran un total de 4 costales de yeso, con un costo de 1125 pesos"

"Prueba 2: Se usaran un total de 8 costales de yeso, con un costo de 4500 pesos"

print(f'Se usaran un total de {cant_tablones_por_m2} de tablones de madera, con un costo de {costo_tablones} pesos' )
"Prueba 1: Se usaran un total de 15 de tablones de madera, con un costo de 75 pesos"

"Prueba 2: Se usaran un total de 30 de tablones de madera, con un costo de 300 pesos"




"""
    Analisis del problema

Datos de entrada 

Sabemos que los ladrillos se venden por piezas
Sabemos que cada costal completo es de 50 kg 
Sabemos que los tablones de madera se dan por pieza
Sabemos que cada costal de yeso pesa 20 kg
Por cada metro cuadrado se necesitaran 25 ladrillos, 5 kilos de cemento, 2.5 kilos de yeso, 1/2 tablones de madera
Necesitamos saber la cantidad de metros cuadrados


Datos de salida 

Mostrar cantidad en piezas y costo total de los ladrillos.
Mostrar cantidad en costales de cemento completos y su costo total.
Mostrar cantidad de tablones de madera completos y su costo total.
Mostrar cantidad de costales de yeso completos y el costo total.
Mostrar el costo total de todos los materiales de construcción para el proyecto sumando los costos individuales de cada material.


Datos de proceso 

cantidad_de_ladrillos_por_m2 = LADRILLOS_POR_M2 * cant_m2
cantidad_de_cemento_por_m2 = KG_CEMENTO_POR_M2 * cant_m2
cantidad_de_yeso_por_m2 = KG_YESO_POR_M2 * cant_m2
cantidad_de_tablones_por_m2 = TABLON_POR_M2 * cant_m2
cantidad_de_costales_de_cemento = math.ceil(cantidad_de_cemento_por_m2 / 50)
cantidad_de_costales_de_yeso = math.ceil(cantidad_de_yeso_por_m2 / 20)
costo_de_ladrillos = cantidad_de_ladrillos_por_m2 * Ladrillo_precio_unidad
costo_del_cemento = cantidad_de_costales_de_cemento * Cemento_precio_costal
costo_del_yeso = cantidad_de_yeso_por_m2 * yeso_precio_costal
costo_de_tablones = cantidad_de_tablones_por_m2 * tablones_de_madera


Datos de trabajo 

Ladrillos por metro cuadrado = 25
Cantidad de cemento por metro cuadrado = 5
Cantidad de yeso por metro cuadrado = 2.5
Tablon por metro cuadrado = 0.5
"""


