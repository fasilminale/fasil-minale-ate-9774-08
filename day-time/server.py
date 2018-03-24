'''
    Server for providing the day and time.
'''
from socket import *
from time import ctime
from threading import Thread

HOST = 'localhost'
PORT = 4000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)


class Server(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

    def run(self):
        msg = (ctime() + " have a nice day").encode('utf-8')

        try:
            self._client.send(msg)
        finally:
            self._client.close()


# The server now just waits for connections from clients # and hands sockets off to client handlers(server)
while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    handler = Server(client)

    handler.start()
