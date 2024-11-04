
# Lista de cajas (global) almacena todas las cajas de fruta
#inventario_cajas = []
inventario_cajas=[("Sandía", "2024-10-31", 3, [("grande", "fresca"), ("pequeño", "fresca"), ("grande", "nofresca")]),("Naranjas", "2024-10-31", 3, [("pequeño", "fresca"), ("grande", "no fresca"), ("grande","fresca")])]

while True:
    print("1.-Registrar nueva caja")
    print("2.-Evaluar la calidad de las cajas")
    print("3.-Añadir mas frutas a una caja")
    print("4.-Salir")
    
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 4:
        break
    if opcion == 1:
        # iniciamos a solicitar los datos de la caja
        nombre = input("Ingrese el nombre de la fruta: ")
        fecha = input("Ingrese la fecha (YYYY/MM/DD): ")
        contador_frutas = 0 #contador de frutas, para saber cuantas hay en una caja particular
        lista_frutas_de_una_caja = []
        #iniciamos a solicitar los datos de cada fruta
        while True: #ciclo para pedir todas las frutas
            tamanio = input(f"Ingrese el tamaño de la fruta {contador_frutas+1}: ").lower()
            frescura = input(f"Ingrese la frescura de la fruta {contador_frutas+1}: ").lower()
            contador_frutas += 1
            tupla_fruta = (tamanio,frescura)
            lista_frutas_de_una_caja.append(tupla_fruta) #ya tenemos los datos de todas las frutas
            continuar = input("Desea registrar otra fruta? s/n ").lower()
            if continuar == "n":
                break
        
        # ya creamos la caja de fruta
        caja = (nombre,fecha,contador_frutas,lista_frutas_de_una_caja)
        #agregamos la caja al inventario global
        inventario_cajas.append(caja)
        
    if opcion == 2:
        print("1.-Mostrar informacion de una fruta particular (nombre fruta)")
        print("2.-Mostrar la informacion de todas las frutas")
        print("3.-Añadir")
        op_tem=int(input("Ingrese la opcion que desea: "))
        contadorBuenas=0
        contadorMalas=0
        contadorCaja=0
        if op_tem==1:
            nombre_fruta=input("Ingrese el nombre de la fruta")
            for caja in inventario_cajas:
                if caja[0]==nombre_fruta:
                    print(f"""{"No Caja":^15}|{"Tipo de fruta":^21}|{"% Frutas buenas":^19}|{"% Frutas malas":^18}
{"":-^74}""")
                    contadorCaja+=1
                    for fruta in caja[3]:#accedemos a la fruta dentro de la caja
                        if fruta[0] =="grande" and fruta[1]=="fresca":
                                contadorBuenas+=1
                        else:
                                contadorMalas+=1
                    porcentajeBuenas=round((contadorBuenas*100)/len(caja[3]),2)
                    porcentajeMalas=round((contadorMalas*100)/len(caja[3]),2)

                    print(f"""{contadorCaja:^15}|{caja[0]:^21}|{porcentajeBuenas:^19}|{porcentajeMalas:^18}
{"":-^74}""")
                    print(f"Total de cajas evaluadas {contadorCaja}")        
        elif op_tem==2:
            print(f"""{"No Caja":^15}|{"Tipo de fruta":^21}|{"% Frutas buenas":^19}|{"% Frutas malas":^18}
{"":-^74}""")
            contadorCaja=0
            for caja in inventario_cajas: #accedemos a cada caja
               
                for fruta in caja[3]:#accedemos a la fruta dentro de la caja
                    if fruta[0] =="grande" and fruta[1]=="fresca":
                        contadorBuenas+=1
                    else:
                        contadorMalas+=1
                porcentajeBuenas=round((contadorBuenas*100)/len(caja[3]),2)
                porcentajeMalas=round((contadorMalas*100)/len(caja[3]),2)

                print(f"""{contadorCaja:^15}|{caja[0]:^21}|{porcentajeBuenas:^19}|{porcentajeMalas:^18}
{"":-^74}""")
            print(f"Total de cajas evaluadas {len(inventario_cajas)}")
                
    if opcion==3:
        print("Añadir mas frutas a una caja")
    
    
        