class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(5, 3)