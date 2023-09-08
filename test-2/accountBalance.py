def atm(X,Y):
    if(X%5==0 and Y>=X+0.50):         #X=Cash withdrawn Y=Account Balance
        Y=Y-X-0.5

    return(Y)

a=int(input("Amount Of Cash To Be Withdrawn: "))
b=float(input("Pooja's initial account balance: "))
print("Current balance is: ",atm(a,b))