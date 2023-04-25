# Intuition
# so how can i save some memory while iterating through the list to get my answer? zip the first half and the second half together, then i chain it and make it a list

# Approach
# Complexity
# Time complexity:
# O(n^2) i think? has to zip and then chain it after that,

Space complexity: 
return list(chain(*zip(nums[:n],nums[n:])))