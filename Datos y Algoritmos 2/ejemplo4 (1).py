import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")

# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[0], [1], [1], [0]], "float32")

# Link para modelos de aquitectueras de redes neuronales
# https://www.aprendemachinelearning.com/breve-historia-de-las-redes-neuronales-artificiales/
n_entrada = len(training_data[0])
n_salida = 2
n_nodos = 16

model = Sequential()
model.add(Dense(n_nodos, input_dim=n_entrada, activation="relu"))  # entradad (2)
model.add(Dense(n_salida, activation="sigmoid"))  # salida (1)

model.compile(loss="mean_squared_error", optimizer="adam", metrics=["binary_accuracy"])
# mas informacion en: https://keras.io/api/metrics/
#
model.fit(
    training_data, target_data, epochs=1000, verbose=0
)  # descripción del entrenamiento

# Guarda el modelo entrenado en un archivo
# model.save('modelo_entrenadoX.know')
# print("trabajo ok y guardado")

# Carga exactamente el mismo modelo solo desde el archivo
# new_model = keras.models.load_model('modelo_entrenadoX.know')

# ========================================
# evaluamos el modelo
scores = model.evaluate(training_data, target_data, verbose=0)
# mas informacion: https://keras.io/api/models/model_training_apis/

print(f"Metrica del modelo: {model.metrics_names[1]}, con un valor de: {scores[1]*100}")

real_data = np.array([[0, 0], [1, 1]], "float32")
# print (model.predict(real_data).round())
# print (f'Resultado: {resultado}')
resultado = model.predict(real_data, verbose=0)
model.summary()
print(f" para la entrada: {real_data[0]} -> {resultado[0]}")
print(f" para la entrada: {real_data[1]} -> {resultado[1]}")
