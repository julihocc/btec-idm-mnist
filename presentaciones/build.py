"""Compile all Beamer decks with latexmk/pdflatex. Run from anywhere."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

DECKS = (
    "00_serie.tex",
    "01_mnist.tex",
    "02_qr.tex",
    "03_aruco.tex",
    "04_moda.tex",
)


def engine() -> list[str]:
    latexmk = shutil.which("latexmk")
    if latexmk:
        return [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error"]
    pdflatex = shutil.which("pdflatex")
    if pdflatex:
        return [pdflatex, "-interaction=nonstopmode", "-halt-on-error"]
    raise FileNotFoundError("Neither latexmk nor pdflatex is on PATH")


def compile_deck(tex: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = engine() + [f"-output-directory={outdir}", tex.name]
    log_path = outdir / (tex.stem + ".build.log")
    proc = subprocess.run(
        cmd,
        cwd=tex.parent,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    log_path.write_text(
        "CMD: " + " ".join(cmd) + "\n\nSTDOUT\n" + proc.stdout + "\nSTDERR\n" + proc.stderr,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{tex.name} failed (exit {proc.returncode}); see {log_path}")
    # latexmk/pdflatex write PDF next to -output-directory
    pdf = outdir / (tex.stem + ".pdf")
    if not pdf.is_file() or pdf.stat().st_size == 0:
        raise RuntimeError(f"{tex.name} produced no PDF at {pdf}")
    return pdf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path(__file__).resolve().parent / "_build",
    )
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent
    pdfs = []
    for name in DECKS:
        pdfs.append(compile_deck(root / name, args.outdir.resolve()))
        print("ok", pdfs[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
