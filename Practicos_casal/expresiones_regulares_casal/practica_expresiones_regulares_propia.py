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
def solo_autorizados(string):
    patron7='[A-Za-z\s0-9]'
    if len(re.findall(patron7, string)) == len(string):
        print("Están todos autorizados")
    else:
        print("No están todos autorizados")

#8
def separar_numeros(string):
    patron8='\d'
    numeros=re.findall(patron8, string)
    print(numeros)

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
        resultado= re.match("(P\w*)\W(P\w*)", elemento)


#12
def reemplazar(string):
    patron12="['\s' + '_' + ':']"
    print(re.sub(patron12, '|', string))

#13
def reemplazar2(string):
    patron13='\W{2}'
    print(re.sub(patron13, "_", string))

#14
def reemplazar3(string):
    patron14='\s'
    print(re.sub(patron14, ";", string))

#15 buscar mails
#r"[\w+_-]@[\w+]\.[\a-z]{2,6}""
#entre corchetes xq estoy haciendo un rango
#{2,6} no es necesario, restringe la cantidad de caracteres
def mail_aceptado(mail):
    patron15=r"[\w+_-]@[\w+]\.[\a-z]"
    mail1=re.findall(patron15, mail)
    if len(mail1) == len(mail):
        print("Mail aceptado")
    else:
        print("mail rechazado")
    