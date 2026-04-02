from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "segredo_t1_flask"

# =========================
# DADOS SIMULADOS
# =========================
usuarios = [
    {"id": 1, "nome": "Caio Silva", "email": "caio@email.com", "perfil": "Administrador"},
    {"id": 2, "nome": "Ana Souza", "email": "ana@email.com", "perfil": "Gerente"},
    {"id": 3, "nome": "Lucas Mendes", "email": "lucas@email.com", "perfil": "Vendedor"},
    {"id": 4, "nome": "Bruna Lima", "email": "bruna@email.com", "perfil": "Atendente"},
    {"id": 5, "nome": "Marcos Alves", "email": "marcos@email.com", "perfil": "Operador"},
]

produtos = [
    {"id": 1, "nome": "Mouse Gamer", "preco": "120,00", "estoque": "15", "categoria": "Periféricos"},
    {"id": 2, "nome": "Teclado Mecânico", "preco": "250,00", "estoque": "8", "categoria": "Periféricos"},
    {"id": 3, "nome": "Monitor 24 Polegadas", "preco": "899,00", "estoque": "6", "categoria": "Monitores"},
    {"id": 4, "nome": "Headset USB", "preco": "180,00", "estoque": "20", "categoria": "Áudio"},
    {"id": 5, "nome": "Notebook i5", "preco": "3500,00", "estoque": "4", "categoria": "Informática"},
]

categorias = [
    {"id": 1, "nome": "Periféricos", "descricao": "Produtos de entrada e interação", "status": "Ativa", "setor": "Tecnologia"},
    {"id": 2, "nome": "Monitores", "descricao": "Telas e monitores para uso geral", "status": "Ativa", "setor": "Tecnologia"},
    {"id": 3, "nome": "Áudio", "descricao": "Fones, caixas de som e headsets", "status": "Ativa", "setor": "Eletrônicos"},
    {"id": 4, "nome": "Informática", "descricao": "Equipamentos e acessórios de informática", "status": "Ativa", "setor": "Tecnologia"},
    {"id": 5, "nome": "Escritório", "descricao": "Itens voltados para rotina administrativa", "status": "Ativa", "setor": "Administrativo"},
]

# =========================
# ROTAS PÚBLICAS
# =========================
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        if not email or not senha:
            flash("Preencha e-mail e senha.")
            return redirect(url_for("login"))

        flash("Login realizado com sucesso.")
        return redirect(url_for("listar_usuarios"))

    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        if not nome or not email or not senha or not confirmar_senha:
            flash("Preencha todos os campos.")
            return redirect(url_for("cadastro"))

        if senha != confirmar_senha:
            flash("As senhas não coincidem.")
            return redirect(url_for("cadastro"))

        flash("Cadastro realizado com sucesso. Faça login para continuar.")
        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/logout")
def logout():
    flash("Logout realizado com sucesso.")
    return redirect(url_for("login"))

# =========================
# USUÁRIOS
# =========================
@app.route("/usuarios/listar")
def listar_usuarios():
    return render_template("usuarios/listar_usuarios.html", usuarios=usuarios)



@app.route("/usuarios/inserir", methods=["GET", "POST"])
def inserir_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        perfil = request.form.get("perfil")
        senha = request.form.get("senha")

        if not nome or not email or not perfil or not senha:
            flash("Preencha todos os campos obrigatórios do usuário.")
            return redirect(url_for("inserir_usuario"))

        novo_usuario = {
            "id": len(usuarios) + 1,
            "nome": nome,
            "email": email,
            "perfil": perfil
        }

        usuarios.append(novo_usuario)
        flash("Usuário inserido com sucesso.")
        return redirect(url_for("listar_usuarios"))

    return render_template("usuarios/inserir_usuarios.html")


@app.route("/usuarios/excluir/<int:id>")
def excluir_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    flash("Usuário excluído com sucesso.")
    return redirect(url_for("listar_usuarios"))
