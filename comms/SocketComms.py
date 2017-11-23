import threading

from multiprocessing.connection import Listener
from multiprocessing.connection import Client
from threading import Thread

def socketListen():
    address = ('localhost', 6000)
    listener = Listener(address, authkey='secret password')
    print 'connection accepted from', listener.last_accepted
    while True:
        conn = listener.accept()
        msg = conn.recv()
        if msg == 'END':
            print msg
            conn.close()
            break;
        else:
            f = open( 'msg.conf', 'w' )
            f.write( msg + '\n' )
            f.close()
    listener.close()

def socketClient(host, port, stringOfnameValuePairs):

    address = (host, port)
    conn = Client(address, authkey='secret password')
    conn.send("val:10")
    conn.close()

if __name__ == '__main__':
    Thread(target = socketListen).start()
    #Thread(target = socketClient).start()