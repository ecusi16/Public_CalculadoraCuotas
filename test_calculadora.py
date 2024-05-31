import unittest
from CalculadoraCuotas.calculadora_cuotas import calcular_cuota_mensual, obtener_cuota_mensual_total

class TestCalculos(unittest.TestCase):

    def test_calcular_cuota_mensual_12_meses(self):
        # Caso de prueba 12 meses
        monto = 11000  
        plazo = 12  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 888.26
        costo_adm_esperado = 8.26
        cuota_balon = 1.47

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=2)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=2)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=2)

        # 2do Caso de prueba 12  meses
        monto = 45000  
        plazo = 12  # en meses
        aporte_inicial = 3150 
        tasa_interes_anual = 16 

        cuota_total_esperada = 3796.05

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)
        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)

        # #er Caso de prueba 12  meses
        monto = 990  
        plazo = 12  # en meses
        aporte_inicial = 69.30 # 7%
        tasa_interes_anual = 16 

        cuota_total_esperada = 83.51

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)
        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)


    def test_calcular_cuota_mensual_24_meses(self):
        # 1er Caso de prueba 24  meses
        monto = 11000  
        plazo = 24  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 479.35
        costo_adm_esperado = 8.26
        cuota_balon = 1.47

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=2)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=2)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=2)

        # 2do Caso de prueba 24  meses
        monto = 30000  
        plazo = 24  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 1307.32
        costo_adm_esperado = 22.53
        cuota_balon = 4

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=2)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=2)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=2)

        # 3er Caso de prueba 24  meses
        monto = 11000  
        plazo = 24  # en meses
        aporte_inicial = 550 
        tasa_interes_anual = 16 

        cuota_total_esperada = 516.01

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)
        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)

        # 4to Caso de prueba 24  meses
        monto = 11000  
        plazo = 24  # en meses
        aporte_inicial = 154 
        tasa_interes_anual = 16 

        cuota_total_esperada = 535.39

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)
        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)


    def test_calcular_cuota_mensual_36_meses(self):
        # Caso de prueba 36 meses
        monto = 11000  
        plazo = 36  # en meses
        aporte_inicial = 110 
        tasa_interes_anual = 16 

        cuota_total_esperada = 388.719

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)

        # Caso de prueba 36 meses
        monto = 11000  
        plazo = 36  # en meses
        aporte_inicial = 2200 
        tasa_interes_anual = 16 

        cuota_total_esperada = 315.2411

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)

        # Caso de prueba 36 meses
        monto = 11000  
        plazo = 36  # en meses
        aporte_inicial = 1650 
        tasa_interes_anual = 16 

        cuota_total_esperada = 334.5775

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)

    def test_calcular_cuota_mensual_48_meses(self):
        # Caso de prueba 48 meses
        monto = 11000  
        plazo = 48  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_total_esperada = 287.18

        cuota_mensual_total, _ = obtener_cuota_mensual_total(monto,
                                                        plazo,
                                                        aporte_inicial=aporte_inicial, 
                                                        tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_mensual_total, cuota_total_esperada, places=2)


    def test_valores_negativos(self):
        with self.assertRaises(ValueError) as cm:
            calcular_cuota_mensual(-1000, 12)
        self.assertEqual(str(cm.exception), "Solo se permiten valores positivos para las variables: monto, aporte inicial y plazo")
        
        with self.assertRaises(ValueError) as cm:
            calcular_cuota_mensual(1000, 12, aporte_inicial=-500)
        self.assertEqual(str(cm.exception), "Solo se permiten valores positivos para las variables: monto, aporte inicial y plazo")
        
        with self.assertRaises(ValueError) as cm:
            calcular_cuota_mensual(1000, -12)
        self.assertEqual(str(cm.exception), "Solo se permiten valores positivos para las variables: monto, aporte inicial y plazo")
    
    
    def test_plazo_no_multiplo_de_6(self):
        with self.assertRaises(ValueError) as cm:
            calcular_cuota_mensual(1000, 7)
        self.assertEqual(str(cm.exception), "El plazo solo puede tomar valores que sean divisibles entre 6")
    

if __name__ == '__main__':
    unittest.main()
