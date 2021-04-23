class Solution:
    def fourSum(self, nums, target: int):
        N = len(nums)
        if N < 4:
            return []
        res = []
        nums.sort()
        for first in range(N - 3):
            if first != 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, N - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                fourth = N - 1
                while third < fourth:
                    if nums[first] + nums[second] + nums[third] + nums[fourth] > target:
                        fourth -= 1
                    elif nums[first] + nums[second] + nums[third] + nums[fourth] < target:
                        third += 1
                    else:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1
                        third += 1
                        fourth -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.fourSum([0, 0, 0, 0], 0)
    print(res)
