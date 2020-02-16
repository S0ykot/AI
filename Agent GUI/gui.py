from tkinter import *
import random
import time

root = Tk() 
root.title("Agent")
root.config(bg="black")




class Agent:
    def __init__(self):
        def program(percept):abstract
        self.program=program
        
class vaccumEnvironment:

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean','Dirty'])
                      }
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right' and agent.location==loc_A: agent.location=loc_B
        elif action=='Right' and agent.location==loc_C: agent.location=loc_D
        elif action=='Left' and agent.location==loc_B: agent.location=loc_A
        elif action=='Left' and agent.location==loc_D: agent.location=loc_C
        elif action=='Up' and agent.location == loc_C: agent.location=loc_A
        elif action=='Up' and agent.location == loc_D: agent.location=loc_B
        elif action=='Down' and agent.location==loc_A: agent.location=loc_C
        elif action=='Down' and agent.location==loc_B: agent.location=loc_D
        elif action=='Suck':
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'


loc_A,loc_B,loc_C,loc_D='A','B','C','D'

class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        model={loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):

            location=percept[0]
            status=percept[1]
            
            print("location=>",location)
            print("status=>",status)
            model[location]=status
            if model[loc_A] == model[loc_B] == model[loc_C] == model[loc_D] == 'Clean': return -1
            elif status == 'Dirty': 
              action= 'Suck'
            elif location == loc_A: action= random.choice(['Right','Down'])
            elif location == loc_B: action= random.choice(['Left','Down'])
            elif location == loc_C: action= random.choice(['Right','Up'])
            elif location == loc_D: action= random.choice(['Left','Up'])

            percept=(location,status)

            #print('Agent perceives %s and does %s'%(percept,action))

            return action                    
            
        self.program=program



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


ve = vaccumEnvironment();

if (ve.status['A']=='Dirty'):
  img1 = PhotoImage(file="d.png")
  photoimage1 = img1.subsample(4,4) 
  lblr1=Label(A_frame,image=photoimage1).pack(side=LEFT)

if (ve.status['B']=='Dirty'):
  img2 = PhotoImage(file="d.png")
  photoimage2 = img2.subsample(4,4) 
  lblr2=Label(B_frame,image=photoimage2).pack(side=LEFT)

if (ve.status['C']=='Dirty'):
  img3 = PhotoImage(file="d.png")
  photoimage3 = img3.subsample(4,4) 
  lblr3=Label(C_frame,image=photoimage3).pack(side=LEFT)

if (ve.status['D']=='Dirty'):
  img4 = PhotoImage(file="d.png")
  photoimage4 = img4.subsample(4,4) 
  lblr4=Label(D_frame,image=photoimage4).pack(side=LEFT)




print("Before=>",ve.status)
env = [A_frame,B_frame,C_frame,D_frame]
img = PhotoImage(file="r.gif")
photoimage = img.subsample(2,2) 
lbld=Label(random.choice(env),image=photoimage).pack(side=RIGHT)



Magent=modelBasedVaccumAgent()
ve.add_object(Magent)
for steps in range(15):
    action=Magent.program(ve.percept(Magent))
    ve.execute_action(Magent,action)
    
    time.sleep(2)
    root.update()
    if ((ve.status['A']=='Clean') and (ve.status['B']=='Clean') and (ve.status['C']=='Clean') and (ve.status['D']=='Clean')):
      img = PhotoImage(file="r.gif")
      photoimage = img.subsample(2,2) 
      lbld=Label(root,text="All clean").grid(row=2, column=2)

    if (ve.status['A']=='Clean'):
      img1 = PhotoImage(file="")
      photoimage1 = img1.subsample(4,4) 
      lblr1=Label(A_frame,image=photoimage1).pack(side=LEFT)
    else:
      img = PhotoImage(file="r.gif")
      photoimage = img.subsample(3,3) 
      lbld=Label(A_frame,image=photoimage).pack(side=RIGHT)

    if (ve.status['B']=='Clean'):
      img2 = PhotoImage(file="")
      photoimage2 = img2.subsample(4,4) 
      lblr2=Label(B_frame,image=photoimage2).pack(side=LEFT)
    else:
      img = PhotoImage(file="r.gif")
      photoimage = img.subsample(3,3) 
      lbld=Label(B_frame,image=photoimage).pack(side=RIGHT)

    if (ve.status['C']=='Clean'):
      img3 = PhotoImage(file="")
      photoimage3 = img3.subsample(4,4) 
      lblr3=Label(C_frame,image=photoimage3).pack(side=LEFT)
    else:
      img = PhotoImage(file="r.gif")
      photoimage = img.subsample(3,3) 
      lbld=Label(C_frame,image=photoimage).pack(side=RIGHT)

    if (ve.status['D']=='Clean'):
      img4 = PhotoImage(file="")
      photoimage4 = img4.subsample(4,4) 
      lblr4=Label(D_frame,image=photoimage4).pack(side=LEFT)
    else:
      img = PhotoImage(file="r.gif")
      photoimage = img.subsample(3,3) 
      lbld=Label(D_frame,image=photoimage).pack(side=RIGHT)




root.mainloop()


