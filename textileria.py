"""
desarrollador:Jesus Manuel Martinez Cortez
Objetivo del programa:calcular los materiales y el tiempo necesario para producir uniformes
"""
import math
CARRETE_HILOCAFE=10000 #metros
CARRETE_HILONEGRO=25000 #metros
ROLLO_TELANEGRA=255 #metros
ROLLO_TELACAFE=365 #metros
PAQUETEBOTONES=100 #piezas
PAQUETECIERRES=25 #piezas
tela_negra_total=0
tela_cafe_total=0
hilo_negro_total=0
hilo_cafe_total=0

tallaS_falda=0
tallaM_falda=0
tallaL_falda=0
tallaXL_falda=0

tallaS_pantalon=0
tallaM_pantalon=0
tallaL_pantalon=0
tallaXL_pantalon=0

dia=1
uniforme_Cliente=0

uniformesTotales=0
faldasTotales=0
pantalonesTotales=0

uniformeNegro=0
uniformeCafe=0

tallaS_falda_total=0
tallaM_falda_total=0
tallaL_falda_total=0
tallaXL_falda_total=0

tallaS_pantalon_total=0
tallaM_pantalon_total=0
tallaL_pantalon_total=0
tallaXL_pantalon_total=0

tallaS_falda_negro=0
tallaM_falda_negro=0
tallaL_falda_negro=0
tallaXL_falda_negro=0

tallaS_pantalon_negro=0
tallaM_pantalon_negro=0
tallaL_pantalon_negro=0
tallaXL_pantalon_negro=0

tallaS_falda_cafe=0
tallaM_falda_cafe=0
tallaL_falda_cafe=0
tallaXL_falda_cafe=0

tallaS_pantalon_cafe=0
tallaM_pantalon_cafe=0
tallaL_pantalon_cafe=0
tallaXL_pantalon_cafe=0

faldas_negras_totales=0
faldas_cafe_totales=0

pantalones_negros_totales=0
pantalones_cafe_totales=0



