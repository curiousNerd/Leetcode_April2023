##
# The question asks to remove all duplicate elements from the sorted array in-place
# Since array do not allow size modification and this question does not allow using separate data structure -
# This should be achieved by the following
#   - Move all the unique elements to the left of the array
#   - Return the count of unique elements
#   - The remaining elements do not matter
from typing import List


# Example -
#   - Input : [0,0,1,1,1,2,2,3,3,4]
#   - Output : [0,1,2,3,4,_,_,_,_,_]
#       - Return value should be : 5

# Important Note :
#   - Input array is sorted
##


##
# Solution :
#   - We can use two pointers to track down all the unique elements
#       - left : points to the current index of the unique element
#       - right : points to the next unique element
#           - When above condition is met : Swap and increment pointers
#
#   - Since we are using tables we can map out different conditions and corresponding operations of the pointers
#       [L] __ [R] | Opr.
#           ==     | L+ , swap , R+
#           !=     | R+
# #

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## initializations
        left = 0
        right = 0
        n = len(nums)

        ## base condition
        if len(nums) == 0:
            return

        ## implementation
            # Iterate through the array and swap whenever next unique number is encountered

        while right < n:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1

    ## Time Complexity : O(n)
    ## Space Complexity : O(1)

class Solution:

    '''

    - Question :
        * Remove all the duplicates from the array
          and return the count of elements which are unique such that the array has all these unique elements till index count -1

    - Assumptions :
        * elements present beyond the index count do not matter

    - Solution :
        * Optimal Solution
            - Use two pointers left and right
                - left : track the first occurrence of a number
                - right : tracks the next unique number
            - conditions
                - [left] == [right] : right+1
                - [left] != [right] : left+1, swap, right+1
            - return
                - left + 1 : Because we need to return the count of unique elements in the array and not the index till which we have unique elements

        * Time Complexity : O(n)
        * Space Complexity : O(1)


    '''

    def removeDuplicates_again(self, nums: List[int])-> int:

        ## initialization
        left = 0
        right = 0
        n = len(nums)

        ## base condition
        if n == 0:
            return

        ## code
        while right < n:

            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1

