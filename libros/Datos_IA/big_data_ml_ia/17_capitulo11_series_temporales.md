# Capítulo 11: Series Temporales y Forecasting

## 11.1 Introducción a Series Temporales

### 11.1.1 Componentes de una Serie Temporal

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Datos de ventas diarias TechStore
ventas_diarias = pd.read_parquet("data/silver/ventas_diarias/")
ventas_diarias = ventas_diarias.set_index("fecha").sort_index()

print(f"Rango: {ventas_diarias.index.min()} → {ventas_diarias.index.max()}")
print(f"Registros: {len(ventas_diarias):,}")
print(f"Frecuencia: {pd.infer_freq(ventas_diarias.index)}")

# Visualización
plt.figure(figsize=(15, 8))
plt.plot(ventas_diarias["ingresos"], label="Ingresos diarios")
plt.title("Ventas Diarias TechStore 2025")
plt.xlabel("Fecha")
plt.ylabel("Ingresos ($)")
plt.legend()
plt.savefig("img/serie_temporal_ventas.png")

# Descomposición
descomposicion = seasonal_decompose(
    ventas_diarias["ingresos"],
    model="additive",
    period=7  # estacionalidad semanal
)

fig, axes = plt.subplots(4, 1, figsize=(15, 10))
descomposicion.observed.plot(ax=axes[0], title="Original")
descomposicion.trend.plot(ax=axes[1], title="Tendencia")
descomposicion.seasonal.plot(ax=axes[2], title="Estacionalidad")
descomposicion.resid.plot(ax=axes[3], title="Residuo")
plt.tight_layout()
plt.savefig("img/descomposicion_serie.png")
```

### 11.1.2 Estacionariedad

```python
# Test de Dickey-Fuller
def test_estacionariedad(serie, nombre=""):
    resultado = adfuller(serie.dropna())
    print(f"=== {nombre} ===")
    print(f"ADF Statistic: {resultado[0]:.4f}")
    print(f"p-value: {resultado[1]:.6f}")
    print(f"Valores críticos:")
    for key, value in resultado[4].items():
        print(f"  {key}: {value:.4f}")

    if resultado[1] <= 0.05:
        print("✅ Serie ESTACIONARIA (rechazamos H0)")
    else:
        print("❌ Serie NO estacionaria (no rechazamos H0)")

test_estacionariedad(ventas_diarias["ingresos"], "Ingresos Original")

# Diferenciación
ventas_diarias["ingresos_diff1"] = ventas_diarias["ingresos"].diff()
test_estacionariedad(ventas_diarias["ingresos_diff1"], "Ingresos Diff(1)")

# ACF y PACF
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
plot_acf(ventas_diarias["ingresos_diff1"].dropna(), ax=axes[0], lags=40)
plot_pacf(ventas_diarias["ingresos_diff1"].dropna(), ax=axes[1], lags=40)
plt.savefig("img/acf_pacf.png")
```

## 11.2 ARIMA

```python
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings("ignore")

# Train/Test split temporal
train = ventas_diarias["ingresos"][:-30]
test = ventas_diarias["ingresos"][-30:]

# ARIMA(p,d,q)
modelo_arima = ARIMA(train, order=(7, 1, 7))
modelo_arima_fit = modelo_arima.fit()

print(modelo_arima_fit.summary())

# Predicción
pred_arima = modelo_arima_fit.forecast(steps=30)

# Evaluación
rmse_arima = np.sqrt(mean_squared_error(test, pred_arima))
mae_arima = mean_absolute_error(test, pred_arima)
print(f"ARIMA(7,1,7) - RMSE: ${rmse_arima:.2f}, MAE: ${mae_arima:.2f}")

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(train.index[-60:], train[-60:], label="Train")
plt.plot(test.index, test, label="Test real")
plt.plot(test.index, pred_arima, label="ARIMA Pred", linestyle="--")
plt.legend()
plt.title("Forecasting con ARIMA")
plt.savefig("img/forecast_arima.png")
```

## 11.3 Prophet (Meta)

```python
from prophet import Prophet

# Preparar datos para Prophet
df_prophet = ventas_diarias.reset_index()[["fecha", "ingresos"]]
df_prophet.columns = ["ds", "y"]

