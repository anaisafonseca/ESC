(COND1)         // inicia o programa, e verifica primeiro se B é menor que zero
    @R0
    D=M
    @R4
    M=D         // armazena a variável B original na posição R4
    @R1
    D = M
    @R5
    M=D         // armazena a variável C original na posição R5
    @R0
    D=M
    @R0
    D=M
    @ ACAO2     // se o valor de B (R0) for menor que zero, ele vai para ação 2. 
    D;JLT

(COND2)
    @R1
    D=M
    @ ACAO3     // se o valor de C (R1) for menor que zero, ele vai para ação 3.
    D;JLT

(COND3)
    @R0
    D=M         // se B=0, vai para ação 1
    @ ACAO1
    D;JEQ
    @R1
    D=M         // se C=0, vai para a ação 1
    @ ACAO1
    D;JEQ 

(MULTIPLIC)     // se ele não caiu em nenhumas das condições anteriores, 
                // realiza a multiplicação normal
    @R0
    D=M
    @ I         // I pega o valor e decrementa
    M=D-1 
    @R1
    D=M
    @R2
    D = D+M     // realiza a soma
    M=D         // guarda a soma na posição R2 (produto)
    @ I
    D = M       // pega o valor do I 
    @ END1
    D;JEQ       // se o valor for zero dá o JUMP para a função END1
    @R0
    M = D       // atualiza o valor da variável
    @ MULTIPLIC // volta o loop
    0;JMP

(MULTIPLIC2)    // a diferença dessa função para a que se encontra acima é que nesse caso B ou C é negativo. 
                // Logo, ao terminar ele vai para a função "inverte", para trocar o sinal do produto
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

(ACAO1)         // atribui o valor de A (produto) como 0
    @R2
    M = 0
    @ END
    0; JMP

(ACAO2)         // nessa função, apenas inverte o sinal de B
    @R0
    D = -M
    M = D
    @ MULTIPLIC2// vai para multiplic2, para fazer a inversão do sinal do produto A depois.
    D;JMP

(ACAO3)         //Nessa função, apenas inverte o sinal de C
    @R1
    D = -M
    M = D
    @ MULTIPLIC2// vai para multiplic2, para fazer a inverter o sinal de A depois.
    D;JMP

(INVERTE)       // inverte o sinal de A se B ou C são negativos
    @R2
    M = -M
    @END1
    0;JMP

(END1)          // restaura os valores originais de B e C 
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

(END)           // finaliza o programa
    @ END
    0; JMP
