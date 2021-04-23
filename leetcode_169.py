from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def myMajority(left, right):
            if left == right:
                return nums[left]
            mid = (left + right) >> 1
            left_num = myMajority(left, mid)
            right_num = myMajority(mid + 1, right)
            if left_num == right_num:
                return left_num
            left_count = sum(1 for num in nums[left: right + 1] if num == left_num)
            right_count = sum( 1 for num in nums[left: right + 1] if num == right_num)

            return left_count if left_count > right_count else right_count
        return myMajority(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 3]
    s = Solution()
    res = s.majorityElement(nums)
    print(res)