print('VARIABLES STRING')

nombre = 'nAcho MendOza'

print(nombre)
print(nombre.title())
print(nombre.upper())
print(nombre.lower())

print('\n\tEsto es python')

intro = ' hola '
aux = '|'

print(intro)
print(intro.lstrip())
print(intro + aux)
print(intro.rstrip() + aux)

print('---------------------')
print('VARIABLES INTEGER')

x=2
y=3

suma = x+y
resta = x-y
mult = x*y
div = y/x
pot = x ** y

print(suma, resta, mult, div, pot)

op1 = 2 + 3 * 4  # 14
op2 = (2 + 3) * 4  # 20

print(op1, op2)

print('---------------------')
print('VARIABLES FLOAT')

a=0.1
b=0.2

suma = a+b
resta = a-b
mult = a*b
div = a/b

print(round(suma, 2), resta, round(mult, 5), div)

aux = 3.400000000
print(round(aux, 5))

print('---------------------')
print('COMBINACION DE VARIABLES')

edad = 15
mensaje = 'Tu edad es ' + str(edad)

print(mensaje)

medida = 0.987566512
it = 5
mensaje = 'La medida en la iteracion ' + str(it) + ' es igual ' + str(round(medida, 3))
print(mensaje)

print('gracias')




