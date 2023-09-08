def stockMax(prices):
    maxprice=float('-inf')
    profit=0
    for i in range(len(prices)-1, -1, -1): #loop from the end
        if prices[i]>maxprice:             #update max price
            maxprice=prices[i]
        if maxprice>prices[i]:             #whenever price is less than max price on a later day
            profit=profit+maxprice-prices[i] #update profit, diff in maxprice and price on that day
    return profit

#driver code
n=int(input())
prices=[]
for i in range(0,n):
    ele=int(input())
    prices.append(ele)
print(stockMax(prices))            