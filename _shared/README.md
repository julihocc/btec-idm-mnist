# Recursos compartidos

- `preamble.tex` — preámbulo Beamer (tema Madrid, español) que cada deck hace `\input{preamble}`.
- `build.py` — compila las cinco presentaciones.

```bash
python _shared/build.py
```

`build.py` pone `_shared/` en `TEXINPUTS` para que `\input{preamble}` funcione desde cada `*/presentaciones/`.
