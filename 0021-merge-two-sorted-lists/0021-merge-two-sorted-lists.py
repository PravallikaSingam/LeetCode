# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify the code
        dummy = ListNode()
        current = dummy
        
        # Traverse through both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If any elements remain in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list (dummy.next points to the head of the merged list)
        return dummy.next

        