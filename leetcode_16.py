class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        """
        求最接近target的三数之和
        :param nums:
        :param target:
        :return:
        """
        res_diff = 2 ** 31 - 1
        res_sum = 2 ** 31 - 1
        nums.sort()
        for first in range(len(nums)):
            if first != 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                current_sum = nums[first] + nums[second] + nums[third]
                if current_sum - target == 0:
                    return current_sum
                elif current_sum < target:
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    if abs(current_sum - target) < res_diff:
                        res_diff = abs(current_sum - target)
                        res_sum = current_sum
                    second += 1
                else:
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    if abs(current_sum - target) < res_diff:
                        res_diff = abs(current_sum - target)
                        res_sum = current_sum
                    third -= 1

        return res_sum


if __name__ == '__main__':
    s = Solution()
    res1 = s.threeSumClosest([0, 2, 1, -3], 1)
    assert res1 == 0
    res2 = s.threeSumClosest([-1, 2, 1, -4], 1)
    assert res2 == 2
