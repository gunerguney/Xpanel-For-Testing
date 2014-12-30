__author__ = 'cal02'

from Tkinter import *

class ToolbarButton(Button):
    def __init__(self, parent, text, command):

        Button.__init__(self, parent)
        self.configure(text=text, height=4, width=10, bg="black", fg="white", command=command)
        self.pack(side=LEFT, expand=YES, fill=X)

class LeftMenuButton(Button):
    def __init__(self,parent, text, command):
        Button.__init__(self, parent)
        self.configure(text=text, height=4, width=25, bg="black", fg="white", command=command)
        self.pack(side=TOP, expand=YES, fill=Y)


class View:

    def __init__(self, master, model):
        self.master = master
        self.model = model

        # create a toolbar
        toolbar_panel = Frame(master)
        toolbar_panel.pack(side=BOTTOM, fill=X)


        toolbar1 = Frame(toolbar_panel)
        toolbar1.config(background="black", bd=0, relief=GROOVE)
        toolbar1.pack(side=TOP, fill=X)

        self.pos_btn = ToolbarButton(toolbar1, "POSITION", model.greet)
        self.env_btn = ToolbarButton(toolbar1, "ENVIRONMENT", model.greet)
        self.fuel_btn = ToolbarButton(toolbar1, "FUEL", model.greet)
        self.weight_btn = ToolbarButton(toolbar1, "WEIGHT", model.greet)
        self.pb_btn = ToolbarButton(toolbar1, "PUSHBACK", model.greet)
        self.ac_btn = ToolbarButton(toolbar1, "AIRCRAFT", model.greet)
        self.fail_btn = ToolbarButton(toolbar1, "FAILURE", model.greet)

        toolbar2 = Frame(toolbar_panel)
        toolbar2.config(background="black", bd=0, relief=GROOVE)
        toolbar2.pack(side=BOTTOM, fill=X)

        self.view_btn = ToolbarButton(toolbar2, "VIEW/SLEW ", model.greet)
        self.bbox_btn = ToolbarButton(toolbar2, "BLACKBOX", model.greet)
        self.comp_btn = ToolbarButton(toolbar2, "COMPUTERS", model.greet)
        self.mtn_btn = ToolbarButton(toolbar2, "MOTION", model.greet)
        self.frz_btn = ToolbarButton(toolbar2, "FREEZE", model.greet)
        self.exit_btn = ToolbarButton(toolbar2, "EXIT", model.greet)
        self.empty_btn = ToolbarButton(toolbar2, "", model.greet)

        #end toolbar


        #left menu for training buttons

        go_panel = Frame(master)
        go_panel.place(x=0.5,y=0.5,relheight=0.7, relwidth=0.14)

        ip_panel = Frame(go_panel)
        ip_panel.config(background="black", bd=0, relief=GROOVE)
        ip_panel.pack(side=TOP, expand=YES, fill=Y)

        #ip_panel
        self.ip_lbl = Label(ip_panel,text= "X-Plane IP:",bg="black", fg="white")
        self.ip_lbl.pack(side=LEFT)

        self.ip = StringVar()
        self.ip.set(model.ip_of_master)

        self.ip_of_master = Entry(ip_panel,textvariable=self.ip)
        self.ip_of_master.pack(side=RIGHT)

        self.submit_ip_btn = Button(go_panel, text="OK", command = lambda :model.set_ip(self.ip_of_master.get()))
        self.submit_ip_btn.pack(side=TOP)

        #end of ip_panel


        self.go_btn = LeftMenuButton(go_panel, "GO / STOP", model.go_stop)
        self.go_btn.config(activebackground='red')

        self.button_1 = LeftMenuButton(go_panel, "Button #1", model.btn1_callback)

        self.button_2 = LeftMenuButton(go_panel, "Button #2", model.btn2_callback)

        self.button_3 = LeftMenuButton(go_panel, "Button #3", model.btn3_callback)

        self.button_4 = LeftMenuButton(go_panel, "Button #4", model.btn4_callback)

        self.button_5 = LeftMenuButton(go_panel, "Button #5", model.btn5_callback)

        #end of left menu for training buttons


