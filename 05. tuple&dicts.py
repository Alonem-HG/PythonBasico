print('hola mundo!')

print('\n-------------------------')
print('TUPLES')

# LISTAS [ ]
# TUPLES ( )

lista1 = ['bmw', 'audi', 'toyota']
tuple1 = ('bmw', 'audi', 'toyota')

print(lista1[0])
print(tuple1[0])

lista1[0] = 'honda'
print(lista1)

#tuple1[0] = 'honda'
#print(tuple1)

print('\n-------------------------')
print('DICCIONARIOS')

# LISTAS [ ]
# TUPLES ( )
# DICCIONARIOS { }

autos = ['bmw', 'audi', 'toyota']
punt = [9, 8, 6]

datos = {'marca': autos, 'puntuacion': punt}
print(datos)

autos2 = ['suzuki', 'chevrolet', 'fiat']
datos['marca'] = autos2
print(datos)

valor = [10000, 9000, 4000, 7000]
datos['valor'] = valor
print(datos)

del datos['valor'][-1]
print(datos)

print('\n-------------------------')
print('ITERAR EN UN DICCIONARIO')

# for i in [1, 2]
# for i in range(3)

for clave, contenido in datos.items():
    print('\nClave ' + clave)
    print('Cont. ' + str(contenido))

print('\n-------------------------')

for i in range(3):
    mensaje = 'El carro marca ' + datos['marca'][i] + ' tiene una puntuacion igual a '  + str(datos['puntuacion'][i]) + ' y su precio es ' + str(datos['valor'][i]) + '.'
    print(mensaje)



