from flask import Flask, render_template, request, Blueprint, flash
from calculadora_cuotas import obtener_cuota_mensual_total

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    cuota_mensual = None
    detalles = None
    tasa_interes = 16  # Tasa de interés predeterminada
    monto = None
    plazo = None
    aporte_inicial = None
    if request.method == 'POST':
        try:
            monto = float(request.form['monto'])
            plazo = int(request.form['plazo'])
            aporte_inicial = float(request.form['aporte_inicial'])

            if plazo % 6 != 0:
                raise ValueError("El plazo solo puede tomar valores que sean divisibles entre 6")

            if monto<=aporte_inicial:
                raise ValueError("La cuota inicial no puede ser igual o mayor al monto del préstamo")
            
            if monto<=0 or plazo<=0 or aporte_inicial<0:
                raise ValueError("Las entradas deben tomar valores positivos")

            cuota_mensual, detalles = obtener_cuota_mensual_total(monto, plazo, aporte_inicial=aporte_inicial)
            
            return render_template('index.html', cuota_mensual=cuota_mensual, detalles=detalles, \
                            tasa_interes=tasa_interes, monto=monto, \
                            plazo=plazo, aporte_inicial=aporte_inicial)
        except ValueError as e:
            error_message = str(e)
        except Exception as e:
            error_message = "Ocurrió un error inesperado. Por favor, verifica tus entradas y vuelve a intentarlo."

        flash(error_message, 'danger')
    
    return render_template('index.html', cuota_mensual=cuota_mensual, \
                           detalles=detalles, \
                           tasa_interes=tasa_interes, monto=monto, \
                           plazo=plazo, aporte_inicial=aporte_inicial)


def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Necesario para usar flash messages
    app.register_blueprint(main)
    return app

"""if __name__ == '__main__':
    app.run(debug=True)
"""