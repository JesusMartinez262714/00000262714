#Definimos los panes y costos disponibles
DICCIONARIO_PANES = {
    "torcido": 10,
    "concha" : 12,
    "cuernito" : 15,
    "leño" : 13
}

# leeNombrePan()
def leeNombrePan():
    while True:
        nombre_pan = input("Ingrese el nombre del pan: ").lower()
        if nombre_pan in DICCIONARIO_PANES.keys() or nombre_pan == "fin":
            return nombre_pan
        
def calculaCostoPan(pan, cantidad):
    costo_total = 0
    for pan_actual in DICCIONARIO_PANES.keys():
        if pan_actual == pan:
            costo_total = cantidad * DICCIONARIO_PANES[pan_actual]
    return costo_total


def imprimeRecibo(listaCompras:list):
    print(f"{'La Clásica':^45}")
    print("-"*45)
    
    print(f"{'Cantidad':<15}{'Pan':<15}{'Total':<15}")
    print("-"*45)
    for pan in listaCompras:
     print(f"{pan[0]:<15}{pan[1]:<15}{f'${pan[2]}':<15}")


#Lista que almacena todos los panes de un pedido particular
listaCompras = []
#Aqui inicia el proceso de realizar una orden
while True: #Dejamos while true porque dice el problema "El programa debe solicitar el tipo de pan y la cantidad deseada, repitiéndose esta operación para cada tipo de pan deseado. "
    #iniciamos a pedir el pan
    nombre_pan = leeNombrePan()
    if nombre_pan == "fin":
        break #si dice fin, procedemos a imprimir el recibo (señal que ya no desea agregar mas panes)
    cantidad = int(input(f"Ingrese cuantos {nombre_pan} desea: "))
    costo_total = calculaCostoPan(nombre_pan,cantidad)
    tupla_pan = (cantidad,nombre_pan,costo_total) #creamos la tupla que simula el pan que se está comprando
    listaCompras.append(tupla_pan) #agregamos el pan a la lista de compras
    
# una vez que salimos del ciclo significa que ya no estamos añadiendo panes a la orden
#Procedemos con la impresión de la orden
imprimeRecibo(listaCompras)
