from flask import Flask, request, render_template
import numpy as np
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Recoge los valores del formulario
    input_features = [float(x) for x in request.form.values()]
    final_features = [np.array(input_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='La potabilidad del agua es: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)