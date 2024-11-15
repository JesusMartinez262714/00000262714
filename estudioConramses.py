#punto 1 estructura
mascotas=[
    {
        "nombre":"duna",
        "fecha de nacimiento":"2024-07-31",
        "ID":1,
        "telefono":6442029146,
        "edad":0.4,
        "servicios":[

            ("consulta general","2024-08-12"),
            ("desparacitacion","2024-09-13"),
            ("vacuna poppy","2024-10-10")
                     
                     
        ]
    },
    {
        'nombre': 'max',
        'fechaNacimiento': '2023-03-15',
        'ID': 2,
        'telefono': 6441234567,
        'edad': 2,
        'servicios': [("Vacunación", "2023-06-20"), ("Corte de uñas", "2023-08-10")]
    },
    {
        'nombre': 'bella',
        'fechaNacimiento': '2022-11-11',
        'ID': 3,
        'telefono': 6449876543,
        'edad': 3,
        'servicios': [("Desparasitación", "2023-02-05"), ("Consulta general", "2023-07-12")]
    },
    {
        'nombre': 'rocky',
        'fechaNacimiento': '2021-05-20',
        'ID': 4,
        'telefono': 6445647382,
        'edad': 4,
        'servicios': [("Limpieza dental", "2023-03-25"), ("Chequeo anual", "2023-09-15")]
    },
    {
        'nombre': 'luna',
        'fechaNacimiento': '2020-08-08',
        'ID': 5,
        'telefono': 6441029384,
        'edad': 5,
        'servicios': [("Vacunación", "2021-01-10")]
    }
]


#punto 2 permitir registro
"""
for i in range(3):
    print(f"registor {i+1}")
    nombre=input("Ingrese el nombre de la mascota: ")
    fechaNac=input("ingrese la fecha de nacimiento de la mascota: ")
    ID=int(input("Ingrese el ID de la mascota: "))
    telefono=int(input("Ingrese el numero de telefono del dueño: "))
    edad=float(input("Ingrese la edad de la mascota en años: "))


    servicios=[]
    while True:
        servicio=input("Ingrese el nombre del servicio(si desea dejar de capturar ingrese 'fin')")
        if servicio.lower()=='fin':
            break
        else:
            fechaServicio=input("Ingrese la fecha en la que se realizo el servicio: ")
            servicios.append((servicio,fechaServicio))

    nuevoRegistro={
         "nombre":nombre,
        "fecha de nacimiento":fechaNac,
        "ID":ID,
        "telefono":telefono,
        "edad":edad,
        "servicios":servicios
    }
    mascotas.append(nuevoRegistro)
"""

#punto 3

"""
nombreAbuscar=input("Ingrese el nombre de la mascota a buscar: ")
telefonoAbuscar=int(input("Ingrese el numero de telefono del dueño de la mascota a buscar: "))
encontrado=False
for buscar in mascotas:
    if buscar["nombre"]==nombreAbuscar and buscar["telefono"]==telefonoAbuscar:
        for x,y in buscar.items():
            print(x,y)
            encontrado=True


if not encontrado:
    print("Esa mascota no esta registrada")
"""
#punto 4
"""
for iterar in mascotas:
    print(iterar["nombre"])
    print(iterar["edad"])
    print(iterar["telefono"])
    print("")
"""

"""
#punto 5
viejitos=sorted(mascotas,key=lambda x:x["edad"],reverse=True)
for ordenar in viejitos:
    for x,y in ordenar.items():
        print(x,y)
"""
#punto 6


mascotaAeliminar=int(input("Ingrese el ID de la mascota que desea eliminar: "))
encontrado=False
for eliminar in mascotas:
    if eliminar["ID"]==mascotaAeliminar:
        print("La mascota eliminada es: ")
        for x,y in eliminar.items():
            print(x,y)
        mascotas.remove(eliminar)
        print("Mascota eliminada")
        encontrado=True

if not encontrado:
    print("Esa mascota no existe")


#punto 7
"""
for mostrar in mascotas:
    if len(mostrar["servicios"]) >= 2:
        for x,y in mostrar.items():
            print(x,y)
"""