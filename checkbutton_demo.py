#This program demnstrates a group of checkbuttons widgets.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Create  Create two frames. One for the checkbuttons and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create three IntVar obhjects to use with the checkbuttons.
        self.cb_var1 = tkinter.IntVar() 
        self.cb_var2 = tkinter.IntVar() 
        self.cb_var3 = tkinter.IntVar() 

        #Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        #create the Checkbutton widgets in the top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,text='Option 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,text='Option 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,text='Option 3', variable=self.cb_var3)

        #Pack the checkbuttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #Create an OK button and a quit button.
        self.ok_button = tkinter.Button(self.bottom_frame,text='OK',command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)

        #Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Start the mainloop.
        tkinter.mainloop()

#The show_choice method is the callback function for the OK button.

def show_choice(self):
    #Create a message string.
    self.message = 'You seleted:\n'

    #Dtermine which  Checkbuttons are selected and build the message string accordingly.
    if self.cb_var1.get()  == 1:
        self.message = self.message + '1\n' 
    if self.cb_var2.get()  == 1:
        self.message = self.message + '2\n' 
    if self.cb_var3.get()  == 1:
        self.message = self.message + '3\n' 

    
    #Display the message in an info dialog box.
    tkinter.messagebox.showinfo('SelectioN', self.message)

#Create an instance of the MyGUI class.
my_gui =MyGUI()