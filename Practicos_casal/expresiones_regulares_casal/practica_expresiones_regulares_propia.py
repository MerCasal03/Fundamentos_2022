#1
import re
texto1= "A la grande le puse -Cuca-, 123456789"
print(re.search("W\w+", texto1))

#2
texto = "2. Tutor de la materia: Guillermo Benitez"
print(re.findall('\S\w*', texto1))

#3
#re.findall("")


#4
string = "Defíni la función aprobar_materias"
re.search('\w' + '_' + '\w', string) 

#5
def empieza_con_numero_especifico(numero_especifico, string):
    if re.search('numero_especifico\A', string) == numero_especifico:
        print("Empieza con caracter indicado")
    else:
        print("No empieza con caracter indicado")

empieza_con_numero_especifico(2, texto1)

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
#or
print(re.findall('\d'))
#8
print(re.findall("[0-9]", texto1))

#9
print(re.findall("[-- ]", texto1))#averiguar que caracter tengo que usar para que tome lo que está dentro de dos -

#10


