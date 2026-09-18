# Taller de IA: de ver dígitos a leer códigos

Un solo taller en **tres partes**. La pregunta es siempre la misma: *¿qué hay en esta imagen?*

1. **Parte 1** — la máquina **aprende** a leer dígitos (Keras) y **ejecuta** esa red con OpenCV (`cv2.dnn`)
2. **Parte 2** — visión en **software**: generar y leer un QR, y usarlo en una mini-app (OpenCV)
3. **Parte 3** — visión en **robótica**: marcadores ArUco, ID + posición (OpenCV)

Hazlas en ese orden. Cada notebook usa TACO: Tarea, Enfoque, Código, Resultado.

## Entorno

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.11 o 3.12
- Internet la primera vez (MNIST se descarga solo)

```bash
uv sync
```

## Parte 1 — `taller_ia_mnist.ipynb`

Red neuronal simple (MLP) que clasifica dígitos 0–9. Objetivo: **>95%** en prueba (ejecución guardada: **97.08%**). Al final, la misma red corre en OpenCV.

1. Preparar las herramientas
2. Cargar MNIST
3. Normalizar y aplanar (28×28 → 784)
4. Diseñar el MLP: 128 ReLU, dropout 20%, 10 softmax
5. Entrenar 5 épocas
6. Evaluar y ver las curvas
7. Mirar predicciones
8. Exportar a TFLite y clasificar con `cv2.dnn` (extra: un dígito a dígito)

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

## Parte 2 — `taller_vision_qr.ipynb`

Un QR es un **texto** dentro de una imagen. OpenCV —el mismo `cv2` del paso 8 de la Parte 1— lo genera y lo lee; tu código usa el string (catálogo, URL, ticket). No se entrena ninguna red. No hace falta webcam.

1. Preparar las herramientas
2. Generar un QR (`SKU-1042`)
3. Detectar y decodificar
4. Mini-app: escanear → consultar catálogo (incluido un código inexistente)

```bash
uv run jupyter notebook taller_vision_qr.ipynb
```

## Parte 3 — `taller_vision_aruco.ipynb`

Cuando el entorno se etiqueta para un robot, OpenCV detecta **ArUco** (ID + esquinas), no un SKU de tienda.

1. Preparar las herramientas
2. Generar un marcador (con margen blanco)
3. Detectar ID y esquinas
4. Tres estaciones: Entrada, Almacén, Salida

```bash
uv run jupyter notebook taller_vision_aruco.ipynb
```
