from tkinter import *
from tkinter import ttk



gui = Tk(className='Guitario - Window Size')

gui.geometry("600x200")

gui.title("Guitario")

tab_control = ttk.Notebook(gui)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab4 = ttk.Frame(tab_control)

tab5 = ttk.Frame(tab_control)

tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text='E-Minor')

tab_control.add(tab2, text='C-Major')

tab_control.add(tab3, text='A-Major')




lbl1 = Label(tab1, text= 'Index finger - 2nd fret - 2nd string ,Middle finger - 2nd fret - 3rd string')

lbl1.grid(column=0, row=0)


lbl2 = Label(tab2, text= 'Index finger - 1st fret - 5th string,  Middle finger - 2nd fret  -3rd string, - Ring finger - 3rd fret -2nd string')

lbl2.grid(column=0, row=0)


lbl3 = Label(tab3, text= 'Index finger - 2nd fret - 3rd string,  Middle finger - 2nd fret  -4th string, - Ring finger - 2nd fret -5th string')

lbl3.grid(column=0, row=0)




btn=Button(gui, text="Start", fg='blue')
btn.place(x=1, y=175)

tab_control.pack(expand=1, fill='both')


gui.mainloop()