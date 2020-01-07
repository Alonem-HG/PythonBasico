print('Hola mundo!')

print('\n-----------------')
print('Manejo de archivos')

'''
datos = open('pi.txt')
contenido = datos.read()
print(contenido)

with open('pi.txt') as datos:
    contenido = datos.read()
    print(contenido)

ruta = 'E:\\Python\\Archivos\\misDatos\\pi.txt'

with open(ruta) as datos:
    contenido = datos.read()
    print(contenido)

with open(ruta) as datos:
    for linea in datos:
        print(linea.rstrip().lstrip())

with open(ruta) as datos:
    lineas = datos.readlines()

for linea in lineas:
    print(linea.rstrip().lstrip())

'''

ruta = 'E:\\Python\\Archivos\\misDatos\\programando.txt'


with open(ruta, 'w') as datos:
    datos.write('Me gusta programar mucho')
    datos.write('\nEstoy aprendiendo python')

with open(ruta, 'a') as datos:
    datos.write('\nMe gusta crear juegos')
    datos.write('\nMe gusta crear aplicaciones web')


    

    




