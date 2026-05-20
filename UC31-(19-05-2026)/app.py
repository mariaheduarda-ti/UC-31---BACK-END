from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/cliente/<nome>')
def cliente(nome):
    return render_template('cliente.html', nome=nome)

@app.route('/lanche/<nome>')
def lanche(nome):
    return render_template('lanche.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)