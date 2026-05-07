from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):

    if sabor == "calabresa":
        return render_template('calabresa.html')

    elif sabor == "frango":
        return render_template('frango.html')

    elif sabor == "portuguesa":
        return render_template('portuguesa.html')

    else:
        return "Sabor não disponível"


if __name__ == '__main__':
    app.run(debug=True)