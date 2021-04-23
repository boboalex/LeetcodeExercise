class Solution:
    def removeDuplicates(self, nums) -> int:

        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                nums[left + 1] = nums[right]
                left += 1
        return left


if __name__ == '__main__':
    s = Solution()
    res = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(res)
