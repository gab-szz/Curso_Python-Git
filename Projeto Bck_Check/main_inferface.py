from tkinter import *
from tkinter import ttk

main_interface = Tk()
main_interface.title("EASoftware")
main_interface.geometry("600x400+330+120")
main_interface["bg"] = '#9999ff'
main_interface.resizable(False,False)

# Primeiro frame

first_frame = Frame(main_interface, bd=4, bg="#b3b3ff", highlightbackground='#1a1aff', highlightthickness=3)


first_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
title_label = Label(first_frame, text="EASoftware", bg=first_frame["bg"], font=('verdana', 15, 'bold'))
title_label.place(relx=0.40, rely=0.01)
execute_button = Button(first_frame,)

main_interface.mainloop()