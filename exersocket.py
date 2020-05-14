''' Exercise: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.

*you could use: data.pr4e.org 80 as input to test
*and use: romeo.txt as sub

from: Python for Everybody
Exploring Data Using Python 3
Charles R. Severance
'''

import socket

url = input('Enter url<space and port>: ')
url_port = url.split()

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(((''.join(url_port[0])), (int(''.join(url_port[1])))))
except ValueError:
    print("SORRY! you entered an invalid port")
except IndexError:
    print('SORRY! you entered only url or port instead of the two')
except:
    print('NO connection')
try:
    reqst = input('Enter sub if any: ')
    cmd = 'GET http://' + ''.join(url_port[0]) + '/' + reqst + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.sendall(cmd)

    count = 0

    while True:
        data = mysock.recv(1000)
        if len(data) < 1:
            break
        count += len(data)
        print(data.decode().rstrip())

    print('Here is the total size of data---', count)
except OSError:
    print('There was no connection!')
except:
    print('You have entered the wrong sub!')
