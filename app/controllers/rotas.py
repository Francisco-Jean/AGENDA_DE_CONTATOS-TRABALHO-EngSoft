from flask.templating import render_template
from flask import request
from app import app
from app.models.models import Usuario, Contato, Buscador

# http://127.0.0.1:5000

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Cadastro")
def subsuser():
    return render_template("cadastro.html")

@app.route("/Login")
def enter():
    return render_template("entrada.html")

@app.route("/Cadastrocontato")
def subs():
    return render_template("cadastro_contato.html")

@app.route("/Buscarcontato")
def busccontato():
    return render_template("busca.html")

@app.route("/Createuser")
def criarUsuario():
    nome = request.args.get("nome")
    senha = request.args.get("senha")

    if not(nome and senha):
        valor = "Insira todos os campos."
    else:
        try:
            user = Usuario(nome, senha)
            user.saveUser()
            valor = "Usuário cadastrado com sucesso!"
        except:
            valor = "Os dados inseridos estão incorretos. Por favor, tente novamente."
    return render_template("cadastro.html", valor = valor)

@app.route("/Createcontato")
def criarConta():
    nome = request.args.get("nome")
    senha = request.args.get("senha")
    nomectt = request.args.get("nomecontato")
    numero = request.args.get("numero")
    email = request.args.get("email")

    if not(nome and senha and nomectt and numero and email):
        valor = "Insira todos os campos"
    else:
        id = Buscador.getIdUser(nome, senha)
        if not id:
            valor = "Os dados inseridos estão incorretos. Por favor, tente novamente."
        else:
            contato = Contato(id, nome,numero, email)
            contato.saveContato()
            valor = "Contato Criado com sucesso!"
    return render_template("cadastro_contato.html", valor = valor)

@app.route("/Listcontatos")
def listarContatos():
    forma = request.args.get("forma")
    dado = request.args.get("dado")
    nome = request.args.get("nome")

    if not(nome):
        lista2 = "Insira todos os campos"
        return render_template("busca.html", lista3 = lista2)
    else:
        contatos = Buscador.getContatos(forma, dado, nome)
        if not contatos:
            lista2 = "Nenhum contato encontrado"
            return render_template("busca.html", lista3 = lista2)
        else:
            lista2 = contatos

    return render_template("busca.html", lista2 = lista2)

@app.route('/Deletarea')
def deletarea():
    return render_template("deletar.html")

@app.route('/Deletarea')
def deletarea1():
    nome = request.args.get("nome")
    senha = request.args.get("senha")
    contato = request.args.get("contato")
