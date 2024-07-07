from typing import BinaryIO

from pefile import PE, PEFormatError

from carve_exe.filetypes.filetype import Filetype


class FiletypePE(Filetype):
    """PE Carver."""

    NAME = "PE"
    MAGIC = b"MZ"

    @classmethod
    def get_size(cls, h_input: BinaryIO) -> int | None:
        """
        Get PE size.

        https://www.strchr.com/creating_self-extracting_executables
        """
        pe_data = h_input.read(cls.DEFAULT_MAX_SIZE)

        try:
            pe = PE(data=pe_data, fast_load=True)
        except PEFormatError:
            return None

        return max(section.PointerToRawData + section.SizeOfRawData for section in pe.sections)

