# Intuition
# If i can sort the list, i'd be able to use the 2 pointer algorithm where i can move the right pointer down if my total is >0, and same thing the other way around(if total < 0, move left pointer>).
# 
# I thought I had to worry about checking the prefixes, but that's actually not an issue
# 
# Approach
# iterate a for loop with a while loop in each iteration to utilize the 2 pointer algorithm, by initializing the left, right pointers, the total, and the answer
# 
# Complexity
# Time complexity:
# O(n^2) i believe, since the time it takes to iterate through the for loop, and then complete while loop depends on length of list
# 
# Space complexity:
# If anyone can help me with this, I'm not too educated on space complexity thanks
nums = sorted(nums)
res = set()
for i in range(len(nums)):
  l = i+1
  r = len(nums)-1
  while l < r:
    total = nums[i] + nums[l] + nums[r]
    ans = (nums[i], nums[l], nums[r])
    if total == 0:
      res.add(ans)
    if total > 0:
       r -= 1
    else:
      l += 1
return res
