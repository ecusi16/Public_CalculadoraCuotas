from flask import Flask, render_template, request, Blueprint
from calculadora_cuotas import obtener_cuota_mensual_total

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    cuota_mensual = None
    detalles = None
    tasa_interes = 16  # Tasa de interés predeterminada
    monto = None
    plazo = None
    aporte_inicial = None
    if request.method == 'POST':
        monto = float(request.form['monto'])
        plazo = int(request.form['plazo'])
        aporte_inicial = float(request.form['aporte_inicial'])

        cuota_mensual, detalles = obtener_cuota_mensual_total(monto, plazo, aporte_inicial=aporte_inicial)
        print(cuota_mensual)
        print(aporte_inicial)
        
        return render_template('index.html', cuota_mensual=cuota_mensual, detalles=detalles, \
                           tasa_interes=tasa_interes, monto=monto, \
                           plazo=plazo, aporte_inicial=aporte_inicial)
    
    return render_template('index.html', cuota_mensual=cuota_mensual, \
                           detalles=detalles, \
                           tasa_interes=tasa_interes, monto=monto, \
                           plazo=plazo, aporte_inicial=aporte_inicial)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

"""if __name__ == '__main__':
    app.run(debug=True)
"""