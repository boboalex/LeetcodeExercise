class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif s[i - 1] == ')':
                    if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] >= 2:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:
                            dp[i] = dp[i - 1] + 2
                max_len = max(max_len, dp[i])
        return max_len

if __name__ == '__main__':
    s = Solution()
    res = s.longestValidParentheses("()))")
    print(res)