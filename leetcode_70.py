class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 1, 1
        for _ in range(n):
            r = p + q
            p = q
            q = r
        return r


class Solution1:
    def climbStairs(self, n: int) -> int:
        p, q, r = 1, 1, 2
        if n == 1:
            return 1
        for i in range(1, n):
            r = p + q
            p = q
            q = r
        return r


class Solution2:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 1, 1
        for _ in range(n):
            r = p + q
            yield r
            p = q
            q = r


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

if __name__ == '__main__':
    s = Solution2()
    f = s.climbStairs(5)
    for res in s.climbStairs(5):
        print(res)

    # for x in fib(5):
    #     print(x)
