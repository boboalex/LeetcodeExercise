class Solution:
    def flipCards(self, n):
        dp = [0] * n
        for i in range(1, n):
            for j in range(i, n, i + 1):
                dp[j] = 1 if dp[j] == 0 else 0
        res = [i + 1 for i in range(n) if dp[i] == 0]
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.flipCards(100)
    print(res)
