class Solution:
    def quick_sort(self, nums: list):
        def partition(left, right):
            slow = left
            pivot = nums[left]
            for fast in range(left + 1, right + 1):
                if nums[fast] < pivot:
                    slow += 1
                    nums[slow], nums[fast] = nums[fast], nums[slow]
            nums[left], nums[slow] = nums[slow], nums[left]
            return slow

        def sort(left, right):
            if left > right:
                return
            index = partition(left, right)
            sort(left, index - 1)
            sort(index + 1, right)

        N = len(nums)
        left, right = 0, N - 1
        sort(left, right)
        return nums


if __name__ == '__main__':
    s = Solution()
    array = [3, 6, 1, 7, 2]
    res = s.quick_sort(array)
    print(res)