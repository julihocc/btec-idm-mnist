# Presentaciones Beamer

Cinco decks (tema Madrid, 16:9), una maestra y una por taller:

| Archivo | Uso |
|---------|-----|
| `00_serie.tex` | Presentación maestra de la serie |
| `01_mnist.tex` | Parte 1 — dígitos MNIST |
| `02_qr.tex` | Parte 2 — códigos QR |
| `03_aruco.tex` | Parte 3 — ArUco |
| `04_moda.tex` | Parte 4 — reto Fashion-MNIST |

Compilar todas (requiere TeX Live con Beamer):

```bash
python presentaciones/build.py
```

O una sola, desde este directorio:

```bash
latexmk -pdf 00_serie.tex
```

`preamble.tex` es el preámbulo compartido (no es un deck).
