import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**8)


def componentsInGraph(gb, n):
    # Write your code here
    adj={}
    visited={}
    component=[]
    
    for i in range(1, 2*n+1):
        visited[i]=0
    for i in range(1, 2*n+1):
        adj[i]=[]
    for u, v in gb:
        adj[u].append(v)
        adj[v].append(u)
    def dfs(node, adj, component):
        component.append(node)
        visited[node]=1
        for i in adj[node]:
            if visited[i]==0:
                visited[i]=1
                dfs(i, adj, component)
        count=len(component)
        return count
        
    lst=[]
    for i in range(1, 2*n+1):
        if visited[i]==0:
            lst.append(dfs(i, adj, []))
    minm=0
    outlst=[]
    for i in lst:
        if i!=1:
            outlst.append(i)
            
    ans=[]
    ans.append(min(outlst))
    ans.append(max(outlst))
    return ans
     