from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as file:
        web = website_input.get()
        em_un = email_un_input.get()
        pw = password_input.get()
        file.write(f"{web} | {em_un} | {pw}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)


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
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# Email/Username Label & Entry
email_un = Label(text="Email/Username:")
email_un.grid(row=2, column=0)

email_un_input = Entry(width=40)
email_un_input.grid(row=2, column=1, columnspan=2)
email_un_input.insert(0, "youremail@email.com")

# Password Label, Input, & Generate PW button
password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=23)
password_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password")
pw_button.grid(row=3, column=2, sticky="nsew")

# Add button
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")


window.mainloop()
