'''
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire docu-
ment and count the total number of characters and display the count
of the number of characters at the end of the document.

*you could use: data.pr4e.org 80 as input to test
*and use: romeo.txt as sub

from: Python for Everybody
Exploring Data Using Python 3
Charles R. Severance
'''

import socket

url = input('Enter url<space and port>: ')
url_port = url.split()
li = list()

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
    received = b''

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count += len(data)
        received = data.decode()
        words = received.split()
        for word in words:
            li.append(word)


    #to remove most of the headers uncomment the two lines below
    #x = li.index('Content-Type:')
    #del li[:x]
    prnt = ''
    for each in li[:3000]:
        hold = ''.join(each)
        prnt += hold + ' '

    print(prnt)


    print('Here is the total size of data---', count)
    print('Here is the numbers of characters: ', len(li))
except OSError:
    print('There was no connection!')
except:
    print('You have entered the wrong sub!')
