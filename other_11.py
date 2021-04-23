class Solution:
    def solve(self , nums ):
        # write code here
        N = len(nums)
        for i in range(N):
            for j in range(i, N - 1):
                a = str(nums[j]) + str(nums[j + 1])
                b = str(nums[j + 1]) + str(nums[j])
                if a < b:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        res = [str(num) for num in nums]
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    res = s.solve([30, 1])
    print(res)
