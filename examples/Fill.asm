// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// addr = first address in screen memory map
@SCREEN
D=A
@addr
M=D

(LOOP)
    (CLEAR)
        // if KBD != 0 goto FILL
        @KBD
        D=M
        @FILL
        D;JNE
        // if addr < SCREEN goto LOOP
        @addr
        D=M
        @SCREEN
        D=D-A
        @LOOP
        D;JLT
        // set RAM[addr] to 0 
        @addr
        A=M
        M=0
        // decrement addr and goto CLEAR
        @addr
        M=M-1
        @CLEAR
        0;JMP

    (FILL)
        // if KBD = 0 goto CLEAR
        @KBD
        D=M
        @CLEAR
        D;JEQ
        // if addr = SCREEN + 8192 goto LOOP
        @SCREEN
        D=A
        @8192
        D=D+A
        @addr
        D=D-M
        @LOOP
        D;JEQ
        // set RAM[addr] to -1
        @addr
        A=M
        M=-1
        // increment addr and goto FILL
        @addr
        M=M+1        
        @FILL
        0;JMP


