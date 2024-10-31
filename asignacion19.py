sueldo = float(input('¿Cuál es el sueldo del empleado? '))
añosTrabajando = float(input('¿Cuántos años lleva trabajando el empleado? '))
incentivo = 0

if sueldo < 5000 and (añosTrabajando >= 5 and añosTrabajando <= 10):
    incentivo = sueldo * 10 / 100
else:
    incentivo = 0


sueldoAPagar = sueldo + incentivo


print(f'El sueldo base del empleado es de {round(sueldo,2)} pesos')
print(f'El incentivo dado es de {round(incentivo,2)} pesos')
print(f'El total a pagar al empleado será de {round(sueldoAPagar,2)} pesos')
