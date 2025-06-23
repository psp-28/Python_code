import tkinter as tk
import random

### list of texts:

texts = ["Credentials are already stored, if you have entered once, if you want to reset credentials then only click on Entering credentials, else not required",
         "Please check the timestamps and verify the report...", "Make sure your screen does not go to sleep, to avoid it use spoon on touchpad.", "In case of Public holiday you need to manually create a report, as days may increase and can lid to time mismatch",
         "Sharing this application to sources other than TOTAL START account is prohibited."]


r = tk.Tk()
r.geometry("700x300")
r.configure(bg="black")

#label
label1 = tk.Label(r, text="", font=("Arial", 12), fg="white", bg="black")
label1.pack(expand=True)


fade_steps = 50
fade_delay = 30
display_time = 7000

def fade_in(text, step= 0):
    intensity = int(255*(step/ fade_steps))
    color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
    label1.config(text=text, fg=color)
    
    if step < fade_steps:
        r.after(fade_delay, fade_in, text, step + 1)
    else:
        r.after(display_time, fade_out, text, fade_steps)
        
def fade_out(text, step):
    intensity = int(255*(step/ fade_steps))
    color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
    label1.config(fg=color)
    
    if step > 0:
        r.after(fade_delay, fade_out, text, step - 1)
    else:
        show_next_text()
        
def show_next_text():
    next_text = random.choice(texts)
    fade_in(next_text)

show_next_text()
r.mainloop()