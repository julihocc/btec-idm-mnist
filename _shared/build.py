"""Compile all Beamer decks with latexmk/pdflatex. Run from anywhere."""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = Path(__file__).resolve().parent

DECKS = (
    ROOT / "00_serie" / "presentaciones" / "00_serie.tex",
    ROOT / "01_mnist" / "presentaciones" / "01_mnist.tex",
    ROOT / "02_qr" / "presentaciones" / "02_qr.tex",
    ROOT / "03_aruco" / "presentaciones" / "03_aruco.tex",
    ROOT / "04_moda" / "presentaciones" / "04_moda.tex",
)


def engine() -> list[str]:
    latexmk = shutil.which("latexmk")
    if latexmk:
        return [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error"]
    pdflatex = shutil.which("pdflatex")
    if pdflatex:
        return [pdflatex, "-interaction=nonstopmode", "-halt-on-error"]
    raise FileNotFoundError("Neither latexmk nor pdflatex is on PATH")


def texinputs_env() -> dict[str, str]:
    env = os.environ.copy()
    sep = ";" if os.name == "nt" else ":"
    # Trailing // = search recursively; trailing sep = keep default TeX tree.
    env["TEXINPUTS"] = str(SHARED) + "//" + sep + env.get("TEXINPUTS", "")
    return env


def compile_deck(tex: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = engine() + [f"-output-directory={outdir}", tex.name]
    log_path = outdir / (tex.stem + ".build.log")
    proc = subprocess.run(
        cmd,
        cwd=tex.parent,
        env=texinputs_env(),
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
    pdf = outdir / (tex.stem + ".pdf")
    if not pdf.is_file() or pdf.stat().st_size == 0:
        raise RuntimeError(f"{tex.name} produced no PDF at {pdf}")
    return pdf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--outdir",
        type=Path,
        default=SHARED / "_build",
    )
    args = parser.parse_args(argv)
    for tex in DECKS:
        if not tex.is_file():
            raise FileNotFoundError(tex)
        pdf = compile_deck(tex, args.outdir.resolve())
        print("ok", pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main())
