from flask import Flask, request

app = Flask(__name__)

historico = []

@app.route("/soma", methods=["POST"])
def somar():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos["numero1"]
    numero2 = dados_recebidos["numero2"]
    resultado = numero1 + numero2
    
    historico.append({"numero1": numero1, "numero2": numero2, "resultado": resultado})
    
    return {'resultado': resultado}

@app.route("/calculos", methods=["GET"])
def calculos():
    return {'historico':historico}