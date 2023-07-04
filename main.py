from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    char_password="".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, char_password)
    pyperclip.copy(password_input.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Warning", message="Some fields are empty...")
    else:

        ok_cancel = messagebox.askokcancel(title=website_input.get(), message=f"Email: {email_input.get()}\n"
                                                                              f"Password: {password_input.get()}\n"
                                                                              f"Is this right?")
        if ok_cancel:
            f = open("passwords.txt", "a")
            f.write(f"Website: {website_input.get()}\n"
                    f"Email/Username: {email_input.get()}\n"
                    f"Password: {password_input.get()}\n"
                    f"-----------------------------------\n")
            f.close()
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# logo image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

# website, email and passsword labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# etries
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(row=2,column=1 , columnspan=2)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", width=15, padx=-20, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(window, text="Add", width=44, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
