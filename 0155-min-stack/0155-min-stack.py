class MinStack:

    def __init__(self):
        self.st = []
        self.mini = None

    def push(self, value: int) -> None:
        if not self.st:
            self.mini = value
            self.st.append(value)
            return
        
        if value > self.mini:
            self.st.append(value)
        else:
            self.st.append(2 * value - self.mini)
            self.mini = value
            
    def pop(self) -> None:
        if not self.st:
            return
        x = self.st.pop()

        if x < self.mini:
            self.mini = 2 * self.mini - x

    def top(self) -> int:
        if not self.st:
            return -1

        x = self.st[-1]

        if self.mini < x:
            return x

        return self.mini
        
    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()