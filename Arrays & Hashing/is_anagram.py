#Is Anagram

#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#Example 1:

#Input: s = "racecar", t = "carrace"
#Output: true

#Example 2:

#Input: s = "jar", t = "jam"
#Output: false

#Constraints:
#s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for x in range(len(s)):
            countS[s[x]] = 1 + countS.get(s[x], 0)
            countT[t[x]] = 1 + countT.get(t[x], 0)
        for y in countS:
            if countS[y] != countT.get(y, 0):
                return False

        return True
