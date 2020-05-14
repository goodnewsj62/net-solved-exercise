'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.

from: Python for Everybody
Exploring Data Using Python 3
Charles R. Severance
'''
from urllib import request
import ssl

#help ignore ssl certificate errors
cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE

url = input('Please enter url: ')
op = request.urlopen(url).read()
txt = op.decode()
file = open('new.txt', 'w')
file.write(txt)
file.close()

li = list()
file = open('new.txt', 'r')

for line in file:
    line = line.rstrip()
    words = line.split()
    for word in words:
        li.append(word)

prnt = ''
for each in li[:3000]:
    hold = ''.join(each)
    prnt += hold + ' '

print(prnt)
print('Number of characters is : ', len(li))




