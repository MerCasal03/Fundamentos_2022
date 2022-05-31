import os
with open("bio3.txt", "w") as f:
    f.write("estoy practicando manipulacion")
with open("bio3.txt", "a") as f:
    f.write("\nagrego texto\nhola")
#1
def no_empiezan_con(archivo, letra):
    with open(archivo, "r") as a:
        word_list=a.read().split("\n")
        for i in word_list:
            contador=[]
            if i[0] != letra:
                contador.append(i)
    print(len(contador))

#2
def imprimir_n(archivo, cantidad_de_lineas):
    with open(archivo, "r") as f:
        for linea in range(0, cantidad_de_lineas):
            for line in f:
                print(line)
#3
def imprimir_ultimas_n(archivo, n):
    with open(archivo, "r") as f:
        lista=[]
        for line in f:
            lista.append(line)
        for line in lista[n:]:
            print(line)

#4
def contador_de_palabras(arch):
    with open(arch, "r") as f:
        palabras=f.read().split()
        print(len(palabras))

#5
def reemplazar(entrada, letra, salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        d=f.read().split()
        for i in d:
            if i==letra:
                s.write(i("letra\n"))

#6
def eliminar_saltos(entrada,salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        for line in f:
            s.write(line.strip("\n"))

#7
def palabra_mas_larga(arch):
    with open(arch, "r") as f:
        p=f.read().split()
        palabra_mayor=len(p[0])
        palabra_mostrar=p[0]
        for i in p:
            if palabra_mayor <= len(i):
                palabra_mostrar=i
                palabra_mayor=len(i)
            else:
                palabra_mostrar=palabra_mostrar
        print(palabra_mostrar)
        print(len(palabra_mostrar))

#8
with open("bio4.txt", "w") as f:
    f.write("hola a todos")
def unir_docs(arch1, arch2, salida):
    with open(arch1, "r") as f1, open(arch2, "r") as f2, open(salida, "a") as s:
        s.write(f1.read() + f2.read())
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