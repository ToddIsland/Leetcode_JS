class MinStack:
    def __init__(self):
        self.min = 0
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = sorted(self.stack)[0]

    def pop(self) -> None:
        self.stack.pop()
        self.min = sorted(self.stack)[0] if len(self.stack) else 0

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
