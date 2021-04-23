import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.queue)
        self.queue.append(x)
        for i in range(n):
            val = self.queue.popleft()
            self.queue.append(val)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.empty())
    print(s.pop())
    print(s.pop())
    print(s.empty())