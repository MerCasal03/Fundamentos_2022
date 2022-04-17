#1
nombre=input("Decime tu nombre: ")
print(len(nombre))

#2
nombre2=input("Decime tu nombre2: ")
print(str.upper(nombre2[5]+nombre2[6]))

#3
nombre_apellido=input("Decime tu nombre completo: ")
print("Hola"+" "+nombre_apellido)

#3 alternativo
def nombre_completo(nombre_apellido):
    print("Hola "+ nombre_apellido)
    
#4
primer_nombre=input("decime tu primer nombre: ")
primer_apellido=input("decime tu apellido: ")
segundo_apellido=input("decime tu segundo apellido: ")
print(str.upper(primer_nombre[0] + primer_apellido[0]+ segundo_apellido[0]))

#5
#numeros=input("Decime tres numeros: ")
#lista=numeros.split("")
#promedio=(int(lista)[0]+int(lista)[1]+int(lista)[2])/len(lista))
#print(promedio)

#6
#horario=input("Minutos: ")
#print((int(horario))/60)

#7
sueldo_comerciante=input("Sueldo del comerciante: ")
ventas=input("Cuantas ventas realizó en el mes: ")
sueldo_final=int(sueldo_comerciante) + (int(sueldo_comerciante)*0.1)*int(ventas)
print(sueldo_final)
    
#8

#9
def tiempo_de_ahorro(sueldo_anual, porcentaje_ahorro_por_mes, costo_total):
    return(sueldo_anual/12)*(porcentaje_ahorro_por_mes/100)






