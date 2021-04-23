class Solution:
    def findPalindrome(self, s: str) -> str:
        N = len(s)
        if N < 2:
            return s
        dp = [[False] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
        res = []
        for j in range(1, N):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    if j - i > 1:
                        res.append([s[i: j + 1]])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findPalindrome("abababbbb")
    print(res)