print('Hola mundo!')

print('\n-----------------')
print('while loop'.upper())

# while condition:
'''
numero = 1
while numero<=5:
    print(numero)
    # numero = numero + 1
    numero += 1

print('Fin de ciclo while')

mensaje = None
while mensaje != 'salir':
    mensaje = input('Ingrese un mensaje: ').lower()
    print(mensaje)

print('Fin de ciclo while')

estado = True
while estado:
     mensaje = input('Ingrese un mensaje: ').lower()

     if mensaje.lower() == 'salir':
         break
     else:
         print(mensaje)

print('Fin de ciclo while')
            
estado = True
while estado:
     mensaje = input('Ingrese un mensaje: ').lower()

     if mensaje.lower() == 'salir':
         estado = False
     else:
         print(mensaje)

print('Fin de ciclo while')


print('\n-----------------')
print('while con listas'.upper())

usuarios = ['alicia', 'vinicio', 'paloma']
asistencias = ['si', 'si', 'no']
usuarios_asistentes = []

while usuarios:
    usuario = usuarios.pop()
    asistencia = asistencias.pop()

    mensaje = 'Verificando usuario ' + usuario.title()
    print(mensaje)

    if asistencia == 'si':
        mensaje = 'El usuario ' + usuario.title() + ' asistira.'
        usuarios_asistentes.append(usuario)
    else:
        mensaje = 'El usuario ' + usuario.title() + ' NO asistira.'

    print(mensaje)

print('Fin de ciclo while')
print('\nUsuarios confirmados')

for usuario in usuarios_asistentes:
    print(usuario.title())


print('\n-----------------')
print('while con diccionarios'.upper())

respuesta = {}
estado = True

while estado:
    nombre = input('Ingrese su nombre: ')
    montana = input('Que montana le gustaria visitar? ')

    respuesta[nombre] = montana

    aux = input('Le gustaria continuar (si/no): ')

    if aux.lower() == 'no':
        break
    elif aux.lower() == 'si':
        continue
    else:
        print('No entiendo su comando \nVoy a asumir que dijo no!')
        break
'''        

print('Fin de ciclo while')
print('\nResultados de la encuesta'.upper())
for nombre, montana in respuesta.items():
    print(nombre.title() + ' le gustaria visitar ' + montana.title() + '.')

















    



