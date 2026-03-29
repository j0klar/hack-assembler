// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

// n = R0
@R0
D=M
@n
M=D
// i = 1
@i
M=1
// prod = 0
@prod
M=0

(LOOP)
    // if i > n goto STOP
    @i
    D=M
    @n
    D=D-M
    @STOP
    D;JGT
    // prod = prod + R1
    @R1
    D=M
    @prod
    M=D+M
    // increments i and loops
    @i
    M=M+1
    @LOOP
    0;JMP

(STOP)
    // R2 = prod
    @prod
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP    



