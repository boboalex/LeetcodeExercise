from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        left = hi
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        right = hi
        return right - left


if __name__ == '__main__':
    s = Solution()
    res = s.search([5, 7, 7, 8, 8, 10], 8)
    print(res)
