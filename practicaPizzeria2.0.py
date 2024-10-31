COSTO_PIZZA=100
costo_ingrediente2=0
costo_ingrediente3=0
ingrediente2=""
ingrediente3=""
porciones_ingrediente2=0
porciones_ingrediente3=0
#datos de entrada
cant_ingredientes=int(input("Ingrese cuantos ingredientes quiere en su pizza(1,2 o 3): "))
costo_porciones=30 if cant_ingredientes==1 else 25 if cant_ingredientes==2 else 20

#proceso

#preguntar ingrediente y porciones en base a si son 1,2 o 3 ingredientes
if (cant_ingredientes==1):
    ingrediente1=input("Ingrese el ingrediente 1: ")
    porciones_ingrediente1=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))
elif(cant_ingredientes==2):

    ingrediente1=input("Ingrese el ingrediente 1: ")
    porciones_ingrediente1=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))
    ingrediente2=input("Ingrese el ingrediente 2: ")
    porciones_ingrediente2=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))

else:
    ingrediente1=input("Ingrese el ingrediente 1: ")
    porciones_ingrediente1=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))
    ingrediente2=input("Ingrese el ingrediente 2: ")
    porciones_ingrediente2=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))
    ingrediente3=input("Ingrese el ingrediente 3: ")
    porciones_ingrediente3=int(input("Ingrese cuantas porciones de ese ingrediente quiere: "))

#calcular el costo de porciones de cada ingrediente
costo_ingrediente1=porciones_ingrediente1*costo_porciones
costo_ingrediente2=porciones_ingrediente2*costo_porciones
costo_ingrediente3=porciones_ingrediente3*costo_porciones

#sumatoria total
totalApagar=costo_ingrediente1+costo_ingrediente2+costo_ingrediente3

#Datos de salida
print(f"""
{"Resumen de la venta":-^45}
{"Producto":<20} {"Cantidad":^10} {"Costo":>10}
{"Pizza Familiar":<20} {"1":^10} {"$"+str(COSTO_PIZZA):>10}
{ingrediente1:<20} {porciones_ingrediente1:^10} {"$"+str(costo_ingrediente1):>10}""")

if cant_ingredientes >= 2:
    print(f"{ingrediente2:<20} {porciones_ingrediente2:^10} {"$"+str(costo_ingrediente2):>10}")

if cant_ingredientes == 3:
    print(f"{ingrediente3:<20} {porciones_ingrediente3:^10} {"$"+str(costo_ingrediente3):>10}")


print(f"""
{"Total a pagar":<30} {"$"+str(totalApagar):>11}\n{'-':-^45}

""")
#se usan las 3 comillas en el print para realizar cadenas de textos de varias lineas y poder usar el print f de una manera mas entendible


"""
--------Resumen de la venta----------
Producto       cantidad       Costo
ingrediente1      1             $12
ingrediente2      2             $12
ingrediente3      3             $12

total a pagar                  $200
-------------------------------------
"""

