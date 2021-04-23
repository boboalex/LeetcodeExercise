class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        max_length = 0
        right = -1
        for left in range(len(s)):

            if left != 0:
                res.remove(s[left-1])

            while right + 1 < len(s) and s[right + 1] not in res:
                res.add(s[right + 1])
                right += 1

            max_length = max(len(res), max_length)
        return max_length
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # 哈希集合，记录每个字符是否出现过
    #     occ = set()
    #     n = len(s)
    #     # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    #     rk, ans = -1, 0
    #     for i in range(n):
    #         if i != 0:
    #             # 左指针向右移动一格，移除一个字符
    #             occ.remove(s[i - 1])
    #         while rk + 1 < n and s[rk + 1] not in occ:
    #             # 不断地移动右指针
    #             occ.add(s[rk + 1])
    #             rk += 1
    #         # 第 i 到 rk 个字符是一个极长的无重复字符子串
    #         ans = max(ans, rk - i + 1)
    #     return ans


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        maxLength = 0
        N = len(s)
        for left in range(N):
            res.add(s[left])
            for right in range(left + 1, N):
                if s[right] not in res:
                    res.add(s[right])

                else:
                    break
            maxLength = max(len(res), maxLength)
            res.remove(s[left])
        return maxLength


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("anviaj")
    print(res)