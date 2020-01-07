print('Hola mundo!')

print('\n--------------------')
print('OPERACIONES BOOLEANAS')

# BOOL True False

auxV = True
auxF = False

aux1 = 12 == 4
print(aux1)

aux1 = 12 != 4
print(aux1)

aux1 = 12 > 4
print(aux1)

aux1 = 12 < 4
print(aux1)

edad1 = 22
edad2 = 18
aux1 = edad1 > 21 and edad2 > 21
print(aux1)

aux1 = edad1 > 21 or edad2 > 21
print(aux1)

print('\n--------------------')
print('ESTRUCTURA IF')

# IF = SI
# if condicion:
#    Hacemos algo
# else:
#    Hacemos algo diferente

print('Ingrese el numero de hermanos')
# num = input()
num = 1

if int(num) <= 0:
    print('Error en el numero ingresado')
else:
    if int(num) > 1:
        print('Yo tengo ' + num + ' hermanos')
    else:
        print('Soy hijo unico')


if int(num) <= 0:
    print('Error en el numero ingresado')
elif int(num) > 1:
    print('Yo tengo ' + num + ' hermanos')
else:
    print('Soy hijo unico')

print('\n--------------------')
print('ESTRUCTURA IF JUNTO CON LISTAS')

carros = ['audi', 'BMW', 'subaru', 'toyota', 'BMW']
cont = 0

for carro in carros:
    if carro.lower() == 'bmw':
        print('Existe un BMW... Contando...')
        cont = cont + 1
    else:
        print('Seguimos buscando...')

print('Hemos encontrado ' + str(cont) + ' carros BMW')
    
print('\n--------------------')
print('VALORES EN LISTAS')

ingredientes_disponibles = ['cebolla', 'tomate', 'queso', 'salami']
ingrediente_deseado = 'carne'

print(ingrediente_deseado in ingredientes_disponibles)
print(ingrediente_deseado not in ingredientes_disponibles)

print('\n--------------------')

ingredientes_deseados = []

if ingredientes_deseados:
    for ingrediente in ingredientes_deseados:
        if ingrediente in ingredientes_disponibles:
            print('Agregando ' + ingrediente)
        else:
            print('Lo sentimos, no tenemos ' + ingrediente)
# else:
#     print('Esta seguro que quiere una pizza sin ingredientes?')


                











