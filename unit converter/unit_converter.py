from tkinter import *
from tkinter.font import *
from UnitConverter import UnitConverter

def calculate_unit():

    # geting item in list_box
    unit_from = list_box_from.get(ACTIVE)
    unit_to = list_box_to.get(ACTIVE)

    # geting value in Entry
    value_from = float(entry_from.get())
    
    # calculate
    con = UnitConverter(unit_from, unit_to, value_from)
    
    # insert result to entry_to
    entry_to.delete(0, END)
    entry_to.insert(END, con.convertor())

    



# root
window = Tk()

# font
my_font = Font(family='Consolas', size=18)

# pading
pad_x = 5
pad_y = 5


# labels
label_from = Label(window, text='from', font=my_font)
label_to = Label(window, text='to', font=my_font)

# place of labels
label_from.grid(row=0, column=0, sticky=W, padx=pad_x, pady=pad_y)
label_to.grid(row=0, column=1, sticky=W, padx=pad_x, pady=pad_y)

# Entrys
entry_from = Entry(window, font=my_font, fg='brown')
entry_to = Entry(window, font=my_font, fg='brown')

# place of Entyrs
entry_from.grid(row=1, column=0, padx=pad_x, pady=pad_y)
entry_to.grid(row=1, column=1, padx=pad_x, pady=pad_y)

# ListBoxes
list_box_from = Listbox(window, exportselection=False, font=my_font)
list_box_to = Listbox(window, exportselection=False, font=my_font)

# place of ListBoxes
list_box_from.grid(row=2, column=0, padx=pad_x, pady=pad_y)
list_box_to.grid(row=2, column=1, padx=pad_x, pady=pad_y)

# insert item to ListBox
list_box_from.insert(END, 'Centimeter')
list_box_from.insert(END, 'Meter')
list_box_from.insert(END, 'Kilometer')


list_box_to.insert(END, 'Centimeter')
list_box_to.insert(END, 'Meter')
list_box_to.insert(END, 'Kilometer')



# Button
button = Button(window, text='Calculate', font=my_font, command=calculate_unit)

# place of Button
button.grid(row=3, column=0, columnspan=2, sticky=W+E, padx=pad_x, pady=pad_y)


# place of window  on screan

def center_window():
    window.update_idletasks()

    # width of window
    w = window.winfo_width()

    # height of window
    h = window.winfo_height()

    # width of screan
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    # new x,y of window

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d'%(w, h, x, y))

center_window()
window.mainloop()