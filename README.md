# Carve Exe

Carve Exe is a simple best effort tool to carve PE and ELF files from arbitrary, binary files (e.g. memory dumps and executables).

Carve Exe is:
 * Simple: it's only a couple of lines of Python.
 * Modular: it's easy to add a new file format.
 * Best effort: it tries to cover the most common cases, but it is likely possible to craft a valid PE/ELF file that will not be carved correctly by this tool, as the PE and ELF formats are complex.
 * Smart about loading files: it is possible to carve 100GB files, without loading the whole file into memory, as the files are parsed byte-per-byte.

Carve Exe depends on [pefile](https://github.com/erocarrera/pefile) and [pyelftools](https://github.com/eliben/pyelftools) 
to do all the heavy lifting of parsing the actual file formats.

It should be noted that executables with wrong values in their headers (e.g. wrong section sizes), will produce wrong output. Garbage in, garbage out.

## Installation
```shell
$ pip install poetry
$ git clone git@github.com:joren485/carve-exe.git
$ cd exe-carver
$ poetry install
```

## Usage
### Help
```shell
$ poetry shell
$ carve-exe --help
                                                                                                                                                                                                                  
 Usage: carve-exe [OPTIONS]                                                                                                                                                                                       
                                                                                                                                                                                                                  
 Carve PE files from binary blob.                                                                                                                                                                                 
                                                                                                                                                                                                                  
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --input               -i      PATH       Input file or directory [default: None] [required]                                                                                                                 │
│ *  --output              -o      DIRECTORY  Output directory [default: None] [required]                                                                                                                        │
│    --install-completion                     Install completion for the current shell.                                                                                                                          │
│    --show-completion                        Show completion for the current shell, to copy it or customize the installation.                                                                                   │
│    --help                                   Show this message and exit.                                                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
### Example
```shell
$ poetry shell
$ carve-exe --input test/input.bin --output /tmp/   # Carve test/input.bin and write output to /tmp/
$ carve-exe --input test/ --output /tmp/            # Carve all files in test/ and write output to /tmp/
```