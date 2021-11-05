(COND1)         
    @R0
    D=M
    @R4
    M=D         
    @R1
    D = M
    @R5
    M=D         
    @R0
    D=M
    @R0
    D=M
    @ ACAO2     
    D;JLT

(COND2)
    @R1
    D=M
    @ ACAO3     
    D;JLT

(COND3)
    @R0
    D=M         
    @ ACAO1
    D;JEQ
    @R1
    D=M         
    @ ACAO1
    D;JEQ

(MULTIPLIC)     
    @R0
    D=M
    @ I         
    M=D-1 
    @R1
    D=M
    @R2
    D = D+M     
    M=D         
    @ I
    D = M       
    @ END1
    D;JEQ       
    @R0
    M = D       
    @ MULTIPLIC 
    0;JMP

(MULTIPLIC2)
    @R0
    D=M
    @ I
    M=D-1
    @R1
    D=M
    @R2
    D = D+M
    M=D
    @ I
    D = M
    @ INVERTE
    D;JEQ
    @R0
    M = D
    @ MULTIPLIC2
    0;JMP

(ACAO1)         
    @R2
    M = 0
    @ END
    0; JMP

(ACAO2)         
    @R0
    D = -M
    M = D
    @ MULTIPLIC2
    D;JMP

(ACAO3)         
    @R1
    D = -M
    M = D
    @ MULTIPLIC2
    D;JMP

(INVERTE)       
    @R2
    M = -M
    @END1
    0;JMP

(END1)          
    @R4
    D=M
    M=0
    @R0
    M=D
    @R5
    D=M
    M=0
    @R1
    M=D
    @ END
    0; JMP

(END)           
    @ END
    0; JMP