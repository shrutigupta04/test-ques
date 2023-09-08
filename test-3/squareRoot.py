def squareroot(x) :
    for i in range (1,x +1) :
        
        if i*i > x :         #if square of a number is greater than x
            return i-1       #one minus that number will be rounded off square root

x = int(input())      
print(squareroot(x))