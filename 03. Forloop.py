print('Hola mundo!')

print('\n-----------------')
print('Iterar una lista\n')

nombres = ['paul', 'javier', 'andres', 'daniel']

for nombre in nombres:
    mensaje = nombre.title() + ' aprende Python conmigo!'
    print(mensaje)

print('\nGracias a todos por aprender conmigo')

print('\n-----------------')

for orden, nombre in enumerate(nombres):
    mensaje = nombre.title() + ' es el ' + str(orden + 1) + ' que aprende Python conmigo!'
    print(mensaje)

print('\n-----------------')

valores = list(range(0, 10, 1))
print(valores)

valores = list(range(4))
print(valores)

# valores = list(range(2, 11, 2))
# print(valores)

for valor in valores:
    print(nombres[valor])

print('\n-----------------')

cuadrados = []
for numero in range(6):
    cuadrado = numero ** 2
    cuadrados.append(cuadrado)

print(cuadrados)

print('\n-----------------')
print('Estadistica basica con listas')

print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))

print('\n-----------------')
print('Recortar listas')

nombres = ['paul', 'javier', 'andres', 'daniel', 'martin']
print(nombres)
print(nombres[0:3])
print(nombres[1:4])
print(nombres[:2])
print(nombres[2:])
print(nombres[-4:])

print('\n-----------------')

for nombre in nombres[:3]:
    print(nombre)

print('\n-----------------')
print('Copiar listas')

nombres = ['paul', 'javier', 'andres', 'daniel', 'martin']
# amigos = nombres.copy()
amigos = nombres[:]

print(amigos)
print(nombres)

nombres.append('ignacio')
print(nombres)
print(amigos)















    

    
    
