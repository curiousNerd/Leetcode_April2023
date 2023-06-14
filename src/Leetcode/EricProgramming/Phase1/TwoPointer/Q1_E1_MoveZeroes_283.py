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

    ### New solution

    ##
    # The idea for this solution remains the same.
    #   - Use two pointers approach
    #       - left : points to first 0 element
    #       - right : points to next non-zero element
    #   - When above condition is met :
    #       - #swap
    #       - increment pointers
    # Caution :
    #   - Left and Right pointers should be in sync
    #       - left should always be smaller than right
    #
    # Approach :
    # Based on this we can create a rough table on how the pointers should be updated
    #       [L] [R] -> Opr.
    #        0  !0  -> Swap , L+ R+
    #        0   0  -> R+
    #       !0   0  -> L+ R+
    #       !0  !0  -> L+ R+
    # this shows :
    #   - Right is always incremented irrespective of the condition
    #   - We only need to manage left
    # #

    def moveZeroes_workingSoln(self, nums: List[int]) -> None:

        left = 0
        right = 0
        n = len(nums)

        while right < n:

            if nums[left] == 0 and nums[right] != 0:
                #swap
                nums[left] = nums[right]
                nums[right] = 0

                left += 1

            elif nums[left] != 0:
                left += 1

            right += 1

    ## Time Complexity : O(n)
    ## Space Complexity : O(1)

    def moveZeroes_workingSoln_AGAIN(self, nums: List[int]) -> None:

        '''
        L | R
        0 | 1

        [L] | [R]
         0  | 0   -> R++
         0  | 1   -> swap, L++, R++
         1  | 0   -> L++, R++
         1  | 1   -> L++, R++
        '''

        ## initialization
        n = len(nums)
        left = 0
        right = 1

        ## base condition
        if len(nums) == 0:
            return

        ## code
        while right < n :

            if left != 0:
                left += 1

            elif nums[left] == 0 and nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1

            right += 1

        ## Time Complexity : O(n)
        ## Space Complexity : O(1)
