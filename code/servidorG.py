from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import threading

app = Flask(__name__)
CORS(app)

pontos_armazenados = {
    "dados": [],
    "timestamp": 0
}

def limpar_dados_apos_delay():
    global pontos_armazenados
    time.sleep(10)
    if time.time() - pontos_armazenados["timestamp"] >= 10:
        pontos_armazenados = {"dados": [], "timestamp": 0}
        print("Dados limpos")

@app.route("/receber-coordenadas", methods=["POST"])
def receber_coordenadas():
    global pontos_armazenados
    dados = request.get_json()
    pontos = dados.get("pontos") or [dados]

    pontos_corrigidos = []
    for p in pontos:
        lat = float(p["lat"])
        lng = float(p["lng"])

        if lat > 0:
            lat = -lat
        if lng > 0:
            lng = -lng

        pontos_corrigidos.append({
            "lat": lat,
            "lng": lng
        })

    pontos_armazenados = {
        "dados": pontos_corrigidos,
        "timestamp": time.time()
    }

    threading.Thread(target=limpar_dados_apos_delay, daemon=True).start()

    print("📍 Pontos recebidos (corrigidos):", pontos_armazenados["dados"])

    return jsonify({"status": "ok", "total": len(pontos_corrigidos)})

@app.route("/receber-coordenadas", methods=["GET"])
def enviar_coordenadas():
    global pontos_armazenados
    return jsonify(pontos_armazenados["dados"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    print('servidor rodando na porta 5001')
