# hack-assembler

An assembler for the Hack assembly language written in Python, built as part of the [Nand2Tetris](https://www.nand2tetris.org/) course (Project 6).

Translates `.asm` files written in the Hack assembly language into `.hack` binary files that can be executed on the Hack computer platform.

## Usage

```bash
python assembler.py <file.asm>
```

The output `.hack` file will be created in the same directory as the input file.

## Examples

Both examples are Hack assembly programs written in Nand2Tetris Project 4:

```bash
python assembler.py Fill.asm   # produces Fill.hack
python assembler.py Mult.asm   # produces Mult.hack
```

- `Fill.asm` - listens to keyboard input, blackening the screen when a key is pressed and clearing it when released
- `Mult.asm` - computes the product of two numbers via repeated addition

## Project Structure

```
hack-assembler/
├── assembler.py      # Main entry point
├── code.py           # Translates mnemonics to binary
├── parser.py         # Parses .asm files into commands
├── symbol_table.py   # Manages labels and variables
└── examples/
    ├── Fill.asm
    ├── Fill.hack
    ├── Mult.asm
    └── Mult.hack
```

