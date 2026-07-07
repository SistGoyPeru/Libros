# Capítulo 9: Deep Learning con TensorFlow/Keras

## 9.1 Introducción a Redes Neuronales

### 9.1.1 El Perceptrón

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, regularizers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Perceptrón simple: una neurona
modelo_lineal = keras.Sequential([
    layers.Dense(1, input_shape=(X_train.shape[1],))
])

modelo_lineal.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

# Equivalente a regresión lineal, pero con redes
historial = modelo_lineal.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

print(f"Loss final: {historial.history['loss'][-1]:.4f}")
```

### 9.1.2 Red Multicapa (MLP)

```python
# MLP para predicción de ingresos TechStore
mlp = keras.Sequential([
    layers.Input(shape=(X_train.shape[1],)),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(32, activation="relu"),
    layers.Dense(1)  # regresión
])

mlp.compile(
    optimizer=optimizers.Adam(learning_rate=0.001),
    loss="mse",
    metrics=["mae", "mse"]
)

mlp.summary()

# Callbacks
callbacks = [
    EarlyStopping(patience=10, restore_best_weights=True),
    ReduceLROnPlateau(factor=0.5, patience=5, min_lr=1e-6),
    ModelCheckpoint("models/mlp_best.keras", save_best_only=True)
]

# Entrenamiento
history = mlp.fit(
    X_train, y_train,
    epochs=100,
    batch_size=64,
    validation_split=0.2,
    callbacks=callbacks,
    verbose=1
)

# Evaluación
loss, mae, mse = mlp.evaluate(X_test, y_test)
print(f"Test MAE: ${mae:.2f}, RMSE: ${np.sqrt(mse):.2f}")
```

### 9.1.3 Regularización en Redes

```python
# Comparación de regularización
def crear_mlp(reg_type="none", dropout_rate=0.0):
    model = keras.Sequential()
    model.add(layers.Input(shape=(X_train.shape[1],)))

    for units in [128, 64, 32]:
        if reg_type == "l1":
            model.add(layers.Dense(units, activation="relu",
                      kernel_regularizer=regularizers.l1(0.001)))
        elif reg_type == "l2":
            model.add(layers.Dense(units, activation="relu",
                      kernel_regularizer=regularizers.l2(0.001)))
        else:
            model.add(layers.Dense(units, activation="relu"))

        if dropout_rate > 0:
            model.add(layers.Dropout(dropout_rate))

    model.add(layers.Dense(1))
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model

configs = [
    ("Sin regul.", crear_mlp("none", 0.0)),
    ("L2", crear_mlp("l2", 0.0)),
    ("Dropout 0.3", crear_mlp("none", 0.3)),
    ("L2 + Dropout", crear_mlp("l2", 0.3))
]

for nombre, modelo in configs:
    h = modelo.fit(X_train, y_train, epochs=50, validation_split=0.2,
                   verbose=0, callbacks=[EarlyStopping(patience=5)])
    val_mae = min(h.history["val_mae"])
    print(f"{nombre:15s} | Val MAE: ${val_mae:.2f}")
```

## 9.2 Redes Convolucionales (CNN)

```python
from tensorflow.keras.layers import Conv1D, MaxPooling1D, GlobalAveragePooling1D

# CNN 1D para datos secuenciales de ventas
def crear_cnn_1d(input_shape):
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        Conv1D(filters=64, kernel_size=3, activation="relu"),
        MaxPooling1D(pool_size=2),
        Conv1D(filters=128, kernel_size=3, activation="relu"),
        MaxPooling1D(pool_size=2),
        Conv1D(filters=64, kernel_size=3, activation="relu"),
        GlobalAveragePooling1D(),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(1)
    ])
    return model

# Reshape datos para CNN 1D: (samples, timesteps, features)
n_timesteps = 30
n_features = len(num_features)
X_cnn = X_train.values.reshape(-1, n_timesteps, n_features // n_timesteps)

cnn = crear_cnn_1d((n_timesteps, X_cnn.shape[2]))
cnn.compile(optimizer="adam", loss="mse", metrics=["mae"])
cnn.summary()
```

## 9.3 Transfer Learning

```python
from tensorflow.keras.applications import ResNet50, VGG16
from tensorflow.keras.preprocessing import image

# No tenemos imágenes, pero el concepto aplica a modelos pre-entrenados
# Ejemplo: usar embeddings pre-entrenados para texto
conceptos_transfer = {
    "Feature Extraction": "Congelar capas base, entrenar solo las nuevas",
    "Fine-tuning": "Descongelar últimas capas y re-entrenar con tasa baja",
    "Adaptive": "Añadir capas de adaptación entre el modelo base y el output"
}

# Aplicación a embeddings de productos
# Simular embeddings pre-entrenados
embedding_dim = 300
productos_embedding = np.random.randn(5000, embedding_dim)

modelo_transfer = keras.Sequential([
    layers.Input(shape=(embedding_dim,)),
    layers.Dense(128, activation="relu", trainable=False),  # capa congelada
    layers.Dense(64, activation="relu"),
    layers.Dense(1)
])

modelo_transfer.layers[0].trainable = False  # feature extraction
modelo_transfer.compile(optimizer="adam", loss="mse")
```

## 9.4 Ejercicios

1. **MLP**: Construye y entrena un MLP con 3 capas ocultas para predecir ventas de TechStore. Compara con Random Forest.
2. **Regularización**: Experimenta con L1, L2 y Dropout. ¿Qué combinación da mejor generalización?
3. **Callbacks**: Implementa EarlyStopping, ReduceLROnPlateau y ModelCheckpoint juntos. Muestra las curvas de aprendizaje.
4. **CNN 1D**: Diseña una CNN 1D para clasificar patrones de compra semanales.
5. **Transfer Learning**: Investiga y explica cómo aplicarías transfer learning con un modelo pre-entrenado de NLP a reseñas de TechStore.
