class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        summ=0         #initialize sum with 0
        maxii=-2**31-1    #initialize maximum sum with minimum integer value
        for i in range(N):
            summ+=arr[i]     #sum after adding every element in given array
            maxii=max(summ,maxii)    #maximum between maximum sum before adding arr[i] and new sum
            
            if(summ<0):   #when sum becomes less than 0
             summ=0       #we update sum to 0 when sum becomes less than 0
        
        
        
        return maxii       #we return the answer as calculated




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
    T = int(input())
    while T > 0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]  # Split the input line into individual integers
        ob = Solution()
        print(ob.maxSubArraySum(arr, n))
        T -= 1




if __name__ == "__main__":
    main()
# } Driver Code Ends