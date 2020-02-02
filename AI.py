##def control(s):
##    if s=='Adnan':
##        print('Legend')
##    else:
##        print("NULL")
##
##s = input("Enter Sting: ")
##r = s [::-1]
##print("Revers Name: "+r)
##
##if s=='zidan':
##    print("pagol pagol")
##else:
##    print("I'm not robot")
##
##
##control(s)



##def countSort(a,b,k):
##    c=[0]*(k/2)
##    for y in range (1,len(a)):
##        c[a[y]]=c[a[y]]+1
##
##        
##    for x in range (1,k):
##        c[x]=c[x]+c[x-1]
##
##    for y in range (len(a),1):
##        b[c[a[y]]]=a[y]
##        c[a[y]]=c[a[y]]-1
##
##    return b
##    
##
##a = [2,5,4,1,7,8]
##b =[0]*len(a)
##countSort(a,b,6)
##
##print(b)




##def bubble(A):
##    n = len(A)
##    swapped = True
##    while(swapped):
##        swapped= False
##        for i in range(1,n):
##            if A[i-1]>A[i]:
##                A[i],A[i-1]=A[i-1],A[i]
##                swapped=True
##            
##    return A
##
##
##a = [59,5,1,42,25,14,0,2]
##
##B = bubble(a)
##
##print(B)

def bubble(A):
    n = len(A)
    print("i","j","s","Array")
    for i in range (1,n):
        for j in range (0,n-i):
            if A[j]>A[j+1]:
                print(i,j,A[j],A)
                print(i,j+1,A[j+1],A)

                A[j],A[j+1]=A[j+1],A[j]

            
    print(A)


a = [9,1,5,8]

bubble(a)






        









    
