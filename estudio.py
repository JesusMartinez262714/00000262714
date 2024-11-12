# Punto 1: Estructura de datos para almacenar mascotas y servicios
# Creamos una lista llamada `mascota` que contiene diccionarios, cada uno representando una mascota.
# Cada mascota tiene 'nombre', 'fechaNacimiento', 'ID', 'telefono', 'edad' y 'servicios' (lista de tuplas con nombre y fecha).
mascota = [
    {
        'nombre': 'duna',
        'fechaNacimiento': '2024-07-29',
        'ID': 1,
        'telefono': 6442029146,
        'edad': 1,
        'servicios': [("Consulta general", "2024-01-01")]
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
        'servicios': [("Vacunación", "2021-01-10"), ("Consulta general", "2022-05-23")]
    }
]

# Punto 2: Registro de nuevas mascotas
# El código permite registrar 3 mascotas pidiendo al usuario los datos requeridos: nombre, fecha de nacimiento, ID, teléfono del dueño, edad y servicios.
for i in range(3):
    print(f'Registro {i+1}')
    nombre = input('Ingrese el nombre de la mascota: ')
    fechaNac = input('Ingresa la fecha de nacimiento de la mascota: ')
    ID = int(input('Ingresa el ID de la mascota: '))
    telefono = int(input('Ingresa el número de teléfono del dueño: '))
    edad = float(input('Ingresa la edad de la mascota: '))

    servicios = []
    while True:
        servicio = input('Ingrese el nombre del servicio (si no desea capturar más servicios, escriba "fin"): ')
        if servicio.lower() == 'fin':
            break
        else:
            fecha = input('Ingrese la fecha en la que se realizó el servicio: ')
            servicios.append((servicio,fecha))

    nuevoRegistro = {
        'nombre': nombre,
        'fechaNacimiento': fechaNac,
        'ID': ID,
        'telefono': telefono,
        'edad': edad,
        'servicios': servicios
    }
    mascota.append(nuevoRegistro)

# Punto 3: Búsqueda de mascota
# Permite buscar una mascota específica por su nombre y teléfono del dueño.
# Si se encuentra, se muestra toda la información de la mascota; si no, muestra "No registrado".
MascotaAbuscar = input('Ingrese el nombre de la mascota a buscar: ')
telefonoAbuscar = int(input('Ingrese el número de teléfono del dueño de la mascota: '))

encontrado = False
for buscar in mascota:
    if MascotaAbuscar == buscar['nombre'] and telefonoAbuscar == buscar['telefono']:
        for x, y in buscar.items():
            if x == 'servicios':
                print(x)
                for servicio, fecha in y:
                    print(servicio, fecha)
            else:    
                print(x, y)
            encontrado = True

if not encontrado:
    print('Esa mascota no está registrada')

# Punto 4: Mostrar detalles de cada mascota
# Recorre la lista de mascotas y muestra el nombre, edad y teléfono del dueño de cada una.
for pet in mascota:
    print(pet['nombre'])
    print(pet['edad'])
    print(pet['telefono'])

# Punto 5: Ordenar mascotas por edad en orden descendente
# Ordena la lista de mascotas de mayor a menor edad y muestra el resultado.
mayores = sorted(mascota, key=lambda x: x['edad'], reverse=True)
print(mayores)

# Punto 6: Eliminar mascota por ID
# Permite eliminar una mascota según su ID y muestra un mensaje de confirmación si se eliminó con éxito.
# Si no existe una mascota con el ID proporcionado, muestra "No registrado".
id_eliminar = int(input('Ingrese el ID de la mascota a eliminar: '))

encontrado = False
for eliminar in mascota:
    if eliminar['ID'] == id_eliminar:
        mascota.remove(eliminar)
        print('Mascota eliminada')
        encontrado = True

if not encontrado:
    print('Esa mascota no existe')

# Punto 7: Filtrar mascotas con mínimo 2 servicios
# Recorre la lista de mascotas y muestra solo aquellas que tienen al menos dos servicios registrados.
for mostrar in mascota:
    if len(mostrar['servicios']) >= 2:
        for x, y in mostrar.items():
            print(x, y)
