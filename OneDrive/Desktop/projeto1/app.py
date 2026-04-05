from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return "<h1>Tela de Login</h1>"

@app.route("/cadastro")
def cadastro():
    return "<h1>Tela de Cadastro</h1>"

if __name__ == "__main__":
    app.run(debug=True)