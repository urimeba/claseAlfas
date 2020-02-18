class Auto:
    """
    Documentacion forzosa del objeto
    Que se pretende que haga, para que sirve o que se desearia
    """
    llantas = 4
    motor = 450
    color = "Rojo"
    ocupantes = 4
    velocidadMaxima = 200 
    manual = False
    movimiento = False

    def __init__(self):
        print("Hola! Soy un nuevo automovil")

    def avanzar(self):
        self.movimiento = True
        print("Me estoy moviendo hacia adelante y he aumentado en 20KM/h")

    def retroceder(self):
        self.movimiento = True
        print("Me estoy moviendo hacia atras!")

    def detenerse(self):
        if(self.movimiento):
            self.movimiento = False
            print("Me detuve")
        else:
            print("No me estoy moviendo")

    def subirPersona(self):
        if(self.ocupantes>0):
            self.ocupantes -= 1
            print("Acabas de subir a una persona")
        else:
            print("Ya no hay espacios en el auto")

vocho = Auto()
vocho.detenerse()