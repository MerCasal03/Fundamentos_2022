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
        self.valor +=1
    
    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor=0

    def valor_nuevo(self, valor_nuevo):
        self.valor=valor_nuevo
    
contador=Contador(0)
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
class Gorriones:
    def __innit__(self, kms, gramos):
        self.kms=kms
        self.gramos=gramos

    def volar(self, kms_nuevos):
        self.kms*=kms_nuevos
    
    def comer(self, gramos):
        self.gramos += gramos
        
    def CSS(self, kilometros_volados, gramos_de_comida):
        self.CSS=kilometros_volados / gramos_de_comida
    
    def CSSP(self, mayores_kilometros, mayor_gramos):
        self.CSSP=mayores_kilometros / mayor_gramos

    def CSSV(self, cantidad_de_vuelos, cantidad_comidas):
            self.CSSV=cantidad_de_vuelos / cantidad_comidas
    
    def equilibrio(self):
        self.CSSP=0.5<self.CSSP<2

molinero=Gorriones(100, 10)