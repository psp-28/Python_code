import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image
from tkinter import *
from tkinter.ttk import *
import pyautogui
from PIL import Image, ImageTk
from tkinter import ttk
import cv2
import os
import random
executed_script = set()




texts = ["Credentials are already stored, if you have entered once, if you want to reset credentials \nthen only click on Entering credentials, else not required",
         "Please check the timestamps and verify the report...", "Make sure your screen does not go to sleep, to avoid it use spoon on touchpad.", "In case of Public holiday you need to manually create a report, as days may increase and can lid to time mismatch",
         "Sharing this application to sources other than TOTAL START account is prohibited."]







# def delete_files():
#     files_to_delete = ["secret.key", "credentials.enc"]
#     for file in files_to_delete:
#         if os.path.exists(file):
#             os.remove(file)

#             print(f"{file} deleted.")
#         else:
#             print(f"{file} does not exist.")






def run_script(script_name):
    
    try:
        subprocess.run(["python", script_name], check=True)
        messagebox.showinfo("Successful", f"{script_name} executed successfully...!!!")
        
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"❌❌❌❌❌ Error running {script_name}: {e}")
        
def close_window():
    root.destroy()
    
def adjust_opacity(image_path, opacity):
    img = Image.open(image_path).convert("RGBA")
    
    a = img.split()[3]
    a = a.point(lambda p: int(p*opacity))
    img.put_a(a)
    return a

def create_gui():
    window = tk.Tk()
    window.title("Sanity Checklist Report")
    window.geometry("1600x1080")
    
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)
    
    
    
    def adjust_opacity(image_path, opacity):
        image_path = image_path.convert("RGBA")
        
        transparent_img = Image.new("RGBA", image_path.size, (255, 255, 255, 0))
        blend_img = Image.blend(transparent_img, image_path, opacity)
        return blend_img
        
    
    opacity = 0.9
    img_path = "Template/TE1.jpg"
    image = Image.open(img_path)
    resized_image = image.resize((1600, 1080))
    
    # resized_image.save("Template/temp_resized.png")
    adjust_img = adjust_opacity(resized_image, opacity)
    photo = ImageTk.PhotoImage(adjust_img)

    
    background_label = tk.Label(window, image=photo)
    background_label.image = photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 
    
    
    # relief "redge": must be flat, groove, raised, ridge, solid, or sunken
    box = tk.Frame(window, bg="white", bd=2, relief="sunken")
    box.place(relx=0.5, rely=0.5, anchor="center", width=600, height=700)
    
    label = tk.Label(window, text ="Select the Check you want to run")
    label.config(font=("Calibri", 16, "bold"))
    label.pack(pady=50)


    cred = tk.Button(box, text="Enter Login Credentials", width= 50, height=2 , command= lambda: [window.destroy(), run_and_restart("Cred_Store.py", "cred")])
    if "cred" in executed_script:
        cred.config(text= "Credentials Stored successfully!",bg="green", fg="white")
    cred.pack(pady=20)
    
    
    btn1 = tk.Button(box, text="SDWAN Check-Up", width= 50, height=2 , command= lambda: [window.destroy(), run_and_restart("SDWAN_Check.py", "btn1")])
    if "btn1" in executed_script:
        btn1.config(bg="green", fg="white")
    btn1.pack(pady=20)
    
    
    btn2 = tk.Button(box, text="Prisma Traffic in SDWAN Check-Up", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart("Prisma_Traffic.py", "btn2")])
    if "btn2" in executed_script:
        btn2.config(bg="green", fg="white")
    btn2.pack(pady=20)
    
    
    btn3 = tk.Button(box, text="Logstash Check", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart("Logstash.py", "btn3")])
    if "btn3" in executed_script:
        btn3.config(bg="green", fg="white")
    btn3.pack(pady=20)

    btn4 = tk.Button(box, text="Cybersec Check", width= 50, height=2, command= lambda: [window.destroy(), run_and_restart("Cybersec.py", "btn4")], state=DISABLED, bg="grey")
    if "btn4" in executed_script:
        btn4.config(bg="green", fg="white")
    btn4.pack(pady=20)

    
    # btn_close = tk.Button(window, text = "Quit",  width= 20, height=2, command =window.destroy,bg="red", fg="white")
    # btn_close.config(font=("Calibri", 11, "bold"))
    # btn_close.pack(padx= 50, pady=20)
    btn_close = tk.Button(box, text = "Quit",  width= 20, height=2, command =lambda: [window.destroy()],bg="red", fg="white")
    btn_close.config(font=("Calibri", 11, "bold"))
    btn_close.pack(padx= 50, pady=20)
    
    
    
    label1 = tk.Label(window, text="", font=("Arial", 12), fg="white", bg="black")
    label1.pack(expand=True, side= "bottom", padx=50, pady= 30, ipadx=50, ipady=30)
    label1.place(relx=0.5, rely=0.9, anchor="center")


    fade_steps = 50
    fade_delay = 30
    display_time = 7000

    def fade_in(text, step= 0):
        intensity = int(255*(step/ fade_steps))
        color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
        label1.config(text=text, fg=color)
        
        if step < fade_steps:
            window.after(fade_delay, fade_in, text, step + 1)
        else:
            window.after(display_time, fade_out, text, fade_steps)
            
    def fade_out(text, step):
        intensity = int(255*(step/ fade_steps))
        color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
        label1.config(fg=color)
        
        if step > 0:
            window.after(fade_delay, fade_out, text, step - 1)
        else:
            show_next_text()
            
    def show_next_text():
        next_text = random.choice(texts)
        fade_in(next_text)
        
    show_next_text()
        
    window.mainloop()


    
    
def run_and_restart(script_name, button_id):
    run_script(script_name)
    executed_script.add(button_id)
    create_gui()
    


def update_frame():
    ret, frame = cap.read()
    if ret:
        
        frame = cv2.resize(frame, (1040, 500))         
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        logo_label.imgtk = imgtk  # Keep a reference to avoid garbage collection
        logo_label.configure(image=imgtk)
        logo_label.update()
        root.after(delay, update_frame)
    else:
        cap.release()


### main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sanity Checklist Report")
    root.geometry("1080x800")       
    logo_label = tk.Label(root)
    logo_label.pack(pady=20)

    label = tk.Label(root, text="Sanity Checklist Report")
    label.config(font=("Calibri", 16, "bold"))
    label.pack(pady=50)

    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=500)
    progress_bar.pack(side=tk.BOTTOM, pady=20)
    progress_bar.start(10)
    
    
    root.after(7000, close_window)

# opencv
    cap = cv2.VideoCapture("Template/TE.gif")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    delay = int(1000 / fps) * 1
    root.after(0, update_frame)


    root.mainloop()
    create_gui()
    