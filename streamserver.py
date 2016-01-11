#!/usr/bin/env python

BIND_ADDRESS = '0.0.0.0'
PORT = 16000

import logging
logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(message)s',
            handlers=[
                logging.StreamHandler()
            ]
)
from gevent.server import StreamServer
from collatz_conjection import max_cycle_count

def serve(socket, address):
    logging.debug('New connection from %s:%s' % address)
    socket.sendall(b'Welcome to the collatz maximum cycle count server! Type quit to exit.\r\n')
    socket.sendall(b'send range in format: start-end.\r\n')

    f_obj = socket.makefile()
    while True:
        line = f_obj.readline()

        if not line:
            logging.info("client disconnected")
            break

        if line.strip().lower() == 'quit':
            logging.info("client quit")
            break

        start, end = map(int, line.strip().split('-'))
        cycle_count = max_cycle_count(start,end)
        f_obj.write('collatz maximum cycle count is [{0}] for range {1}\n'.format(cycle_count, line))
        f_obj.flush()

if __name__ == '__main__':
    server = StreamServer((BIND_ADDRESS, PORT), serve)
    logging.info('Starting collatz maximum cycle count server on port {0}'.format(PORT))
    server.serve_forever()