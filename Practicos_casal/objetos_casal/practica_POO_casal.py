#1
#Los atributos de la clase Perro son: alimento y caricias
#La interfaz de la clase Perro: energia, comer, acariciar, estaDebil
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
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

#3
class Notebook:
    def __innit__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    
    def descuentos(self, porcentaje_de_descuento):
        self.precio -= self.precio*(porcentaje_de_descuento/100)

hp = Notebook("HP", "Lean", 10000)
macbook = Notebook("Apple", "Air", 20000)


#4
class Contador:
    def __innit__(self, valor_actual):
        self.valor=valor_actual
    
    def inc(self):
        self.valor += 1
    
    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor=0

    def valor_nuevo(self, valor_nuevo):
        self.valor=valor_nuevo
    
valor_1=Contador(0)
#5

#6
class Calculadora:
    def __innit__(self, accion):
        self.accion=accion
    # def cargar(self):

    # def sumar(self):
    #     self += X

    # def restar(self):
    #     X
    
    # def multiplicar(self):
    #     X
    
    # def ValorActual():
    #     X
    
#7
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

