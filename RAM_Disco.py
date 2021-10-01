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


"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This part measures the time the RAM needs to load data from the hard drive
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
This function loads to RAM the info of Test.txt file, this file is created by this program
"""


def from_drive_to_ram():
    f = open("Test.txt", "r")
    x = f.read()
    f.close()


"""
This function tells how many time the RAM needed to read of Test.txt file
Parameter size tells the amount of bytes read
"""


def print_drive_to_ram(size):
    time = 1000000 * timeit.timeit(from_drive_to_ram, number=1)
    time = "{:f}".format(time)

    print("Tiempo para cargar un archivo de " + str(size) + " bytes. Pasar data de disco duro a RAM")
    print("Tiempo transcurrido: " + time + " microsegundos")

    return float(time)


"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This part measures the time the RAM needs to save data permanently into the hard drive
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
This function writes n bytes to hard drive
"""


def ram_writes_in_drive(my_string):
    f = open("Test.txt", "w")
    f.write(my_string)
    f.close()


"""
This function creates the data that will be uploaded and measures the time it takes to be saved in hard drive
Size tells the amount of bytes to be written
"""


def print_ram_writes(size):
    print("Tiempo para escribir " + str(size) + " bytes en un archivo. Escribir data de RAM a disco duro.")

    my_string = ""
    for i in range(0, size):
        my_string += "1"

    time = 1000000*timeit.timeit(lambda: ram_writes_in_drive(my_string), number=1)
    time = "{:f}".format(time)
    print("Tiempo transcurrido: " + time + " microsegundos")

    return float(time)


"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
big data
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


# 404MB
def load_padron():
    try:
        f = open("PADRON_COMPLETO.txt", "w")
        f.read()
        f.close()
    except Exception as e:
        print("El archivo padron fallo", e)


# 586MB
def load_lorem1():
    try:
        f = open("lorem1.txt", "w")
        f.read()
        f.close()
    except Exception as e:
        print("El archivo lorem1 fallo", e)


# 1.18GB
def load_lorem2():
    try:
        f = open("lorem2.txt", "w")
        f.read()
        f.close()
    except Exception as e:
        print("El archivo lorem2 fallo", e)


"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Output
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
This function draws one graphic for the user
lista_n is the number of each test
lista_y is the time of each test
titulo is the desired upper title
color is colour desired for line
"""


def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra (n)')
    plt.ylabel('Tiempo (ms)')
    plt.title(titulo)
    plt.show()


"""
This function makes many tests with a desired amount of bytes and prints to user
First it writes a file of n bytes
Then it reads to RAM that created file
Each process is done 6 times to get different attempts
All the info is printed in console
and a graphic is done for write and another one for read
Size is the amount of bytes we want to test
This function specifically works with local Test.txt
"""


def draw_info_test1(size):
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


"""
This function prints the time needed to read the heavy files
Also creates a graphic of it
"""


def draw_big_data():
    # Measure time for each heavy file
    timeL = timeit.timeit(load_padron, number=1)
    timeL = "{:f}".format(timeL)
    print("Tiempo para cargar de disco duro a RAM 404MB: " + timeL)

    timeXL = timeit.timeit(load_lorem1(), number=1)
    timeXL = "{:f}".format(timeXL)
    print("Tiempo para cargar de disco duro a RAM 586MB: " + timeXL)

    timeXXL = timeit.timeit(load_lorem2(), number=1)
    timeXXL = "{:f}".format(timeXXL)
    print("Tiempo para cargar de disco duro a RAM 1.18GB: " + timeXXL)


    # Draw the graphic of each time
    graficar([404, 586, 1180], [int(timeL), int(timeXL), int(timeXXL)], 'Datos pesados', 'r')





"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Testing
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


draw_info_test1(ultra_mini)
draw_info_test1(mini)
draw_info_test1(small)
draw_info_test1(kilobyte)
draw_info_test1(medium_small)
draw_info_test1(medium)
draw_info_test1(megabyte)

print("\n\n")
#draw_big_data()
