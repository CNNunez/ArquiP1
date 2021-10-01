import timeit
import os
from matplotlib import pyplot as plt


ultra_mini = 17  # 17 bytes
mini = 215  # 215 bytes
small = 786  # 786 bytes
kilobyte = 1024  # 1 kb
medium_small = 86016  # 86kb
medium = 293888  # 287kb
megabyte = 1048576  # 1mb


# This part measures the time the RAM needs to load data from the hard drive


def from_drive_to_ram():
    f = open("Test.txt", "r")
    x = f.read()
    f.close()


def print_drive_to_ram(size):
    time = 1000000 * timeit.timeit(lambda: from_drive_to_ram(), number=1)
    time = "{:f}".format(time)

    print("Tiempo para cargar un archivo de " + str(size) + " bytes. Pasar data de disco duro a RAM")
    print("Tiempo transcurrido: " + time + " microsegundos")

    return float(time)


# This part measures the time the RAM needs to save data permanently into the hard drive


def ram_writes_in_drive(my_string):
    f = open("Test.txt", "w")
    f.write(my_string)
    f.close()


def print_ram_writes(size):
    print("Tiempo para escribir " + str(size) + " bytes en un archivo. Escribir data de RAM a disco duro.")

    my_string = ""
    for i in range(0, size):
        my_string += "1"

    time = 1000000*timeit.timeit(lambda: ram_writes_in_drive(my_string), number=1)
    time = "{:f}".format(time)
    print("Tiempo transcurrido: " + time + " microsegundos")

    return float(time)


def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra (n)')
    plt.ylabel('Tiempo (ms)')
    plt.title(titulo)
    plt.show()


def draw_info(size):
    result_time = []
    n = []
    # Write data. RAM to drive

    for i in range(1, 7):
        print(i)
        result_time.append(print_ram_writes(size))
        print("")
        n.append(i)

    graficar(n, result_time, 'Escribir ' + str(size), 'r')
    print("\n")

    # Read data. RAM to drive
    result_time2 = []
    n2 = []

    for i in range(1, 7):
        print(i)
        result_time2.append(print_drive_to_ram(size))
        print("")
        n2.append(i)

    print("\n\n")
    graficar(n2, result_time2, 'Leer ' + str(size), 'r')


draw_info(ultra_mini)
draw_info(mini)
draw_info(small)
draw_info(kilobyte)
draw_info(medium_small)
draw_info(medium)
draw_info(megabyte)
