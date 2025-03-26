from flask import Flask, request

app = Flask (__name__)

alunos = [
    {'nome': 'bernardo'},
    {'nome': 'julia'},
    {'nome': 'augusto'}
]

@app.route("/", methods=["GET"])
def metodo_get():
    return alunos 

@app.route("/", methods=["Post"])
def metodo_post():
    dados_recebidos = request.get_json()
    alunos.append(
        {'nome': dados_recebidos['nome']}
    )
    return {'mensage', 'ok'}
