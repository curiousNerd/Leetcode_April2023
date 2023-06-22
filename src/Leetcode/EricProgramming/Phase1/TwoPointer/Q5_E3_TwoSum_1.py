'''

Question -
    * Given an array - find 2 numbers that add up to give the target

Assumptions -
    * We have to return the first pair that adds up to the number
    * Each number is counted only once

Solution -
    * Brute Force
        - Use a nested for loop with
            - i : 0 to n
            - j : i+1 to n
        - Check if the elements at i and j add up to the target
        - return if such a pair is found

        * Time Complexity : O(n^2)
        * Space Complexity : O(1)

    * Optimal Solution
        - Maintain a dictionary to store element with its corresponding index
        - Iterate over the array and check
            - If the complement (target - curr_elem) is present in the dictionary
            - If found in dictionary -> we have found 2 numbers that add up to the target

        - Approach :
            1.
            - Iterate once - Create the dictionary
            - Iterate again - Find if complement is present in the dictionary

            2.
            - Iterate only once and do both steps together

        * Time Complexity : O(n)
        * Space Complexity : O(1)
'''

from typing import List


def twoSum_twoParse(self, nums: List[int], target: int) -> List[int]:
    index_dict = {}

    for x in range(len(nums)):

        if nums[x] not in index_dict:
            index_dict[nums[x]] = x

    for x in range(len(nums)):

        complement = target - nums[x]

        if complement in index_dict and index_dict[complement] != x:
            ## This and condition is very important otherwise for cases like [3,2,4], 6 3 will be counted twice
            return [index_dict[complement] + 1, x + 1]

    return []

def twoSum_SingleParse(self, nums: List[int], target: int) -> List[int]:
    index_dict = {}

    for x in range(len(nums)):

        complement = target - nums[x]

        if complement in index_dict:
            return [x, index_dict[complement]]
        else:
            index_dict[nums[x]] = x

    return []

