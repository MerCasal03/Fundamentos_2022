#1
nombre=input("Decime tu nombre: ")
print(len(nombre))

#2
nombre2=input("Decime tu nombre2: ")
print(nombre2[5]+nombre2[6])

#3
nombre_apellido=input("Decime tu nombre completo: ")
print("Hola"+" "+nombre_apellido)

#4
def iniciales(primer_nombre, primer_apellido, segundo_apellido):
    return str.upper([primer_nombre][0]+[primer_apellido][0]+[segundo_apellido][0])

