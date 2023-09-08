def matchingStrings(stringList, queries):
    c=0
    count=[]
    for i in range(0, len(queries)):        #loop through query list
        for j in range(0, len(stringList)): #loop through string list
            if queries[i]==stringList[j]:
                c=c+1                       #update counter when you find a matching string
        count.append(c)
        c=0
    return count

#driver code
stringList=[]
queries=[]
n=int(input())
m=int(input())
for i in range (0,n) :  
    a = input()
    stringList.append(a) 
    
for i in range (0,m) :  
    b = input()
    queries.append(b)
    
print(matchingStrings(stringList, queries))           