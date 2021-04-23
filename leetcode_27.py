from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = -1
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left + 1] = nums[right]
                left += 1
        return left + 1


if __name__ == '__main__':
    s = Solution()
    res = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(res)
