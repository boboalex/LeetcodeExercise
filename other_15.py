from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]):
        lo = 0
        res = []
        N = len(nums)
        for hi in range(N):
            if hi == N - 1 or nums[hi] + 1 != nums[hi + 1]:
                if lo == hi:
                    res.append([nums[lo]])
                else:
                    res.append([nums[lo], nums[hi]])
                lo = hi + 1
        return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    s = Solution()
    res = s.summaryRanges(nums)
    print(res)
