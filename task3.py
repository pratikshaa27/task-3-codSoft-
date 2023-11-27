import random
import string
import tkinter as tk


def password_generator():
    length = int(leng.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_label.config(text="Your password is: " + password)
    
root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Enter the length of the password:")
label.pack()

leng = tk.Entry(root)
leng.pack()

generate_button = tk.Button(root, text="Generate Password", command=password_generator)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()

