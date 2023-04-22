# Approach
# got stuck, so looked at others' answers and the neetcode guys' answer, and took the O(n) approach, where I had 2 lists:
# -1st one kept track of highest height on left side of current iteration
# -2nd one kep track of the right side
# after finding that, i implemented min(highest left side, highest right side) - current height to see how much water it can contain,

# note: a negative or zero value means the current height is too high to hold water compared to left and right heights

# but then i discovered that this solution takes too long for long lists

# then the last approach is neetcode guys' solution, where he showed an algorithm that kept track of the current max for left side and can calculate how much water it can hold at current iteration
# if the left side is smaller than the next side, then the leftmax would become that new next side, and become the new left side of container, 2. then when the next side becomes smaller than the left side, we can get how much water is trapped. Do the same for right side.

# Algorithm:
# Obtain the max height compared between the current height and last height.
# Use the max height and subtract it from the current height.

# This algorithm will accomplish the following:
# Returns 0 if the left side is smaller than or same as current side.
# Returns 1 if left side is taller(which is what we want to add to our answer)

# Oh sheesh, is this how topography maps work?
# index for left and right side
l= 0
r = len(height)-1
#the current maximum height for the left and right side
leftmax = height[l]
rightmax = height[r]
#the answer
res = 0
while l < r:
#move up the smaller side, because that side could be zero, and we can't find a container with a side of zero
#if move up left pointer, give leftMax a new value by comparing the current height w last leftMax height
#after finding max height, subtract it from current height to see how much water it can hold
if leftmax < rightmax:
    l +=1
    leftmax = max(leftmax, height[l])
    res += leftmax - height[l]
else:
    r -= 1
    rightmax = max(rightmax, height[r])
    res += rightmax - height[r]
return res
