#Single Number

#https://www.youtube.com/watch?v=qMPX1AOa83k&ab_channel=NeetCode
 
#You are given a non-empty array of integers nums. Every integer appears twice except for one.
#Return the integer that appears only once.
#You must implement a solution with 𝑂(𝑛) runtime complexity and use only 
#𝑂(1) extra space.

#Example 1:

#Input: nums = [3,2,3]
#Output: 2

#Example 2:

#Input: nums = [7,6,6,7,8]
#Output: 8

#Constraints:
#1 <= nums.length <= 10000
#-10000 <= nums[i] <= 10000

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            print(res)
            res = n ^ res
            print(res)
        return res
