from socket import *

'''
Client for obtaining the day and time.
'''

class Client(object):
    def __init__(self):
        self._HOST = 'localhost'
        self._PORT = 4000
        self._BUFSIZE = 1024
        self._ADDRESS = (self._HOST, self._PORT)

    def get_service(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect(self._ADDRESS)

        self.day_and_time = self.server.recv(self._BUFSIZE)
        print(self.day_and_time)

        self.server.close()


if __name__ == '__main__':
    client = Client()
    client.get_service()
