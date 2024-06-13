import numpy_financial as npf

def calcular_cuota_mensual(monto, plazo, tasa_interes_anual=18, aplica_cuota_balon=True, cuota_balon_porcentaje=1, \
                           aporte_inicial=None, aporte_inicial_porcentaje=10, \
                            seguro_porcentaje=0.75):
    
    cuota_balon = 0
    
    if aporte_inicial is None:
        aporte_inicial = monto*(aporte_inicial_porcentaje/100)

    if monto<0 or aporte_inicial<0 or plazo<0:
        raise ValueError("Solo se permiten valores positivos para las variables: monto, aporte inicial y plazo")
    if plazo % 6 != 0:
        raise ValueError("El plazo solo puede tomar valores que sean divisibles entre 6")

    if aplica_cuota_balon:
        cuota_balon = (monto*(cuota_balon_porcentaje/100))
    # Monto del préstamo después del aporte inicial
    monto_prestamo = monto - aporte_inicial - cuota_balon 
    
    # Convertir tasa anual a mensual y de porcentaje a decimal
    tasa_interes_mensual = (tasa_interes_anual) / 12 / 100  
    tasa_seguro_anual = seguro_porcentaje*0.87/0.84*(1+(tasa_interes_anual/100))

    # Calcular la cuota mensual
    if tasa_interes_mensual > 0:
        cuota_mensual = npf.pmt(tasa_interes_mensual, plazo, -monto_prestamo)
    else:
        # Si la tasa de interés es 0%, la fórmula del pago mensual es simplemente el préstamo dividido entre el número de meses
        cuota_mensual = monto_prestamo / plazo

    return cuota_mensual, \
        (monto*(tasa_seguro_anual/100)/12), \
        (tasa_interes_mensual*cuota_balon)

def obtener_detalles_cuotas(monto, plazo, tasa_interes_anual=18, aplica_cuota_balon=True, cuota_balon_porcentaje=1, \
                           aporte_inicial=None, aporte_inicial_porcentaje=10, \
                            seguro_porcentaje=0.75):
    cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto, plazo, tasa_interes_anual,\
                         aplica_cuota_balon, cuota_balon_porcentaje, aporte_inicial, aporte_inicial_porcentaje, \
                            seguro_porcentaje)
    resultado = {"Cuota k+i": round(cuota_calculada, 2),
            "Costo Adm.": round(costo_adm_calculado, 2),
            "Cuota Balon": round(cuota_balon_calculado, 2)}
    return resultado


def obtener_cuota_mensual_total(monto, plazo, tasa_interes_anual=18, cuota_balon_porcentaje=1, \
                           aporte_inicial=None, aporte_inicial_porcentaje=10, \
                            seguro_porcentaje=0.75, aplica_cuota_balon=True):
    
    cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto, plazo, tasa_interes_anual, \
                            aplica_cuota_balon, cuota_balon_porcentaje, aporte_inicial, aporte_inicial_porcentaje, \
                            seguro_porcentaje)
    
    return round(cuota_calculada + costo_adm_calculado + cuota_balon_calculado, 2), \
            {"Cuota k+i": round(cuota_calculada, 2),
            "Costo Adm.": round(costo_adm_calculado, 2),
            "Cuota Balon": round(cuota_balon_calculado, 2)}
