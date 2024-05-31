#Longest Substring Without Duplicates

#https://www.youtube.com/watch?v=wiGpQwVHdE0&ab_channel=NeetCode

#Given a string s, find the length of the longest substring without duplicate characters.
#A substring is a contiguous sequence of characters within a string.

#Example 1:

#Input: s = "zxyzxyz"
#Output: 3

#Explanation: The string "xyz" is the longest without duplicate characters.

#Example 2:

#Input: s = "xxxx"
#Output: 1

#Constraints:
#0 <= s.length <= 1000
#s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, result = 0, 0

        for x in range(len(s)):
            while s[x] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[x])
            result = max(result, x - l + 1)
        return result
