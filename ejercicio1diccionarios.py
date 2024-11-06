#Crear el diccionario de deudores
# “nombre”:“Uziel”,”adeudo”:150.00,”ciudad”:”Ciudad Obregon”, 
#“colonia”:“Centro”, “codigoPostal”:85000
#1. Crear el diccionario
deudor = {
    "nombre" : "Uziel",
    "adeudo" : 150,
    "ciudad" : "Ciudad Obregón",
    "colonia" : "Centro",
    "codigoPostal" : 85000
}
#2. Imprime el valor del adeudo
print(f'su deuda es de ${deudor["adeudo"]}')

# 3. Modifica el adeudo a $400 e imprime
deudor["adeudo"] = 400
print(f'su nueva deuda es de ${deudor["adeudo"]}')

print(deudor)
#4. agrega el correo uziel@correo.com
deudor["correo"] = "uziel@correo.com"
print(deudor)

#5. Indique la expresión para crear en un solo paso una lista 
# de deudores cuyo contenido sea solamente el diccionario deudor .
lista_deudores = [deudor]

# 6. agregar los diccionarios “nombre”:“ Andrea”,”adeudo”: 200.00,”ciudad”:” Guaymas”, “colonia”:“ San Juan”, “codigoPostal”: 83922
# “nombre”:“ Verónica”,”adeudo”: 250.00,”ciudad”:” Ciudad Obregon”, “colonia”:“Centro”, “codigoPostal”: 85000
lista_deudores.append({"nombre":"Andrea","adeudo": 200.00,"ciudad":" Guaymas","colonia":"San Juan", "codigoPostal": 83922})
lista_deudores.append({"nombre":"Veronica","adeudo": 250.00,"ciudad":" Ciudad Obregon","colonia":"Centro", "codigoPostal": 85000})
print(lista_deudores)

# Utilizando la sentencia repetitiva WHILE, muestre el código que imprime 
# los elementos de la lista deudores creada en el paso anterior.
contador = 0
while contador < len(lista_deudores):
    diccionario = lista_deudores[contador] #obtienen el diccionario
    llaves = list(diccionario.keys()) #Convertimos las llaves en una lista
    contador2 = 0
    while contador2 < len(llaves) : #iteramos sobre la lista de llaves
        print(f"{llaves[contador2]}: {diccionario[llaves[contador2]]}") #mostramos la llave junto con el valor dependiendo de la posicion
        
        contador2+=1
    print('')
    contador += 1


# Utilizando la sentencia FOR, muestre un código que imprima los 
# elementos de la lista deudores.
"""for deudor in lista_deudores:
    for x,y in deudor.items():
        print(f"{x}: {y}")
    print()
    

"""





