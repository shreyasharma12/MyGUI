import tkinter

class MyGUI: 
    def __init__(self): 
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window,text = "Hello World!")

        self.label2 = tkinter.Label(self.main_window,text = "This is my GIU program.") 

        self.label1.pack(side = "top")
        self.label2.pack(side = "bottom") 

        tkinter.mainloop()

my_gui = MyGUI() 

print("Moving on.....")  