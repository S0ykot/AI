from math import sqrt

def linearSearch(l,s):
	print("\n-------Linear Search---------\n");
	for x in range(0,len(a)):
		print("Checking:",a[x],"=",s)
		if a[x]==s:
			print("\nFound =>",s," in the index of ",x,"\n")




# def binarySearch(a,l,h,key):
# 	print("\n-------Binary Search---------\n");
# 	while l<=h:
# 		mid=int(l+(h-1)/2)
# 		print("mid value = ",mid)
# 		if a[mid]>key:	
# 			h=mid-1
# 			print("a[mid] in bigger then KEY [high]= ",h)
# 		elif a[mid]<key:
# 			l=mid+1
# 			print("a[mid] in smaller then KEY [low] = ",l)
# 		else:
# 			print("Found! Index number",mid)
# 			break


def jumpSearch(a,key):
	size = len(a)
	bsize = int(sqrt(size))
	start=0
	end=bsize
	while a[end]<=key and end<size:
		start=end
		end=end+bsize
		if end>s-1:
			end=size

	for i in range(size,end):
		if a[i]==key:
			return i



a = [1,4,7,8,5,2,3,6,9]

print(jumpSearch(a,2))