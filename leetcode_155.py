import math

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = math.inf
        self.diff_stack = []

    def push(self, x: int) -> None:
        if not self.diff_stack:
            self.min_val = x
            self.diff_stack.append(0)
        else:
            diff = x - self.min_val
            self.min_val = x if diff < 0 else self.min_val
            self.diff_stack.append(diff)

    def pop(self) -> None:
        diff = self.diff_stack.pop()
        if diff > 0:
            top = diff + self.min_val
        else:
            top = self.min_val
            self.min_val = top - diff
        return top

    def top(self) -> int:
        diff = self.diff_stack[-1]
        return self.min_val if diff < 0 else self.min_val + diff

    def getMin(self) -> int:
        return self.min_val


if __name__ == '__main__':
    s = MinStack()
    s.push(1)
    s.push(2)
    print(s.getMin())
    print(s.top())
    print(s.pop())
    print(s.getMin())
    print(s.top())