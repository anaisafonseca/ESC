from ecs_simulator import *

Library.author("Anaísa Fonseca")

Mux4way = Library.load('Mux4way')
Mux8way = Library.load('Mux8way')
Dmux4way = Library.load('Dmux4way')
Dmux8way = Library.load('Dmux8way')

Mux4way16 = Circuit(
    'Mux4way16',
    lbs('a',16)+lbs('b',16)+lbs('c',16)+lbs('d',16)+['sel1','sel0'],
    lbs('out',16)
)
Mux4way16.add_components((Mux4way,16))
for i in range(16):
    Mux4way16.set_as_input(i,'a',f'a{i}')
    Mux4way16.set_as_input(i,'b',f'b{i}')
    Mux4way16.set_as_input(i,'c',f'c{i}')
    Mux4way16.set_as_input(i,'d',f'd{i}')
    Mux4way16.set_as_input(i,'sel1','sel1')
    Mux4way16.set_as_input(i,'sel0','sel0')
    Mux4way16.set_as_output(i,'out',f'out{i}')
Mux4way16.save()
# Mux4way16.test_set([
#     [1]*16 + [0]*16 + [0]*16 + [0]*16 + [0] + [0], # saída tudo 1
#     [0]*16 + [1]*16 + [0]*16 + [0]*16 + [0] + [1], # saída tudo 1
# ],label_display_order=['sel1','sel0']+lbs('a',16)+lbs('b',16)+lbs('c',16)+lbs('d',16))

Mux8way16 = Circuit(
    'Mux8way16',
    lbs('a',16)+lbs('b',16)+lbs('c',16)+lbs('d',16)+lbs('e',16)+
    lbs('f',16)+lbs('g',16)+lbs('h',16)+['sel2','sel1','sel0'],
    lbs('out',16)
)
Mux8way16.add_components((Mux8way,16))
for i in range(16):
    Mux8way16.set_as_input(i,'a',f'a{i}')
    Mux8way16.set_as_input(i,'b',f'b{i}')
    Mux8way16.set_as_input(i,'c',f'c{i}')
    Mux8way16.set_as_input(i,'d',f'd{i}')
    Mux8way16.set_as_input(i,'e',f'e{i}')
    Mux8way16.set_as_input(i,'f',f'f{i}')
    Mux8way16.set_as_input(i,'g',f'g{i}')
    Mux8way16.set_as_input(i,'h',f'h{i}')
    Mux8way16.set_as_input(i,'sel2','sel2')
    Mux8way16.set_as_input(i,'sel1','sel1')
    Mux8way16.set_as_input(i,'sel0','sel0')
    Mux8way16.set_as_output(i,'out',f'out{i}')
Mux8way16.save()
# Mux8way16.test_set([
#     [1]*16 + [0]*16 + [0]*16 + [0]*16 + [0]*16 + [0]*16 +
#     [0]*16 + [0]*16 + [0] + [0] + [0] # saída tudo 1
# ],label_display_order=['sel1','sel1','sel0']+ lbs('a',16)+ lbs('b',16) + lbs('c',16)
# + lbs('d',16) + lbs('e',16) + lbs('f',16) + lbs('g',16) + lbs('h',16))

Dmux4way16 = Circuit(
    'Dmux4way16',
    lbs('in',16)+['sel1','sel0'],
    lbs('a',16)+lbs('b',16)+lbs('c',16)+lbs('d',16)
)
Dmux4way16.add_components((Dmux4way, 16))
for i in range(16):
    Dmux4way16.set_as_input(i,'in',f'in{i}')
    Dmux4way16.set_as_input(i,'sel1','sel1')
    Dmux4way16.set_as_input(i,'sel0','sel0')
    Dmux4way16.set_as_output(i,'a',f'a{i}')
    Dmux4way16.set_as_output(i,'b',f'b{i}')
    Dmux4way16.set_as_output(i,'c',f'c{i}')
    Dmux4way16.set_as_output(i,'d',f'd{i}')
Dmux4way16.save()

Dmux8way16 = Circuit(
    'Dmux8way16',
    lbs('in',16)+['sel2','sel1','sel0'],
    lbs('a',16)+lbs('b',16)+lbs('c',16)+lbs('d',16)+
    lbs('e',16)+lbs('f',16)+lbs('g',16)+lbs('h',16),
)
Dmux8way16.add_components((Dmux8way, 16))
for i in range(16):
    Dmux8way16.set_as_input(i,'in',f'in{i}')
    Dmux8way16.set_as_input(i,'sel2','sel2')
    Dmux8way16.set_as_input(i,'sel1','sel1')
    Dmux8way16.set_as_input(i,'sel0','sel0')
    Dmux8way16.set_as_output(i,'a',f'a{i}')
    Dmux8way16.set_as_output(i,'b',f'b{i}')
    Dmux8way16.set_as_output(i,'c',f'c{i}')
    Dmux8way16.set_as_output(i,'d',f'd{i}')
    Dmux8way16.set_as_output(i,'e',f'e{i}')
    Dmux8way16.set_as_output(i,'f',f'f{i}')
    Dmux8way16.set_as_output(i,'g',f'g{i}')
    Dmux8way16.set_as_output(i,'h',f'h{i}')
Dmux8way16.save()

# Mux4way16 = Library.load('Mux4way16')
# Mux8way16 = Library.load('Mux8way16')
# Dmux4way16 = Library.load('Dmux4way16')
# Dmux8way16 = Library.load('Dmux8way16')