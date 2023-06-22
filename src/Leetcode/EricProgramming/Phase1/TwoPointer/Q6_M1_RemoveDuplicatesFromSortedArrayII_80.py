'''

    Question
        - Each number in the array is allowed to appear 0,1,2 times - meaning - 1 duplicate is allowed.
            If there are more than one duplicate, it should be moved at last.
            Return should be the index till which all numbers appear at most twice

    Solution
        - two pointer approach
            - left : points at the first or first duplicate occurrence of the element
            - right : points at the next unique element in the list
        - two cases
            [left] == [right]
                if duplicate < 1
                    - duplicate += 1
                    - left += 1
                    - right += 1
                else
                    - right += 1

            [left] != [right]
                - left += 1
                - swap
                - right += 1
                - duplicate = 0

    The catch!
        - in cases like [1,1,1,2,3,3]
        - as the code progresses
            - [1,1,1,1,2,3,3]
            -    L     R        duplicate > 1
            - [1,1,2,1,2,3,3]
            -      L     R      duplicate = 0
            - [1,1,2,3,2,3,3]
            -        L     R    duplicate = 0
            - [1,1,2,3,2,3,3]
            -          L     R  duplicate = 1

            - return left+1 = 5 => [1,1,2,3,2]

        - when we are in condition [left] == [right]
            - left always point to first/or 1st duplicate of a number
            - so when we have [left] != [right]
            - then we find the first occurrence of a new number (at right)
            - so we do [left+1] = [right]; right += 1
            - If now [left] == [right]
            - It means that it is a duplicate
            - so if the value of the duplicate variable is < 1
            - this is the first duplicate
            - so we can safely do [left+1] = right
            - This way we can be sure of two things
                - we do ot miss this duplicate if the code ends at this iteration
                - we do not miss this duplicate

    * Time Complexity : O(n)
    * Space Complexity : O(1)

'''

from typing import List
class Solution:

    def removeDuplicatesFromSortedArrayII(self, nums: List[int]) -> int:

        ## initializations
        left = 0
        right = 1
        n = len(nums)
        duplicate = 0

        ## base case
        if len(nums) < 3:
            return

        ##code

        while right < n:

            if nums[left] == nums[right]:
                if duplicate < 1:
                    duplicate += 1
                    left += 1
                    nums[left] = nums[right]
            else:
                left += 1
                nums[left] = nums[right]
                duplicate = 0

            right += 1

        return left + 1