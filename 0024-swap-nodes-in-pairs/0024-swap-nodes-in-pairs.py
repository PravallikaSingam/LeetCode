# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify the swapping logic
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Identify the two nodes to swap
            first = head
            second = head.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the prev and head pointers forward by two steps
            prev = first
            head = first.next
        
        # Return the new head, which is the next of the dummy node
        return dummy.next

        