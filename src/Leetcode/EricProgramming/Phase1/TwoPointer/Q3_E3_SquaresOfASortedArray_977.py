##
# The question asks to return sorted square array from the given sorted input array
# Input: [-30,-20,0,10]
# Output: [0,100,400,900]
#
#
# Approach :
#   - Since the input array is sorted we should leverage it.
#   - Naive solution will be to square the input array and then sort it again
#       - but this would result in O(n log n) time complexity and O(n) or O(log n) space complexity
#   - Better Solution :
#       - Keep extra array to store the sorted squared results
#       - Use two pointers left and right
#           - left : points at the first element
#           - right : points at the last element
#       - We can compare the squared elements at these two pointers
#           - populate the output array from back with the larger square
#       - update pointers
# We can map out different conditions for two pointers
#   [L]^2 __ [R]^2  | Opr.
#          >        | Insert [L]^2 L+
#          <=       | Insert [R]^2 R+
##

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ## initialization

        left = 0
        n = len(nums)
        right = n - 1
        output = [0] * n
        p = n - 1

        ## base condition
        if n == 0:
            return

        ## implementation

        # compare squared elements at left and right pointers
        # insert larget one in output array from back
        # update pointers

        while left <= right:

            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                output[p] = left_sq
                left += 1

            else:
                output[p] = right_sq
                right -= 1

            p -= 1

        return output


class Solution:

    '''
        * Question :
            - Input array has both +ive and -ive numbers
            - Input array is sorted
            - return a sorted square array

        * Solution :
            - 2 pointers
                - left : points at the 1st element
                - right : points at the last element
            - We have to leverage the fact that input array is sorted
                - we know [left] is smaller than all the subsequent elements aka [right]
                - Hence :
                - if [left_sq] > [right_sq] :
                    - [left_sq] is bigger than all the elements square till right
                    - aka [left_sq] is the biggest and it should be present at the end of the output array
                - if [right_sq] > [left_sq]:
                    - [right_sq] is bigger than all the elements square till right

        * Catch
            - while condition should not be
                - while left < right => This will skip the last element
            - It should either be
                - while left <= right
                - while index >= 0

        * Time Complexity :  O(n)
        * Space Complexity : O(n)

    '''

class Solution:

    def squaresOfASortedArray(self, nums: List[int]) -> List[int]:

        ## initialization
        left = 0
        n = len(nums)
        right = n - 1
        output = [0] * n
        index = n - 1

        ## base condition
        if n == 0:
            return

        ## code
        while index >= 0:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                left += 1
                output[index] = left_sq
            else:
                right -= 1
                output[index] = right_sq

            index -= 1

        return output
