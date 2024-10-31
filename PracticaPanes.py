import math

# Constantes costos
COSTOKG_HARINA = 13  # 1 KiloGramo
COSTOL_LECHE = 18  # 1 Litro
HUEVO = 2.5  # pieza
COSTOGR_MANTEQUILLA = 8  # 100gr
COSTOGR_AZUCAR = 4.5  # 100gr
COSTOGR_SAL = 1.7  # 100gr
alquiler = 5500
gastos = 18500

descuento_aplicado_panes = 0
descuento_aplicado_galletas = 0

mes = input('Ingrese qué mes del año es: ')
panesMensuales = int(input("Ingrese cuántos panes quiere hacer en el mes: "))
docenasGalletas_mensuales = int(input("Ingrese cuántas docenas de galletas quiere hacer en el mes: "))

# Ingredientes panes convertido a KG,L
harinaTotal_panes = (panesMensuales * 800) / 1000
LecheTotal_panes = (panesMensuales * 500) / 1000
huevos_panes = panesMensuales * 6
mantequillaTotal_panes = (panesMensuales * 300) / 1000
azucarTotal_panes = (panesMensuales * 400) / 1000
salTotal_Panes = (panesMensuales * 1) / 1000

# Precio ideal
panPrecio_Ideal = (
    (harinaTotal_panes * COSTOKG_HARINA) +
    (LecheTotal_panes * COSTOL_LECHE) +
    (huevos_panes * HUEVO) +
    (mantequillaTotal_panes * (COSTOGR_MANTEQUILLA * 10)) +
    (azucarTotal_panes * (COSTOGR_AZUCAR * 10)) +
    (salTotal_Panes * (COSTOGR_SAL * 10)) +
    (alquiler / 2) + (gastos / 2) * 1.5
)

galletas_mensuales = docenasGalletas_mensuales * 12

# Ingredientes Galletas convertido a KG,L
harinaTotal_galleta = (galletas_mensuales * 500) / 1000
LecheTotal_galleta = (galletas_mensuales * 100) / 1000
huevos_galleta = galletas_mensuales * 2
mantequillaTotal_galleta = (galletas_mensuales * 25) / 1000
azucarTotal_galleta = (galletas_mensuales * 40) / 1000
salTotal_galleta = (galletas_mensuales * 2) / 1000

# Precio ideal galletas
galletasPrecio_Ideal = (
    (harinaTotal_galleta * COSTOKG_HARINA) +
    (LecheTotal_galleta * COSTOL_LECHE) +
    (huevos_galleta * HUEVO) +
    (mantequillaTotal_galleta * (COSTOGR_MANTEQUILLA * 10)) +
    (azucarTotal_galleta * (COSTOGR_AZUCAR * 10)) +
    (salTotal_galleta * (COSTOGR_SAL * 10)) +
    (alquiler / 2) + (gastos / 2) * 1.4
)

# Costo unitario por pan y galleta
pan = math.ceil(panPrecio_Ideal / panesMensuales)
galleta = math.ceil(galletasPrecio_Ideal / galletas_mensuales)



if mes == "enero" or mes == "febrero":
    panesConDescuento = panesMensuales / 2
    panesSinDescuento = panesMensuales / 2
    panConDescuento = pan * 0.80  # 20% de descuento en el 50% de los panes

    galletasConDescuento = galletas_mensuales / 2
    galletasSinDescuento = galletas_mensuales / 2
    galletaConDescuento = galleta * 0.70  # 30% de descuento en el 50% de las galletas

    # Descuento aplicado a panes
    descuento_aplicado_panes = math.ceil(pan * 0.20 * panesConDescuento)

    # Descuento aplicado a galletas
    descuento_aplicado_galletas = math.ceil(galleta * 0.30 * galletasConDescuento)

# TOTAL INGREDIENTES
harinaTotal = harinaTotal_panes + harinaTotal_galleta
LecheTotal = LecheTotal_galleta + LecheTotal_panes
HuevosTotales = huevos_galleta + huevos_panes
mantequillaTotal = mantequillaTotal_galleta + mantequillaTotal_panes
azucarTotal = azucarTotal_galleta + azucarTotal_panes
salTotal = salTotal_galleta + salTotal_Panes

