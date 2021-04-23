from typing import List
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(left, right):
            if left < right:
                pivotindex = random.randint(left, right)

                arr[pivotindex], arr[left] = arr[left], arr[pivotindex]
            pivot = arr[left]
            # 这里需要注意如果j=left+1会有越界的可能
            j = left
            for i in range(left + 1, right + 1):
                if arr[i] < pivot:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[left], arr[j] = arr[j], arr[left]
            return j

        N = len(arr)
        left, right = 0, N - 1
        while True:
            index = partition(left, right)
            if index < k - 1:
                left = index + 1
            elif index > k - 1:
                right = index - 1
            else:
                return arr[:k]


if __name__ == '__main__':
    arr = [0, 0, 2, 3, 2, 1, 1, 2, 0, 4]
    s = Solution()
    res = s.getLeastNumbers(arr, 10)
    print(res)
