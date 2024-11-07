import sys
from pathlib import Path
from typing import Annotated

import typer
from loguru import logger

from carve_exe.carver import carver

app = typer.Typer(name="Carve Exe", no_args_is_help=True)


@app.command()
def carve(
    path_input: Annotated[
        Path,
        typer.Option(
            "-i",
            "--input",
            help="Input file to carve or directory of files to carve.",
            dir_okay=True,
            file_okay=True,
            exists=True,
            readable=True,
        ),
    ],
    path_output: Annotated[
        Path,
        typer.Option(
            "-o",
            "--output",
            help="Output directory to write found executables to.",
            dir_okay=True,
            file_okay=False,
            writable=True,
        ),
    ],
    verbose: Annotated[bool, typer.Option("-v", "--verbose", help="Verbose output")] = False,
) -> None:
    """Carve PE files from binary blob."""
    if not verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")

    if path_input.is_file():
        carver(path_input, path_output)

    elif path_input.is_dir():
        for subpath in path_input.rglob("*"):
            if subpath.is_file():
                carver(subpath, path_output)


if __name__ == "__main__":
    app()
