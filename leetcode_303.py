class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            self.sum[i + 1] = nums[i] + self.sum[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]