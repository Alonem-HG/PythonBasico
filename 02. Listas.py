print('hola mundo!')

print('\n-----------------------')
print('Crear listas')

bicicletas = ['trek', 'cannodale', 'redline', 'specialized']
print(bicicletas)

persona = ['paul', 17, 8.43, True]
print(persona)

print('\n-----------------------')
print('Acceder a datos en listas')

nombre = persona[0].title()
print('Mi nombre es ' + nombre)

edad = persona[1]
print(edad)

aprobado = persona[3]
print(aprobado)

nota = persona[-2]
print(nota)

mensaje = 'Mi nombre es ' + nombre + ' y mi edad es ' + str(edad)
print(mensaje)

print('\n-----------------------')
print('Agregar elementos a listas')

motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

motocicletas[0] = 'ducati'
print(motocicletas)

motocicletas = ['honda', 'yamaha', 'suzuki']
motocicletas.append('ducati')
print(motocicletas)

print('\n-----------------------')

motocicletas = []
print(motocicletas)

motocicletas.append('honda')
motocicletas.append('yamaha')
motocicletas.append('suzuki')
motocicletas.append('ducati')

print(motocicletas)

print('\n-----------------------')
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
motocicletas.insert(1, 'ducati')
print(motocicletas)

print('\n-----------------------')
print('Remover elementos de listas')

motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
del motocicletas[0]
print(motocicletas)

print('\n-----------------------')
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
aux = motocicletas.pop(0)
print(motocicletas)
print(aux)

mensaje = 'Mi primera motocicleta fue ' + aux.title() + '.'
print(mensaje)

print('\n-----------------------')
motocicletas = ['honda', 'yamaha', 'suzuki', 'yamaha']
print(motocicletas)
motocicletas.remove('yamaha')
motocicletas.remove('yamaha')
print(motocicletas)

print('\n-----------------------')
print('Organizar elementos de listas')

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort()
print(carros)

carros.sort(reverse=True)
print(carros)

print('\n-----------------------')
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)
print(sorted(carros))
print(carros)

print('\n-----------------------')
carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.reverse()
print(carros)

print('\n-----------------------')
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(len(carros))

carros.append('mazda')
print(len(carros))












