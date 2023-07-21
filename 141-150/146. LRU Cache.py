class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.stack = []

    def get(self, key: int) -> int:
        return self.store.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self.store:
            if len(self.stack) == self.cap:
                temp = self.stack.pop()
                self.store.pop(temp)
            self.stack.append(key)
        self.store[key] = value


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)