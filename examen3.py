Artistas=[
    [
        ("pepe","2020","GEVA"),
        "666",
        ["payaso","malabares"]
    ]
]

inventario = [
{"ID": 1, "Nombre": "Sombrero", "Cantidad": 15, "Precio": 200},
{"ID": 2, "Nombre": "Pelota", "Cantidad": 25, "Precio": 50},
{"ID": 3, "Nombre": "Aro", "Cantidad": 10, "Precio": 100}
]

def registro():
    nombre=input("Ingrese el nombre del artista: ")
    fechaNac=input("Ingrese la fecha de nacimiento del artista: ")
    Curp=input("Ingrese la curp del artista: ")
    telefono=input("Ingrese el numero de telefono")
    actuaciones=[]
    while True:
        actuacion=input("Ingrese la actuacion,(ingrese fin para salir)")
        if actuacion=="fin":
            break
        Artistas.append("actuacion")
    
    nuevoArtista=[(nombre,fechaNac,Curp),telefono,actuaciones]
    Artistas.append(nuevoArtista)

def buscaCurp(curp):
    encontrado=False
    for artista in Artistas:
        if curp==artista[0][2]:
            print(artista)
            encontrado=True
    if not encontrado:
        print(f"El artista con curp {curp} no existe")

def imprimirInventario():
    print(f"""|{"":-^10}+{"":-^10}|
|{"Nombre":^10}|{"Cantidad":^10}|
|{"":-^10}+{"":-^10}|""")
    for objeto in inventario:
        print(f"""|{objeto['Nombre']:^10}|{objeto['Cantidad']:^10}|
|{"":-^10}+{"":-^10}|""")




while True:
    print("Menu")
    print("1.-registrar artistas")
    print("2.-buscar artista por CURP")
    print("3.-Imprimir inventario")
    print("4.-Crear espectaculos")
    print("5.-Eliminar espectaculo")
    print("6.-Actualizar lista de espectaculos")
    print("7.-Salir")
    opcion=int(input("Ingrese la opcion:   "))

    if opcion==7:
        break
    elif opcion==1:
        while True:
            registro()
            respuesta=input("Desea registrar otro artista s/n: ").lower()
            if respuesta=="n":
                break
        print("")
    elif opcion==2:
        curp=input("Ingrese la curp a buscar: ")
        buscaCurp(curp)    
    elif opcion==3:
        imprimirInventario()