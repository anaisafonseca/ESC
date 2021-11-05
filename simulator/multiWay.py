from ecs_simulator import *

Library.author("Anaísa Fonseca")

Mux = Library.load('Mux')
Dmux = Library.load('Dmux')

And8way = Gate('And8way', 8, lbs('in',8), 'out')
And8way.set_as_vcc(0,'C')
And8way.set_as_gnd(7,'E')
i=1
while(i<8):
    And8way.connect(i-1,'E',i,'C')
    i+=1
for i in range(8):
    And8way.set_as_input(i,'B',f'in{i}')
And8way.set_as_output(7,'E','out')
And8way.save()
# And8way.test_all()

Or8way = Gate('Or8way', 8 , lbs('in',8), 'out')
Or8way.set_as_vcc(0,'C')
Or8way.set_as_gnd(1,'E')
for i in range(1,8):
    Or8way.connect(0,'C',i,'C')
    Or8way.connect(0,'E',i,'E')
for i in range(8):  
    Or8way.set_as_input(i,'B',f'in{i}')
Or8way.set_as_output(0,'E','out')
Or8way.save()
# Or8way.test_all()

Mux4way = Circuit('Mux4way', lbs('@',4)+['sel1','sel0'], 'out')
Mux4way.add_components((Mux,3))
Mux4way.set_as_input(2,'sel','sel1')
Mux4way.set_as_input(0,'sel','sel0')
Mux4way.set_as_input(1,'sel','sel0')
Mux4way.set_as_input(0,'a','a')
Mux4way.set_as_input(0,'b','b')
Mux4way.set_as_input(1,'a','c')
Mux4way.set_as_input(1,'b','d')
Mux4way.set_as_output(2,'out','out')
Mux4way.connect(0,'out',2,'a')
Mux4way.connect(1,'out',2,'b')
Mux4way.save()
# Mux4way.test_all(label_display_order=['sel1','sel0']+lbs('@',4))

# 16 bit são o mesmo componente em paralelo
# Mux4way16 apenas é colocar o mux4way em paralelo
Mux8way = Circuit('Mux8way', lbs('@',8)+['sel2','sel1','sel0'], 'out')
Mux8way.add_components((Mux4way,2), Mux)
Mux8way.set_as_input(0,'sel0','sel0')
Mux8way.set_as_input(0,'sel1','sel1')
Mux8way.set_as_input(1,'sel0','sel0')
Mux8way.set_as_input(1,'sel1','sel1')
Mux8way.set_as_input(2,'sel','sel2')
Mux8way.set_as_input(0,'a','a')
Mux8way.set_as_input(0,'b','b')
Mux8way.set_as_input(0,'c','c')
Mux8way.set_as_input(0,'d','d')
Mux8way.set_as_input(1,'a','e')
Mux8way.set_as_input(1,'b','f')
Mux8way.set_as_input(1,'c','g')
Mux8way.set_as_input(1,'d','h')
Mux8way.connect(0,'out',2,'a')
Mux8way.connect(1,'out',2,'b')
Mux8way.set_as_output(2,'out','out')
Mux8way.save()
# Mux8way.test_all(label_display_order=['sel2','sel1','sel0']+lbs('@',8))

Dmux4way = Circuit('Dmux4way', ['in','sel1','sel0'], ['a','b','c','d'])
Dmux4way.add_components((Dmux,3))
Dmux4way.set_as_input(0,'in','in')
Dmux4way.set_as_input(0,'sel','sel1')
Dmux4way.set_as_input(1,'sel','sel0')
Dmux4way.set_as_input(2,'sel','sel0')
Dmux4way.connect(0,'a',1,'in')
Dmux4way.connect(0,'b',2,'in')
Dmux4way.set_as_output(1,'a','a')
Dmux4way.set_as_output(1,'b','b')
Dmux4way.set_as_output(2,'a','c')
Dmux4way.set_as_output(2,'b','d')
Dmux4way.save()
# Dmux4way.test_all()

Dmux8way = Circuit('Dmux8way',
    ['in','sel2','sel1','sel0'],
    ['a','b','c','d','e','f','g','h']
)
Dmux8way.add_components(Dmux,(Dmux4way,2))
Dmux8way.set_as_input(0,'in','in')
Dmux8way.set_as_input(0,'sel','sel2')
Dmux8way.connect(0,'a',1,'in')
Dmux8way.connect(0,'b',2,'in')
Dmux8way.set_as_input(1,'sel0','sel0')
Dmux8way.set_as_input(1,'sel1','sel1')
Dmux8way.set_as_input(2,'sel0','sel0')
Dmux8way.set_as_input(2,'sel1','sel1')
Dmux8way.set_as_output(1,'a','a')
Dmux8way.set_as_output(1,'b','b')
Dmux8way.set_as_output(1,'c','c')
Dmux8way.set_as_output(1,'d','d')
Dmux8way.set_as_output(2,'a','e')
Dmux8way.set_as_output(2,'b','f')
Dmux8way.set_as_output(2,'c','g')
Dmux8way.set_as_output(2,'d','h')
Dmux8way.save()
# Dmux8way.test_all()

Nor = Gate('Nor', 2, ['a','b'], ['out'])
Nor.set_as_vcc(0,'C')
Nor.set_as_gnd(1,'E')
Nor.connect(0,'C',1,'C')
Nor.connect(0,'E',1,'E')
Nor.set_as_input(0,'B','a')
Nor.set_as_input(1,'B','b')
Nor.set_as_output(0,'C','out')
Nor.save()
# Nor.test_all()

Nor16way = Gate('Nor16way', 16, lbs('in',16), 'out')
Nor16way.set_as_vcc(0,'C')
Nor16way.set_as_gnd(1,'E')
for i in range(1,16):
    Nor16way.connect(0,'C',i,'C')
    Nor16way.connect(0,'E',i,'E')
for i in range(16):
    Nor16way.set_as_input(i,'B',f'in{i}')
Nor16way.set_as_output(0,'C','out')
Nor16way.save()
# Nor16way.test_set([
#     [0]*16,                        # saída tudo 1
#     [0]*8 + [1]*8,                 # saída tudo 0
#     [0]*4 + [1]*4 + [0]*4 + [1]*4, # saída tudo 0
#     [1]*16,                        # saída tudo 0
# ])

# And8way = Library.load('And8way')
# Or8way = Library.load('Or8way')
# Mux4way = Library.load('Mux4way')
# Mux8way = Library.load('Mux8way')
# Dmux4way = Library.load('Dmux4way')
# Dmux8way = Library.load('Dmux8way')
# Nor = Library.load('Nor')
# Nor16way = Library.load('Nor16way')