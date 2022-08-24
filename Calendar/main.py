from tkinter import *
from tkinter.font import *
from tkinter import messagebox
import requests
import threading

###########

def get_data():

    # threading
    my_thread = threading.Thread(target=get_data_from_server)
    my_thread.start()

        
def get_data_from_server():
    
    # DISABLED button
    button['state'] = DISABLED
    # DISABLED entry
    entry['state'] = DISABLED


    # get data from entry
    date = entry.get()

    # request to API
    r = requests.get('https://persiancalapi.ir/jalali/'+date)

    # procces on json file
    if r.status_code == 200:
        # convert to json
        data = r.json()

        list_box.delete(0, END)
        if data['is_holiday'] == True:
            list_box.insert(END,'روز تعطیل')
        for item in data['events']:
            list_box.insert(END, item['description'])
    else:
        messagebox.showerror('دریافت ناموفق اطلاعات',f'خطای {r.status_code}')
    

    # NORMAL button
    button['state'] = NORMAL
    # NORMAL entry
    entry['state'] = NORMAL

###########
# root
window = Tk()
window.resizable(0, 0)

# font
my_font = Font(family='Vazir', size=18)

# pading
pad_x = 10
pad_y = 10


# label
label = Label(window, text=':لطفا تاریخ را وارد کنید', font=my_font)
# place of labels
label.grid(row=0, sticky=E, padx=pad_x, pady=pad_y)

# entry
entry = Entry(window, font=my_font, fg='brown')
# place of label
entry.grid(row=1, sticky=E, padx=pad_x, pady=pad_y)


# list_box
list_box = Listbox(window, font=my_font, height=7, width=50)
# place of list_box
list_box.grid(row=2, sticky=W+E, padx=pad_x, pady=pad_y)
# insert to list box
list_box.configure(justify=RIGHT)


# Button
button = Button(window, text='دریافت اطلاعات', font=my_font, command=get_data)
# place of button
button.grid(row=3, sticky=E+W, padx=pad_x, pady=pad_y )



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