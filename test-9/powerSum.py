import math
import os
import random
import re
import sys

def powerSum(X, N):
    # Write your code here
    def helper(total, power, num):
        val=total-num**power
        if val==0:
            return 1
        if val<0:
            return 0
        return helper(val, power, num+1) + helper(total, power, num+1)
    ans=helper(X, N, 1)
    return ans

x=int(input())
n=int(input())
ans=powerSum(x, n)
print(ans)