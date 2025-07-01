from flask import Flask, request, jsonify
from flask_cors import CORS  # Importante para desenvolvimento

app = Flask(__name__)
CORS(app)  # Habilita CORS (apenas para dev!)

@app.route('/receber-coordenadas', methods=['POST'])
def receber_coordenadas():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso"})

if __name__ == '__main__':
    app.run(debug=True)