# COSTOS 
gastoHarina = harinaTotal * COSTOKG_HARINA
gastoLeche = LecheTotal * COSTOL_LECHE
gastoHuevos = HuevosTotales * HUEVO
gastoMantequilla = mantequillaTotal * (COSTOGR_MANTEQUILLA * 10)
gastoAzucar = azucarTotal * (COSTOGR_AZUCAR * 10)
gastoSal = salTotal * (COSTOGR_SAL * 10)

# Descuentos en ingredientes
if harinaTotal >= 200:
    gastoHarina *= 0.88
if LecheTotal >= 300:
    gastoLeche *= 0.92
if HuevosTotales >= 300:
    gastoHuevos *= 0.85
if mantequillaTotal >= 80:
    gastoMantequilla *= 0.90
if azucarTotal >= 50:
    gastoAzucar *= 0.91
if salTotal >= 30:
    gastoSal *= 0.93

costoTotal = gastoHarina + gastoLeche + gastoHuevos + gastoMantequilla + gastoAzucar + gastoSal + alquiler + gastos

tiempo = math.ceil((panesMensuales / 5) + (docenasGalletas_mensuales * 0.5))
limite = tiempo - 550

# mostrar tiempo de produccion
if limite > 0:
    print(f"En total se requieren {tiempo} horas para la producción del mes. Por lo que se sobrepasa el límite por {limite} horas.")
else:
    print(f"En total se requieren {tiempo} horas para la producción del mes. No se sobrepasa el tiempo disponible.")

#impresion formateada
print(f"""
{"Detalles de la Producción Mensual":-^98}
{"Producto":<28}{"Cantidad Total":<24}{"Costo Unitario":<24}Ganancias
{"":_^98}
{"Pan":<28}{math.ceil(panesMensuales):<24}{math.ceil(pan):<24}{math.ceil(pan * panesMensuales)}
{"Docena de Galletas":<28}{math.ceil(docenasGalletas_mensuales):<24}{math.ceil(galleta):<24}{math.ceil(galleta * docenasGalletas_mensuales)}
{"":_^98}
""")


# Mostrar la tabla de producción mensual con descuento solo si se aplicó un descuento
if mes == "enero" or mes == "febrero":
    print(f"""
{"Detalles de la Producción Mensual Con Descuento":-^98}
{"Producto":<28}{"Cantidad Total":<24}{"Costo Unitario":<24}Ganancias
{"":_^98}
{"Pan":<28}{math.ceil(panesConDescuento):<24}{math.ceil(panConDescuento):<24}{math.ceil(panConDescuento * panesConDescuento)}
{"Docena de Galletas":<28}{math.ceil(galletasConDescuento):<24}{math.ceil(galletaConDescuento):<24}{math.ceil(galletaConDescuento * galletasConDescuento)}
{"":_^98}
""")

 
 #insumos requeridos
print(f"""
{"Detalle de los Insumos Requeridos":-^98}
{"Ingrediente":<28}{"Cantidad Total":<24}{"Costo Total":<24}Descuento Aplicado
{"":_^98}
{"Harina":<28}{math.ceil(harinaTotal):<24}{math.ceil(gastoHarina):<24}{"$ " + str(math.ceil(gastoHarina * 0.12)) if harinaTotal >= 200 else 0}
{"Leche":<28}{math.ceil(LecheTotal):<24}{math.ceil(gastoLeche):<24}{"$ " + str(math.ceil(gastoLeche * 0.08)) if LecheTotal >= 300 else 0}
{"Huevos":<28}{math.ceil(HuevosTotales):<24}{math.ceil(gastoHuevos):<24}{"$ " + str(math.ceil(gastoHuevos * 0.15)) if HuevosTotales >= 300 else 0}
{"Mantequilla":<28}{math.ceil(mantequillaTotal):<24}{math.ceil(gastoMantequilla):<24}{"$ " + str(math.ceil(gastoMantequilla * 0.10)) if mantequillaTotal >= 80 else 0}
{"Azúcar":<28}{math.ceil(azucarTotal):<24}{math.ceil(gastoAzucar):<24}{"$ " + str(math.ceil(gastoAzucar * 0.09)) if azucarTotal >= 50 else 0}
{"Sal":<28}{math.ceil(salTotal):<24}{math.ceil(gastoSal):<24}{"$ " + str(math.ceil(gastoSal * 0.07)) if salTotal >= 30 else 0}
{"":_^98}
Costo Total de los Ingredientes: {math.ceil(costoTotal)}
""")