# Crear y entrenar modelo
modelo_prophet = Prophet(
    yearly_seasonality=False,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode="multiplicative",
    changepoint_prior_scale=0.05
)

# Añadir regresores externos
df_prophet["es_fin_semana"] = (df_prophet["ds"].dt.dayofweek >= 5).astype(int)
df_prophet["dia_mes"] = df_prophet["ds"].dt.day

modelo_prophet.add_regressor("es_fin_semana")
modelo_prophet.add_regressor("dia_mes")

modelo_prophet.fit(df_prophet)

# Predecir 30 días
future = modelo_prophet.make_future_dataframe(periods=30)
future["es_fin_semana"] = (future["ds"].dt.dayofweek >= 5).astype(int)
future["dia_mes"] = future["ds"].dt.day

forecast = modelo_prophet.predict(future)

# Visualización
fig = modelo_prophet.plot(forecast)
plt.title("Forecasting con Prophet")
plt.savefig("img/forecast_prophet.png")

# Componentes
fig2 = modelo_prophet.plot_components(forecast)
plt.savefig("img/prophet_components.png")

# Evaluación
pred_prophet = forecast.set_index("ds").loc[test.index, "yhat"]
rmse_prophet = np.sqrt(mean_squared_error(test, pred_prophet))
mae_prophet = mean_absolute_error(test, pred_prophet)
print(f"Prophet - RMSE: ${rmse_prophet:.2f}, MAE: ${mae_prophet:.2f}")
```

## 11.4 LSTM para Series Temporales

```python
from sklearn.preprocessing import MinMaxScaler

# Preparar datos para LSTM
scaler = MinMaxScaler()
serie_scaled = scaler.fit_transform(ventas_diarias[["ingresos"]])

def crear_secuencias(data, seq_length=14):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 14
X_seq_ts, y_seq_ts = crear_secuencias(serie_scaled, seq_length)

# Split temporal
split = len(X_seq_ts) - 30
X_train_ts, X_test_ts = X_seq_ts[:split], X_seq_ts[split:]
y_train_ts, y_test_ts = y_seq_ts[:split], y_seq_ts[split:]

# Modelo LSTM
modelo_lstm_ts = keras.Sequential([
    layers.LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    layers.Dropout(0.2),
    layers.LSTM(50, return_sequences=False),
    layers.Dropout(0.2),
    layers.Dense(1)
])

modelo_lstm_ts.compile(optimizer="adam", loss="mse", metrics=["mae"])
modelo_lstm_ts.summary()

# Entrenar
hist_lstm_ts = modelo_lstm_ts.fit(
    X_train_ts, y_train_ts,
    epochs=50,
    batch_size=16,
    validation_split=0.1,
    callbacks=[EarlyStopping(patience=5)],
    verbose=1
)

# Predecir
pred_scaled = modelo_lstm_ts.predict(X_test_ts)
pred_lstm = scaler.inverse_transform(pred_scaled)
real_lstm = scaler.inverse_transform(y_test_ts)

rmse_lstm = np.sqrt(mean_squared_error(real_lstm, pred_lstm))
mae_lstm = mean_absolute_error(real_lstm, pred_lstm)
print(f"LSTM - RMSE: ${rmse_lstm:.2f}, MAE: ${mae_lstm:.2f}")

# Comparación final
resultados_ts = pd.DataFrame({
    "Modelo": ["ARIMA(7,1,7)", "Prophet", "LSTM(14 días)"],
    "RMSE": [rmse_arima, rmse_prophet, rmse_lstm],
    "MAE": [mae_arima, mae_prophet, mae_lstm]
})
print("\n=== Comparación de Modelos ===")
print(resultados_ts.to_string(index=False))
```

## 11.5 Ejercicios

1. **Descomposición**: Descompón las ventas semanales de TechStore en tendencia, estacionalidad y residuo. ¿Qué patrones observas?
2. **ARIMA**: Encuentra los mejores parámetros (p,d,q) usando auto_arima o análisis de ACF/PACF.
3. **Prophet**: Añade 3 regresores externos (día festivo, promociones, temperatura) y mide el impacto en el forecast.
4. **LSTM**: Experimenta con diferentes sequence_length (7, 14, 30) y número de unidades LSTM.
5. **Comparación**: Evalúa ARIMA, Prophet y LSTM en los mismos 30 días de test y determina el mejor modelo para el negocio.