#Pedidoss de uniformes
while dia <=7:
    print(f'Empieza el dia {dia}')
    while True:
        uniforme_Cliente = int(input("Ingrese cuantos uniformes desea: "))

        if uniforme_Cliente <500:
            print("no podemos tomar su pedido solo aceptamos pedidos de 500 en adelante")
            continue

        faldas=int(input("Ingrese cuantas faldas desea: "))
        pantalones=int(input("ingrese cuantos pantalones desea: "))

        if faldas+pantalones != uniforme_Cliente:
            print("Las cantidades no concuerdad,solicite otra vez")
            continue
       

        tallaS_falda=int(input("Ingrese cuantas faldas de talla S "))
        tallaM_falda=int(input("Ingrese cuantas faltas talla M "))
        tallaL_falda=int(input("Ingrese cuantas faldas talla L "))
        tallaXL_falda=int(input("Ingrese cuantas faldas talla XL "))

        tallasFaldas=tallaS_falda+tallaM_falda+tallaL_falda+tallaXL_falda

        tallaS_pantalon=int(input("Ingrese cuantas pantalonde talla S "))
        tallaM_pantalon=int(input("Ingrese cuantas pantalon talla M "))
        tallaL_pantalon=int(input("Ingrese cuantas pantalon talla L "))
        tallaXL_pantalon=int(input("Ingrese cuantas pantalon talla XL "))
        
        tallasPantalones=tallaS_pantalon+tallaM_pantalon+tallaL_pantalon+tallaXL_pantalon

        if tallasFaldas+tallasPantalones != uniforme_Cliente:
            print("Las cantidades no concuerdad,solicite otra vez")
            continue


        while True:
            color = input("Ingrese de qué color quiere los uniformes (negro o cafe): ").lower()
            if color == "negro" or color == "cafe":
                if color == 'negro':
                    #materiales
                    uniformeNegro+=uniforme_Cliente
                    tallaS_falda_negro+=tallaS_falda
                    tallaM_falda_negro+=tallaM_falda
                    tallaL_falda_negro+=tallaL_falda
                    tallaXL_falda_negro+=tallaXL_falda

                    faldas_negras_totales=tallaS_falda_negro+tallaM_falda_negro+tallaL_falda_negro+tallaXL_falda_negro

                    tallaS_pantalon_negro+=tallaS_pantalon
                    tallaM_pantalon_negro+=tallaM_pantalon
                    tallaL_pantalon_negro+=tallaL_pantalon
                    tallaXL_pantalon_negro+=tallaXL_pantalon
                    pantalones_negros_totales=tallaS_pantalon_negro+tallaM_pantalon_negro+tallaL_pantalon_negro+tallaXL_pantalon_negro


                    #faldas
                    tela_negra_falda_TallaS=tallaS_falda_negro*.5
                    hilo_negro_falda_TallaS=tallaS_falda_negro*100
                            
                    tela_negra_falda_TallaM=tela_negra_falda_TallaS*2
                    hilo_negro_falda_TallaM=hilo_negro_falda_TallaS*2
                            
                    tela_negra_falda_TallaL=tela_negra_falda_TallaM*1.5
                    hilo_negro_falda_TallaL=hilo_negro_falda_TallaM*1.5
                            
                    tela_negra_falda_TallaXL=tela_negra_falda_TallaL*1.20
                    hilo_negro_falda_tallaXL=hilo_negro_falda_TallaL*1.20
                    #pantalon
                    tela_negra_pantalon_TallaL=tallaL_pantalon_negro*1.7
                    hilo_negro_pantalon_TallaL=tallaL_pantalon_negro*350

                    tela_negra_pantalon_TallaM=tela_negra_pantalon_TallaL*.8
                    hilo_negro_pantalon_TallaM=hilo_negro_pantalon_TallaL*.8

                    tela_negra_pantalon_TallaS=tela_negra_pantalon_TallaL*.65
                    hilo_negro_pantalon_TallaS=hilo_negro_pantalon_TallaL*.65

                    tela_negra_pantalon_TallaXL=tela_negra_pantalon_TallaM*2
                    hilo_negro_pantalon_TallaXL=hilo_negro_pantalon_TallaM*2

                    tela_negra_total+=tela_negra_falda_TallaS+tela_negra_falda_TallaM+tela_negra_falda_TallaL+tela_negra_falda_TallaXL+tela_negra_pantalon_TallaL+tela_negra_pantalon_TallaM+tela_negra_pantalon_TallaS+tela_negra_pantalon_TallaXL
                    hilo_negro_total+=hilo_negro_falda_TallaS+hilo_negro_falda_TallaM+hilo_negro_falda_TallaL+hilo_negro_falda_tallaXL+hilo_negro_pantalon_TallaL+hilo_negro_pantalon_TallaM+hilo_negro_pantalon_TallaS+hilo_negro_pantalon_TallaXL        

                    uniformesTotales+=uniforme_Cliente
                    faldasTotales+=faldas
                    pantalonesTotales+=pantalones
                else:
                    uniformeCafe+=uniforme_Cliente
                    tallaS_falda_cafe+=tallaS_falda
                    tallaM_falda_cafe+=tallaM_falda
                    tallaL_falda_cafe+=tallaL_falda
                    tallaXL_falda_cafe+=tallaXL_falda

                    faldas_cafe_totales=tallaS_falda_cafe+tallaM_falda_cafe+tallaL_falda_cafe+tallaXL_falda_cafe

                    tallaS_pantalon_cafe+=tallaS_pantalon
                    tallaM_pantalon_cafe+=tallaM_pantalon
                    tallaL_pantalon_cafe+=tallaL_pantalon
                    tallaXL_pantalon_cafe+=tallaXL_pantalon

                    pantalones_cafe_totales=tallaS_pantalon_cafe+tallaM_pantalon_cafe+tallaL_pantalon_cafe+tallaXL_pantalon_cafe
                
                    tallaS_falda_total+=tallaS_falda
                    tallaM_falda_total+=tallaM_falda
                    tallaL_falda_total+=tallaL_falda
                    tallaXL_falda_total+=tallaXL_falda

                    tallaS_pantalon_total+=tallaS_pantalon
                    tallaM_pantalon_total+=tallaM_pantalon
                    tallaL_pantalon_total+=tallaL_pantalon
                    tallaXL_pantalon_total+=tallaXL_pantalon


                    #faldas
                    tela_cafe_falda_TallaS=tallaS_falda_cafe*.5
                    hilo_cafe_falda_TallaS=tallaS_falda_cafe*100
                            
                    tela_cafe_falda_TallaM=tela_cafe_falda_TallaS*2
                    hilo_cafe_falda_TallaM=hilo_cafe_falda_TallaS*2
                    
                            
                    tela_cafe_falda_TallaL=tela_cafe_falda_TallaM*1.5
                    hilo_cafe_falda_TallaL=hilo_cafe_falda_TallaM*1.5
                            
                    tela_cafe_falda_TallaXL=tela_cafe_falda_TallaL*1.20
                    hilo_cafe_falda_TallaXL=hilo_cafe_falda_TallaL*1.20
                    #pantalones
                    tela_cafe_pantalon_TallaL=tallaL_pantalon_cafe*1.7
                    hilo_cafe_pantalon_TallaL=tallaL_pantalon_cafe*350

                    tela_cafe_pantalon_TallaM=tela_cafe_pantalon_TallaL*.8
                    hilo_cafe_pantalon_TallaM=hilo_cafe_pantalon_TallaL*.8

                    tela_cafe_pantalon_TallaS=tela_cafe_pantalon_TallaL*.65
                    hilo_cafe_pantalon_TallaS=hilo_cafe_pantalon_TallaL*.65

                    tela_cafe_pantalon_TallaXL=tela_cafe_pantalon_TallaM*2
                    hilo_cafe_pantalon_TallaXL=hilo_cafe_pantalon_TallaM*2

                    tela_cafe_total+=tela_cafe_falda_TallaS+tela_cafe_falda_TallaM+tela_cafe_falda_TallaL+tela_cafe_falda_TallaXL+tela_cafe_pantalon_TallaL+tela_cafe_pantalon_TallaM+tela_cafe_pantalon_TallaS+tela_cafe_pantalon_TallaXL
                    hilo_cafe_total+=hilo_cafe_falda_TallaS+hilo_cafe_falda_TallaM+hilo_cafe_falda_TallaL+hilo_cafe_falda_TallaXL+hilo_cafe_pantalon_TallaL+hilo_cafe_pantalon_TallaM+hilo_cafe_pantalon_TallaS+hilo_cafe_pantalon_TallaXL

                    uniformesTotales+=uniforme_Cliente
                    faldasTotales+=faldas
                    pantalonesTotales+=pantalones    
                break  # Si el color es válido, se sale del bucle
            else:   
                print("Color no válido, solicite otra vez. Le recordamos que solo tenemos color cafe o negro.")
                continue

        tomarPedido=input("desea tomar otro pedido en este dia? (si,no)")
        if tomarPedido=="si":
            continue
        else:
            dia+=1
            break

