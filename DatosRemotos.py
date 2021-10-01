from timeit import default_timer as timer
import matplotlib.pyplot as plt
import poplib




"""
    Solucion del proyecto:
        A continuacion se presentan las funciones creadas para el desarrollo
        del proyecto.

        Utiliza poplib para poder conectar con el server del corre. Es necesario
        instalar esto: pip install pycopy-poplib
"""


"""
    Visualizacion de datos
"""
def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra (n)')
    plt.ylabel('Tiempo (ms)')
    plt.title(titulo)
    plt.show()


"""
    Leer correos del servidor
"""
def ReadEmail(user, pwd, ht, pp):
    username = user
    passwd = pwd
    host = ht
    port = pp

    time = 0
    
    # Connect to pop3 email server.
    try:
        start = timer()
        print('   start connect')
        server  = poplib.POP3_SSL(host, port) 
        server .set_debuglevel(1)
        server .user(username) 
        server .pass_(passwd)

        # Loop through list of emails
        for i in range(len(server .list()[1])):
            print('   in for')
            
            # Get one email.
            for msg in server .retr(i+1)[1]:
                # Print message
                print(msg)
        server .quit()
        end = timer()
        time = (end-start)*1000
    except Exception as error:
        print (" -> ERROR: ", str(error))
    return time



def mail():
    # Variables
    cantidad_Test = 25
    result_time = []
    n = []

    # Informacion de cuenta de prueba
    username = 'testeremail.001.2021@gmail.com'
    password = '001.2021'
    hostGmail = 'pop.gmail.com'
    portGmail = '995'
    
    # Realizar las pruebas y guardar los resultados
    print('START Test')
    for i in range(cantidad_Test):
        print(i)
        time = ReadEmail(username,password,hostGmail,portGmail)
        result_time.append(time)
        n.append(i)
    print('END Test')
    print("Numeros de muestra: ")
    print(n)
    print("Tiempos medidos: ")
    print(result_time)
    print(" ")




    print("Hola mundo")

    # Graficar resultados obtenidos
    graficar(n, result_time, 'Resultados Computadora A', 'r')


mail()
