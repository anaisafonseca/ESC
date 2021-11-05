    @R0                 // armazenando valores originais para recuperar depois
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
    D;JEQ               // pula para "division by zero" caso o denominador seja 0
    @R0
    D=M
    @ DIVIDE
    D;JNE               // pula para "divide" caso o numerador seja diferente de 0
    @R2                 // define quociente como 0 caso o numerador seja 0
    M=0
    @R3                 // define resto como 0 caso o numerador seja 0
    M=0

(DIVIDE)                // início de "divide"
    @R1
    D=M
    @ COND1             
    D;JLT               // pula pra condição 1 caso o denominador seja menor que 0
    @R0
    D=M
    @ COND2
    D;JLT               // pula pra condição 2 caso o numerador seja menor que 0
    @ DIVIDEUNSIGNED    
    0;JMP               // pula para "divide unsigned" se denominador e numerador são maiores que 0

(COND1)                 // início de "condição 1"
    @R1                 // inverte o valor do denominador e volta para "divide"
    D=M
    D=-D
    M=D
    @ DIVIDE
    0;JMP               

(COND2)                 // início de "condição 2"
    @R0                 // inverte o valor do numerador e volta para "divide"
    D=M
    D=-D
    M=D
    @ DIVIDE
    0;JMP

(DIVIDEUNSIGNED)        // início de "divide unsigned"
    @R2                 // define o quociente como 0
    M=0
    @R0                 // define o resto como o numerador (invertido)
    D=M
    @R3
    M=D
    (WHILE)             // laço para somar 1 ao quociente enquanto subtrai o 
                        // denominador do resto (que agora é o numerador)
        @R3
        D=M
        @R1
        D=D-M
        @ RESTORE       
        D;JLT           // caso a condição do laço não seja mais satisfeita, pula para "restore"
        @R2
        M=M+1
        @R1
        D=M
        @R3
        M=M-D
        @ WHILE
        0;JMP           // volta para o início do laço

(DIVISIONBYZERO)        // início de "division by zero"
    @R5                 // define o quociente como 0
    M=0
    @R2                 // define o resto como o máximo inteiro positivo de 16bits (32767)
    M=0
    @32767
    D=A
    @R3
    M=D
    @ END     
    0; JMP              // pula para o fim do programa

(RESTORE)               // início de "restore"
    @R5                 // restaura o valor do numerador para o original (não invertido)
    D=M
    M=0
    @R0
    M=D
    @ IFELSE            
    D;JLT               // pula para "if-else" caso esse numerador seja menor que 0
    (CONTINUE)
    @R6                 // restaura o valor do denominador para o original (não invertido)
    D=M
    M=0
    @R1
    M=D
    
    @ END               
    D;JGT               // pula pro fim do programa caso esse denominador seja maior que 0
    @R2                 // inverte o valor do quociente caso o denominador seja menor que 0
    M=-M
    @ END 
    0;JMP               // pula para o fim do programa

(IFELSE)                // início de "if-else"
    @R3
    D=M
    @ELSE
    D;JNE               // pula para "else" se o resto for diferente de 0
    @R2                 // inverte o quociente caso o resto seja 0
    M=-M
    @ CONTINUE  
    0;JMP               // volta no "restore" para continuar a restauração dos valores originais
    (ELSE)              //início de "else"
        @R2             // faz Q = -Q - R
        M=-M
        M=M-1
        @R1             // faz R = D - R
        D=M
        @R3
        M=D-M
        @ CONTINUE 
        0;JMP           // volta no "restore" para continuar a restauração dos valores originais

(END)                   // início de "end"
    @ END
    0;JMP               // loop de fim de programa