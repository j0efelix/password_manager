from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Cannot save blank info")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save the information\n Email: {email} \n Password: {password}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"Website: {website} | Email/Username: {email}"
                           f" | Password: {password} |\n")

    website_input.delete(0, END)
    password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_image)
logo.grid(column=1, row=0)


website_name = Label(text="Website:")
website_name.grid(column=0, row=1)
email_or_username = Label(text="Email/Username:")
email_or_username.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "joefelix.a2003@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_generator = Button(text="Generate Password", command=generate_password)
password_generator.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()