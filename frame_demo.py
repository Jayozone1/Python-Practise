#This program creates labelsin two different frames.

import tkinter

class MyGUI:
    def __init__(self):
        #Create the main window widget.
        self.main_window = tkinter.Tk()

        #Create two frames, one for the top of thw window, andone for the bottom.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create three Label widgets for the top frame.
        self.label1 = tkinter.Label(self.top_frame, text='Winken')
        self.label2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label3= tkinter.Label(self.top_frame, text='Nod')

        #Pack the labels that are in the top frame. Use the side='top' argument to stack them one on top of the other.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        #Create three Label widgets for the bottom frame.
        self.label4 = tkinter.Label(self.bottom_frame, text='Winken')
        self.label5 = tkinter.Label(self.bottom_frame, text='Blinken')
        self.label6 = tkinter.Label(self.bottom_frame, text='Nod')

        #Pack the labels that are in the bottom frame use the side='left argument to arrange them horizontally from the lef of the frame.
        self.label4.pack(side='bottom')
        self.label5.pack(side='bottom')
        self.label6.pack(side='bottom')

        #Yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop.
        tkinter.mainloop()

#Create an instance of the MyGUI class.
my_gui = MyGUI()

