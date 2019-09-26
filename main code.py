from tkinter import *
root = Tk()
root.geometry("300x400")
root.title("Login")
root.resizable(0,0)

def call1():
    L1.destroy()
    L2.destroy()
    L3.destroy()
    E1.destroy()
    E2.destroy()
    b1.destroy()
    b2.destroy()
    c.destroy()
    fl1 = Label(root, text="you are login", font=("Harlow Solid", 30))
    fl1.pack()

def call2():
    L1.destroy()
    L2.destroy()
    L3.destroy()
    E1.destroy()
    E2.destroy()
    b1.destroy()
    b2.destroy()
    c.destroy()
    text1 = Label(root, text="Signup", font=("Harlow Solid", 30))
    text1.pack()
    text2 = Label(root, text="Lastname")
    text2.pack(pady=10)

    E3 = Entry(root)
    E3.pack()
    text3 = Label(root, text="Lastname")
    text3.pack(pady=5)

    E4 = Entry(root)
    E4.pack()
    text4 = Label(root, text="Gmail")
    text4.pack(pady=5)

    E5 = Entry(root)
    E5.pack()
    text5 = Label(root, text="Password")
    text5.pack(pady=5)

    E6 = Entry(root,  justify=CENTER, show="*")
    E6.pack()

    


p1 = PhotoImage(file="b2.png")

L1 = Label(root, image=p1)
L1.pack(pady=15)

L2 = Label(root, text="Name", font=("Harlow Solid", 15))
L2.pack()

E1 = Entry(root, bg="#B527A0", fg="#FDFEFE", font=("Harlow Solid", 9), width=25, bd=2, justify=CENTER)
E1.pack()

L3 = Label(root, text="Password", font=("Harlow Solid", 15))
L3.pack()

E2 = Entry(root, bg="#B527A0", fg="#FDFEFE", font=("Harlow Solid", 9), width=25, bd=2, justify=CENTER, show="*")
E2.pack()

c = Checkbutton(root, text="Remember me")
c.pack()

p2 = PhotoImage(file="b6.png")
b1 = Button(root, image=p2, command=call1)
b1.pack()

p3 = PhotoImage(file="b1.png")

b2 = Button(root, image=p3, command=call2)
b2.pack()


















root.mainloop()