from timeit import default_timer as timer
import math
import random

#Global
num = 15000;

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
    lista1 = [];
    lista2 = [];

    llenarLista(lista1);
    llenarLista(lista2);

    for i in range(num):
        print(i,": ",lista1[i]);

    start = timer();
    
    Operaciones(lista1,lista2);
    end = timer();
    time = (end-start);
    
    for i in range(num):
        print(i,": ", lista1[i]);

    
    
    print("Tiempo total:",time);


main();