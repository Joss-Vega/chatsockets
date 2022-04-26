from socket import *

direccionServidor = "localhost"
puertoServidor = 9099

socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind( (direccionServidor, puertoServidor) )
socketServidor.listen()

while True:
#conexion
    socketConexion, addr = socketServidor.accept()
    print("Conectado con un cliente", addr)
    while True:
#mensaje del cliente
        mensajeRecibido = socketConexion.recv(4096).decode()
        print(mensajeRecibido)

        if mensajeRecibido =='adios':
            break
#mandamoss mensaje al cliente
        socketConexion.send(input().encode())
    print("Desconectado el cliente", addr)
    #cerramos conexion
    socketConexion. close ()
