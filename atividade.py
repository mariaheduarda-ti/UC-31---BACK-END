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

if __name__ == '__main__':
    app.run(debug=True)