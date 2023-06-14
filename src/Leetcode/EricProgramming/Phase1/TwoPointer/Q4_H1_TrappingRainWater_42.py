##
# The question gives a non-negative array heights and asks to find the units of water that can be trapped
#   - Water can only be trapped if there are edges present
#   - If there is no edge - amount of water trapped will be zero.
#   Example :
#       - Input : [0,1,0,2,1,0,1,3,2,1,2,1]
#       - Output : 6 (Draw diagram and check)
##

## First Approach in mind :
#   - Calculate water trapped between two walls
#   - It means that there will be two pointers needed to point at these two walls
#       - left and right
#   - Now the task becomes to find water trapped between these two distant walls.
#       - This becomes complicated very quickly - because now you realize that
#           - Within all such walls you need to find water trapped at each location
#           - Once found - sum all these values
#   - But if it comes down to calculating water at each index only - then why not start with this only??
##

##
# Cleaner, better and less complicated Approach
# Core idea : find water trapped at each instant
#      Brute Force
#       -  If for each location we can find :
#           - Maximum left height
#           - Maximum right height
#           - Find water stored at this particular location :
#               - min(left height, right height) minus height at current location
#       -  This will calculate water at each location
##

from typing import List

class Solution:
    def trap_bruteForce(self, heights: List[int]) -> int:

        n = len(heights)
        # For each position find the max height on the left
        left_max = [0] * n
        for i in range(len(heights)):
            left_max[i] = heights[i] if i == 0 else max(heights[i], left_max[i-1])

        right_max = [0] * n
        for i in range(n-1 ,-1, -1):
            right_max[i] = heights[i] if i == n-1 else max(heights[i], right_max[i+1])

        sum = 0
        for i in range(len(heights)):
            sum += min(left_max[i], right_max[i]) - heights[i]

        return sum

    ## Time Complexity : O(n^2)
    ## Space Complexity

