import math
import os
import random
import re
import sys


def twoStacks(maxSum, a, b):
    # Write your code here
    summ = 0
    st1 = 0
    st2 = 0
    arr = []
    for i in range(len(a)) :
        if (summ+a[i]) > maxSum :
            break
        summ = summ + a[i]
        st1 = st1 +1
    arr.append(st1)
    
    for i in range(len(b)) :
        summ = summ + b[i]
        st2 = st2 + 1
        while summ > maxSum and st1 > 0:
            summ = summ - a[st1-1]
            st1 = st1 - 1
        
        if summ <= maxSum :
            arr.append(st1+st2)
    
    
    return max(arr)

lst=[]
n=int(input("enter no. of elements in lis1 "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
lst1=[]
m=int(input("enter no. of elements in lis2 "))
for i in range(0, m):
    ele = int(input())
    lst1.append(ele)
maxs=int(input())
ans=twoStacks(maxs, lst, lst1)
print(ans)