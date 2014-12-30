from wx.lib.wxpTag import _param2dict

__author__ = 'cal02'

import socket
from struct import*

global ip_of_master

def send_command(message):
    UDP_IP = ip_of_master
    UDP_PORT = 49000

    message = "CMND0" + message
    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))
    print str(bytes(message)) + " sent"


def send_dref(dref,param):
    UDP_IP = ip_of_master
    UDP_PORT = 49000

    header = "DREF0"

    valOfDref = bytearray([ord(param[0]),ord(param[1]),ord(param[2]),ord(param[3])])
    #valOfDref = bytearray([0,160,42,70])

    lenOfBlank = 509-len(header)-len(valOfDref)-len(dref)

    filler = ""
    filler = filler.ljust(lenOfBlank)

    message = header + valOfDref + dref + filler

    print message

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))
    print str(bytes(message)) + " sent"

def send_papt(param1,param2,param3,param4):
    UDP_IP = ip_of_master
    UDP_PORT = 49000

    header = "PAPT\0"

    airport = param1 + "\0\0\0\0"

    message = header + airport + param2 + param3 + param4

    print message

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))
    print str(bytes(message)) + " sent"

def send_dsel(numOfGroup):

    UDP_IP = ip_of_master
    UDP_PORT = 49000

    header = "DSEL0"

    message = header

    for i in range(0,numOfGroup):
        message += bytearray([i,0,0,0])

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))
    print str(bytes(message)) + " sent"


def send_fail(equipment):

    UDP_IP = ip_of_master
    UDP_PORT = 49000

    header = "FAIL"+"\0"
    equipment = equipment +"\0"

    message = header + equipment

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))





