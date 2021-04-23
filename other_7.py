class Solution:
    def convert(self, num_str):
        N = len(num_str)
        res = num_str[0]
        isNegtive = False
        if res == "-":
            res = 0
            isNegtive = True
        else:
            res = int(res)
        for i in range(1, N):
            res = res * 10 + int(num_str[i])
        return res if not isNegtive else -res


if __name__ == '__main__':
    s = Solution()
    res = s.convert("-123")
    print(res)