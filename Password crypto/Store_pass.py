# pip install cryptography


from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox


def get_credentials():
    """Will get the login credentials (username and password)"""
    global root

    user = None
    passw = None

    root = tk.Tk()
    root.title("Login")
    root.geometry("950x640")
    root.configure(bg="#9FB6F5")

    overlay = tk.Frame(root, bg="#192938", bd=0)
    overlay.place(relx=0.5, rely=0.5, anchor="center")

    # Banner
    banner = tk.Label(overlay, text="Login to MyApps", font=("Arial", 16, "bold"),
                      fg="white", bg="#192938")
    banner.grid(row=0, column=0, columnspan=2, padx=10, pady=(30, 10))

    # Username Label
    username_label = tk.Label(overlay, text="Username:", font=("Arial", 14, "bold"),
                              fg="white", bg="#192938")
    username_label.grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(overlay, font=("Arial", 12), bd=0, relief="flat", fg="black", width=30)
    username_entry.grid(row=1, column=1, padx=10, pady=10)

    # Password Label
    password_label = tk.Label(overlay, text="Password:", font=("Arial", 14, "bold"),
                              fg="white", bg="#192938")
    password_label.grid(row=2, column=0, padx=10, pady=10)

    password_entry = tk.Entry(overlay, font=("Arial", 12), bd=0, relief="flat", fg="gray", width=30)
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    placeholder_text = "Enter your password"

    def add_placeholder(event=None):
        if not password_entry.get():
            password_entry.insert(0, placeholder_text)
            password_entry.config(fg="gray", show="")

    def remove_placeholder(event=None):
        if password_entry.get() == placeholder_text:
            password_entry.delete(0, tk.END)
            password_entry.config(fg="black", show="*")

    password_entry.bind("<FocusIn>", remove_placeholder)
    password_entry.bind("<FocusOut>", add_placeholder)
    add_placeholder()

    # Toggle password visibility
    def toggle_password():
        if password_entry.cget("show") == "*":
            password_entry.config(show="", fg="black")
            toggle_button.config(text="Hide Password")
        else:
            if password_entry.get() != placeholder_text:
                password_entry.config(show="*", fg="black")
            toggle_button.config(text="Show Password")

    toggle_button = tk.Button(overlay, text="Show Password", font=("Arial", 10),
                              command=toggle_password, bg="#0f2840", fg="white", bd=0)
    toggle_button.grid(row=3, column=1, pady=5)

    credentials_entered = False

    def submit():
        nonlocal user, passw, credentials_entered
        user = username_entry.get().strip()
        passw = password_entry.get()

        if not user:
            messagebox.showwarning("Input Error", "Please enter a username")
            return

        if passw == placeholder_text or not passw:
            messagebox.showwarning("Input Error", "Please enter a password")
            return

        credentials_entered = True
        root.quit()

    submit_button = tk.Button(root, text="Login", font=("Arial", 12),
                              bg="#4CAF50", fg="white", command=submit)
    submit_button.place(relx=0.5, rely=0.85, anchor="center")

    root.bind("<Return>", lambda event: submit())
    root.mainloop()
 
    if credentials_entered:
        print("✅ Credentials captured")
        return user, passw
    else:
        print("❌ No valid credentials entered or user canceled")
        return None, None
    
    
    
    
    
## Generate the key (do this only one time.)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    return open("secret.key","rb").read()

# store creads.
def store_creds(username, password):
    key = load_key()
    f = Fernet(key)
    credentials = f"{username} : {password}".encode()
    encrypted = f.encrypt(credentials)
    with open("credentials.enc","wb") as cred_file:
        cred_file.write(encrypted)
        
# main flow::::
if not os.path.exists("secret.key"):
    generate_key()
    
user, passw = get_credentials()

# username = user
# password = passw
store_creds(user, passw)
print("\n Credentials stored successfully..")
