class fileLog(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, function):
        def fileLogDecorator(*args, **kwargs):
            open(self.logfile, 'a').write("Se ha llamado al método" + function.__name__ + '\n')
            return function(*args, **kwargs)
        return fileLogDecorator;

class consoleLog(object):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("Se ha llamado al método" + self.function.__name__)
        return self.function(*args, **kwargs)

@consoleLog
def devolverCuadrado(numero):
    return numero * 2;

@fileLog(logfile="output.log")
def imprimirMensaje(mensaje):
    print(mensaje)

if __name__ == "__main__":
    print("El cuadrado de 2 es", devolverCuadrado(2))
    print("El cuadrado de 3 es", devolverCuadrado(3))
    imprimirMensaje("Mi mensaje")