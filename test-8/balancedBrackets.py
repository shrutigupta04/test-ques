

import math
import os
import random
import re
import sys


def isBalanced(s):
    # Write your code here
    if len(s)==0 or len(s)==1:
        return 'NO'
    c=d=0
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if ch=='(' or ch=='{' or ch=='[':
            stack.append(ch)
            c=c+1
        elif len(stack)!=0:
            d=d+1
            if ch==')' and stack[-1]=='(':
                stack.pop()
            elif ch=='}' and stack[-1]=='{':
                stack.pop()
            elif ch==']' and stack[-1]=='[':
                stack.pop()
            else:
                return 'NO'
        
    if len(stack)==0 and c!=0 and d!=0 and c+d==len(s):
        return 'YES'
    else:
        return 'NO'
            
inp=input()
ans=isBalanced(inp)
print(ans)

