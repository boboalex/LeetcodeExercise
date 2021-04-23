class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        def div(a, b):
            a = -a if a < 0 else a
            b = -b if b < 0 else b
            if a < b:
                return 0
            count = 1
            tb = b
            while tb + tb < a:
                count += count
                tb += tb
            return count + div(a - tb, b)

        if dividend == 0:
            return 0
        # if divisor == 1:
        #     return dividend
        # if divisor == -1:
        #     return -dividend if dividend > INT_MIN else INT_MAX
        sign = False if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else True
        res = div(dividend, divisor)
        if sign:
            return res if res <= INT_MAX else INT_MAX
        else:
            return -res


if __name__ == '__main__':
    s = Solution()
    res = s.divide(-2147483648, -1)
    print(res)