print(uniformesTotales)

botonesTotales=uniformesTotales
cierresTotales=uniformesTotales


rollo_aComprar_tela_negra=math.ceil(tela_negra_total/ROLLO_TELANEGRA)
rollo_aComprar_tela_cafe=math.ceil(tela_cafe_total/ROLLO_TELACAFE)

carrete_aComprar_hilo_negro=math.ceil(hilo_negro_total/CARRETE_HILONEGRO)
carrete_aComprar_hilo_cafe=math.ceil(hilo_cafe_total/CARRETE_HILOCAFE)

paquete_botonesAcomprar=math.ceil(botonesTotales/PAQUETEBOTONES)
paquete_cierresAcomprar=math.ceil(cierresTotales/PAQUETECIERRES)


#trabajadores

trabajador=1 #contador
tiempo_trabaja=0
uniformesPorHora=0
uniformesPorDia=0

cant_trabajadores=int(input('Ingrese la cantidad de trabajadores disponibles: '))
while trabajador<=cant_trabajadores:
    tiempo_trabaja=int(input(f'cuanto tiempo trabaja el trabajador {trabajador} al dia: '))
    uniformesPorHora=int(input(f'cuantos uniformes por hora hace el trabajador {trabajador}: '))

    uniformesPorDia+=tiempo_trabaja*uniformesPorHora
    trabajador+=1
dias_necesarios_para_completar_pedido=math.ceil(uniformesTotales/uniformesPorDia)


print(f'en esta semana se recibieron pedidos de uniformes con un total de {uniformesTotales} uniformes completos,{faldasTotales} faldas y{pantalonesTotales} pantalones ')
print(f'de los cuales {faldas_negras_totales} fueron faldas de color negro,{pantalones_negros_totales} fueron pantalones de color negro')
print(f'de los cuales {faldas_cafe_totales} fueron faldas de color cafe ,{pantalones_cafe_totales} fueron pantalones de color cafe')
print(f'para la creacion de estos uniformes se necesitaran,{rollo_aComprar_tela_negra} rollos de tela negra,{carrete_aComprar_hilo_negro} carretes de hilo negro')
print(f'y {rollo_aComprar_tela_cafe} rollos de tela cafe,{carrete_aComprar_hilo_cafe} carretes de hilo cafe')
print(f'ademas se necesitan comprar {paquete_botonesAcomprar} paquetes de botones y {paquete_cierresAcomprar} paquetes de cierres')
print(f'se estima que con {cant_trabajadores} trabajadores,los {uniformesTotales} uniformes,estaran terminados en {dias_necesarios_para_completar_pedido} dias')