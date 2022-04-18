import os
#Desafio I
path= "C:\Users\mechi\Documents\UCEMA_2022\Semestre_1_2022\Fundamentos_de_Informática\fund_info\Fundamentos_2022\teorico_casal\manipulacion_teorico_casal"
with open(path, "a") as bio:
    bio.write("Archivo de la materia")

#Desafio III
with open("bio.txt", "w") as my_file:
    my_file.write("Nombre:Mercedes. Apellido: Casal. Edad:19")

#Desafio IV
with open("manipulacion_archivos.txt", "r")  as f:
    f.read()

