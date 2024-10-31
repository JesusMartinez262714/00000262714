import math as tresTristesTigres
mes=1
capitalFinal=0
continuar=True
numeroDeMeses=0


capital_inicial=float(input('Ingrese su capital inicial a invertir: '))
tasaInteres_Anual=float(input('ingrese el porcentaje de la tasa de interes: '))
numeroDeMeses=int(input('Ingrese durante cuantos meses desea invertir: '))

tasaInteres_Anual=tasaInteres_Anual/100
tasaInteres_Mensual=tasaInteres_Anual/12

print(f"""|{"":-^10}+{"":-^13}|
|{"MES":^10}|{"CAPITAL":^13}|
|{"":-^10}+{"":-^13}|""")

while continuar: 
    if numeroDeMeses >0:
        if mes <= numeroDeMeses:
            capitalFinal=capital_inicial*round(tresTristesTigres.pow(1+tasaInteres_Mensual,mes),2)
            print(f"|{mes:^10}|{round(capitalFinal, 2):^13}|")
            print(f"|{"":-^10}+{"":-^13}|")
            mes += 1

            
        else:
            break
    else:
        numeroDeMeses=int(input('error,debe ingresar al menos 1 mes '))
        continue
else:
    print('------------------------')



    