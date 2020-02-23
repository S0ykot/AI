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

print("R: ",randNum)


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


print("Selected : => ",select)









