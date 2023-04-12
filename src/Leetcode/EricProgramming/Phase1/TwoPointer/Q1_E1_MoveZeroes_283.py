from typing import List


class Solution:

    ##
    # This is an easy question but still a tricky one.
    #   - First Solution that comes to  mind
    #       - Keep two pointers left and right
    #           - left - keeps track of current zero element
    #           - right - keeps track of non-zero element
    #       - Swap whenever above condition is achieved
    # #
    def moveZeroes_firstSolutionInMind(self, nums: List[int]) -> None: ## this fails

        ## input :  [0,0,2,5,0,6,3,6,0,0,1]
        ## output : [2,5,6,3,6,1,0,0,0,0,0]

        left = 0
        right = 0
        n = len(nums)

        while (right < n):

            ## right should point to next non-zero element so
            if (nums[right] == 0):
                right += 1
            ## as soon as right points to non-zero element
            else:
                ## point left element to the zero element
                if(nums[left] != 0):
                    left += 1
                else:
                    ## Now left element is zero : so swap
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
                    right += 1

    ##
    #   The issue with this solution is -
    #       - We are not keeping check on how left is incrementing -
    #           - Once the pointer is inside else condition
    #               - that is as soon as right is pointing to non-zero element
    #               - left pointer is left unchecked
    #               - Resulting in list index out of range
    #       Example -
    #           input = [1,0,1]
    #           Iteration 1
    #               - right will be at 0 : non-zero element
    #                   - left at 1
    #                   - [1,0,1]
    #                   - [R,L]
    #                   - #swap : [0,1,1]
    #                   - left = 2, right = 1
    #           Iteration 2
    #               - right is at non-zero element : It will go in else block directly
    #                   - It keeps on incrementing left in hopes to find next 0 element
    #                       - Thus giving index-out-of-bounds error
    #   The key thing to note is :
    #       - Issue 1 : left should always be behind right
    #       - Issue 2 : left can't be left unchecked
    #
    # #