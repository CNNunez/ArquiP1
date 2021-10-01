import timeit
import os


# This part measures the time the RAM needs to load data from the hard drive
from matplotlib import pyplot as plt


def from_drive_to_ram_mini():
    f = open("MiniTestRead.txt", "r")
    f.read()
    f.close()


def print_drive_to_ram_mini():
    size = os.path.getsize("MiniTestRead.txt")
    print("Tiempo para cargar un mini archivo de " + str(size) + " bytes")
    print("Tiempo transcurrido: " + format(timeit.Timer(from_drive_to_ram_mini).timeit(number=1), '.8f') + " segundos")


# This part measures the time the RAM needs to save data permanently into the hard drive


def ram_writes_in_drive_mini():
    f = open("TestWrite.txt", "w")
    f.write("123456789")
    f.close()


def print_ram_writes_mini():
    size = os.path.getsize("TestWrite.txt")
    print("Tiempo para pasar 9 bytes de RAM a un archivo a disco duro para guardarlo permanentemente")

    time = timeit.timeit(ram_writes_in_drive_mini, number=1)
    time = "{:f}".format(time)
    print("Tiempo transcurrido: " + time + " segundos")

    return time



def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra (n)')
    plt.ylabel('Tiempo (ms)')
    plt.title(titulo)
    plt.show()


result_time = []
n = []

for i in range(1, 4):
    result_time.append(print_ram_writes_mini())
    n.append(i)


graficar(n, result_time, 'Escribir mini', 'r')

