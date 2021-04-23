from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        num_times = {}
        for num in nums:
            if num not in num_times:
                num_times[num] = 1
            else:
                num_times[num] += 1
        for key, value in num_times.items():
            if value > 1:
                return key


if __name__ == '__main__':
    s = Solution()
    res = s.findRepeatNumber([1, 1, 1])
    print(res)
