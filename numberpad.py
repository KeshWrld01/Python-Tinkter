from tkinter import *

root = Tk()
root.title("Number Pad")
root.geometry('250x300')


frame = Frame(master=root, height=200, width=360, bg="lightgrey")
numbers = [[7, 8, 9],[4, 5, 6],[1, 2, 3],['#', 0, '*']]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = Frame(
            master = root,
            relief = SUNKEN,
            borderwidth = 1,
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Label(master = frame, text=numbers[i][j], bg="white")
        label.pack()
root.mainloop()
