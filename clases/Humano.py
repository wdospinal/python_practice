class Humano:
    i = 0
    def __init__(self):
        self.edad = 23

    def hablar(self,mensaje):
        print("Nombre %s edad %d"  % (mensaje ,self.edad))

pedro = Humano()

jaime = Humano()

jaime.hablar("Jaime")