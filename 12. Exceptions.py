################ Excepciones ##########################

print('\n-----------------------------')
print('Excepciones')

def operar(a, b):
    print('\nSuma:\t', a + b)
    print('Resta:\t', a - b)
    print('Mult:\t', a * b)
    print('Div:\t', a/b)

    return None

operar(5,2)
# operar(5,0)

print('\n-----------------------------')

def operarE(a, b):
    print('\nSuma:\t', a + b)
    print('Resta:\t', a - b)
    print('Mult:\t', a * b)

    try:
        print('Div:\t', a/b)
    except ZeroDivisionError:
        print('No se puede dividir para 0!')

    return None

operarE(5,2)
operarE(5,0)

print('\n-----------------------------')
print('Excepciones con bloque else')

print('\nPor favor, ingrese dos numeros para dividir: ')
print('Ingrese Q/q para terminar.')

while True:
    numeroA = input('\nPrimer numero: ')
    if numeroA == 'Q' or numeroA == 'q':
        break

    numeroB = input('Segundo numero: ')
    if numeroB == 'Q' or numeroB == 'q':
        break

    try:
        res = int(numeroA)/int(numeroB)
    except ZeroDivisionError:
        print('No se puede dividir para 0!')
    else:
        print('Resultado:\t', res)





        



        






    


