import math
import os
import random
import re
import sys


def summ(s, sum2):
    while s!=0:
        rem=s%10
        sum2+=rem
        s=s//10
    if sum2//10==0:
        return sum2
    else:
        s=sum2
        sum2=0
    return summ(s, sum2)

def superDigit(n, k):
    # Write your code here
    s=0
    num=int(n)
    while num!=0:
        s=s+(num%10)
        num=num//10
    sum2=0
    s=s*k
    sum1=summ(s, sum2)
    return sum1

n=input()
k=int(input())
ans=superDigit(n, k)
print(ans)