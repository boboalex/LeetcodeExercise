class Solution:
    def myPow(self, x: float, n: int) -> float:
        def positive_pow(N):
            result = 1.0
            x_con = x
            while N > 0:
                if N & 0x01 == 1:
                    result *= x_con
                x_con *= x_con
                N = N >> 1
            return result

        return positive_pow(n) if n >= 0 else 1.0 / positive_pow(-n)


if __name__ == '__main__':
    s = Solution()
    res = s.myPow(2, 6)
    print(res)
