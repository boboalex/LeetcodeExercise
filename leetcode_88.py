from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p2 >= 0 and nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            elif p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1


if __name__ == '__main__':
    s = Solution()
    # s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge([0], 0, [1], 1)