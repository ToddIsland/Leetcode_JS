class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.q = collections.deque()

    def get(self, key: int) -> int:
        ret = self.store.get(key, -1)
        if ret != -1:
            if len(self.q) == self.cap:
                
        return ret

    def put(self, key: int, value: int) -> None:
        if key not in self.store:
            if len(self.q) == self.cap:
                temp = self.q.popleft()
                self.store.pop(temp)
            self.q.append(key)
        self.store[key] = value


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)