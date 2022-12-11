from tkinter import Label, Tk
import time

application_window = Tk()
application_window.title("Clock Widget")
application_window.geometry("400x150")
application_window.resizable(1, 1)

text_font = ("Helvetica", 64, "bold")
background = "#6266a3"
nums = "#000000"
border = 30

label = Label()


label = Label(application_window, font = text_font, bg = background, fg = nums, bd = border)
label.grid(row = 0, column = 1)

def clock_App():
       live = time.strftime("%H:%M:%S")
       label.config(text = live)
       label.after(200, clock_App)
       
clock_App()
application_window.mainloop()
