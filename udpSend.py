__author__ = 'Mattapy'
__date__ = 'January 24th, 2014'
__updated__ = 'February 8th, 2014'

'''Simple UDP packet sending script.
   Gets user input for address and ports
   to send a UDP packet, along with a user
   inputted message, X amount of times.
'''

import socket

ip_url = input('Input a I.P or URL address. \n>')
port = int(input('Port number? \n>'))
msg = input('And what message would you like to send? \n>')
a = int(input('How many times do you want to send this message? \n>'))

for x in range(0, a):

    print('Sending "{}" to {}:{}'.format(msg, ip_url, port))
    host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host.sendto(msg.encode('utf-8'), (ip_url.encode('utf-8'), port))

print('Completed')
