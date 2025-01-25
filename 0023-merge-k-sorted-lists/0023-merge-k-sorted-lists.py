import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Define a priority queue (min-heap)
        min_heap = []
        
        # Initialize the heap with the head nodes of each list
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        # Dummy node to simplify the result handling
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest element from the heap and then add its next element if exists
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next

        