#Reorder Linked List

#https://www.youtube.com/watch?v=S5bfdUTrKLM&ab_channel=NeetCode

#You are given the head of a singly linked-list.
#The positions of a linked list of length = 7 for example, can intially be represented as:

#[0, 1, 2, 3, 4, 5, 6]

#Reorder the nodes of the linked list to be in the following order:

#[0, 6, 1, 5, 2, 4, 3]

#Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

#[0, n-1, 1, n-2, 2, n-3, ...]

#You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

#Example 1:

#Input: head = [2,4,6,8]
#Output: [2,8,4,6]

#Example 2:

#Input: head = [2,4,6,8,10]
#Output: [2,10,4,8,6]

#Constraints:
#1 <= Length of the list <= 1000.
#1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge two halfs
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
