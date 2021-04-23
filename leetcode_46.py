from typing import List
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path)
                return

            for i in range(size):
                if not used[i]:
                    # used[i] = True
                    new_path = copy.deepcopy(path)
                    new_used = copy.deepcopy(used)

                    new_path.append(nums[i])
                    new_used[i] = True
                    dfs(nums, size, depth + 1, new_path, new_used, res)

                    # used[i] = False
                    # path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        path = []
        dfs(nums, size, 0, path, used, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
