"""Assembles a single correct .asm-file into a correct .hack-file."""

from parser import Parser
from code import Code
from symbol_table import SymbolTable
import sys

def main():
    file_in = sys.argv[1]
    symbol_table = SymbolTable()
    line_count = 0
    
    parser = Parser(file_in)
    while parser.more_lines():
        parser.advance()
        if parser.command_type() == "A_COMMAND" or parser.command_type() == "C_COMMAND":
            line_count += 1
        elif parser.command_type() == "L_COMMAND":
            symbol_table.add_entry(parser.symbol(), line_count)
            
    parser = Parser(file_in)
    free_addr = 16
    with open(file_in[:-4]+".hack", "w") as file_out:
        while parser.more_lines():
            parser.advance()
            
            if parser.command_type() == "A_COMMAND":
                transl = parser.symbol()
                if not parser.symbol().isdigit():
                    if symbol_table.contains(parser.symbol()):
                        transl = symbol_table.get_address(parser.symbol())
                    else:
                        symbol_table.add_entry(parser.symbol(), free_addr)
                        transl = free_addr
                        free_addr += 1
                binary = bin(int(transl))
                bin_str = str(binary)[2:].zfill(16)
                if parser.more_lines():
                    file_out.write(bin_str + "\n")
                else:
                    file_out.write(bin_str)
                
            elif parser.command_type() == "C_COMMAND":
                dest = Code.dest(parser.dest())
                comp = Code.comp(parser.comp())
                jump = Code.jump(parser.jump())
                bin_str = "111" + comp + dest + jump
                if parser.more_lines():
                    file_out.write(bin_str + "\n")
                else:
                    file_out.write(bin_str)
          
if __name__ == "__main__":
    main()
