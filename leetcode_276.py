class Solution:
    def numWays(self, n: int, k: int) -> int:
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                res[i] = k
            elif i == 2:
                res[i] = k * k
            else:
                res[i] = (k - 1) * (res[i - 1] + res[i - 2])
        return res[n]


if __name__ == '__main__':
    s = Solution()
    res = s.numWays(0, 0)
    print(res)
