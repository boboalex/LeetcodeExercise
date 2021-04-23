class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)
        if N == 0:
            return 0

        for i in range(N - M + 1):
            for j in range(M):
                if haystack[i] != needle[j]:
                    break
                if j == M - 1:
                    return i
        return -1

if __name__ == '__main__':
    s = Solution()
    res1 = s.strStr("hello", "ll")
    assert res1 == 2
    res2 = s.strStr("aaaaa", "bba")
    assert res2 == -1
    res3 = s.strStr("a", "a")
    assert res3 == 0