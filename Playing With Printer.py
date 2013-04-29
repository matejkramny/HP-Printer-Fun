#!/usr/bin/env python

import socket
import sys
import os.path

for i in [1,255]:
    # Default configuration
    host = '10.1.54.'+ str(i)
    port = 9100 #9100 is the default port.

    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error, e:
        print 'Connection error %s: %s.' % (e[0], e[1])
        continue;
    
    print 'Connected'
    
    title = "Title"
    job = "Job name"
    message = "Hello there"
    copies = "2"
    
    command = "\x1B%%-12345X@PJL RDYMSG DISPLAY = \"%s\"\r\n" % message
    command = command + "@PJL JOB NAME = \"%s\"\r\n" % job
    command = command + "@PJL SET COPES = %s\r\n" % copies
    command = command + "@PJL SET RET = OFF\r\n"
    command = command + "@PJL ENTER LANGUAGE = PCL\r\n"
    command = command + "\x1B\r\n%s\x1BE\7E\x1B%%-12345X@PJL \r\n" % message
    command = command + "@PJL EOJ\r\n"
    command = command + "\x1B%%-12345X\r\n"
    
    print 'Sending print job to %s title %s' % (host, title)
    
    sock.sendall(command)
