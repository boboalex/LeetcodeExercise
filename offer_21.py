from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if (nums[lo] & 1) == 1:
                lo += 1
                continue
            if (nums[hi] & 1) == 0:
                hi -= 1
                continue
            nums[lo], nums[hi] = nums[hi], nums[lo]
        return nums

if __name__ == '__main__':
    s = Solution()
    res = s.exchange([1, 2, 3, 4])
    print(res)