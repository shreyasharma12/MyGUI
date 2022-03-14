import tkinter
import tkinter.messagebox 

class KiloConverterGUI: 
    def __init__(self): 
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window) 

        self.prompt_label = tkinter.Label(self.top_frame,text = "Enter a distance in Kilometers")

        self.kilo_entry = tkinter.Entry(self.top_framce,width = 10)


        self.calcbutton = tkinter.Button(self.main_window, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(se)
    

        self.calcbutton.pack(side = "left")
        self.kilo_entry.apck(side = "right")

        self.descr_label = tkinter.Label(self.midframe, text = "Converted to miles:")

        self.miles_var = tkinter.StringVar()

        self.miles_label - tkinter.Label(self.mid_frame, textvaribale = self.miles_variable)
        

        tkinter.mainloop()

        

    def convert(self):

        kilo = float(self.kilo_entry.get())
        
        miles = round((kilo * 0.6214),2)

        tkinter.mesagebox.showinfo("Results",str(kilo) + " kilometers is equal to " + str(miles) + " miles."))



my_gui = KiloConverterGUI() 
