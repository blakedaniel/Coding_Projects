'''
# creating a mini web browswer
import socket

# establish socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to sever at host on port number
mysocket.connect(('data.pr4e.org', 80))

# send GET request to pull text from host
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

# while loop that pulles every line of html code until a line of code has 0 characters
while True:
    data = mysocket.recv(600)
    if (len(data) < 1):
        break
    print(data.decode())
mysocket.close
'''

# using urllib to get information from websites
import urllib.error
import urllib.parse
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    line = line.decode().rstrip()
    print(line)
