from flask import Flask, render_template, request
from calculadora_cuotas import obtener_cuota_mensual_total



@app.route('/', methods=['GET', 'POST'])
def index():
    cuota_mensual = None
    detalles = None
    tasa_interes = 16  # Tasa de interés predeterminada
    if request.method == 'POST':
        monto = float(request.form['monto'])
        plazo = int(request.form['plazo'])
        aporte_inicial = float(request.form['aporte_inicial'])

        cuota_mensual, detalles = obtener_cuota_mensual_total(monto, plazo, aporte_inicial=aporte_inicial)
        print(cuota_mensual)
        print(aporte_inicial)
        
        return render_template('index.html', cuota_mensual=cuota_mensual, detalles=detalles)
    
    return render_template('index.html', cuota_mensual=cuota_mensual, detalles=detalles, tasa_interes=tasa_interes)

def create_app():
    app = Flask(__name__)
    return app

"""if __name__ == '__main__':
    app.run(debug=True)
"""