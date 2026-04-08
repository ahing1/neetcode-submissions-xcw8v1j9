class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.history) == 0 or val <= self.history[-1]:
            self.history.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if self.history and top == self.history[-1]:
            self.history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.history[-1]
