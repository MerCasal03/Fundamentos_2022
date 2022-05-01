#1
class Titan:
    def __init__(self, salud):
        self.salud=salud
    
    def salud_actual(self):
        return self.salud
    
    def recibir_ataque(self, danio_recibido):
        self.salud -= danio_recibido * 1.5
    
    def esta_vivo(self):
        return self.salud >= 0 
    
    def grito(self):
        print("¡Aaaarrrg!")
    
    def cuantas_casas(self):
        return (8/(100/self.salud))

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
# titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())

#2
class Enterprise:
    def __init__(self):
        self.potencias=50
        self.nivel_de_coraza=5

    def potencia(self):
        if 0<=self.potencias<=100:
            return self.potencias 
        else:
            if self.potencias>100:
                 self.potencias = 100
            if self.potencias<0:
                 self.potencias = 0

    def coraza(self):
        if 0 <= self.nivel_de_coraza <=50:
            return self.nivel_de_coraza
        else:
            if self.nivel_de_coraza>50:
                self.nivel_de_coraza = 50
            if self.nivel_de_coraza < 0:
                self.nivel_de_coraza = 0   

    def encontrarPilaAtomica(self):
        self.potencias += 25

    def encontrarEscudo(self):
        self.nivel_de_coraza += 10

    def recibirAtaque(self, puntos):
        if self.nivel_de_coraza >= puntos:
            self.nivel_de_coraza -= puntos
        else:
            self.potencias-=(puntos - self.nivel_de_coraza)
            self.nivel_de_coraza = 0
    
    def fortalezaDefensiva(self): 
        self.nivel_de_coraza = 5

    def necesitaFortalecerse(self):
        return (self.potencias < 20  and self.nivel_de_coraza == 0)
    
    def fortalezaOfensiva(self):
        if self.potencias < 20:
            return 0
        else:
            return (self.potencias - 20) / 2


enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.coraza())
print(enterprise.potencia())
enterprise.fortalezaDefensiva()
print(enterprise.coraza())
enterprise.necesitaFortalecerse()
enterprise.fortalezaOfensiva()

#3
class Persona:
    def __init__(self, energia):
        self.energia=energia
        self.feliz=False

    def energia_actual(self):
        return self.energia

    def dormir(self, horas_de_sueño):
        if horas_de_sueño >= 8:
            self.energia=100
        else:
            self.energia += (100/(8/horas_de_sueño))

    def comer(self):
        self.energia += 10

    def hacer_ejercicio(self, minutos):
        self.energia -= (25/(30/minutos))

class Estudiante(Persona):
    def __init__(self, energia):
        self.energia = energia
    def estudiar(self, horas_de_estudio):
        self.energia -= horas_de_estudio * 20

    def aprobar(self):
         self.feliz = True
         return self.feliz

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())