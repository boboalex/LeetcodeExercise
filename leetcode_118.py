from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row_num in range(numRows):
            level = []
            for i in range(row_num + 1):
                if i == 0 or i == row_num:
                    level.append(1)
                else:
                    level.append(res[row_num - 1][i] + res[row_num - 1][i - 1])
            res.append(level)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.generate(5)
    print(res)