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


class Notebook:
    def __innit__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    
    def descuentos(self, porcentaje_de_descuento):
        self.precio - self.precio+porcentaje_de_descuento

hp = Notebook(7, 200, 10000)
mac = Notebook(9, 23, 20000)

print(mac)

