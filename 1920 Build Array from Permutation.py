# Intuition
# get the ith element for that position and either add to new list for answer or change it in another list ie. [0,0,0,0]

# Approach
# do a for loop to get all the values

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(n) but should be O(1) for the other way
    
l=[]
for i in range(len(nums)):
    l.append(nums[nums[i]])
return l