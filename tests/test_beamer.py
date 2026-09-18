"""Gating checks for the Beamer decks (sources + real latexmk/pdflatex compile)."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PRES = ROOT / "presentaciones"
BUILD = ROOT / "presentaciones" / "build.py"

DECKS = {
    "00_serie.tex": {
        "terms": [
            r"¿qué hay en esta imagen\?",
            "Parte 1",
            "Parte 2",
            "Parte 3",
            "Parte 4",
        ],
    },
    "01_mnist.tex": {"terms": ["MNIST", "Keras", r"cv2\.dnn"]},
    "02_qr.tex": {"terms": ["QR", "SKU", "catálogo"]},
    "03_aruco.tex": {"terms": ["ArUco", "estaciones"]},
    "04_moda.tex": {"terms": ["Fashion-MNIST", "es_calzado", "calzado", "80"]},
}


def test_five_distinct_beamer_sources():
    names = set(DECKS)
    found = {p.name for p in PRES.glob("*.tex") if p.name != "preamble.tex"}
    assert names <= found
    assert (PRES / "preamble.tex").is_file()
    assert len(names) == 5


@pytest.mark.parametrize("name", sorted(DECKS))
def test_each_deck_is_beamer_with_frames(name: str):
    text = (PRES / name).read_text(encoding="utf-8")
    assert r"\documentclass" in text and "{beamer}" in text
    assert r"\begin{frame}" in text or r"\frame{" in text
    n_frames = len(re.findall(r"\\begin\{frame\}", text))
    assert n_frames >= 2, f"{name} needs more than a title slide"


@pytest.mark.parametrize("name,spec", sorted(DECKS.items()))
def test_workshop_terms_in_source(name: str, spec: dict):
    text = (PRES / name).read_text(encoding="utf-8")
    for term in spec["terms"]:
        assert re.search(term, text), f"{name} missing {term!r}"


def test_master_is_not_a_companion():
    master = (PRES / "00_serie.tex").read_text(encoding="utf-8")
    assert "Presentación maestra" in master or "Serie de talleres" in master
    assert "01_mnist.tex" != "00_serie.tex"


def test_build_script_compiles_all_five():
    if not (shutil.which("latexmk") or shutil.which("pdflatex")):
        pytest.skip("no Beamer-capable LaTeX engine on PATH")
    import tempfile

    with tempfile.TemporaryDirectory(prefix="beamer-test-") as tmp:
        outdir = Path(tmp) / "beamer"
        proc = subprocess.run(
            [sys.executable, str(BUILD), "--outdir", str(outdir)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        for name in DECKS:
            pdf = outdir / (Path(name).stem + ".pdf")
            assert pdf.is_file() and pdf.stat().st_size > 0, pdf
