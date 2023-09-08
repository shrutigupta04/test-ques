def missingNumber(arr, n):
    sum = 0
    sum1 = 0
    for i in range(1, n+1):  #sum of first n integers
    
        sum=sum+i
    for i in range(0,n-1):   #sum of elements of array
        sum1=sum1+arr[i]
    return sum-sum1          #difference of sum for missing number
#driver code
n=int(input())
lst=[]
for i in range(0, n-1):
    ele=int(input())
    lst.append(ele)
print(missingNumber(lst, n))    
