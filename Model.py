__author__ = 'cal02'

import comm as comm
from struct import*

class Model:

    def __init__(self):
        self.ip_of_master = "192.168.1.23"
        comm.ip_of_master = self.ip_of_master

    def set_ip(self,input_ip):
        self.ip_of_master = input_ip
        comm.ip_of_master = input_ip

        print "IP set for " + input_ip

    def greet(self):
        print("Greetings!")

    def go_stop(self):

        print("GO Button Pressed")

        param = 10920
        paramF = pack('f',param)

        dref = "sim/cockpit2/radios/actuators/nav1_frequency_hz[0]"
        comm.send_dref(dref, paramF)

    def btn1_callback(self):
        print "Button1 pressed"

        cmd = "sim/operation/pause_toggle"                    #buraya ilgili komutu yazabilirsiniz
        comm.send_command(cmd)

    def btn2_callback(self):
        print "Button2 pressed"

        param = 11250
        paramF = pack('f',param)

        dref = "sim/cockpit2/radios/actuators/nav1_frequency_hz[0]"
        comm.send_dref(dref, paramF)


    def btn3_callback(self):
        print "Button3 pressed"

        airport = "LTBA"
        type_start = 13
        local_rwy_ramp = 0
        backwards = 0

        #10 RAMP
        #11 RWY TAKE OFF
        #12 APPROACH 3 nm
        #13 APPROACH 10 nm


        param1I =  pack('i',type_start)
        param2I =  pack('i',local_rwy_ramp)
        param3I =  pack('i',backwards)

        comm.send_papt(airport,param1I,param2I,param3I)

    def btn4_callback(self):
        print "Button4 pressed"

        equipment = "26"

        comm.send_fail(equipment)

    def btn5_callback(self):
        print "Button5 pressed"

        seriesOfDataIO = 11  #means from 0 to 10

        comm.send_dsel(seriesOfDataIO)

    def btn6_callback(self):
        print "Button6 pressed"

        user_aircraft = 0;

        order = pack('i',user_aircraft)
        aircraft = "Aircraft/Gliders/ASK21/ASK21.acf"

        comm.send_vehn(aircraft,order)

    def btn7_callback(self):
        print "Button6 pressed"

        comm.receive_data()

