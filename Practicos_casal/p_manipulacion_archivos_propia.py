#1

#9
def word_counter(archivo):
    frecuencias=dict()
    with open(archivo, "r") as f:
        word_list=f.read().split()
        for i in word_list:
            if i in frecuencias:
                frecuencias[i] +=1
            else:
                frecuencias[i] = 1
        for word in frecuencias.keys():
            frecuencias[word]=round(frecuencias[word]/len(word_list,3))
    print(frecuencias)

#open("mi_arch.txt", "r").read()


import glob
import os
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt=glob.glob("*.txt")

    with open(archivo, "a") as s:
        for f in lista_txt:
            file=open(f, "r")
            s.write(file.read())
            file.close()