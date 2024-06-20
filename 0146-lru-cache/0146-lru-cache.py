class ListNode:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = self.right = ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.left, self.left.next
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key] 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)