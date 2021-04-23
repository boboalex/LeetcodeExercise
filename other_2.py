class Solution:
    def convert(self, num):
        res = ""
        flag = False if num < 0 else True
        num = -num if num < 0 else num
        while num:
            remain_num = num % 2
            res = str(remain_num) + res
            num //= 2
        return "-" + res if not flag else res

    def convert1(self, num):
        y = num if num > 0 else -num
        res = ""
        while y > 0:
            bit = y % 2
            res = str(bit) + res
            y //= 2
        return res if num > 0 else ("-" + res)


if __name__ == '__main__':
    s = Solution()
    res = s.convert1(-10)
    print(res)
