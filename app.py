from flask import Flask, render_template, request, Blueprint, flash, make_response, session
from calculadora_cuotas import obtener_cuota_mensual_total
from datetime import datetime
import pdfkit

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    cuota_mensual = None
    detalles = None
    tasa_interes = 18  # Tasa de interés predeterminada
    monto = session.get('monto')
    plazo = session.get('plazo')
    aporte_inicial_percent = session.get('aporte_inicial')
    cuota_balon = session.get('cuota_balon')
    
    # Obtener la fecha actual
    fecha_calculo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        try:
            monto = float(request.form['monto'].replace(',', ''))
            plazo = int(request.form['plazo'])
            aporte_inicial_percent = float(request.form['aporte_inicial'])
            aporte_inicial = monto * (aporte_inicial_percent / 100)
            cuota_balon = request.form.get('cuota_balon', 'NO') == 'SI'

            if plazo not in [6, 12, 24, 36, 48, 60]:
                raise ValueError("El plazo solo puede tomar valores de 6, 12, 24, 36, 48 o 60 meses")

            if monto<=aporte_inicial:
                raise ValueError("La cuota inicial no puede ser igual o mayor al monto del préstamo")
            
            if monto<=0 or plazo<=0 or aporte_inicial<0:
                raise ValueError("Las entradas deben tomar valores positivos")

            cuota_mensual, detalles = obtener_cuota_mensual_total(monto, plazo, \
                                    aplica_cuota_balon=cuota_balon, aporte_inicial=aporte_inicial, \
                                    aporte_inicial_porcentaje=aporte_inicial_percent)
            
            # Guardar los valores en la sesión
            session['monto'] = monto
            session['plazo'] = plazo
            session['aporte_inicial'] = aporte_inicial_percent
            session['cuota_balon'] = cuota_balon
            
            return render_template('index.html', cuota_mensual=cuota_mensual, detalles=detalles, \
                            tasa_interes=tasa_interes, monto=monto, \
                            plazo=plazo, aporte_inicial=aporte_inicial_percent,\
                            cuota_balon=cuota_balon,\
                            fecha_calculo=fecha_calculo)
        except ValueError as e:
            error_message = str(e)
        except Exception as e:
            print(e)
            error_message = "Ocurrió un error inesperado. Por favor, verifica tus entradas y vuelve a intentarlo."

        flash(error_message, 'danger')
    
    return render_template('index.html', cuota_mensual=cuota_mensual, \
                           detalles=detalles, \
                           tasa_interes=tasa_interes, monto=monto, \
                           plazo=plazo, aporte_inicial=aporte_inicial_percent,\
                           cuota_balon=cuota_balon,\
                           fecha_calculo=fecha_calculo)

@main.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener los datos del formulario
    monto = request.form.get('monto')
    plazo = request.form.get('plazo')
    aporte_inicial = request.form.get('aporte_inicial')
    tasa_interes = request.form.get('tasa_interes')
    
    # Realizar el cálculo de la cuota mensual (ejemplo simplificado)
    cuota_mensual = 89.8  # Aquí deberías poner tu cálculo real
    detalles_cuota = {
        'cuota_ki': 88.92,
        'costo_adm': 0.75,
        'cuota_balon': 0.13
    }
    detalles_prestamo = {
        'monto': monto,
        'plazo': plazo,
        'aporte_inicial': aporte_inicial,
        'tasa_interes': tasa_interes
    }
    
    # Obtener la fecha actual
    fecha_calculo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Renderizar la plantilla HTML para el PDF
    rendered = render_template('pdf_template.html', 
                               cuota_mensual=cuota_mensual, 
                               detalles_cuota=detalles_cuota,
                               detalles_prestamo=detalles_prestamo,
                               fecha_calculo=fecha_calculo)
    
    # Convertir la plantilla HTML a PDF
    pdf = pdfkit.from_string(rendered, False)
    
    # Crear la respuesta de Flask
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cuota_prestamo.pdf'
    
    return response



def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Necesario para usar flash messages
    app.register_blueprint(main)
    return app

"""if __name__ == '__main__':
    app.run(debug=True)
"""