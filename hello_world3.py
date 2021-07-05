#This program uses the side='left' argumenr with the pack method to change the layout of the widgets.

import tkinter

class MyGUI:
    def __init__(self):
        #Create the main window widget.
        self.main_window = tkinter.Tk()

        #Create two label widgets.
        self.label1 = tkinter.Label(self.main_window,text='Hello World!')

        self.label2 = tkinter.Label(self.main_window,text='This is my GUI program.')
        #Call both Label widgets' pack method.
        self.label1.pack(side='top')
        self.label2.pack(side='bottom')

        #Enter the tkinter main loop
        tkinter.mainloop()

#Create an instance of the MyGUI class
my_gui = MyGUI()