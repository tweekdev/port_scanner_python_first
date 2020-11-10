# -*-coding:Latin-1-*
import socket
import subprocess
import sys
from datetime import datetime

import errno

subprocess.call('clear', shell=True) #nettoyer le terminal
remote_server=input('Enter the domain name: ')
remote_server_ip=socket.gethostbyname(remote_server)

print('IPv4 : ', remote_server_ip) #affiche l'addresse ip de la cible

print("-"*60)
print('Please wait while scanning', remote_server_ip)
print("-"*60)

t1=datetime.now()
port_table: list=[21, 22, 23, 25, 53, 80, 110, 119, 443]
try:
    for port in port_table:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = connection.connect_ex((remote_server_ip, port))
        if result==0:
            print('Port {}: open'.format(port))
        else:
            print('Port {}: closed'.format(port))
except KeyboardInterrupt:
    print('PRESS CTRL + C')
except:
    print('Something wrong !!!')
    sys.exit()
t2=datetime.now()

t_total=t2-t1
print("-"*60)
print('Scan done in ', t_total, 'Second')

