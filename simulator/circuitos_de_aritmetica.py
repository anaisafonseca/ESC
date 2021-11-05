from ecs_simulator import *

Library.author("Anaísa Fonseca")

Not = Library.load('Not')
And = Library.load('And')
Or = Library.load('Or')
Nand = Library.load('Nand')
Xor = Library.load('Xor')
Nor = Library.load('Nor')
Not16 = Library.load('Not16')
And16 = Library.load('And16')
Mux16 = Library.load('Mux16')
Nor16way = Library.load('Nor16way')

HalfAdder = Circuit('HalfAdder', ['a','b'], ['sum','carry'])
HalfAdder.add_components(Xor,And)
HalfAdder.set_as_input(0,'a','a')
HalfAdder.set_as_input(1,'a','a')
HalfAdder.set_as_input(0,'b','b')
HalfAdder.set_as_input(1,'b','b')
HalfAdder.set_as_output(0,'out','sum')
HalfAdder.set_as_output(1,'out','carry')
HalfAdder.save()
# HalfAdder.test_all()

FullAdder = Circuit('FullAdder', ['a','b','cin'], ['sum','carry'])
FullAdder.add_components((HalfAdder,2),Or)
FullAdder.set_as_input(0,'a','a')
FullAdder.set_as_input(0,'b','b')
FullAdder.set_as_input(1,'b','cin')
FullAdder.connect(0,'sum',1,'a')
FullAdder.connect(0,'carry',2,'b')
FullAdder.connect(1,'carry',2,'a')
FullAdder.set_as_output(1,'sum','sum')
FullAdder.set_as_output(2,'out','carry')
FullAdder.save()
# FullAdder.test_all()

Add16 = Circuit('Add16', lbs('a',16)+lbs('b',16), lbs('out',16))
Add16.add_components(HalfAdder,(FullAdder,15))
for i in range(16):
    Add16.set_as_input(i,'a',f'a{i}')
    Add16.set_as_input(i,'b',f'b{i}')
    Add16.set_as_output(i,'sum',f'out{i}')
for i in range(1,16):
    Add16.connect(i-1,'carry',i,'cin')
Add16.save()
# Add16.test_set([
#     [0]*12+[1,0,1,1] + 
#     [0]*12+[0,0,1,0],   # saída [0]*12 + [1,1,0,1]
# ])

Inc16 = Circuit('Inc16', lbs('in',16), lbs('out',16))
Inc16.add_components((HalfAdder,16))
Inc16.set_as_input(0,'a','in0')
Inc16.set_high_input(0,'b')
Inc16.set_as_output(0,'sum','out0')
for i in range(1,16):
    Inc16.connect(i,'b',i-1,'carry')
    Inc16.set_as_input(i,'a',f'in{i}')
    Inc16.set_as_output(i,'sum',f'out{i}')
Inc16.save()
# Inc16.test_set([
#     [0]*16,       # saída [0]*15 + [1]
#     [0]*15 + [1], # saída [0]*14 + [1,0]
# ])

Alu = Circuit(
    'Alu',
    lbs('x',16)+lbs('y',16)+['zx','nx','zy','ny','f','no'],
    lbs('out',16) + ['zr','ng']
)
Alu.add_components(
    (Mux16,2),  # 0,1
    (Not16,2),  # 2,3
    (Mux16,2),  # 4,5
    And16,      # 6
    Add16,      # 7
    Mux16,      # 8
    Not16,      # 9
    Mux16,      # 10
    Nor16way    # 11
)
for i in range(16):
    Alu.set_as_input(0,f'a{i}',f'x{i}')
    Alu.set_low_input(0,f'b{i}')
    Alu.set_as_input(1,f'a{i}',f'y{i}')
    Alu.set_low_input(1,f'b{i}')

    Alu.connect(0,f'out{i}',2,f'in{i}')
    Alu.connect(0,f'out{i}',4,f'a{i}')
    Alu.connect(2,f'out{i}',4,f'b{i}')
    
    Alu.connect(1,f'out{i}',3,f'in{i}')
    Alu.connect(1,f'out{i}',5,f'a{i}')
    Alu.connect(3,f'out{i}',5,f'b{i}')

    Alu.connect(4,f'out{i}',6,f'a{i}')
    Alu.connect(4,f'out{i}',7,f'a{i}')

    Alu.connect(5,f'out{i}',6,f'b{i}')
    Alu.connect(5,f'out{i}',7,f'b{i}')

    Alu.connect(6,f'out{i}',8,f'a{i}')
    Alu.connect(7,f'out{i}',8,f'b{i}')

    Alu.connect(8,f'out{i}',9,f'in{i}')
    Alu.connect(8,f'out{i}',10,f'a{i}')
    Alu.connect(9,f'out{i}',10,f'b{i}')

    Alu.connect(10,f'out{i}',11,f'in{i}')

    Alu.set_as_output(10,f'out{i}',f'out{i}')

Alu.set_as_input(0,'sel','zx')
Alu.set_as_input(1,'sel','zy')
Alu.set_as_input(4,'sel','nx')
Alu.set_as_input(5,'sel','ny')
Alu.set_as_input(8,'sel','f')
Alu.set_as_input(10,'sel','no')

Alu.set_as_output(11,'out','zr')
Alu.set_as_output(10,'out15','ng')

Alu.save()
# Alu.test_set([
#     [0]*16 + [0]*15+[1] + [0,0,0,0,1,0], # saída = x+y = [0]*15+[1]

#     [0]*16 + [1]*16 + [0,0,1,1,0,0],     # saída =  x  = [0]*16
#     [0]*16 + [1]*16 + [1,1,0,0,0,0],     # saída =  y  = [1]*16

#     [0]*16 + [1]*16 + [0,0,1,1,0,1],     # saída = !x  = [1]*16
#     [0]*16 + [1]*16 + [1,1,0,0,0,1],     # saída = !y  = [0]*16

#     [0]*16 + [1]*16 + [0,1,1,1,1,1],     # saída = x+1 = [0]*15+[1]
#     [0]*16 + [1]*16 + [1,1,0,1,1,1],     # saída = y+1 = [0]*16

#     [0]*16 + [0]*16 + [0,0,0,0,0,0],     # saída = x&y = [0]*16
#     [0]*16 + [1]*16 + [0,0,0,0,0,0],     # saída = x&y = [0]*16
#     [1]*16 + [1]*16 + [0,0,0,0,0,0],     # saída = x&y = [1]*16

#     [0]*16 + [0]*16 + [0,1,0,1,0,1],     # saída = x|y = [0]*16
#     [0]*16 + [1]*16 + [0,1,0,1,0,1],     # saída = x|y = [1]*16
#     [1]*16 + [1]*16 + [0,1,0,1,0,1],     # saída = x|y = [1]*16
# ])

# para os testes da ALU:
# zr ng
# 0   0
# 1   0
# 0   1
# 0   1
# 1   0
# 0   0
# 1   0
# 1   0
# 1   0
# 0   1
# 1   0
# 0   1
# 0   1