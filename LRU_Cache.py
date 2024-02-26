# Ordered Dict Approach

import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash=collections.OrderedDict()
    def get(self, key: int) -> int:
        if key in self.hash:
            self.hash.move_to_end(key)
            return self.hash[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key]=value
            self.hash.move_to_end(key)
        elif len(self.hash)==self.capacity:
            self.hash.popitem(last=False)
            self.hash[key]=value
        else:
            self.hash[key]=value

# Doubly Linked List

class ListNode:
    def __init__(
        self, key: int,
        value: int,
        next: "ListNode" = None,
        prev: "ListNode" = None
    ):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}

        # Sentinel nodes for the head and tail of the double-linked list
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """Update the cache with the given key-value pair. If the cache is at capacity, remove the least recently used item."""
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove_from_list(node)
            self.insert_into_head(node)
            node.value = value
        else:
            if len(self.dictionary) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key, value)   
            self.insert_into_head(node)
            self.dictionary[key] = node
    
    def remove_from_list(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert_into_head(self, node: ListNode) -> None:
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        
    def remove_from_tail(self) -> None:
        """Remove the least recently used item (tail) from the cache."""
        if len(self.dictionary) == 0:
            return
        
        tail_prev = self.tail.prev
        self.remove_from_list(tail_prev)
        del self.dictionary[tail_prev.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
