from flask import Flask, render_template #render serve parar puxar as pags html

app = Flask(__name__)  # Convenção do flask passar esta variavel

@app.route("/") # nome do site "app" + a rota que vai ser chamada
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


if __name__ == "__main__": # Executa o codigo somente se o arquivo que foi executado for o main
    app.run(debug=True)  # Executa o site
#