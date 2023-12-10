import pickle

# Suponiendo que tu modelo está guardado en un archivo .pkl
model_filename = '../models/modelo_entrenado.pkl'
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

def predict(input_data):
    return loaded_model.predict(input_data)

