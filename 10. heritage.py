print('Hola mundo!')

print('\n----------------')
print('Herencias y clases')

class carro():

    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

        
    def obtenerNombre(self):
        nombre = str(self.ano) + ' ' + self.modelo

        return nombre


    def leerOdometro(self):
        print('Este carro tiene ' + str(self.odometro) + ' kms.')

        return None

    def actualizarOdometro(self, kilometros):
        if kilometros >= self.odometro:
            self.odometro = kilometros
        else:
            print('Accion no permitida')

        return None

    def incrementarOdometro(self, kilometros):
        self.odometro += kilometros

        return None

##########################################################

class carroElectrico(carro):

    def __init__(self, marca, modelo, ano):
        super().__init__(modelo, ano)
        self.marca = marca
        self.bateria = 70

    def describirBateria(self):
        print('Este carro tiene una bateria de ' + str(self.bateria) + ' kWh.')

        return None

##########################################################

        
print('\n----------------')

mi_carro = carro('modelo A', 2006)
print(mi_carro.obtenerNombre())
mi_carro.leerOdometro()
mi_carro.incrementarOdometro(1000)
mi_carro.leerOdometro()

print('\n----------------')

mi_tesla = carroElectrico('testa', 'modelo S', 2016)
print(mi_tesla.obtenerNombre())
mi_tesla.leerOdometro()
mi_tesla.incrementarOdometro(20)
mi_tesla.leerOdometro()
mi_tesla.describirBateria()


