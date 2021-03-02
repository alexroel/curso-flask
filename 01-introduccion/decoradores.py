def decorador(func):

    def decorar(*args):
        print('Inicia la ejecución de la función:', func.__name__)
        func(*args)
        print('Termina la ejecución de la función: ', func.__name__)
    
    return decorar

@decorador
def hola(nombre):
    print('Hola', nombre)

@decorador
def sumar(a, b):
    suma = a + b
    print('La suma es: ', suma)

hola('Alex')

sumar(10, 20)
