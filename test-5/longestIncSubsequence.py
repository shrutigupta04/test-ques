def longIncSubsequ(nums):
    piles = []  # Each pile represents a subsequence
    
    # Iterate through the input numbers
    for num in nums:
        # Binary search to find the pile where the current number can be placed
        left, right = 0, len(piles) - 1
        while left <= right:
            mid = (left + right) // 2
            if piles[mid][-1] < num:
                left = mid + 1
            else:
                right = mid - 1
            
        # If the number can't fit in any existing pile, create a new pile
        if left == len(piles):
            piles.append([num])
        else:
            # Otherwise, add the number to the appropriate pile
            piles[left].append(num)
    
    # The length of the final piles list represents the length of the longest increasing subsequence
    for i in range(len(piles)):
        print(piles[i])
    return len(piles)

n=int(input("Number of elements: "))
nums=[]
for i in range(0, n):
    ele = int(input())
    nums.append(ele) 

print("Length of the longest increasing subsequence is: ")
print(longIncSubsequ(nums))