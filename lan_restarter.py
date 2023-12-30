
#!/usr/bin/env python

import urllib
import xml.etree.ElementTree as ET
import string
import socket
import time

lr_url = 'http://172.1.1.161/st0.xml'
host = "127.0.0.1"
port = 50012
nodeid = 99

doc = urllib.urlopen(lr_url).read()
tree = ET.fromstring(doc)

temp0 = float(tree.find('ia0').text)/10
vcc = float(tree.find('ia1').text)/10
temp1 = float(tree.find('ia10').text)/10
tempext = float(tree.find('ia11').text)/10
temp2 = float(tree.find('ia12').text)/10
tempint = float(tree.find('ia13').text)/10
humidity = float(tree.find('ia14').text)/10

print 'Temp0: ', temp0
print 'VCC: ', vcc
print 'Temp1: ', temp1
print 'Temp ext: ', tempext
print 'Temp2: ', temp2
print 'Temp int: ', tempint
print 'Humidity: ', humidity

# Send the frame of data via a socket
def send(frame,host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    frame = frame + '\r\n'
    s.send(frame)
    s.close()

t = time.time()

# Create a space seperated frame, timestamp nodeid val1 val2 etc
frame = str(t)+' '+str(nodeid)+' '+str(temp1)+' '+str(tempext)+' '+str(temp2)+' '+str(temp0)+' '+str(tempint)+' '+str(humidity)+' '+str(vcc)
send(frame, host)
