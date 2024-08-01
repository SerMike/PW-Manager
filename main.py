from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
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
print(website_input.get())
website_input.grid(row=1, column=1, columnspan=2)

# Email/Username Label & Entry
email_un = Label(text="Email/Username:")
email_un.grid(row=2, column=0)

email_un_input = Entry(width=40)
print(email_un_input.get())
email_un_input.grid(row=2, column=1, columnspan=2)

# Password Label, Input, & Generate PW button
password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=23)
print(password_input.get())
password_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password")
pw_button.grid(row=3, column=2, sticky="nsew")

# Add button
add_button = Button(text="Add", width=30)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")


window.mainloop()
