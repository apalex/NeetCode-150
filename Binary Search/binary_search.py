#Binary Search

#Easy
#https://www.youtube.com/watch?v=s4DPM8ct1pI&ab_channel=NeetCode

#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

#Your solution must run in 𝑂(𝑙𝑜𝑔𝑛) time.

#Example 1:

#Input: nums = [-1,0,2,4,6,8], target = 4
#Output: 3

#Example 2:

#Input: nums = [-1,0,2,4,6,8], target = 3
#Output: -1

#Constraints:

#1 <= nums.length <= 10000.
#-10000 < nums[i], target < 10000

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
