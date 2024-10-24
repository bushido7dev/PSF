from flask import Flask, render_template, request
from colorama import init



from resultados import (
    abdominales,
    barras,
    carrera,
    flexionCodoFemenino,
    flexionCodoMasculino,
)

from nutricion import nutricion

app = Flask(__name__)

init(autoreset=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializar variables
    nombre = edad = peso = altura = sexo = resultadoCarrera = resultadoAbdominales = resultadoBarras = resultadoFlexionCodoFemenino = resultadoFlexionCodoMasculino = imc = mjeNutricion = None

    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            nombre = request.form.get('nombre')
            edad = int(request.form.get('edad', 0))  # Asegúrate de convertir a entero
            peso = float(request.form.get('peso', 0))  # Convertir a float
            altura = float(request.form.get('altura', 0))  # Convertir a float
            sexo = request.form.get('sexo')

            # Calcular IMC
            if altura > 0:  # Evitar división por cero
                imc = round(peso / (altura ** 2)*10000, 2)
            else:
                imc = "Altura no válida"

            mjeNutricion = nutricion(imc)

            # Obtener resultados
            resultadoCarrera = carrera(edad, sexo)
            resultadoAbdominales = abdominales(edad)
            resultadoBarras = barras(edad, sexo)
            resultadoFlexionCodoFemenino = flexionCodoFemenino(edad, sexo)
            resultadoFlexionCodoMasculino = flexionCodoMasculino(edad, sexo)

        except (ValueError, TypeError) as e:
            resultadoCarrera = f"Error en la entrada: {e}"
            imc = "No se pudo calcular el IMC."

    return render_template('index.html', nombre=nombre, edad=edad, peso=peso, altura=altura, sexo=sexo, resultadoFinal1=resultadoCarrera, resultadoFinal2 = resultadoAbdominales, resultadoFinal3 = resultadoBarras, resultadoFinal4 = resultadoFlexionCodoFemenino, resultadoFinal5 = resultadoFlexionCodoMasculino, imc=imc, mjeNutricion = mjeNutricion)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
