__author__ = 'mattapy'
__date__ = 'February 8th, 2014'

'''Simple TCP packet sending script.'''

import socket

tcp_Addr = input('Address? \n>')
tcp_Port = int(input('Port? \n>'))
msg = input('Message?')
c = int(input('How many times?'))
buffer_Size = 1024

for x in range(0, c):

    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.connect((tcp_Addr.encode('utf-8'), tcp_Port))
    host.send(msg.encode('utf-8'))
    data = s.recv(buffer_Size)
    host.close()
    print('Sent "{}" to {}:{}, and received: {}'.format
          (msg, tcp_Addr, tcp_Port, data))

print('Complete')
