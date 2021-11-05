from ecs_simulator import *

Library.author("Anaísa Fonseca")

Not = Library.load('Not')
And = Library.load('And')
Or = Library.load('Or')
Mux = Library.load('Mux')

Not16 = Circuit('Not16', lbs('in',16), lbs('out',16))
Not16.add_components((Not,16))
for i in range(16):
    Not16.set_as_input(i,'in',f'in{i}')
    Not16.set_as_output(i,'out',f'out{i}')
Not16.save()
# Not16.test_set([
#     [1]*16, # saída tudo 0
#     [0]*16, # saída tudo 1
# ])

And16 = Circuit('And16', lbs('a',16)+lbs('b',16), lbs('out',16))
And16.add_components((And,16))
for i in range(16):
    And16.set_as_input(i,'a',f'a{i}')
    And16.set_as_input(i,'b',f'b{i}')
    And16.set_as_output(i,'out',f'out{i}')
And16.save()
# And16.test_set([
#     [0]*16 + [0]*16, # saída tudo 0
#     [0]*16 + [1]*16, # saída tudo 0
#     [1]*16 + [1]*16, # saída tudo 1
# ])

Or16 = Circuit('Or16', lbs('a',16)+lbs('b',16), lbs('out',16))
Or16.add_components((Or,16))
for i in range(16):
    Or16.set_as_input(i,'a',f'a{i}')
    Or16.set_as_input(i,'b',f'b{i}')
    Or16.set_as_output(i,'out',f'out{i}')
Or16.save()
# Or16.test_set([
#     [0]*16 + [0]*16, # saída tudo 0
#     [0]*16 + [1]*16, # saída tudo 1
#     [1]*16 + [1]*16, # saída tudo 1
# ])

Mux16 = Circuit('Mux16', lbs('a',16)+lbs('b',16)+['sel'], lbs('out',16))
Mux16.add_components((Mux,16))
for i in range(16):
    Mux16.set_as_input(i,'a',f'a{i}')
    Mux16.set_as_input(i,'b',f'b{i}')
    Mux16.set_as_input(i,'sel','sel')
    Mux16.set_as_output(i,'out',f'out{i}')
Mux16.save()
# Mux16.test_set([
#     [1]*16 + [0]*16 + [0], # saída tudo 1
#     [0]*16 + [1]*16 + [1], # saída tudo 1
# ],label_display_order=['sel']+lbs('a',16)+lbs('b',16))
# Mux16.test_all()
# print(Mux16.inputs.labels)
# print(Mux16.outputs.labels)

# Not16 = Library.load('Not16')
# And16 = Library.load('And16')
# Or16 = Library.load('Or16')
# Mux16 = Library.load('Mux16')