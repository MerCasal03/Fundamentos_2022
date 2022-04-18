#1
# def(archivo, letra):
#      with open(archivo, "r") as a:
#          word_list=a.read().split()
#         for i in word_list:
#             if i[0] = letra:
                

#2
def imprimir_n(archivo, cantidad_de_lineas):
    with open(archivo, "r") as f:
        for linea in range(0, cantidad_de_lineas):
            for line in f:
                print(line)
#3
def ultimas_n_lineas(archivo, cantidad_de_lineas):
    lista=[]
    with open(archivo, "r") as f:
        for linea in f:
            lista.append(linea)
        for linea in f[linea-1:]:
            print(linea)

#4
def contador_de_palabras(archivo):
    with open(archivo, "r") as f:
        word_list=f.read().split()
        print(len(word_list))

#5


#6
def eliminar_saltos(entrada,salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        for line in f:
            s.write(line.strip("\n"))

#7


#8
def join_files(file1,file2,file3):
    with open(file1,"r") as f1, open (file2,"r") as f2, open(file3,"a") as f3:
        f3.write(f1.read() + f2.read())
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

#10
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