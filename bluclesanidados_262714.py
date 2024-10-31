"""
    ejercicio:Bucle Anidados
    datos de entrada:solicitar n como numero entero positivo
    datos de salida:la secuencia de numero en base a n


    
"""

"""
while True:
    n=int(input("ingrese un numero"))
    if n>=1:
        break

contadorExterior=1

while contadorExterior <= n:
    contadorInterior=1
    while contadorInterior <= contadorExterior:
        print(contadorInterior,end=" ")
        contadorInterior +=1
    print("")
    contadorExterior+=1
"""

while True:
    n=int(input("ingrese un numero "))
    if n>=1:
        break

contadorExterior=1

while contadorExterior <= n:
    contadorInterior=1
    suma=0
    while contadorInterior <= contadorExterior:
        suma += contadorInterior
        if contadorInterior - contadorExterior:
            print(contadorInterior,end="+")
            contadorInterior +=1
        else:
            print(contadorInterior,end="=")
            contadorInterior +=1
            
        
    print(suma)
    contadorExterior+=1

