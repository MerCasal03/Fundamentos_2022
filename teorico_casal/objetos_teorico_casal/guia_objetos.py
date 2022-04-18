#Desafio I
class AnimalAlado:
  def esta_feliz(self):
      return self.energia > 500

  # def entrenamiento_intesivo(self):
  #   self.energia <=0

class Golondrina(AnimalAlado):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia < 10
    
  def hipo(self): #deben aprender a comer peces
    self.energia -= self.volar(20)
    self.energia += self.comer_alpiste(10)

class Dragon(AnimalAlado):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10
  
  def esta_debil(self, energia):
    return self.energia < 50

  def hipo(self):
    self.energia -= 20
    self.energia += 300

#Desafio II
class Entrenador:
  def __innit__(self, equipo):
    self.equipo = equipo
  
  def el_equipo(self):
    return self.equipo

  def agregar_miembros(self, animal):
    """""este metodo toma un bojeto animal alado que tendrá todos los atributos de esa clase"""""
    self.equipo.append(animal)
  
  def entrenar_dragon(self, dragon):
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)
  def entrenar_equipo(self):
    for dragon in self.equipo:
      self.entrenar_dragon(dragon)

  
   

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)
chimuelo=Dragon(200, 1000)
hipo=Entrenador([roberta])