@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)

    if not usuario:
        flash("Usuário não encontrado.")
        return redirect(url_for("listar_usuarios"))

    if request.method == "POST":
        usuario["nome"] = request.form.get("nome")
        usuario["email"] = request.form.get("email")
        usuario["perfil"] = request.form.get("perfil")

        flash("Usuário atualizado com sucesso.")
        return redirect(url_for("listar_usuarios"))

    return render_template("usuarios/editar_usuarios.html", usuario=usuario)

# =========================
# PRODUTOS
# =========================
@app.route("/produtos/listar")
def listar_produtos():
    return render_template("produtos/listar_produtos.html", produtos=produtos)


@app.route("/produtos/inserir", methods=["GET", "POST"])
def inserir_produto():
    if request.method == "POST":
        nome = request.form.get("nome")
        preco = request.form.get("preco")
        estoque = request.form.get("estoque")
        categoria = request.form.get("categoria")

        if not nome or not preco or not estoque or not categoria:
            flash("Preencha todos os campos obrigatórios do produto.")
            return redirect(url_for("inserir_produto"))

        novo_produto = {
            "id": len(produtos) + 1,
            "nome": nome,
            "preco": preco,
            "estoque": estoque,
            "categoria": categoria
        }

        produtos.append(novo_produto)
        flash("Produto inserido com sucesso.")
        return redirect(url_for("listar_produtos"))

    return render_template("produtos/inserir.produtos.html")


@app.route("/produtos/excluir/<int:id>")
def excluir_produto(id):
    global produtos
    produtos = [produto for produto in produtos if produto["id"] != id]
    flash("Produto excluído com sucesso.")
    return redirect(url_for("listar_produtos"))

@app.route("/produtos/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    produto = next((p for p in produtos if p["id"] == id), None)

    if not produto:
        flash("Produto não encontrado.")
        return redirect(url_for("listar_produtos"))

    if request.method == "POST":
        produto["nome"] = request.form.get("nome")
        produto["preco"] = request.form.get("preco")
        produto["estoque"] = request.form.get("estoque")
        produto["categoria"] = request.form.get("categoria")

        flash("Produto atualizado com sucesso.")
        return redirect(url_for("listar_produtos"))

    return render_template("produtos/editar.produtos.html", produto=produto)

# =========================
# CATEGORIAS
# =========================
@app.route("/categorias/listar")
def listar_categorias():
    return render_template("categorias/listar_categorias.html", categorias=categorias)


@app.route("/categorias/inserir", methods=["GET", "POST"])
def inserir_categoria():
    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        status = request.form.get("status")
        setor = request.form.get("setor")

        if not nome or not descricao or not status or not setor:
            flash("Preencha todos os campos obrigatórios da categoria.")
            return redirect(url_for("inserir_categoria"))

        nova_categoria = {
            "id": len(categorias) + 1,
            "nome": nome,
            "descricao": descricao,
            "status": status,
            "setor": setor
        }

        categorias.append(nova_categoria)
        flash("Categoria inserida com sucesso.")
        return redirect(url_for("listar_categorias"))

    return render_template("categorias/inserir_categorias.html")


@app.route("/categorias/excluir/<int:id>")
def excluir_categoria(id):
    global categorias
    categorias = [categoria for categoria in categorias if categoria["id"] != id]
    flash("Categoria excluída com sucesso.")
    return redirect(url_for("listar_categorias"))

@app.route("/categorias/editar/<int:id>", methods=["GET", "POST"])
def editar_categoria(id):
    categoria = next((c for c in categorias if c["id"] == id), None)

    if not categoria:
        flash("Categoria não encontrada.")
        return redirect(url_for("listar_categorias"))

    if request.method == "POST":
        categoria["nome"] = request.form.get("nome")
        categoria["descricao"] = request.form.get("descricao")
        categoria["status"] = request.form.get("status")
        categoria["setor"] = request.form.get("setor")

        flash("Categoria atualizada com sucesso.")
        return redirect(url_for("listar_categorias"))

    return render_template("categorias/editar_categorias.html", categoria=categoria)
# =========================
# EQUIPE
# =========================
@app.route("/equipe")
def equipe():
    return render_template("sobre_equipe.html")


if __name__ == "__main__":
    app.run(debug=True)