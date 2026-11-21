
// initialize result


@R2
M=0

// Initialize counter

@R1
D=M
@R3
M=D

// multiplication loop

(Loop)
    @R3
    D=M
    @END
    D;JEQ
    

// add R0 to result

    @R0
    D=M
    @R2
    M=D+M

// ecrement counter

    @R3
    M=M-1

// repeat

    @Loop
    0;JMP

(END)
    @END
    0;JMP