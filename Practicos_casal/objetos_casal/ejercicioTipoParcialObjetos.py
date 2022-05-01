class Persona:
    def __innit__(self, energia):
        self.energia=energia
        self.felicidad= False

    def energia(self):
        return self.energia
        
    def recuperarEnergia(self, horasDeSueño):
        if horasDeSueño >= 8:
            self.energia = 100
        else:
            self.energia += (100/(8/horasDeSueño))

    def comer(self):
        self.energia += 10
    
    def hacerEjercicio(self, minutos):
        self.energia -= (minutos *25)/30

class Estudiante(Persona):
    def __innit__(self, energia, felicidad):
        self.energia=energia
        self.felicidad=False
    
    def estudiar(self, horasEstudio):
        self.energia-=20*horasEstudio

    def aprobar(self):
        self.felicidad=True
        return self.felicidad

estudiante=Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())
