# using urllib

# - reading a text file from the web
import socket
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

'''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
'''
# - reading webpages from the web
'''
fhand = urllib.request.urlopen('http://www.dr-chuck.com/pages1.htm')
for line in fhand:
    print(line.decode().strip())
'''
# - pulling an image from the web and saving it to hd
# -- use http://data.pr4e.org/cover3.jpg as the url for the image
# -- todo: need to use regex to remove everthing after the ? and #'s (including the # and the ?)
'''
img_types = ['jpg', 'jpeg', 'png', 'svg']
input_img = input('what image would you like to save? ')
input_img = input_img.lower()

img = urllib.request.urlopen(input_img)

input_img = input_img.replace('/', '.')
input_img = input_img.split('.')
print(input_img)

for type in img_types:
    try:
        input_img.index(type)
        img_pos = input_img.index(type)
        img_name = input_img[(img_pos - 1)] + '.' + input_img[img_pos]
        # print(img_name)
    except Exception:
        print('...')

fhand = open(img_name, 'wb')
size = 0
while True:
    # this reads 100,000 characters at a time, then moves to the next 100,000 characters/bytes
    # this is done to presever memory
    info = img.read(100000)
    # this checks if there are any other characters to read, if not it breaks to the if loop
    if len(info) < 1:
        break
    # this records the # of characters in the image, to give you a sense of the size
    size = size + len(info)
    # this writes the 100,000 of the image to fhand, which we opened on line 24 to save the image to
    fhand.write(info)

print(size, 'characters copied to desktop')
'''
'''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
'''

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
'''
'''
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1644298.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
# print(soup)

# retrive all span tags
sum = 0
tags = soup('span')
for tag in tags:
    # print(tag.contents[0], type(tag.contents[0]))
    sum = sum + int(tag.contents[0])
print(sum)
'''

'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# count up to 4
count = 0
# postioon up to 3
position = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Shawnpaul.html'
while count < 7:
    print('WHILE LOOP REPEAT')
    position = 0
    count += 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        position += 1
        # print(tag)
        # print(tag.get('href'))
        if not position == 18:
            continue
        else:
            url = tag.get('href')
            print(url)
            break
