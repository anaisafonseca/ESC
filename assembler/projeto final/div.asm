    @R0   
    D=M
    @R5
    M=D
    @R1
    D=M
    @R6
    M=D
    
    @R1
    D=M
    @ DIVISIONBYZERO
    D;JEQ
    @R0
    D=M
    @ DIVIDE
    D;JNE
    @R2
    M=0
    @R3
    M=0

(DIVIDE)
    @R1
    D=M
    @ COND1
    D;JLT
    @R0
    D=M
    @ COND2
    D;JLT
    @ DIVIDEUNSIGNED
    0;JMP

(COND1)
    @R1
    D=M
    D=-D
    M=D
    @ DIVIDE
    0;JMP

(COND2)
    @R0
    D=M
    D=-D
    M=D
    @ DIVIDE
    0;JMP

(DIVIDEUNSIGNED)
    @R2
    M=0
    @R0
    D=M
    @R3
    M=D
    (WHILE)
        @R3
        D=M
        @R1
        D=D-M
        @ RESTORE
        D;JLT
        @R2
        M=M+1
        @R1
        D=M
        @R3
        M=M-D
        @ WHILE
        0;JMP

(DIVISIONBYZERO)
    @R5
    M=0
    @R2
    M=0
    @32767
    D=A
    @R3
    M=D
    @ END
    0; JMP

(RESTORE)
    @R5
    D=M
    M=0
    @R0
    M=D
    @ IFELSE
    D;JLT
    (CONTINUE)
        @R6
        D=M
        M=0
        @R1
        M=D
        @ END
        D;JGT
    @R2
    M=-M
    @ END
    0;JMP

(IFELSE)
    @R3
    D=M
    @ELSE
    D;JNE
    @R2
    M=-M
    @ CONTINUE
    0;JMP
    (ELSE)
        @R2
        M=-M
        M=M-1
        @R1
        D=M
        @R3
        M=D-M
        @ CONTINUE
        0;JMP

(END)
    @ END
    0;JMP