class Solution:
    def threeSum(self, nums: list) -> list:
        """
        求三数之和为0
        :param nums:
        :return:
        """
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort()

        for first in range(len(nums)):
            if nums[first] > 0:
                break
            if first != 0 and nums[first] == nums[first - 1]:
                first += 1
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                if nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                elif nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    second += 1
                    third -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(res)