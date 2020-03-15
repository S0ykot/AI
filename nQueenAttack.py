# def check(A,i,j,k,l):
# 	one =abs(k-i)
# 	two = abs(j-l) 
# 	if (one==two):
		


# N=[False]*4

# check(N,)

# print(N)

# def recQueen(Q,r):
# 	n = len(Q)
# 	if r==n:
# 		print(Q)
# 	else:
# 		for j in range(0,n):
# 			legal = True
# 			for i in range(0,r):
# 				if ((Q[i]==j) or (Q[i]==j+r-i) or (Q[i]==j-r+i)):
# 					legal=False
# 			if legal:
# 				Q[r]=j
# 				recQueen(Q,r+1)



# N=[0]*4



# recQueen(N,0)


def manual(Q):
	n = len(Q)
	for i in range(0,1):
		# print('Q[i+1]',Q[i+1])
		for x in range(1,n):
			j=0
			k=i+1
			l=x
			if (Q[i+1]==Q[i]) or (abs(j-l)==abs(k-i)):
				print('matched')
			else:
				Q[i+1]=x
				#print('Q[i+1]=>',Q[i+1])
			print(Q)	
	
				


N = [2,-1,-1,-1]


manual(N)