from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def sink(i):
            while 2 * i + 1 <= k - 1:
                j = 2 * i + 1
                if j + 1 < k - 1 and nums[j + 1] < nums[j]:
                    j += 1
                if nums[i] < nums[j]:
                    break

                nums[i], nums[j] = nums[j], nums[i]
                i = j

        def swim(i):
            while i > 0:
                j = (i - 1) // 2
                if nums[j] < nums[i]:
                    break
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = j

        N = len(nums)
        for i in range(k):
            swim(i)

        for j in range(k, N):
            if nums[j] > nums[0]:
                nums[0], nums[j] = nums[j], nums[0]
                sink(0)
        return nums[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    s = Solution()
    res = s.findKthLargest(nums, 2)
    print(res)