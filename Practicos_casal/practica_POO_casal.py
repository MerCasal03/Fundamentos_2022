# class Golondrina:
#     def __init__(self, energia):
#         self.energia = energia

#     def comer_alpiste(self, gramos):
#         self.energia += 4 * gramos

#     def volar_en_circulos(self):
#         self.volar(0)

#     def volar(self, kms):
#         self.energia -= 10 + kms

#     def esta_debil(self):
#         self.energia < 10
  
#     def esta_feliz(self):
#         self.energia > 500

#     def hipo(self): #deben aprender a comer peces?
#      self.energia -= self.volar(20)
#         self.energia += self.comer_alpiste(10)

# pepita = Golondrina(100)
# anastasia = Golondrina(200)
# maria = Golondrina(42)

#3
from os import lseek
from re import X #¿qué es lseek?


class Notebook:
    def __innit__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    
    def descuentos(self, porcentaje_de_descuento):
        self.precio -= self.precio*porcentaje_de_descuento

hp = Notebook("HP", "Lean", 10000)
macbook = Notebook("Apple", "Air", 20000)

print(macbook)

#4

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
        self.kms=kilometros_volados
        self.gramos=gramos_de_comida

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