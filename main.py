__author__ = 'cal02'

from Tkinter import *
from View import *
from Model import *
import comm

class Xpanel(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="black")
        self.pack(fill=BOTH, expand=1)

        self.parent = parent
        self.parent.title("Xpanel-V0.1")
        self.initUI()

    def initUI(self):
        model = Model()
        view = View(self.parent,model)

        reading = comm.Read()
        reading.receive_data()



    def onExit(self):
        self.quit()


def main():

    root = Tk()
    root.geometry("{0}x{1}+0+0".format(600, 400))
    app = Xpanel(root)
    root.mainloop()


if __name__ == '__main__':
    main()


