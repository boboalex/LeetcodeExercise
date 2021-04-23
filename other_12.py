class Solution:
    def select_sort(self, nums: list):
        N = len(nums)
        for i in range(N):
            min_index = i
            for j in range(i + 1, N):
                min_index = j if nums[j] < nums[min_index] else min_index
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    def insert_sort(self, nums: list):
        N = len(nums)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums

if __name__ == '__main__':
    s = Solution()
    res = s.insert_sort([9, 1, 3, 2, 5, 4])
    print(res)