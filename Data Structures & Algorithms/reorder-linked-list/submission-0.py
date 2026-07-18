# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #base case: 1-2 nodes:
        if not head.next or not head.next.next:
            return
        
        #find the middle and split into two lists:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        p2 = slow.next
        slow.next = None

        #reverse the linked list:
        #set prev to None so we can swap pointer and prev later on
        prev = None
        while p2 and p2.next:
            #save
            temp = p2.next
            #create new pointing direction
            p2.next = prev
            #update
            prev = p2
            #swap
            p2 = temp
        
        p2.next = prev
        #merge the lists zipper style:
        p1 = head
        while p1 and p2:
            p1next = p1.next
            p2next = p2.next
            #point to new end of second list
            p1.next = p2
            #point to new end of first list
            p2.next = p1next
            p1 = p1next
            p2 = p2next


