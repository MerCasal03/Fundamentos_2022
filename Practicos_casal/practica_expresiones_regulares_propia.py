#1
import re
texto1= "A la grande le puse -Cuca-, 123456789"
patron1="[A-Z0-9a-z]+"
patron2="[2]"
# coinsidencias=print(re.findall(patron1, texto1))
# xxx=re.search(patron1, texto1).group(0)
# print(xxx)
# if len(coincidencias) > 0:
#     print (True)
#2

#3
#re.findall("")


#4

#5
# def empieza_con_numero_especifico(numero_especifico, string):
#      if re.search(numero_especifico\A, string).group() == numero_especifico:
#          print("Empieza con caracter indicado")
#      else:
#          print("No empieza con caracter indicado")

# empieza_con_numero_especifico("[2]", texto1)

print(re.search(patron2, texto1).group())

#6
listaprueba=["Ana Maria",
             "Juana Lopez"]

# def encontrar_frase(frase, lista):
#     for e in lista:
#         if re.findall(frase, lista):
#             print("Se encontró frase dada")
#         else:
#             print("No se encontró frase dada")

# encontrar_frase("[Ana Maria]", listaprueba)

#7
print(re.findall("[A-Za-z\s0-9]", texto1))

#8
print(re.findall("[0-9]", texto1))

#9
print(re.findall("[-- ]", texto1))#averiguar que caracter tengo que usar para que tome lo que está dentro de dos -

#10


