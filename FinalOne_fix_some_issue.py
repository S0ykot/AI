import random

def fitness(crom):
	return ((crom[0]-crom[1])+(crom[2]-crom[3])+(crom[4]-crom[5])+(crom[6]-crom[7]))


def probablity(fit,total):
	return (fit/total)


def expectedC(p):
	return p*4


def AssocBin(stop,start=0.0):
	return start+stop

def rand():
	return round(random.uniform(0,1),2)

def crossOver(p1,p2):
	x=random.randint(0,7)
	# print("Parent1:",p1)
	# print("Parent2:",p2)
	p1[x],p2[x]=p2[x],p1[x]
	return [p1,p2]
	# print("After swap")
	# print("Parent1:",p1)
	# print("Parent2:",p2)




x1= [9,8,7,6,5,4,3,2]
x2= [6,5,9,8,3,2,5,4]
x3= [3,2,5,4,7,6,9,8]
x4= [2,1,6,5,7,6,5,4]


fit = [fitness(x1),fitness(x2),fitness(x3),fitness(x4)]
totalFitness = sum(fit)
avgFitness=(totalFitness/len(fit))



proba = [probablity(fit[0],totalFitness),probablity(fit[1],totalFitness),probablity(fit[2],totalFitness),probablity(fit[3],totalFitness)]
totalProb = sum(proba)
avgProb = totalProb/len(proba)


EC = [expectedC(proba[0]),expectedC(proba[1]),expectedC(proba[2]),expectedC(proba[3])]


x1B = AssocBin(0.25)
x2B = AssocBin(x1B,0.25)
x3B = AssocBin(x2B,0.25)
x4B = AssocBin(x3B,0.25)

ABin ={
	"x1" : [0.0,x1B],
	"x2" : [x1B,x2B],
	"x3" : [x2B,x3B],
	"x4" : [x3B,x4B]
}


 #print(ABin)

randNum = [rand(),rand(),rand(),rand()]

#print("R: ",randNum)


select = []

for x in range(4):
	if (0<randNum[x]<ABin['x1'][1]):
		select.append(x1)
	if (ABin['x2'][0]<randNum[x]<ABin['x2'][1]):
		select.append(x2)
	if (ABin['x3'][0]<randNum[x]<ABin['x3'][1]):
		select.append(x3)
	if (ABin['x4'][0]<randNum[x]<ABin['x4'][1]):
		select.append(x4)


parent = []

print("Selected : => ",select,"\n Length=>",len(select))

if (len(select)<4):
	print("Run the program again")
else:
	if (select[0]==select[1] or select[0]==select[2] or select[0]==select[3]):
		parent.extend(select[0])
	else:
		if ((select[1]==select[0] or select[1]==select[2] or select[1]==select[3])):
			parent.extend(select[1])
		else:
			if (select[2]==select[0] or select[2]==select[1] or select[2]==select[3]):
				parent.extend(select[2])
			else:
				if (select[3]==select[0] or select[3]==select[1] or select[3]==select[2]):
					parent.extend(select[3])


select.remove(parent)
select.remove(parent)

##print(select)
##print(parent)
#AfterCrossOver
afterCross = []

afterCross.append(crossOver(select[0],parent))
afterCross.append(crossOver(select[1],parent))



#print("After Cross",afterCross)



newFit = [fitness(afterCross[0][0]),fitness(afterCross[0][1]),fitness(afterCross[1][0]),fitness(afterCross[1][1])]
newTotalFitness = sum(newFit)

newAvgFitness = newTotalFitness/len(newFit)


print("Previous Average fitness:" ,avgFitness)
print("New Average fitness: " ,newTotalFitness)

if (newAvgFitness>round(avgFitness),0):
	print("Fitness improved")
else:
	print("Fitness not improved. Do another iteration. Thank you.")



#newProba = [probablity(newFit[0],newTotalFitness),probablity(newFit[1],newTotalFitness),probablity(newFit[2],newTotalFitness),probablity(newFit[3],newTotalFitness)]
#print(afterCross[0][0],afterCross[0][1],afterCross[1][0],afterCross[1][1],afterCross[2][0],afterCross[2][1],afterCross[3][0],afterCross[3][1])





