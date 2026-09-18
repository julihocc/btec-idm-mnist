# Taller de IA: de ver dígitos a leer códigos

Un solo taller en **cuatro partes**. La pregunta es siempre la misma: *¿qué hay en esta imagen?*

Cada parte vive en su carpeta, con `codigo/` (notebook) y `presentaciones/` (Beamer):

| Parte | Carpeta | Código | Diapositivas |
|-------|---------|--------|----------------|
| Maestra | `00_serie/` | — | `presentaciones/00_serie.tex` |
| 1 Dígitos | `01_mnist/` | `codigo/01_taller_mnist.ipynb` | `presentaciones/01_mnist.tex` |
| 2 QR | `02_qr/` | `codigo/02_taller_qr.ipynb` | `presentaciones/02_qr.tex` |
| 3 ArUco | `03_aruco/` | `codigo/03_taller_aruco.ipynb` | `presentaciones/03_aruco.tex` |
| 4 Moda (reto) | `04_moda/` | `codigo/04_taller_moda.ipynb` | `presentaciones/04_moda.tex` |

1. **Parte 1** — la máquina **aprende** a leer dígitos (Keras) y **ejecuta** esa red con OpenCV (`cv2.dnn`)
2. **Parte 2** — visión en **software**: generar y leer un QR, y usarlo en una mini-app (OpenCV)
3. **Parte 3** — visión en **robótica**: marcadores ArUco, ID + posición (OpenCV)
4. **Parte 4** — **reto** de visión en moda: Fashion-MNIST + OpenCV (calzado vs no calzado)

Hazlas en ese orden. Cada notebook usa TACO: Tarea, Enfoque, Código, Resultado.

Preámbulo Beamer y compilador: `_shared/`. Compilar las cinco decks:

```bash
python _shared/build.py
```

## Entorno

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.11 o 3.12
- Internet la primera vez (MNIST y Fashion-MNIST se descargan solos)

```bash
uv sync
```

## Parte 1 — `01_mnist/`

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
uv run jupyter notebook 01_mnist/codigo/01_taller_mnist.ipynb
```

| Capa | Unidades | Activación | Parámetros |
|------|----------|------------|------------|
| Entrada | 784 | — | 0 |
| Densa | 128 | ReLU | 100,480 |
| Dropout | 20% | — | 0 |
| Densa | 10 | Softmax | 1,290 |
| **Total** | | | **101,770** |

## Parte 2 — `02_qr/`

Un QR es un **texto** dentro de una imagen. OpenCV —el mismo `cv2` del paso 8 de la Parte 1— lo genera y lo lee; tu código usa el string (catálogo, URL, ticket). No se entrena ninguna red. No hace falta webcam.

1. Preparar las herramientas
2. Generar un QR (`SKU-1042`)
3. Detectar y decodificar
4. Mini-app: escanear → consultar catálogo (incluido un código inexistente)

```bash
uv run jupyter notebook 02_qr/codigo/02_taller_qr.ipynb
```

## Parte 3 — `03_aruco/`

Cuando el entorno se etiqueta para un robot, OpenCV detecta **ArUco** (ID + esquinas), no un SKU de tienda.

1. Preparar las herramientas
2. Generar un marcador (con margen blanco)
3. Detectar ID y esquinas
4. Tres estaciones: Entrada, Almacén, Salida

```bash
uv run jupyter notebook 03_aruco/codigo/03_taller_aruco.ipynb
```

## Parte 4 — `04_moda/`

Reto para estudiantes. Dataset abierto **Fashion-MNIST** (Zalando, 10 prendas). OpenCV mide forma (umbral, contornos). Hay que completar `es_calzado` y **superar 80%** en 2,000 imágenes de prueba. El baseline de brillo medio rinde ~43%.

1. Cargar Fashion-MNIST
2. Ver las 10 clases
3. Contorno, caja y aspecto con OpenCV
4. Reto: calzado vs no calzado (sin entrenar una red)

```bash
uv run jupyter notebook 04_moda/codigo/04_taller_moda.ipynb
```
