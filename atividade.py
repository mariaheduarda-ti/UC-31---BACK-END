#Atividade 1
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template_string("""
    <h2>Login</h2>
    <form method="post">
        Usuário: <input type="text" name="usuario"><br><br>
        Senha: <input type="password" name="senha"><br><br>
        <button type="submit">Entrar</button>
    </form>
    """)

@app.route('/alunos')
def alunos():
    alunos = [
        {"nome": "Ana", "matricula": "111"},
        {"nome": "Bruno", "matricula": "222"}
    ]

    return render_template_string("""
    <h2>Alunos</h2>
    <table border="1">
        <tr><th>Nome</th><th>Matrícula</th></tr>
        {% for a in alunos %}
        <tr>
            <td>{{ a.nome }}</td>
            <td>{{ a.matricula }}</td>
        </tr>
        {% endfor %}
    </table>
    """, alunos=alunos)

#Atividade 2

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template_string("""
    <h3>Login</h3>
    Usuário: <input type="text"><br><br>
    Senha: <input type="password"><br><br>
    <button>Entrar</button>
    """)

@app.route('/alunos')
def alunos():
    lista = [
        {"nome": "Alice", "matricula": "123456"},
        {"nome": "Bruno", "matricula": "654321"}
    ]

    return render_template_string("""
    <h3>Alunos</h3>
    <table border="1">
        <tr><th>Nome</th><th>Matrícula</th></tr>
        {% for a in lista %}
        <tr>
            <td>{{ a.nome }}</td>
            <td>{{ a.matricula }}</td>
        </tr>
        {% endfor %}
    </table>
    """, lista=lista)




#Atividade 3 
from flask import Flask

app = Flask(__name__)

# 1. Saudação personalizada
@app.route('/ola/<nome>')
def ola(nome):
    return f'Olá, {nome}! Seja bem-vinda ao sistema.'


# 2. Operação matemática
@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    soma = n1 + n2
    return f'A soma de {n1} + {n2} é {soma}'


# 3. Verificação de idade
@app.route('/idade/<nome>/<int:idade>')
def idade(nome, idade):
    if idade >= 18:
        return f'{nome} é maior de idade.'
    else:
        return f'{nome} é menor de idade.'


# 4. Produto com preço
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f'O produto {nome} custa R$ {preco:.2f}'


# 5. Mensagem repetida
@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    return (palavra + ' ') * vezes


if __name__ == '__main__':
    app.run(debug=True)