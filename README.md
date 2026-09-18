# Taller de IA: de ver dígitos a leer etiquetas

Un solo taller en **dos partes**. La pregunta es siempre la misma: *¿qué hay en esta imagen?*

1. **Parte 1** — la máquina **aprende** a leer dígitos a mano (Keras + MNIST)
2. **Parte 2** — la máquina **usa un detector que ya existe** para leer marcadores ArUco (OpenCV)

Hazlas en ese orden. Cada notebook usa TACO: Tarea, Enfoque, Código, Resultado.

## Entorno

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.11 o 3.12
- Internet la primera vez (MNIST se descarga solo)

```bash
uv sync
```

## Parte 1 — `taller_ia_mnist.ipynb`

Red neuronal simple (MLP) que clasifica dígitos 0–9. Objetivo: **>95%** en prueba (ejecución guardada: **97.23%**).

1. Preparar las herramientas
2. Cargar MNIST
3. Normalizar y aplanar (28×28 → 784)
4. Diseñar el MLP: 128 ReLU, dropout 20%, 10 softmax
5. Entrenar 5 épocas
6. Evaluar y ver las curvas
7. Mirar predicciones (extra: un dígito a dígito)

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

Cuando el entorno se puede etiquetar, no hace falta otra red: OpenCV detecta **ArUco** (ID + esquinas).

1. Preparar las herramientas
2. Generar un marcador (con margen blanco)
3. Detectar ID y esquinas
4. Tres estaciones: Entrada, Almacén, Salida

No hace falta webcam. Al final hay un extra opcional para cámara.

```bash
uv run jupyter notebook taller_vision_aruco.ipynb
```
