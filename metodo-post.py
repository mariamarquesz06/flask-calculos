from flask import Flask, request
import uuid

app = Flask(__name__)

historico = []

@app.route("/soma", methods=["POST"])
def somar():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos["numero1"]
    numero2 = dados_recebidos["numero2"]
    resultado = numero1 + numero2
    
    historico.append({
        "id": str(uuid.uuid4()),
        "numero1": numero1, 
        "numero2": numero2, 
        "resultado": resultado})
    
    return {'resultado': resultado}

@app.route("/calculos", methods=["GET"])
def calculos():
    return {'historico':historico}


@app.route("/deletar/<id>", methods=["DELETE"])
def deletar_item(id):
    global historico
    historico = [d for d in historico if d.get ('id') != id]

    return{}

@app.route("/editar/<id>", methods=["PUT"])
def editar_item(id):
    global historico
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos["numero1"]
    numero2 = dados_recebidos["numero2"]

    lista_temp = []
    for calculo in historico :
        if calculo ["id"] == id:
            resultado = numero1 + numero2
            historico.append({
            "id": id,
            "numero1": numero1, 
            "numero2": numero2, 
            "resultado": resultado})
        else:
            lista_temp.append(calculo)
    historico = lista_temp
    return{}