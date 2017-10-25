from functools import wraps

def fileLog(logfile="output.log"):
    def fileLogDecoratorFunction(function):
        @wraps(function)
        def fileLogDecoratorParameter(*args, **kwargs):
            open(logfile, 'a').write('Llamando al método' + function.__name__)
            return function(*args, **kwargs)
        return fileLogDecoratorParameter;
    return fileLogDecoratorFunction;

def consoleLog(function):
    @wraps(function)
    def decoratorADevolver(*args, **kwargs):
        print('Llamando al método', function.__name__)
        return function(*args, **kwargs)
    return decoratorADevolver;

@consoleLog
def devolverCuadrado(numero):
    return numero * 2;

@fileLog(logfile="output.log")
def devolverMitad(numero):
    return numero * 2;

if __name__ == "__main__":
    print("El cuadrado de 2 es", devolverCuadrado(2))
    print("El cuadrado de 3 es", devolverCuadrado(3))
    print("La mitad de 4 es", devolverMitad(4))