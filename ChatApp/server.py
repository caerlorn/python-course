import socket
import threading

# Yildirim Can Sehirlioglu - 156336IVCM - Hmw4
# put together and tested with 2.7 on Windows

ENCODING = 'utf-8'
HOST = ''
PORT = 9999
BUFSIZE = 1024
connection_lock = threading.Lock()
clients = set()


def broadcast(message, connection):
    connection_lock.acquire()
    count = 0
    print "Sending %s" % message
    for con in clients:
        if con == connection:
            continue
        try:
            con.send(message.encode(ENCODING))
            count += 1
        except socket.error:
            con.close()
            pass
    print "Data sent to %d clients \n" % count
    connection_lock.release()


def incoming(connection):
    while True:
        print "Waiting for message\n"
        message = connection.recv(BUFSIZE).decode(ENCODING)
        if not message:
            print "Removing from client list"
            connection_lock.acquire()
            clients.remove(connection)
            connection_lock.release()
            return
        print "Received %s, sending to others" % message
        broadcast(message, connection)


sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind((HOST, PORT))
sckt.listen(5)

while True:
        print "\nWaiting for a connection..."
        (connection, address) = sckt.accept()
        print "Connection received.. adding to client list"
        connection_lock.acquire()
        clients.add(connection)
        connection_lock.release()
        print "Spawning thread for client " + str(address[0]) + ":" + str(address[1])
        threading.Thread(target=incoming, args=[connection]).start()
