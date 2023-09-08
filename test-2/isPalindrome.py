#User function Template for python3
def isPalindrome(S):
		# code here
      
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(S)/2)):
        if S[i] != S[len(S)-i-1]:    #check for inequality from start and end of string
            return 0
        return 1

S=input()
print(isPalindrome(S))
