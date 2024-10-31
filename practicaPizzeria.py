"""
Ejercicio:Practica Pizzeria
Desarrollador: Jesus Manuel Martinez Cortez 00000262714
Objetivo:Calcular el costo de distintos tipos de pizza dependiendo de la cantidad de ingredientes,realizar condicioner ternarias 
    y mostrar la informacion usando expresiones de cadena
"""

# Constantes
COSTO_FAMILIAR = 200
COSTO_INDIVIDUAL = 100

# Datos de entrada
tamanio = input("Ingrese el tamaño (I/F): ")
cantidad_ingredientes = int(input("Ingrese la cantidad de ingredientes: "))

costo_pizza = COSTO_INDIVIDUAL if tamanio == "I" else COSTO_FAMILIAR

costo_ingredientes = ((cantidad_ingredientes - 1) * 20 if cantidad_ingredientes > 3 else (cantidad_ingredientes - 1) * 25) if tamanio == "I" else ((cantidad_ingredientes - 1) * 35 if cantidad_ingredientes > 3 else (cantidad_ingredientes - 1) * 40)


total = costo_pizza + costo_ingredientes

tam = "Familiar" if tamanio == "F" else "Individual"


print(f"\n{'Pizza ' + tam + ' ' + str(cantidad_ingredientes) + ' ingredientes':^40}\n{'Producto':<20}{'Cantidad':<10}{'Costo':>10}\n{'Pizza ' + tam:<20}{1:<10}{costo_pizza:>10,.2f}\n{'Ingredientes':<20}{cantidad_ingredientes:<10}{costo_ingredientes:>10,.2f}\n{'Total a pagar':<30}{total:>10,.2f}")
