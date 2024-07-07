from pathlib import Path

from loguru import logger

from carve_exe.filetypes import FILETYPES


def carver(path_input: Path, path_output: Path) -> None:
    """Carve files from an input file."""
    logger.info(f"Carving {path_input} ({path_input.stat().st_size} bytes)")

    with path_input.open("rb") as h_input:
        while b := h_input.read(1):

            next_read_offset = h_input.tell()

            for filetype in FILETYPES:

                if b[0] != filetype.MAGIC[0]:
                    continue

                b += h_input.read(len(filetype.MAGIC) - len(b))
                if b == filetype.MAGIC:
                    executable_offset = h_input.tell() - len(b)
                    h_input.seek(executable_offset)

                    logger.info(f"@0x{executable_offset:x}: {filetype.NAME} candidate.")

                    # handle
                    executable_size = filetype.get_size(h_input)
                    if executable_size is not None:

                        logger.info(f"@0x{executable_offset:x}: {filetype.NAME} file of {executable_size} bytes.")

                        h_input.seek(executable_offset)
                        executable_data = h_input.read(executable_size)

                        if len(executable_data) == executable_size:
                            path_out = path_output / f"{path_input.stem}_{filetype.NAME}_0x{executable_offset:x}.bin"
                            with path_out.open("wb") as h_out:
                                h_out.write(executable_data)
                            logger.info(f"Wrote {filetype.NAME} to {path_out}.")

                        else:
                            logger.warning(f"@0x{executable_offset:x} Failed to read {executable_size} bytes.")

                    else:
                        logger.warning(f"@0x{executable_offset:x} Failed to load {filetype.NAME} candidate.")

                b = b[:1]
                h_input.seek(next_read_offset)


