#1
import re
texto1= "A la grande le puse -Cuca-, 123456789"
print(re.search("\S\w+", texto1))

#2
texto = "2. Tutor de la materia: Guillermo Benitez"
print(re.findall('\S\w*', texto1))

#3
def encontrar_patron(string):
    patron="he"
    if re.search(patron, string) is not None:
        return "Se encontró el patron"
    else:
        return "No se encontró el patron"
 #search-->si aparece o no y desde-hasta que posición
 #findall-->encuentra y devuelve todas



#4
string = "Defíni la función aprobar_materias"
re.search('\S\w*' + '_' + '\S\w*', string) 

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
def entre_guiones(string):
    #print(re.findall("['-' + '\w*' + '-' ]", texto1))
    return re.findall(r"-(.*?)-", string)
    #r que se lea literalmente lo que está entre comillas
    #.cualquier caracter
    #*0 o mas veces
    #? ve todos los patrones dentro de string, no solo el primero y el ultimo
    #^ no contar un caracter/rango que venga despues de ^
    #\. que aparezca literalmente un punto, no el metacaracter
    #+ 0 o más veces
#10
def entre_simbolos(string):
    print(re.findall(r"@(.*?)&", string))

#11 tipico de parcial
def dos_P(lista):
    for elemento in lista:
        resultado= re.match("(P\w*)\W(P\w*)", elemento  )


#12
re.sub("['\s' + '_' + ':']", "|", texto1)

#13
re.sub("[\W{2}]", "_", texto1)

#14
re.sub("[\s]", ";", texto1)

#15 buscar mails
#r"[\w+_-]@[\w+]\.[\a-z]{2,6}
#entre corchetes xq estoy haciendo un rango
#{2,6} no es necesario, restringe la cantidad de caracteres