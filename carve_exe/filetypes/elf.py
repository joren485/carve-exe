import io
from typing import BinaryIO

from elftools.common.exceptions import ELFError
from elftools.elf.elffile import ELFFile

from carve_exe.filetypes.filetype import Filetype


class FiletypeELF(Filetype):
    """PE Carver."""

    NAME = "ELF"
    MAGIC = b"\x7fELF"

    @classmethod
    def get_size(cls, h_input: BinaryIO) -> int | None:
        """Get ELF size."""
        elf_data = h_input.read(cls.DEFAULT_MAX_SIZE)
        h_data = io.BytesIO(elf_data)

        try:
            elf = ELFFile(h_data)
        except ELFError:
            return None

        size = 0
        for section in elf.iter_sections():
            if section["sh_type"] == "SHT_NOBITS":
                continue
            size = max(size, section["sh_offset"] + section["sh_size"])

        size = max(size, elf["e_shoff"] + elf["e_shentsize"] * elf["e_shnum"])
        return max(size, elf["e_phoff"] + elf["e_phentsize"] * elf["e_phnum"])

