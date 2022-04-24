#1
class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	    print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	    print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4

""""Los estados de las clases son alimento y caricias"""""
""""las interfaces que comparten son energia, comer, acariciar y estaDebil. Aparte de eso, Perro posee la interfaz pasear, mientras que Gato no lo hace """""
""""Comparten interfaz parcialmente ya que Gato no comprende todas las interfaces que Perro"""""
""""No son polimorficas porque a pesar de que entiendan los mismos métodos, no responden de la misma manera"""""

#2
class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
              self.energia += 4 * gramos

    def volar_en_circulos(self):
          self.volar(0)

    def volar(self, kms):
        if self.energia > 0:
          self.energia -= 10 + kms #preguntar como hacer funcion si tiene la energia suficiente para volar, pero luego de hacerlo queda en <=0
        else:
            return "No tiene suficiente energia"

    def esta_debil(self):
         self.energia < 10
  
    def esta_feliz(self):
         self.energia > 500

    def hipo(self): #deben aprender a comer peces
         self.energia -= self.volar(20)
         self.energia += self.comer_alpiste(10)

    def estaEnEquilibrio(self):
        return 150 <= self.energia <= 300

pepita = Golondrina(100)
anastasia = Golondrina(200)
maria = Golondrina(42)

class Gorrion:
    def __innit__(self):
        self.kmsActuales=0
        self.gramosActuales=0
        self.listaGramos=[]
        self.listaKms=[]

    def volar(self, kms_nuevos):
        self.kmsActuales+=kms_nuevos
        self.kmsActuales.append(kms_nuevos)
    
    def comer(self, gramos):
        self.gramosActuales += gramos
        self.listaGramos.append(gramos)
        
    def CSS(self):
        if self.gramosActuales > 0:
            return self.kmsActuales / self.gramosActuales
        else:
            return None
    
    def CSSP(self):
        return max(self.listaKms) / min(self.listaGramos)

    def CSSV(self):
        return len(self.listaKms) / len(self.listaGramos)
    
    def equilibrio(self):
        return 0.5<=self.CSS()<=2

#3
class Ornitologo:
    def __innit__(self):
        self.aves=[]

    def estudiarAve(self):
        self.aves.append(self)

    def avesEnEstudio(self):
        return self.aves

    def avesEnEquilibrio(self):
        return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]
        
    def realizarRutinaSobreAves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]

ornitologo=Ornitologo()
golondrina1=Golondrina(80)
golondrina2=Golondrina(75)
gorrion1=Gorrion()
gorrion2=Gorrion()


#4
class ModoTransporte:
    def __innit__(self, combustible):
        self.combustible=combustible

    def cargar_combustible(self, combustibleCargado):
        self.combustible+=combustibleCargado

    def entran(self, personas):
        if self.personas <= self.maxPersonas

class Auto(ModoTransporte):
    def __innit__(self, combustible):
        self.combustible=combustible
        self.pasajeros= 0<self.pasajeros<=5

    def recorrer(self, kmsRecorridos):
        self.combustible-=kmsRecorridos*0.5

    def maxPersonas(self):
        return 5

class Moto(ModoTransporte):
    def __innit__(self, combustible):
        self.combustible=combustible
        self.pasajeros= 0<self.pasajeros<=2

    
    def recorrer(self, kmsRecorridos):
        self.combustible-=kmsRecorridos

    def maxPersonas(self):
        return 2
