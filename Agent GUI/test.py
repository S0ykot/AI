from tkinter import *
import random
import time



status1={'loc_A':random.choice([True,False]),
        'loc_B':random.choice([True,False]),
        'loc_C':random.choice([True,False]),
        'loc_D':random.choice([True,False])
        }




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




print('Before=>',status1)

if ( not status1['loc_A']):
	img1 = PhotoImage(file="d.png")
	photoimage1 = img1.subsample(4,4) 
	lblr1=Label(A_frame,image=photoimage1).pack(side=LEFT)

if (not status1['loc_B']):
	img1 = PhotoImage(file="d.png")
	photoimage2 = img1.subsample(4,4) 
	lblr2=Label(B_frame,image=photoimage2).pack(side=LEFT)

if (not status1['loc_C']):
	img1 = PhotoImage(file="d.png")
	photoimage3 = img1.subsample(4,4) 
	lblr3=Label(C_frame,image=photoimage3).pack(side=LEFT)

if (not status1['loc_D']):
	img1 = PhotoImage(file="d.png")
	photoimage4 = img1.subsample(4,4) 
	lblr4=Label(D_frame,image=photoimage4).pack(side=LEFT)


env = [A_frame,B_frame,C_frame,D_frame]
img = PhotoImage(file="r.gif")
photoimage = img.subsample(2,2) 
lbld=Label(random.choice(env),image=photoimage).pack(side=RIGHT)


if (status1['loc_A'] and status1['loc_B'] and status1['loc_C'] and status1['loc_D']):
		print('All clean')


print('After =>',status1)
root.mainloop()