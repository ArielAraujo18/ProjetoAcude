from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
import controle

app = Flask(__name__)
CORS(app)

def conectar_bd():
    try:
        return pymysql.connect(
            host=controle.host,
            user=controle.user,
            password=controle.password,
            database=controle.database,
            cursorclass=pymysql.cursors.DictCursor  #retorna o json
        )
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
        raise #mostra o erro

@app.route("/casas")
def listar_casas():
    try:
        conn = conectar_bd()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    Id,
                    Nome,
                    Telefone,
                    Logradouro,
                    Bairro,
                    CoordenadasM
                FROM cadastroGeral
            """)
            casas = cursor.fetchall()
        conn.close()
        return jsonify(casas)
    
    except Exception as e:
        print("Erro ao buscar dados:", e)
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
    print('Servidor rodando na porta 5003')