from tkinter import *

window  = Tk()
window.title("Login App")
window.geometry('400x400')

frame = Frame(master=window, height=200, width=360, bg="lightblue")

username = Label(frame, text="Full Name:", bg="lightblue", fg="white", width=12)
email = Label(frame, text="Email:", bg="lightblue", fg="white", width=12)
password = Label(frame, text="Password:", bg="lightblue", fg="white", width=12)

username_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def show():
    name = username_entry.get()
    greet = "Hey "+ name
    message = "\nCongratulations, you are a codingal new student!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
textbox = Text(bg="grey", fg="black")

btn = Button(text="Create account", command=show, bg="green")

frame.place(x=20, y=0)
username.place(x=20, y=20)
username_entry.place(x=150, y=20)
email.place(x=20, y=80)
email_entry.place(x=150, y=80)
password.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=150, y=210)
textbox.place(y=250)

window.mainloop()