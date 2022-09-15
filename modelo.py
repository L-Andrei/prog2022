from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoa.db')

from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Estruturas(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(254))
    quantidade = db.Column(db.Integer)


@app.route('/criar_tabelas')
def criar_tabela():
    db.create_all()
    return 'tabelas criadas!'

@app.route('/cadastrar_estrutura')
def cadastrar_estrutura():
    resposta = jsonify({'Detalhes':'OK'})
    dados = request.get_json()
    nova_estrutura = Estruturas(**dados)
    db.session.add(nova_estrutura)
    db.session.commit()
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route('/obter_dados')
def pegar_dados():
    resposta = jsonify({'Detalhes':'OK'})
    nomes = []
    quantidades = []
    for nome in db.session.query(Estruturas.nome).all():
        nomes = nomes.append(nome)
    for quant in db.session.query(Estruturas.quantidade).all():
        quantidades = quantidades.append(quant)
    resposta = jsonify({'detalhes':'Ok','nomes':nomes,'quantidades':quantidades})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
