def merge(ar1, ar2, m, n):
 
    # Iterate through all elements of ar2[] starting from the last element
    for i in range(n-1, -1, -1):
 
        # Find the smallest element greater than ar2[i]. 
        # Move all elements one position ahead till the smallest greater element is not found
        last = ar1[m-1]
        j = m-2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1
 
        # If there was a greater element
        if (last > ar2[i]):
 
            ar1[j+1] = ar2[i]
            ar2[i] = last


m=int(input("Length of first array: "))
n=int(input("Length of second array: "))

ar1=[]
ar2=[]
print("The first array is: ")
for i in range(0,m):
    ele = int(input())
    ar1.append(ele) 
print("The second array is: ")
for i in range(0,n):
    ele = int(input())
    ar2.append(ele) 
 
merge(ar1,ar2,m,n)
print("The first array becomes: ")
for i in ar1:
    print(i)
print("The second array becomes: ")
for i in ar2:
    print(i)

 