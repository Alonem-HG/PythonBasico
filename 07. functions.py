print('Hola mundo!')
'''
print('\n-----------------------------')
print('FUNCIONES\n')


a = 4
b = 5

a+b
a-b
a*b
a/b

c = 12
d = 7

c+d
c-d
c*d
a/d

--------------------

def funcion(a, b):
    a+b
    a-b
    a*b
    a/b

    return a+b

a = 4
b = 5
res1 = funcion(a,b)

c = 12
d = 7
funcion(c, d)


def operaciones(x, y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)

    return None


a = 4
b = 5
operaciones(a, b)
print('\n-----------------------------')

c = 12
d = 7
operaciones(c, d)

print('\n-----------------------------')
print('el orden de los argumentos importa\n')

def mascota(dueno, nombre):
    print('\nMi nombre es: ' + nombre.title())
    print('Mi dueno es: ' + dueno.title())

    return None

dueno_ext = 'Ana'
nombre_ext = 'Baloo'

mascota(dueno_ext, nombre_ext)
mascota('Andres', 'luz')
mascota(nombre='firulais', dueno='Karen')

print('\n-----------------------------')
print('Retornar valores')

def operar(x, y, tipo):
    if tipo == 'suma':
        res = x+y
    elif tipo == 'resta':
        res = x-y
    else:
        res = None

    return res

def operar2(x, y, tipo):
    if tipo == 'suma':
        return x+y
    elif tipo == 'resta':
        return x-y
    else:
        return None
    

aux1 = operar2(2, 6, 'suma')
print(aux1)
aux2 = operar2(2, 6, 'resta')
print(aux2)
aux3 = aux1 + aux2
print(aux3)

print('\n-----------------------------')
print('Elementos opcionales')

def obtenerNombre(nombre, apellido, apodo=''):
    return (nombre + ' ' + apellido + ' (' + apodo + ')').title()

def obtenerNombre2(nombre, apellido, apodo=None):
    if apodo:
        res = (nombre + ' ' + apellido + ' (' + apodo + ')').title()
    else:
        res = (nombre + ' ' + apellido).title()
        
    return res

print(obtenerNombre('Paul', 'Albornoz', 'gordo'))
print(obtenerNombre('Paul', 'Albornoz'))
print('-----------------------------')
print(obtenerNombre2('Paul', 'Albornoz', 'gordo'))
print(obtenerNombre2('Paul', 'Albornoz'))


'''

print('\n-----------------------------')
print('FUNCIONES SEGUNDA PARTE\n')

def imprimirDisenos(disenos_imprimir, disenos_impresos):
    while disenos_imprimir:
        diseno_actual = disenos_imprimir.pop()
        print('Imprimiendo modelo: ' + diseno_actual)
        disenos_impresos.append(diseno_actual)

    return None


def mostrarModelsCompletados(disenos_impresos):
    print('\nLos siguientes modelos han sido completados')
    for diseno in disenos_impresos:
        print(diseno)


disenos_imprimir_principal = ['robot', 'cubo', 'protector']
disenos_impresos_principal = []

disenos_imprimir = disenos_imprimir_principal.copy()
disenos_impresos = disenos_impresos_principal.copy()

imprimirDisenos(disenos_imprimir, disenos_impresos)
mostrarModelsCompletados(disenos_impresos)

print(disenos_imprimir_principal)
print(disenos_impresos_principal)

print('\n-----------------------------')
print('argumentos arbitrarios\n')

def prepararPizza(*ingredientes):
    print('Los ingredientes son: ')
    for ingrediente in ingredientes:
        print(ingrediente)

    return None

prepararPizza('pollo', 'queso','pimiento')

def prepararPizza2(tamano, *ingredientes):
    print('\nPreparando pizza de tamano ' + str(tamano) + ' pulgadas')
    
    print('Los ingredientes son: ')
    for ingrediente in ingredientes:
        print(ingrediente)

    return None

prepararPizza2(12, 'pollo', 'queso','pimiento')

print('\n-----------------------------')
print('argumentos arbitrarios y diccionarios\n')

def crearPerfil(nombre, apellido, **info):
    perfil = {}

    perfil['nombre'] = nombre
    perfil['apellido'] = apellido

    for clave, valor in info.items():
        perfil[clave] = valor

    return perfil


persona1 = crearPerfil('albert', 'einstein')
print(persona1)

persona1 = crearPerfil('albert', 'einstein', universidad='princeton')
print(persona1)

persona1 = crearPerfil('albert', 'einstein', universidad='princeton', campo='fisica')
print(persona1)





