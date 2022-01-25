from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    my_random_password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, my_random_password)
    pyperclip.copy(pass_input.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updating data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            # email_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- SEARCH SETUP ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="", message=f"{website}", detail=f"\nEmail: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)

web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "patalin.py@example.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_random_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
