from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_vol = 0
        while left < right:
            max_vol = min(height[left], height[right]) * (right - left)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_vol


if __name__ == '__main__':
    s = Solution()
    res = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(res)