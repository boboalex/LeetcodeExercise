class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        lo, hi = 2, num // 2
        while lo <= hi:
            mid = (lo + hi) >> 1
            squared_num = mid * mid
            if squared_num == num:
                return True
            elif squared_num < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    res = s.isPerfectSquare(14)
    print(res)