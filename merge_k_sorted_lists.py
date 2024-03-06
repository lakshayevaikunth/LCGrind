# Brute force

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        # Merge lists one by one
        for head in lists:
            merged = self.merge_two_lists(merged, head)
        return merged
    
    # Helper function to merge two sorted linked lists
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

#  Divide and Conquer Approach - Merge sort
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Helper function to merge two sorted linked lists
        def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge_two_lists(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_lists(l1, l2.next)
                return l2
        
        # Helper function to merge lists recursively
        def merge_lists(lists: List[Optional[ListNode]], start: int, end: int) -> ListNode:
            if start == end:
                return lists[start]
            mid = (start + end) // 2
            left_merged = merge_lists(lists, start, mid)
            right_merged = merge_lists(lists, mid + 1, end)
            return merge_two_lists(left_merged, right_merged)
        
        # Check for empty lists
        if not lists:
            return None
        return merge_lists(lists, 0, len(lists) - 1)
      
# Priority Queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        for l in lists:
            push_node(heap, l)
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                push_node(heap, node.next)

        return dummy.next
