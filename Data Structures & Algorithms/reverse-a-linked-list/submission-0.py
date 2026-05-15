# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #save the next node
            temp = curr.next
            #reverse the pointer
            curr.next = prev
            #update prev to point to current
            prev = curr
            #swap curr and temp
            curr = temp
        return prev