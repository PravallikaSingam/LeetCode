class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a part of the linked list
        def reverse_linked_list(head, k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, head  # Return the new head and the old tail
        
        # Edge case: if the list is empty or k = 1, no change is needed
        if not head or k == 1:
            return head
        
        # Create a dummy node to simplify head manipulations
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # This is the node before the group being reversed
        
        # Count the total number of nodes in the list
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        # Reverse nodes in groups of k
        while count >= k:
            group_head = group_prev.next
            group_tail = group_head
            for _ in range(k - 1):
                group_tail = group_tail.next  # Find the last node of the current group
            
            # Temporarily break the group from the rest of the list
            next_group = group_tail.next
            group_tail.next = None
            
            # Reverse the group of k nodes
            new_group_head, group_head = reverse_linked_list(group_head, k)
            
            # Connect the previous part to the new head of the reversed group
            group_prev.next = new_group_head
            # Connect the old tail of the reversed group to the next part of the list
            group_head.next = next_group
            
            # Move the group_prev pointer to the end of the reversed group
            group_prev = group_head
            
            # Decrease the count by k (since we've processed one group of k nodes)
            count -= k
        
        return dummy.next
