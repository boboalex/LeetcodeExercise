class Solution:
    def isUgly(self, num: int) -> bool:
        ugly_nums = [2, 3, 5]
        for i in ugly_nums:
            while num % i == 0:
                num //= i
        return num == 1


if __name__ == '__main__':
    s = Solution()
    res = s.isUgly(6)
    print(res)
