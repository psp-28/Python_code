import tkinter as tk
import keyboard
import threading
import ctypes
from playsound import playsound


def unblock_keyboard():
    for i in range(150):
        keyboard.unblock_key(i)


def block_keyboard():
    for i in range(150):
        keyboard.block_key(i)
        


def check_ctrl_a():
    while True:
        if keyboard.is_pressed('ctrl+a'):
            unblock_keyboard()
            unblock_mouse()
            break

block_keyboard()

threading.Thread(target=check_ctrl_a, daemon=True).start()
threading.Thread(target=lambda: playsound('til.mp3')).start()


# threading.Timer(30, unblock_keyboard).start()

def move_message():
    global i, size, color_index
    row = [''] * 10
    row[i] = f'❌❌ You have been Hacked !!!! ❌❌ \n 💀💀💀💀💀💀💀💀💀💀💀💀💀💀'
    label.config(text=''.join(row), font=('Helvetica', size), fg=colors[color_index])
    i = (i + 1) % 10
    size = 24 + (i % 5) * 2 #want to change size dynamically
    color_index = (color_index + 1) % len(colors)  # want to change color dynamically
    root.after(100, move_message)
    
    
def block_mouse():
    ctypes.windll.user32.BlockInput(True)

def unblock_mouse():
    ctypes.windll.user32.BlockInput(False)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')
colors = ['red', 'green', 'blue', 'yellow', 'purple']
size = 24
color_index = 0

label = tk.Label(root, text='', font=('Helvetica', 24), fg='red', bg='black')
label.pack(expand=True)

i = 0
move_message()

block_mouse()

root.mainloop()

unblock_mouse()