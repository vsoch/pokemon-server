import socket
import threading
from pokemon.skills import catch_em_all
from time import sleep

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.pokemons = catch_em_all()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                client.send("Would you like to see pokemon?")
                data = client.recv(size)
                if data:
                    for key,data in self.pokemons.items():
                        client.send(data['ascii'])  # echo
                        client.send("\t%s" %data['name'])  # echo
                        sleep(2)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    port_num = 5005
    ThreadedServer('',port_num).listen()
