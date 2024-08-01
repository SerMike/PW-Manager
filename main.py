from tkinter import *
from tkinter import messagebox
import random

# -------------------------------- PASSWORD GENERATOR ----------------------------------- #
def generate_password():
    """Generates a strong password by randomly generating alphanumeric and special characters into a single output"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for _ in range(nr_letters)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = pw_letters + pw_numbers + pw_symbols
    random.shuffle(password_list)

    # Join all character groups into one output and display it in 'Password' input field for user.
    strong_password = "".join(password_list)
    password_input.insert(0, strong_password)


# -------------------------------- SAVE PASSWORD ----------------------------------- #
def save():
    """Saves inputs from 'Website', 'Email/Username', and 'Password' fields
    into a data.txt file in a pipe delimited format. Clears contents from
    'Website' and 'Password' fields"""
    web = website_input.get()
    em_un = email_un_input.get()
    pw = password_input.get()

    # Checks to see if 'Website' or 'Password' input fields are empty
    if len(web) == 0 or pw == 0:
        messagebox.showwarning(title="Warning!", message="Please don't leave any fields blank!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \n"
                                                          f"Email: {em_un} \n"
                                                          f"Password: {pw} \n"
                                                          f"Is it ok to save?")
        # If fields are populated prompt the user to 'Save' contents or cancel.
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web} | {em_un} | {pw}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()


# ------------------------------------- UI SETUP ---------------------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label & Entry
website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email/Username Label & Entry
email_un = Label(text="Email/Username:")
email_un.grid(row=2, column=0)

email_un_input = Entry(width=40)
email_un_input.grid(row=2, column=1, columnspan=2)
email_un_input.insert(0, "your_email@email.com")

# Password Label, Input, & Generate PW button
password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=23)
password_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(row=3, column=2, sticky="nsew")

# Add button
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")


window.mainloop()
