import tkinter as tk
from time import strftime, gmtime
from datetime import datetime, timedelta
# from win10toast import ToastNotifier

def update_time():
    current_time_cet = datetime.utcnow() + timedelta(hours=1) # timedelta hours=1 means in CET is UTC+1
    current_time_ist = datetime.utcnow() + timedelta(hours=5, minutes=30) # Here we want time differce of 5.30 hours as per timezone in Paris.
    
    string_ist = current_time_ist.strftime('IST: %H:%M:%S %p')
    string_cet = current_time_cet.strftime('CET: %H:%M:%S %p')

    label_cet.config(text=string_cet)
    label_ist.config(text=string_ist)

    # toaster.show_toast("Digital Clock", string_cet, string_cet, duration=1)
    root.after(1000,update_time)

root = tk.Tk()
root.title("IST and CET Dual clock Widget")

# toaster= ToastNotifier()

# def popup():
#     popup = tk.Toplevel(root)

#Label for IST time stamp

label_ist = tk.Label(root,font=('calibri',20,'bold'), background = 'black', foreground= 'white')
label_ist.pack(anchor='center', pady= 10),

#Label for CET time stamp
label_cet = tk.Label(root, font=('calibri',20,'bold'), background = 'black', foreground= 'white')
label_cet.pack(anchor='center', pady = 10)


update_time()
root.mainloop()    # mainloop of Tk