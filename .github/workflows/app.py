from flask import Flask, request, jsonify
from PIL import Image
import os

app = Flask(__name__)

@app.route('/comparar', methods=['POST'])
def comparar():
    data = request.get_json()
    ruta1 = data.get('rutaImagen1')
    ruta2 = data.get('rutaImagen2')

    if not os.path.exists(ruta1) or not os.path.exists(ruta2):
        return jsonify({"error": "Una o ambas rutas no existen"}), 400

    # Lógica para comparar las imágenes
    img1 = Image.open(ruta1)
    img2 = Image.open(ruta2)

    # Aquí va tu lógica de comparación
    son_iguales = img1.size == img2.size  # Solo como ejemplo

    return jsonify({"resultado": son_iguales})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
