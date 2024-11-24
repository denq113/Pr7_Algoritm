from tkinter import*

def Zanesty(event):
    listBox1.insert(END,entry1.get())

def Vynesty(event):
    entry1.insert(END,listBox1.get(listBox1.curselection()))

root = Tk()

f1 = Frame()
f2 = Frame()

entry1 = Entry(f1)
entry1.pack()

button1 = Button(f1,text="Занести")
button1.bind('<Button-1>', Zanesty)
button1.bind('<Return>', Zanesty)
button1.pack()

listBox1 = Listbox(f2)
listBox1.bind('<Double-Button-1>',Vynesty)
listBox1.pack()

f1.pack(side = RIGHT)
f2.pack(side = LEFT)

root.mainloop()
