# Intuition
# Initially, the approach was to brute force it, by having 2 for loops to get 2 pointers, but then time complexity would be O(n^2), there's another strategy to use 2 pointers, which is with a while loop and initializing left and right variable.

# We just have to use the highest height so far and update our highest area

# Approach
# Area is height * width, but water can only be contained in the one w lesser height,

# initialize the width(r-l) and height(min(height[l],height[r]))
# update the highest area by comparing it to the current area in the while loop

# Complexity
# Time complexity:
# O(n) because it's only 1 while loop and time depends on length of list, unlike the brute force method, which is n^2,

# Space complexity:
# no idea

highest_area = 0
l = 0
r = len(height)-1
while l < r:
    distance = r - l
    min_height = min(height[l],height[r])
    area = distance * min_height
    highest_area = max(highest_area, (area))

    if height[l] < height[r]:
        l +=1
    else:
        r -=1
return highest_area