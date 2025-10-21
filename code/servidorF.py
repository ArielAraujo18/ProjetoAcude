from flask import Flask, request, jsonify
from flask_cors import CORS
import utm
import controle
import pymysql
import json

app = Flask(__name__)
CORS(app)

# Variável global para armazenar pontos UTM
pontos_utm_armazenados = []

# Função para enviar as coordenadas para o BD
def enviar(coordenadasF, coordenadasM):
    mydb = pymysql.connect(
        host=controle.host,
        user=controle.user,
        password=controle.password,
        database=controle.database
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO coordenadas(`coordenadas`, `coordenadasM`) VALUES (%s, %s)"
    valores = (coordenadasF, coordenadasM)
    mycursor.execute(sql, valores)
    mydb.commit()
    print(mycursor.rowcount, 'Registro(s) inserido(s)')

    mycursor.close()
    mydb.close()

@app.route('/receber-coordenadas', methods=['POST'])
def receber_coordenadas():
    dados = request.get_json()
    pontos_latlng = dados.get('pontos', [])
    pontos_utm = []
    pontos_revertidos = []

    for ponto in pontos_latlng:
        lat = ponto.get('lat')
        lng = ponto.get('lng')
        if lat is not None and lng is not None:
            # Conversão para UTM
            easting, northing, zone_number, zone_letter = utm.from_latlon(lat, lng)
            pontos_utm.append({
                'easting': easting,
                'northing': northing,
                'zone_number': zone_number,
                'zone_letter': zone_letter
            })

            # Conversão reversa para verificar
            lat_r, lng_r = utm.to_latlon(easting, northing, zone_number, zone_letter)
            pontos_revertidos.append({'lat': lat_r, 'lng': lng_r})

    global pontos_utm_armazenados
    pontos_utm_armazenados = pontos_utm

    easting_formatado = [f"{int(round(c['easting']))}E" for c in pontos_utm_armazenados]
    print("UTM formatado:", easting_formatado)
    print("LatLng original:", pontos_latlng)
    print("LatLng revertido:", pontos_revertidos)

    controle.coordenadasF = ','.join(easting_formatado)
    controle.coordenadasM = json.dumps(pontos_revertidos, ensure_ascii=False)

    # Envia para o banco
    enviar(controle.coordenadasF, controle.coordenadasM.replace('[', '').replace(']', '').replace('}', '').replace('{', '').replace('[', '').replace('l', '').replace('a', '').replace('t', '').replace('n', '').replace('g', '').replace('"', '').replace(':', '').replace('-', ''))

    return jsonify({
        "status": "sucesso",
        "pontos_utm": pontos_utm,
        "pontos_revertidos": pontos_revertidos
    })

if __name__ == '__main__':
    app.run(debug=True)
    print('Servidor rodando')