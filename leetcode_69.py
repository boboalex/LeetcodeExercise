class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) >> 1
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    res = s.mySqrt(0)
    print(res)