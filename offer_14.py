class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        for i in range(4, n + 1):
            max_product = 0
            for j in range(1, i // 2 + 1):
                max_product = max(dp[j] * dp[i - j], max_product)
            dp[i] = max_product
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    res = s.cuttingRope(10)
    print(res)