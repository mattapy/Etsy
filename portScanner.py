__author__ = 'Mattapy'

import socket
host_Ip = input('Host IP? \n>')
port_start = int(input('Port to start from? \n>'))
port_end = int(input('Port to end on? \n>'))

for port in range(port_start, port_end):
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if (host.connect((host_Ip.encode('utf-8'), port)) == 0):
        print('Port "{}" is open on {}'.format(port, host_Ip))
    #else:
        #print('Port "{}" is closed on {}'.format(port, host_Ip))
    host.close()

