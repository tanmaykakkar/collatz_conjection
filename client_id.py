import gevent

from gevent import monkey

monkey.patch_all()

from gevent import socket

import time

import random


def get_socket(address):
    sock = socket.create_connection(address)
    return sock

def get_start_end():
    start = 100
    end = 0
    while start > end:
        start = random.randrange(1,1000000)
        end = random.randrange(1,1000000)
    return (start, end)
def collatz_client(host, port, times, pid):
    try:
        sock = get_socket((host,port))
        # To receive welcome message
        # print sock.recv(1024)
        # print sock.recv(1024)

        while times > 0:
            # printing on which term client is running now
            print "Client id %s time %d-->" % (pid,times)

            start, end = get_start_end()
            query = "%s-%s\n"%(start,end)
            print ("Client id %s sent:"%(pid)),
            print (query),
            sock.sendall(query)
            s = sock.recv(1024)
            print ("Client id %s received:"%(pid)),
            print (s),
            times -= 1
        sock.close()
    except socket.error:
        print "Could not communicate with server. Is the server ready and listening at %s:%s?"%(host, port)

queries = {}

def talk_to_server(host, port, pid):
    global queries
    times = random.randrange(1,100)
    queries[pid] = times
    collatz_client(host, port, times, pid)


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 16000
    no_of_clients = int(raw_input("Enter the number of clients from this machine:"))
    print "Spawning %s clients"%(no_of_clients)
    start = time.time()
    coroutines = [gevent.spawn(talk_to_server,host, port, i) for i in xrange(0,no_of_clients)]
    gevent.joinall(coroutines)
    end = time.time()
    tot_queries = 0
    for k, v in queries.iteritems():
        tot_queries += v
    print ""
    print "============================================================"
    print "%4d queries processed in %ss time"%(tot_queries,(end - start))