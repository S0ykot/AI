

def linearSearch(l,s):
	print("\n-------Linear Search---------\n");
	for x in range(0,len(a)):
		print("Checking:",a[x],"=",s)
		if a[x]==s:
			print("\nFound =>",s," in the index of ",x,"\n")




def binarySearch(a,l,h,key):
	print("\n-------Binary Search---------\n");
	a.sort()
	while l<=h:
		mid=int((l+h)/2)
		if a[mid]==key:
			print("mid value = ",mid)
			print('found')
			break
		elif a[mid]>key:	
			h=mid-1
			print("a[mid] in bigger then KEY [high]= ",h)
		else:
			l=mid+1
			print("a[mid] in smaller then KEY [low] = ",l)





# ar = [1,4,7,8,5,2,3,6,9]

# binarySearch(ar,0,len(ar),5)


def jumpSearch(a,n,x):
	a.sort();
	step = n**0.5
	prev = 0

	while a[int(min(step,n)-1)]<x:
		prev=step
		step=step+n**0.5
		if prev>=n:
			print("Noting found")

	while a[int(prev)]<x:
		prev+=1
		if prev==min(step,n):
			print("Not found")

	if a[int(prev)]==x:
		print("Found at ",int(prev))



a = [1,4,7,8,5,2,3,6,9]
jumpSearch(a,len(a),6)


