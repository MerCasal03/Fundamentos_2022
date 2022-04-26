import os
with open("bio3.txt", "w") as f:
    f.write("estoy practicando manipulacion")
with open("bio3.txt", "a") as f:
    f.write("\nagrego texto\nhola")

# bio=open("bio3.txt", "r")
# print(bio.read())
# bio.readline()

def reemplazar(entrada, letra, salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        d=f.read().split()
        for i in d:
            if i==letra:
                s.write(i("letra\n"))

os.remove(os.getcwd()+"\prueba.txt")
