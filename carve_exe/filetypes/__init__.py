from carve_exe.filetypes.elf import FiletypeELF
from carve_exe.filetypes.filetype import Filetype
from carve_exe.filetypes.pe import FiletypePE

FILETYPES = Filetype.__subclasses__()

__all__ = ["Filetype", "FiletypeELF", "FiletypePE", "FILETYPES"]
