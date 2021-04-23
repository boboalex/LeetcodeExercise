import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = -2 ** 31

    def isValidBST(self, root: TreeNode) -> bool:

        def validation(node):
            if not node:
                return True
            if not validation(node.left):
                return False
            if node.val < self.pre:
                return False
            self.pre = node.val
            return validation(node.right)

        return validation(root)


if __name__ == '__main__':
    t0 = TreeNode(0)
    s = Solution()
    res = s.isValidBST(t0)
    print(res)