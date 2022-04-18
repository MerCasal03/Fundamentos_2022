#guia practica 2
#1
cadena=input("Decime una palabra: ")
lista_de_palabra=list(cadena)
if lista_de_palabra[0]==lista_de_palabra[0].upper():
    print("Mayúscula")
if lista_de_palabra[0]==lista_de_palabra[0].lower():
    print("Minúscula")
# 2
par_o_impar=input("Número: ")
numero=int(par_o_impar)
if numero>0 and numero%2==0:
    print("Positivo y par")
if numero>0 and numero%2!=0:
    print("Positivo e impar")
if numero<0 and numero%2==0:
    print("Negativo y par")
if numero<0 and numero%2!=0:
    print("Negativo e impar") 
if numero==0:
    print("0")

#3
del_1_al_6=input("Decime un numero del 1 al 6: ")
dado=int(del_1_al_6)
if dado<1 or dado > 6:
    print("Número ingresado incorrecto")
if dado == 1:
    print(6)
if dado == 2:
    print(5)
if dado == 3:
    print(4)
if dado == 4:
    print(3)
if dado == 5:
    print(2)
if dado == 6:
    print(1)


#4
peso_de_paquete_en_gramos1=input("Peso de paquete: ")
peso_de_paquete_en_gramos=int(peso_de_paquete_en_gramos1)
continente_de_destino=input("Continente de destino: ")
if peso_de_paquete_en_gramos>5000:
    print("No se realiza el envío")
else:
    if continente_de_destino == "América del Sur":
        print((peso_de_paquete_en_gramos*10000)+"dolares")
    if continente_de_destino == "América Central":
        print((peso_de_paquete_en_gramos*15000)+"dolares")
    if continente_de_destino == "América del Norte":
        print((peso_de_paquete_en_gramos*18000)+"dolares")
    if continente_de_destino == "Europa":
        print((peso_de_paquete_en_gramos*24000)+"dolares")
    if continente_de_destino == "Asia":
        print((peso_de_paquete_en_gramos*30000)+"dolares")
# peso_de_paquete_en_gramos=int(input("Decime el peso del paquete en gramos: "))
# continente_de_destino=input("Decime el continente de destino: ")
# if (peso_de_paquete_en_gramos/1000)>=5:
#     print("No se realiza el envío")
# if peso_de_paquete_en_gramos<5000 and continente_de_destino=="America del sur":
#     print((peso_de_paquete_en_gramos/1000)*10000)
# if peso_de_paquete_en_gramos<5000 and continente_de_destino=="America central":
#     print((peso_de_paquete_en_gramos/1000)*15000)
# if peso_de_paquete_en_gramos<5000 and continente_de_destino=="America del norte":
#     print((peso_de_paquete_en_gramos/1000)*18000)
# if peso_de_paquete_en_gramos<5000 and continente_de_destino=="Europa":
#     print((peso_de_paquete_en_gramos/1000)*24000)
# if peso_de_paquete_en_gramos<5000 and continente_de_destino=="Asia":
#     print((peso_de_paquete_en_gramos/1000)*30000)

        
#costo_de_logistica(4000, "América del Sur")


#5
numero_de_la_semana=input("Dia de la semana: ")
dia_de_la_semana=int(numero_de_la_semana)
if dia_de_la_semana<0 or dia_de_la_semana>7:
    print("Número ingresado es incorrecto")
if dia_de_la_semana == 1:
    print("Lunes")
if dia_de_la_semana == 2:
    print("Martes")
if dia_de_la_semana == 3:
    print("Miércoles")
if dia_de_la_semana == 4:
    print("Jueves")
if dia_de_la_semana == 5:
    print("Viernes")
if dia_de_la_semana == 6:
    print("Sábado")
if dia_de_la_semana == 7:
    print("Domingo")

##Listas

#6
lista=input("Decime 5 palabras: ")
lista1=list(lista.split(","))
lista2=list(lista1).reverse()
print(lista2)

#7
# numeros_de_lista=int(input("Números de lista: "))
# for num in numeros_de_lista:
#      lista3=[]
#      while num >=0:
#          lista3.append(num)
# print(lista3)

#8
lista_1=input("Decime 5 números para lista 1: ")
lista_1=list(lista_1.split(","))
lista_2=input("Decime 5 números para lista 2: ")
lista_2=list(lista_2.split(","))
lista_3=map(sum, zip(lista_1, lista_2))
print(lista_1) #transformar la lista de string a int para poder sumar

#9

##Diccionarios

#10

cadena=input("introducir cadena de texto: ")
caracteres={}

for caracter in cadena:
    caracter.append(caracteres)
print(caracteres)

#12
cantidad=int(input("introducir cantidad de alumnos: "))
alumnos={}

for num in range(cantidad):
    alumno = input("alumno: ")
    notas=[]
    nota=int(input("nota: "))
    while nota >=0:
        notas.append(nota)
        nota=int(input("nota: "))
    alumnos[alumno]=notas
print(alumnos)

for alumno in alumnos:
    print(alumno, sum(alumnos[alumno])/len(alumnos[alumno]))

#Funciones
#13
numeros=input("Dos numeros enteros: ")
numeros_enteros=numeros.split(",")
numero1=int(numeros_enteros[0])
numero2=int(numeros_enteros[1])
print(numero1)
def esMultiplo(numero1, numero2):
    if numero1 % numero2 == 0 or numero2 % numero1 ==0:
        print("Son multiplos")
    else:
        print("No son multiplos")

esMultiplo(numero1, numero2)

#14
def temperatura_media(temperatura_max, temperatura_min):
    print((temperatura_max + temperatura_min)/ 2)

temperatura=int(input("introducir cantidad de dias a medir: "))
dias={}

for temp in range(temperatura):
    dia=input("Dia: ")
    temp_media=[]
    temperatura_max=int(input("Temp Máxima del día: "))
    temperatura_min=int(input("Temp mínima del día: "))
    temp_media.append(temperatura_media(temperatura_max, temperatura_min))
    dias[dia]=temp_media
print(dias)

#15
cant_socios=int(input("Cantidad de socios a introducir: "))
socios={1:{"numero_socio":1, "nombre_y_apellido":"Florencia Ocampo", "fecha_de_ingreso":"14/09/2001", "cuota_al_dia": "Si"}, 2:{"numero_socio":2, "nombre_y_apellido":"David Estévez", "fecha_de_ingreso":"14/09/2001", "cuota_al_dia": "Si"}, 3:{"numero_socio":3, "nombre_y_apellido":"Sofía Cáceres", "fecha_de_ingreso":"14/09/2001", "cuota_al_dia": "Si"}}
print(socios)
for persona in range(cant_socios):
    socio=[]
    numero_socio=int(input("numero de socio: "))
    nombre_y_apellido=input("Nombre y apellido: ")
    fecha_de_ingreso=input("Fecha de ingreso: ")
    cuota_al_dia=input("Cuota al dia: ")
    socio.append(numero_socio)
    socios[numero_socio]=socio
print(socios)








