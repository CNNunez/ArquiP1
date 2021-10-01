from timeit import default_timer as timer
import matplotlib.pyplot as plt
import math
import random

#Global
num = 100000;

def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra (n)')
    plt.ylabel('Tiempo (ms)')
    plt.title(titulo)
    plt.show()

def Operaciones( a, b):
    contador = 0;
    for i in range(num):
        if(contador == 0):
            a[i] = math.sqrt(a[i]);
            contador+=1;
        elif(contador == 1):
            a[i] *= b[i];
            contador+=1;
        elif(contador == 2):
            a[i] = math.pow(a[i],b[i]);
            contador+=1;
        elif(contador == 3):
            a[i] /= b[i];
            contador+=1;
        elif(contador == 4):
            a[i] = math.log(a[i]+b[i]) ;
            contador+=1;
        else:
            a[i]+=b[i];
            contador = 0;

def llenarLista(lista):
    for i in range(num):
        lista.append(random.randint(1,100));

def main():
    repeticiones = 100;
    tiempos = [];
    reps = [];
    lista1 = [];
    lista2 = [];
    llenarLista(lista1);
    llenarLista(lista2);

    for i in range(repeticiones):
        a = lista1.copy();
        b = lista2.copy();

        start = timer();
        Operaciones(lista1,lista2);
        end = timer();
        time = (end-start);
        tiempos.append(time);
        reps.append(i);
    
    graficar(reps,tiempos,"Prueba A",'r');
    print("Numeros de Muestra:")
    print(reps);
    print("Tiempos medidos:")
    print(tiempos);

main();
