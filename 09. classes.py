print('Hola mundo!')

print('\n--------------------------')
print('CLASES')


class Perro():

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.raza = None
        self.tamano = None

    def sit(self):
        print(self.nombre.title() + ' esta sentado.')

        return None

    def rollOver(self):
        print(self.nombre.title() + ' ha realizado un roll over!')

        return None

    def actualizarTamano(self, tamano):
        self.tamano = tamano

        return None
   

mi_perro = Perro('luz', 7)
mi_perro.raza = 'labrador'
mi_perro.actualizarTamano('grande')

print('Mi perro se llama ' + mi_perro.nombre.title() + '.')
print('Y tiene ' + str(mi_perro.edad) + '.')

mi_perro.sit()
mi_perro.rollOver()

print(mi_perro.raza)
print(mi_perro.tamano)

print('\n--------------------------')

tu_perro = Perro('max', 3)
tu_perro.raza = 'bulldog'
tu_perro.actualizarTamano('mediano')

print('Tu perro se llama ' + tu_perro.nombre.title() + '.')
print('Y tiene ' + str(tu_perro.edad) + '.')

tu_perro.sit()
tu_perro.rollOver()

print(tu_perro.raza)
print(tu_perro.tamano)







