from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Coordenadas dos ESPs
ESPS = {
    "esp1": (0.0, 0.0),
    "esp2": (0.0, 1.0),
    "esp3": (1.0, 0.0),
    "esp4": (1.0, 1.0),
    "esp_central": (0.5, 0.5)
}

def get_patio_limits():
    xs = [coord[0] for name, coord in ESPS.items() if name.startswith("esp")]
    ys = [coord[1] for name, coord in ESPS.items() if name.startswith("esp")]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    return min_x, max_x, min_y, max_y

def simulate_rssi(moto_pos):
    rssi_data = {}
    for esp, (x, y) in ESPS.items():
        dist = ((moto_pos[0]-x)**2 + (moto_pos[1]-y)**2) ** 0.5
        rssi = -30 - (dist * 70) + random.uniform(-2,2)
        rssi_data[esp] = round(rssi, 2)
    return rssi_data

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    moto_id = data.get('id')

    # Sorteia localização aleatória dentro dos limites do pátio
    min_x, max_x, min_y, max_y = get_patio_limits()
    x = round(random.uniform(min_x, max_x), 4)
    y = round(random.uniform(min_y, max_y), 4)

    rssi = simulate_rssi((x, y))
    response = {
        "motoId": moto_id,
        "rssiPorEsp": rssi,
        "localizacaoSorteada": {"x": x, "y": y}
    }
    return jsonify(response)

@app.route('/patio-coords', methods=['GET'])
def patio_coords():
    coords = [{"nome": esp, "x": x, "y": y} for esp, (x, y) in ESPS.items()]
    return jsonify({"coordenadas": coords})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
