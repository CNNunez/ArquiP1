#from timeit import default_timer as timer
import matplotlib.pyplot as plt
import poplib
import os
import string
import logging




"""
    Solucion del proyecto:
        A continuacion se presentan las funciones creadas para el desarrollo
        del proyecto.

        Utiliza pop3 para poder conectar con el server del corre. Es necesario
        instalar esto: pip install Aspose.Email-for-Python-via-NET
"""


"""
    Visualizacion de datos
"""
def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Numero de muestra')
    plt.ylabel('Tiempo')
    plt.title(titulo)
    plt.show()


"""
    Leer correos del servidor
"""
def ReadEmail():
    print('START')

    user_name = 'testeremail.001.2021@gmail.com'
    passwd = '001.2021'
    pop3_server_domain = 'pop.gmail.com'
    pop3_server_port = '995'
    
    # Connect to pop3 email server.
    print('   start connect')
    mail_box = poplib.POP3(pop3_server_domain, pop3_server_port) 
    mail_box.user(user_name) 
    mail_box.pass_(passwd)

    # Get number of existing emails.
    number_of_messages = len(mail_box.list()[1])
    # Loop in the all emails.
    for i in range(number_of_messages):
        print('   in for')
        # Get one email.
        for msg in mail_box.retr(i+1)[1]:
            # Get the email from address. 
            msg_r = msg.get('From')
            print('This message is: ' + msg_r)
    mail_box.quit()
    print('END')




#ReadEmail()


def prueba():
    SERVER = "pop.gmail.com"
    USER  = 'testeremail.001.2021@gmail.com'
    PASSWORD = '001.2021'

    # connect to server
    logging.debug('connecting to ' + SERVER)
    server = poplib.POP3_SSL(SERVER)
    #server = poplib.POP3(SERVER)

    # login
    logging.debug('logging in')
    server.user(USER)
    server.pass_(PASSWORD)

    # list items on server
    logging.debug('listing emails')
    # Get number of existing emails.
    number_of_messages = len(server.list()[1])
    # Loop in the all emails.
    for i in range(number_of_messages):
        print('   in for')
        # Get one email.
        for msg in server.retr(i+1)[1]:
            # Get the email from address. 
            msg_r = msg.get('From')
            print('This message is: ' + msg_r)
    server.quit()
    print('END')




prueba()

