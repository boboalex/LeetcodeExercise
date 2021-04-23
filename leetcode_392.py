class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p0 = 0
        for p1 in range(len(t)):
            if t[p1] == s[p0]:
                p0 += 1
        if p0 < len(s) - 1:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    res = s.isSubsequence("ahbgdc", "ahbgdc")
    print(res)