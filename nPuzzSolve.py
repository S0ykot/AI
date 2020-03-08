
def inversion(A):
	c =0;
	for x in range(0,len(A)-1):
		for y in range(x+1,len(A)):
			if (A[x]==1000):
				continue
			elif(A[x]>A[y]):
				c = c+1
	return c



def isEven(value):
	if (value%2==0):
		return True
	else:
		return False


def findBlank(A):
	for i in range(len(A)):
		if (1000 in A[i]):
			return i+1

def solveAble(A,P):
	inv = inversion(P)
	dim = len(A)
	position = len(A)-findBlank(A)+1

	if (isEven(dim)==False and isEven(inv)==True):
		print("1)Puzzle Can be solve")
	elif(isEven(dim) and isEven(position)==False and isEven(inv)):
		print("2)Puzzle Can be solve")
	elif(isEven(dim) and isEven(position) and isEven(inv)==False):
		print("3)Puzzle Can be solve")
	else:
		print("Sorry to say. I can't solve it")




# r = int(input("Enter the row number: "))
# c = int(input("Enter the cloumn number: "))
# B=[[6,1,10,2],[7,11,4,14],[5,1000,9,15],[8,12,13,3]]
# P=[6,1,10,2,7,11,4,14,5,1000,9,15,8,12,13,3]
C = [[7,1,2],[5,1000,4],[8,3,6]]
P = [7,1,2,5,1000,4,8,3,6]


# inv = inversion(P)
# dimention = len(B)
# print('\n',B[0],'\n',B[1],'\n',B[2],'\n',B[3])
# point = len(B)-findBlank(B)+1

# print("inversion =>",inv)
# print("dimention= >",dimention,'*',len(B[0]))
# print("Blank point ==> ",point)


solveAble(C,P)

# l=[]
# marge = []
# for x in range(0,r):
# 	l=[]
# 	for y in range(0,c):
# 		print(x,y)
# 		l.append(int(input("Enter value:")))
# 	P.append(l)


# for x in range(0,r):
# 	for y in range(0,c):
# 		marge.append(P[x][y])


# print(P)

# print(isEven(inv))


	