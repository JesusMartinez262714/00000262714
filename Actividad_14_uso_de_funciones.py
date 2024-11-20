panes={
    "torcido":10,
    "concha":12 ,
    "cuernito":15,
    "leno":13,
}
lista_Compras=[

]
def leernombrePan():
    while True:
        pan=input("Ingrese el nombre del pan que desea comprar(ingrese 'fin' si desea dejar de tomar pedido): ")
        if pan in panes.keys() or pan=="fin":
            return pan
        else:
            print("Ingrese un pan valido")


def calcularCosto(pan,cantidad):
    costoTotal=0
    for panActual in panes.keys():
        if panActual==pan:
            costoTotal=cantidad*panes[panActual]
    return costoTotal
    

def listaCompras(pan,cantidad,precio):
    lista_Compras.append((pan,cantidad,precio))

def imprimeRecibo():
    suma_total=0
    print(f""" {"La clasica":^35}
{"":-^35}
{"Cantidad":<15}{"Pan":<10}Total
{"":-^35}""")
    for posiscion in lista_Compras:
        print(f"""{posiscion[0]:<15}{posiscion[1]:<10}${posiscion[2]}""")
        suma_total+=posiscion[2]
    print(f"""{"":-^35}
                         ${suma_total}""")

    

bandera=False
while True:     
    continuar=input('Desea tomar un pedido? s/n: ')
    if continuar=='s':
        pan=leernombrePan()
        cantidad=int(input(f"Ingrese cuantos {pan}s desea comprar: "))
        costo=calcularCosto(pan,cantidad)
        listaCompras(pan,cantidad,costo)
        bandera=True
    else:
        break

if not bandera:
    print('No se registro ningun pedido')


imprimeRecibo()

