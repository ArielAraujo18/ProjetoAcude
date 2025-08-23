from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pontos_armazenados = []

@app.route("/receber-coordenadas", methods=["POST"])
def receber_coordenadas():
    global pontos_armazenados
    dados = request.get_json()
    pontos = dados.get("pontos") or [dados]

    pontos_corrigidos = []
    for p in pontos:
        lat = float(p["lat"])
        lng = float(p["lng"])

        # Corrige os sinais para o RN (Sul e Oeste)
        if lat > 0:
            lat = -lat
        if lng > 0:
            lng = -lng

        pontos_corrigidos.append({
            "lat": lat,
            "lng": lng
        })

    pontos_armazenados.extend(pontos_corrigidos)
    print("Pontos recebidos (corrigidos):", pontos_armazenados)

    return jsonify({"status": "ok", "total": len(pontos_armazenados)})

@app.route("/receber-coordenadas", methods=["GET"])
def enviar_coordenadas():
    global pontos_armazenados
    return jsonify(pontos_armazenados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
