from tkinter import *
from tkinter import messagebox
from PIL import Image

root = Tk()
root.title("Denomination Counter")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
#image = ImageTk.PhotoImage(upload)
#label = Label(root, image=upload, bg="lightblue")
#label.place(x=180, y=50)

label1 = Label(root,
               text="Hey there! Welcome to Denomination Counter",
               bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msgBox = messagebox.showinfo("Alert", "Do you want calculate the denomination count?")
    if msgBox == 'ok':
        topwin()

button1 = Button(root,
                 text="Let's get started", command=msg,
                 fg="brown", bg="white")

def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.geometry("600x350+50+50")
    top.configure(bg="light grey")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="light grey")
    l1 = Label(top, text="100", bg="light grey")
    l2 = Label(top, text="50", bg="light grey")
    l3 = Label(top, text="20", bg="light grey")
    l4 = Label(top, text="10", bg="light grey")
    l5 = Label(top, text="5", bg="light grey")
    l6 = Label(top, text="2", bg="light grey")
    l7 = Label(top, text="1", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)


    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note100 = amount // 100 
            amount %= 100 
            note50 = amount // 50 
            amount %= 50
            note20 = amount // 20 
            amount %= 20 
            note10 = amount // 10 
            amount %= 10 
            note5 = amount // 5
            amount %= 5
            note2 = amount // 2 
            amount %= 2
            note1 = amount // 1
    
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)
            t7.delete(0, END)
        
            t1.insert(0, str(note100))
            t2.insert(0, str(note50))
            t3.insert(0, str(note20))
            t4.insert(0, str(note10))
            t5.insert(0, str(note5))
            t6.insert(0, str(note2))
            t7.insert(0, str(note1))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer amount")
    btn = Button(top, text="Calculate", command=calculate, fg="brown", bg="white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=350, y=200)
    l6.place(x=350, y=230)
    l7.place(x=350, y=260)

    t1.place(x=250, y=200)
    t2.place(x=250, y=230)
    t3.place(x=250, y=260)
    t4.place(x=250, y=290)
    t5.place(x=420, y=200)
    t6.place(x=420, y=230)
    t7.place(x=420, y=260)

    top.mainloop()

button1.place(x=270, y=370)
root.mainloop()