class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) >> 1
            cost = (mid + 1) * mid // 2
            if cost == n:
                return mid
            elif cost < n:
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    s = Solution()
    res = s.arrangeCoins(5)
    print(res)
