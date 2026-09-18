# Taller de Inteligencia Artificial: Reconocimiento de Dígitos

Notebook introductorio para entrenar una red neuronal simple (MLP) con Keras sobre el dataset **MNIST** y clasificar dígitos escritos a mano (0–9).

Objetivo del taller: superar **95%** de precisión en el conjunto de prueba (en la ejecución guardada el modelo alcanza **97.23%**) y usar esa red como percepción de un **robot 2D simulado**.

## Qué vas a hacer

El notebook `taller_ia_mnist.ipynb` sigue nueve pasos (TACO: Tarea, Enfoque, Código, Resultado):

1. Configurar el entorno (TensorFlow, NumPy, Matplotlib)
2. Cargar y visualizar MNIST (60,000 imágenes de entrenamiento y 10,000 de prueba)
3. Normalizar píxeles y aplanar cada imagen 28×28 a un vector de 784 valores
4. Definir un MLP: 128 neuronas ReLU, Dropout 20%, 10 salidas softmax
5. Entrenar 5 épocas
6. Evaluar en prueba y graficar el aprendizaje
7. Ver predicciones y, en el bonus, inspeccionar un dígito del conjunto de prueba
8. Traducir cada dígito a un comando de robot, rechazando lecturas con confianza menor al 85%
9. Ejecutar una misión: el robot 2D (matplotlib) sigue los comandos y no se mueve si la percepción es incierta

Los pasos 8 y 9 no necesitan hardware: cada imagen de prueba simula un fotograma de cámara.

## Requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.11 o 3.12 (`uv` puede instalarlo si no está en el sistema)
- Conexión a internet la primera vez (Keras descarga MNIST automáticamente)

## Entorno

Desde la raíz del repositorio:

```bash
uv sync
```

Esto crea `.venv` y instala las dependencias fijadas en `uv.lock`.

## Cómo ejecutar el taller

```bash
uv run jupyter notebook taller_ia_mnist.ipynb
```

Elige el kernel del `.venv` del proyecto y ejecuta las celdas en orden. No hace falta activar el entorno a mano: `uv run` lo usa solo.

El entrenamiento de 5 épocas suele tardar unos segundos en CPU. Los números de cada época pueden variar un poco entre máquinas; el umbral del taller es **>95%** en prueba, no un valor exacto.

## Arquitectura

| Capa | Unidades | Activación | Parámetros |
|------|----------|------------|------------|
| Entrada | 784 | — | 0 |
| Densa | 128 | ReLU | 100,480 |
| Dropout | 20% | — | 0 |
| Densa | 10 | Softmax | 1,290 |
| **Total** | | | **101,770** |

Pérdida: `sparse_categorical_crossentropy`. Optimizador: Adam. Batch size: 128. Validación: 10% del entrenamiento.
