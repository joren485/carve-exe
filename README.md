# Exe Carver

* Simple
* Best effort
* Recursive
* Modular
* Memory usage
* Wrong values: wrong output

## Installation
```shell
$ pip install poetry
$ git clone ...
$ cd exe-carver
$ poetry install
```

## Usage
### Help
```shell
$ poetry shell
$ exe-carve --help

                                                                                                                                                                                                                  
 Usage: exe-carve [OPTIONS]                                                                                                                                                                                       
                                                                                                                                                                                                                  
 Carve PE files from binary blob.                                                                                                                                                                                 
                                                                                                                                                                                                                  
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --input               -i      PATH       Input file or directory [default: None] [required]                                                                                                                 │
│ *  --output              -o      DIRECTORY  Output directory [default: None] [required]                                                                                                                        │
│    --max-size            -s      INTEGER    The max size of PE files to parse in bytes [default: 10485760]                                                                                                     │
│    --install-completion                     Install completion for the current shell.                                                                                                                          │
│    --show-completion                        Show completion for the current shell, to copy it or customize the installation.                                                                                   │
│    --help                                   Show this message and exit.                                                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
### Example
```shell
$ poetry shell
$ exe-carve --input test/input.bin --output /tmp/
$ exe-carve --input test/ --output /tmp/
```