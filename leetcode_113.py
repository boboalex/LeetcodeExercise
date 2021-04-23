class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        res, path = [], []

        def dfs(node, sum):
            if not node:
                return
            path.append(node.val)
            sum -= node.val
            if sum == 0 and not node.left and not node.right:
                res.append(path[:])
            dfs(node.left, sum)
            dfs(node.right, sum)
            path.pop()

        dfs(root, targetSum)
        return res

# class Solution:
#     def pathSum(self, root: TreeNode, total: int):
#         ret = list()
#         path = list()
#
#         def dfs(root: TreeNode, total: int):
#             if not root:
#                 return
#             path.append(root.val)
#             total -= root.val
#             if not root.left and not root.right and total == 0:
#                 ret.append(path[:])
#             dfs(root.left, total)
#             dfs(root.right, total)
#             path.pop()
#
#         dfs(root, total)
#         return ret


if __name__ == '__main__':
    t0, t1, t2, t3, t4, t5 = TreeNode(5), TreeNode(4), TreeNode(8), TreeNode(11), TreeNode(7), TreeNode(2)
    t6, t7, t8, t9 = TreeNode(13), TreeNode(4), TreeNode(5), TreeNode(1)
    t0.left, t0.right = t1, t2
    t1.left = t3
    t3.left, t3.right = t4, t5
    t2.left, t2.right = t6, t7
    t7.left, t7.right = t8, t9
    s = Solution()
    res = s.pathSum(t0, 22)
    print(res)