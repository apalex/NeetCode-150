#Duplicate Integer

#https://www.youtube.com/watch?v=3OamzN90kPg&ab_channel=NeetCode

#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#Example 1:

#Input: nums = [1, 2, 3, 3]
#Output: true

#Example 2:

#Input: nums = [1, 2, 3, 4]
#Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y] and x != y:
                    return True

        return False

#Solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
      
