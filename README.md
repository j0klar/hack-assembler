# hack-assembler

An assembler for the Hack assembly language written in Python, built as part of the [Nand2Tetris](https://www.nand2tetris.org/) course (Project 6).

Translates `.asm` files written in the Hack assembly language into `.hack` binary files that can be executed on the Hack computer platform.

## Usage

```bash
python assembler.py <file.asm>
```

The output `.hack` file will be created in the same directory as the input file.

## Project Structure

```
hack-assembler/
├── assembler.py      # Main entry point
├── parser.py         # Parses .asm files into commands
├── code.py           # Translates mnemonics to binary
├── symbol_table.py   # Manages labels and variables
```

