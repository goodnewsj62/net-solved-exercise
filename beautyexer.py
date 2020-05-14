from urllib import request
from bs4 import BeautifulSoup
import ssl

# bypass ssl certificate
cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
op = request.urlopen(url,context = cxt).read()
soup = BeautifulSoup(op,'html.parser')
tags = soup('p')

count = 0

for tag in tags:
    count += 1

print(count)