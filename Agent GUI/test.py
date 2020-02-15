from tkinter import *
import random 


root = Tk() 
root.title("Agent")
root.config(bg="black")


A_frame = Frame(root, width=300, height=300)
A_frame.grid(row=0, column=0, padx=10, pady=5)
A_frame.pack_propagate(False) 
lblA= Label(A_frame,text="A",font=("Helvetica", 9)).pack()



B_frame = Frame(root, width=300, height=300)
B_frame.grid(row=0, column=1, padx=10, pady=5)
B_frame.pack_propagate(False) 
lblB= Label(B_frame,text="B",font=("Helvetica", 9)).pack()




C_frame = Frame(root, width=300, height=300)
C_frame.grid(row=1, column=0, padx=10, pady=5)
C_frame.pack_propagate(False) 
lblC= Label(C_frame,text="C",font=("Helvetica", 9)).pack()



D_frame = Frame(root, width=300, height=300)
D_frame.grid(row=1, column=1, padx=10, pady=5)
D_frame.pack_propagate(False) 
lblD= Label(D_frame,text="D",font=("Helvetica", 9)).pack()


env = [A_frame,B_frame,C_frame,D_frame]

img1 = PhotoImage(file="d.png")
photoimage1 = img1.subsample(3,3) 
lblr=Label(random.choice(env),image=photoimage1).pack(side=LEFT)

img = PhotoImage(file="r.gif")
photoimage = img.subsample(2,2) 
lbld=Label(random.choice(env),image=photoimage).pack(side=RIGHT)



root.mainloop()