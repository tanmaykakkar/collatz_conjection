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
import threading

from collatz_conjection import max_cycle_count

def max_cycle_count_and_flush(start, end, f_obj):
    cycle_count, number = max_cycle_count(start, end)
    f_obj.write('Collatz maximum cycle count is [{0}] of number {1} for range {2}-{3}\n'.format(cycle_count, number, start, end))
    f_obj.flush()

def serve(socket, address):
    logging.debug('New connection from %s:%s' % address)
    socket.sendall(b'Welcome to the collatz maximum cycle count server! Type quit to exit.\r\n')
    socket.sendall(b'Send range in format: start-end.\r\n')

    f_obj = socket.makefile()
    while True:
        line = f_obj.readline()

        if not line:
            logging.info("client disconnected")
            break

        if line.strip().lower() == 'quit':
            logging.info("client quit")
            break
        try:
            if '-' in line:
                start, end = map(int, line.strip().split('-'))
                threading.Thread(target=max_cycle_count_and_flush, args=(start, end, f_obj)).start()
        except ValueError as e:
            logging.exception(e)

if __name__ == '__main__':
    server = StreamServer((BIND_ADDRESS, PORT), serve)
    logging.info('Starting collatz maximum cycle count server on port {0}'.format(PORT))
    server.serve_forever()