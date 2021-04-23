from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        N = len(a)
        left = [1 for _ in range(N)]
        right = [1 for _ in range(N)]
        for i in range(1, N):
            left[i] = left[i - 1] * a[i - 1]
        for j in range(N-2, -1, -1):
            right[j] = right[j + 1] * a[j + 1]
        res = [1 for _ in range(N)]
        for index in range(0, N):
            res[index] = left[index] * right[index]
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.constructArr([1, 2, 3, 4, 5])
    print(res)