def bubble(A):
    n = len(A)
    print("\n\n     Bubble Sort     ");
    print("---------------------");
    print("i","j","s","   Array")
    for i in range (1,n):
        for j in range (0,n-i):
            if A[j]>A[j+1]:
                print(i,j,A[j],A)
                print(i,j+1,A[j+1],A)

                A[j],A[j+1]=A[j+1],A[j]

            
    print("\nSorted :",A)
    print("---------------------");


def selection(a):
    n=len(a)
    print("\n\n     Selection Sort     ");
    print("------------------------------");
    for i in range(0,n-1):
        mi=i
        for j in range(i+1,n):
            #print("Minimum value: ",mi)
            print("i = ",i,"\nj=",j,"\nminimim=",mi)
            print("------------------------------");
            print("a[j] < a[mi] :",a[j],"<",a[mi]," [When j=",j, "& min = ",mi,"]")
            if a[j]<a[mi]:
                mi=j
                print("\nMinimum = ",mi," [Minimum=j]")
                print("------------------------------");
        if mi!=i:
            print("------------------------------");
            print ("Minimum=",mi,'\ni=',i)
            print("\n\t----------SWAP START---------");
            print("\t\tSWAP : a[mi]<=>a[i]")
            print("\t\tSWAP : ",a[mi],"<=>",a[i],"\n")
            print("\t\tNow the list is : ",a)
            a[mi],a[i]=a[i],a[mi]
            print("\t----------SWAP END---------\n");
    print("\nSelection sort: ",a)



# def insertion(a):
#     for i in range(2,len(a)):
#         key=a[i]
#         print("Key=",key)
#         j=i-1
#         print("\nj=",j)
#         print (j,'>0 and ',a[j],'>',key)
#         while j>0 and a[j]>key:
#             print(a[j+1] ,'=', a[j])
#             a[j+1] = a[j]
#             print(a[j+1] ,'=', a[j])
#             j=j-1

#         a[j+1]=key









def countSort(a,b,k):
   c=[0]*(k/2)
   for y in range (1,len(a)):
       c[a[y]]=c[a[y]]+1

       
   for x in range (1,k):
       c[x]=c[x]+c[x-1]

   for y in range (len(a),1):
       b[c[a[y]]]=a[y]
       c[a[y]]=c[a[y]]-1

   return b
   

def shellSort(a,n):
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            tmp=a[i]
            j=i
            while j>=gap and a[j-gap]>tmp:
                a[j]=a[j-gap]
                j=j-gap

            a[j]=tmp
        gap=gap//2


# a = [ 12, 34, 54, 2, 3] 
# shellSort(a,len(a))

# print(a)


def cocltailSort(a,n):
    swp=True
    start = 0
    end = n-1
    while swp==True:
        swp=False
        for i in range(start,end):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swp=True
        if swp==False:
            break

        swp=False
        end=end-1

        for i in range(end-1,start-1,-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swp=True


        start+=1


a = [5, 1, 4, 2, 8, 0, 2] 
cocltailSort(a,len(a)) 
print(a)