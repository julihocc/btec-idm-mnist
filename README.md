# Taller de Inteligencia Artificial

Dos partes independientes:

1. **Dígitos MNIST** — entrenar una red neuronal (Keras)
2. **Marcadores ArUco** — visión por computadora con OpenCV (sin entrenar)

## Parte 1 — `taller_ia_mnist.ipynb`

Red neuronal simple (MLP) que clasifica dígitos escritos a mano (0–9). Objetivo: **>95%** en prueba (en la ejecución guardada: **97.23%**).

Pasos (TACO: Tarea, Enfoque, Código, Resultado):

1. Configurar el entorno (TensorFlow, NumPy, Matplotlib)
2. Cargar y visualizar MNIST
3. Normalizar y aplanar cada imagen 28×28 a 784 valores
4. Definir el MLP: 128 ReLU, Dropout 20%, 10 softmax
5. Entrenar 5 épocas
6. Evaluar y graficar el aprendizaje
7. Ver predicciones (bonus: inspeccionar un dígito)

```bash
uv run jupyter notebook taller_ia_mnist.ipynb
```

| Capa | Unidades | Activación | Parámetros |
|------|----------|------------|------------|
| Entrada | 784 | — | 0 |
| Densa | 128 | ReLU | 100,480 |
| Dropout | 20% | — | 0 |
| Densa | 10 | Softmax | 1,290 |
| **Total** | | | **101,770** |

## Parte 2 — `taller_vision_aruco.ipynb`

Los robots no suelen leer dígitos a mano: usan **marcadores ArUco** (cuadrados con un ID). OpenCV ya trae el detector; no se entrena ninguna red.

1. Importar OpenCV
2. Generar un marcador (con margen blanco)
3. Detectar ID y esquinas
4. Escena con tres estaciones (Entrada, Almacén, Salida)

No hace falta webcam. Al final hay un extra opcional para cámara.

```bash
uv run jupyter notebook taller_vision_aruco.ipynb
```

## Entorno

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.11 o 3.12
- Internet la primera vez (MNIST se descarga solo)

```bash
uv sync
```
