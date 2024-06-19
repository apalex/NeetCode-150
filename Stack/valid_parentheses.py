#Validate Parentheses

#Easy
#https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode

#You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#The input string s is valid if and only if:
#Every open bracket is closed by the same type of close bracket.
#Open brackets are closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Return true if s is a valid string, and false otherwise.

#Example 1:

#Input: s = "[]"
#Output: true

#Example 2:

#Input: s = "([{}])"
#Output: true

#Example 3:

#Input: s = "[(])"
#Output: false

#Explanation: The brackets are not closed in the correct order.

#Constraints:
#1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in Map:
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack 
     
#OR

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
