from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Cargar el modelo entrenado
with open("../models/water_model.pkl", "rb") as file:
    model = pickle.load(file)
    
# Ruta para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos de entrada desde la solicitud POST
        data = request.get_json()

        # Realizar predicciones utilizando el modelo cargado
        features = [data['ph'], data['Hardness'], data['Solids'], data['Chloramines'], data['Sulfate'], data['Conductivity'], data['Organic_carbon'], data['Trihalomethanes'], data['Turbidity']]
        prediction = model.predict([features])[0]

        # Devolver la predicción como JSON
        result = {'potabilidad_agua': prediction}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)