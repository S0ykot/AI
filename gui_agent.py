from tkinter import *
m = Tk() 
m.title("Hello")



lblA=Label(m,text="A",font=("Arial",100),bg="red")
lblA.pack()
lblA.place(x=200,y=200)
lblA.grid(column=0,row=0)

lblB=Label(m,text="B",font=("Arial",100),bg="green")
lblB.pack()

lblB.grid(column=0,row=1)

lblC=Label(m,text="C",font=("Arial",100),bg="blue")
lblC.grid(column=1,row=0)


lblD=Label(m,text="D",font=("Arial",100),bg="yellow")
lblD.grid(column=1,row=1)


m.geometry('500x500')
m.mainloop()