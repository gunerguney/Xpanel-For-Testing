__author__ = 'cal02'

import socket
from struct import*
from threading import *
from time import *


global ip_of_master

ip_of_master = "127.0.0.1"


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

    param = pack('f',param)

    term = pack('b',0)

    valOfDref = bytearray([ord(param[0]),ord(param[1]),ord(param[2]),ord(param[3])])
    #valOfDref = bytearray([0,160,42,70])

    lenOfBlank = 509-len(header)-len(valOfDref)-len(dref)-len(term)

    filler = ""
    filler = filler.ljust(lenOfBlank)

    message = header + valOfDref + dref + term +filler

    #print message

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))
    print str(bytes(message)) + " sent"

def send_papt(airport,type_start,local_rwy_ramp,backwards):
    UDP_IP = ip_of_master
    UDP_PORT = 49000

    type_start      =  pack('i',type_start)
    local_rwy_ramp  =  pack('i',local_rwy_ramp)
    backwards       =  pack('i',backwards)

    header = "PAPT\0"

    airport = airport + "\0\0\0\0"

    message = header + airport + type_start + local_rwy_ramp + backwards

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

def request_dref():

    UDP_IP = ip_of_master
    UDP_PORT = 49000

    header = "RREF\0"

    frequency = 20
    index = 1

    frequency = pack('i',frequency)
    index = pack('i',index)


    drefString = "sim/flightmodel/position/indicated_airspeed"

    lenOfBlank = 400-len(drefString)

    filler = "0"
    filler = filler.ljust(lenOfBlank)

    message = header  + frequency + index + drefString + filler

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

def send_vehn(aircraft,order):
    UDP_IP = ip_of_master
    UDP_PORT = 49000

    param = pack('i',17)

    header = "VEHN0" + param

    aircraft = aircraft.ljust(150,'\0')

    weapon = ""
    weapon = weapon.ljust(960,'\0')

    message = header + "0" + aircraft + weapon

    print len(message)

    sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock2.sendto(message, (UDP_IP, UDP_PORT))



class Read():

    dataFromSim = []

    #for receive data output indexes and data
    def receive_data(self):
        t = Thread(target= self.start_reading)
        t.start()

    def start_reading(self):
        UDP_IP = "127.0.0.1"
        UDP_PORT = 49007
        BUFFER_SIZE = 4793      #133*36 + 5 = numberOfGroup * sizeOfEachGroup + sizeOfHeader

        sock3 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock3.bind((UDP_IP, UDP_PORT))

        while True:
            data = sock3.recv(BUFFER_SIZE)

            print data
            self.parseRRefData(data)

            #self.parseUDPData(data)

    def parseRRefData(self,message):

        sizeOfHeader = 5
        header = message[0:sizeOfHeader]

        #msg = unpack('i',message[5:7])

        print "Header: "+header

    def parseUDPData(self,message):

        sizeOfHeader = 5
        sizeOfEachData = 4
        numberOfDataInGroup = 8
        numberOfGroup = 133
        sizeOfEachGroup = 36

        header = message[0:sizeOfHeader]

        self.listOfGroup = []

        #0-5 header
        #5-41 1st group
        #41-77 2nd group
        #77-113 3rd group
        #113-149 4th group
        #149-185 5th group
        #185-221 6th group
        #221-257 7th group

        #0-4 index
        #4-8 1st
        #8-12 2nd
        #12-16 3rd
        #16-20 4th
        #20-24 5th
        #24-28 6th
        #28-32 7th
        #32-36 8th

        for i in range(sizeOfHeader,sizeOfEachGroup*numberOfGroup,sizeOfEachGroup):

            part = message[i:i+sizeOfEachGroup]

            group = {}
            order = 0

            for j in range(0,sizeOfEachGroup,sizeOfEachData):

                if j == 0:
                    group['index'] = unpack('i',part[j:j+sizeOfEachData])[0]
                else:
                    group[order] = unpack('f',part[j:j+sizeOfEachData])[0]
                    order += 1

            self.listOfGroup.append(group)

        self.dataFromSim = self.listOfGroup
        print "All Group was Received"
        print self.dataFromSim


    def getData(self,index1,index2):

        try:
            return self.dataFromSim[index1][index2]
        except IndexError:
            return 0











