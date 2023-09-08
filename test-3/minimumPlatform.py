def minimumPlatform(n,arr,dep):
    # code here
    
    arr.sort()        #sort arrival and departure arrays
    dep.sort()
    i = 0
    j = 0
    count = 0
    l = []
    while i < n and j < n :
        
        if arr[i] <= dep[j] :    #when second train's arrival is before first train's departure, we need a diff platform
            count = count + 1
            l.append(count)      #append updated platform in a list
            i = i + 1   
            
        else :
            count = count - 1
            l.append(count)
            j = j + 1  
            
    
    m = max(l)                 #return the updated minimum number of platforms required
    return m

# driver code
arrival = []
departure = []
n = int(input())
for i in range (0,n) :  
    a = int(input())
    arrival.append(a)

for i in range (0,n) : 
    b = int(input())
    departure.append(b)

print(minimumPlatform(n,arrival,departure))
 