from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculodescuento', methods=['GET', 'POST'])
def calculoDescuento():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        resultado = numero1 * (numero2/100)
        return render_template('calculodescuento.html', resultado=resultado, numero1=numero1, numero2=numero2)
    return render_template('calculodescuento.html')


@app.route('/calculonumeros', methods=['GET', 'POST'])
def calculoNumeros():
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        resultado1 = numero1 + numero2
        resultado2 = numero1 - numero2
        resultado3 = numero1 * numero2
        resultado4 = round(numero1 / numero2,1)
        return render_template('calculonumeros.html', resultado1=resultado1,resultado2=resultado2,resultado3=resultado3,resultado4=resultado4, numero1=numero1, numero2=numero2)
    return render_template('calculonumeros.html')

@app.route('/nombreyedad', methods=['GET', 'POST'])
def nombreyedad():
    if request.method == 'POST':
        resultado= ''
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        edad1= int(request.form['edad1'])
        edad2= int(request.form['edad2'])
        if edad1 == edad2:
            resultado = nombre1+' y '+nombre2+' tienen la misma edad'
        elif edad1>edad2:
            mayor = edad1-edad2
            resultado = nombre1+' es mayor que '+nombre2+' por '+str(mayor)+ ' años'
        else:
            mayor = edad2 - edad1
            resultado = nombre2 + ' es mayor que ' + nombre1 + ' por ' + str(mayor) + ' años'
        return render_template('nombreyedad.html', resultado=resultado)
    return render_template('nombreyedad.html')

@app.route('/numerocapicua', methods=['GET', 'POST'])
def esCapicua():
    if request.method == 'POST':
        resultado = None
        numero1 = str(request.form['numero1'])
        lista= list(numero1)
        numeroInvertido = lista[::-1]
        if lista == numeroInvertido:
            resultado = "es Capicúa"
        else:
            resultado = "NO es Capicúa"
        return render_template('numerocapicua.html',numero1=numero1,resultado=resultado)
    return render_template('numerocapicua.html')


if __name__ == '__main__':
    app.run(debug=True)