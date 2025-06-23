import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image
from tkinter import *
from tkinter.ttk import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import ttk
import os


executed_script = set()



def delete_files():
    files_to_delete = ["secret.key", "credentials.enc"]
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)

            print(f"{file} deleted.")
        else:
            print(f"{file} does not exist.")


        
        
        
        

def run_script(script_name):
    
    try:
        subprocess.run(["python", script_name], check=True)
        messagebox.showinfo("Successful", f"{script_name} executed successfully...!!!")
        
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"❌❌❌❌❌ Error running {script_name}: {e}")
        
def close_window():
    root.destroy()

def create_gui():
    window = tk.Tk()
    window.title("Sanity Checklist Report")
    window.geometry("800x1080")
    
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
    
    # image = Image.open(r"Template\\TE1.jpg")
    # photo = ImageTk.PhotoImage(image)
    
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    
    
    image = Image.open('Template/TE1.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(window, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)
    ## label with image;
    
    # background_label = Label(window, image=photo)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1) 
    
    label = tk.Label(window, text ="Select the Check you want to run")
    label.config(font=("Calibri", 14, "bold"))
    label.pack(pady=50)
    
    ### button for each check:
    # btn1 = tk.Button(window, text="SDWAN Check-Up", command = lambda: [window.destroy(), run_and_restart("SDWAN_Check.py")])
    # btn1.pack(pady=20)


    cred = tk.Button(window, text="Enter Login Credentials", width= 50, height=2 , command= lambda: [window.destroy(), run_and_restart("Cred_Store.py", "cred")])
    if "cred" in executed_script:
        cred.config(text= "Credentials Stored successfully!",bg="green", fg="white")
    cred.pack(pady=20)
    
    
    btn1 = tk.Button(window, text="SDWAN Check-Up", width= 50, height=2 , command= lambda: [window.destroy(), run_and_restart("SDWAN_Check.py", "btn1")])
    if "btn1" in executed_script:
        btn1.config(bg="green", fg="white")
    btn1.pack(pady=20)
    
    
    btn2 = tk.Button(window, text="Prisma Traffic in SDWAN Check-Up", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart("Prisma_Traffic.py", "btn2")])
    if "btn2" in executed_script:
        btn2.config(bg="green", fg="white")
    btn2.pack(pady=20)
    
    
    btn3 = tk.Button(window, text="Logstash Check", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart("Logstash.py", "btn3")])
    if "btn3" in executed_script:
        btn3.config(bg="green", fg="white")
    btn3.pack(pady=20)
    
    
    # btn4 = tk.Button(window, text="Test", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart(pyautogui.alert("Hello", "test"), "btn4")])
    # if "btn4" in executed_script:
    #     btn4.config(bg="green", fg="white", state = tk.DISABLED)  # state = 'disable' will also work same.
    # btn4.pack(pady=20)


    btn_close = tk.Button(window, text = "Quit",  width= 20, height=2, command =lambda: [delete_files(), window.destroy()],bg="red", fg="white")
    btn_close.config(font=("Calibri", 11, "bold"))
    btn_close.pack(padx= 50, pady=20)

    window.mainloop()


    
    
def run_and_restart(script_name, button_id):
    run_script(script_name)
    executed_script.add(button_id)
    create_gui()
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sanity Checklist Report")

    # load image

    image = Image.open(r"Template\\TE1.jpg")
    photo = ImageTk.PhotoImage(image)

    # Display image
    logo_label = tk.Label(root, image = photo)
    logo_label.pack(pady=20)

    label = tk.Label(root, text ="Sanity Checklist Report")
    label.config(font=("Calibri", 16, "bold"))
    label.pack(pady=50)

    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate",length=400)
    progress_bar.pack(side=tk.BOTTOM, pady=50)
    progress_bar.start(10)
    #schedule showing menu after 5 seconds which is 5000 ms

    root.after(5000, close_window)
    root.mainloop()
    
    create_gui()



























# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk

# root = Tk()
# root.title("Title")
# root.geometry('600x600')

# def resize_image(event):
#     new_width = event.width
#     new_height = event.height
#     image = copy_of_image.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(image)
#     label.config(image = photo)
#     label.image = photo #avoid garbage collection

# image = Image.open('Template/TE1.jpg')
# copy_of_image = image.copy()
# photo = ImageTk.PhotoImage(image)
# label = ttk.Label(root, image = photo)
# label.bind('<Configure>', resize_image)
# label.pack(fill=BOTH, expand = YES)

# root.mainloop()
