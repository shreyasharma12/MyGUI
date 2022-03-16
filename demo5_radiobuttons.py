import tkinter
import tkinter.messagebox


class KILO_Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("200x200")
        self.main_window.title("input Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        #set the intVar object to 1 
        self.radio_var.set(10)
        self.rb1 = tkinter.Radiobutton(self.top_frame, text = "Option 1", variable = self.radio_var, value = 10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = "Option 1", variable = self.radio_var, value = 20)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = "Option 1", variable = self.radio_var, value = 30)

        #pack the 

     

        self.top_frame.pack(side = ("top")
        self.bottom_frame.pack(side = ("top")

        self.okbutton = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.reserbutton = tkinter.Button(self.bottom_frame, text = "Reset", command = radio_var.set(10))
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.ok_button.pack(side = "left")
        self.reset_button.pack(side = "left") 
        self.quit_button.pack(side = "left")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection","You have ")
        

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)

        self.miles_var.set(miles)


kilo_conv = KILO_Converter()


print("Moving on...")