#Permutation String

#You are given two strings s1 and s2.
#Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
#Both strings only contain lowercase letters.

#Example 1:

#Input: s1 = "abc", s2 = "lecabee"
#Output: true

#Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

#Example 2:

#Input: s1 = "abc", s2 = "lecaabee"
#Output: false

#Constraints:
#1 <= s1.length, s2.length <= 1000

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = Counter()

        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            s2_map[s2[i]] += 1
            if i >= len(s1):
                if s2_map[s2[i - len(s1)]] > 1:
                    s2_map[s2[i - len(s1)]] -= 1                    
                else:
                    del s2_map[s2[i - len(s1)]]
            if s1_map == s2_map:
                return True 

        return False
