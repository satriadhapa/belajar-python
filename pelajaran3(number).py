# python number
# terdapat beberapa type data dalam number
#int
# float
# complex

x = 1 # int
y = 0.2 # float
z = 2j # complex

# cara mendapat kan type data

print(type(x))
print(type(y))
print(type(z))

# integer

angka1 = 1 
angka2 = 33412414834
angka3 = -223312312

# float

float1 = 1.00
float2 = 0.223312312
float3 = -23.66

# complex

complex1 = 34e4
complex2 = 12E3
complex3 = -66.8e33

# cara menkonversi ke type data tertentu

konv = 1
konv2 = 2.00
konv3 = 2j

# convert from int to float
kon = float(konv)
print(type(kon))

# convert from float to int
kon2 = int(konv2)
print(type(kon2))

# convert from int to complex
kon3 = complex(konv)
print(type(kon3))

# cara untuk membuat kombinasi acak / random dari sebuah angka 

import random

print(random.randrange(1,4))
