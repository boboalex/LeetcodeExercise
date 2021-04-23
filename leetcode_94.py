class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stk = []
        # if root:
        #     stk.append(root)
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            # if root.right:
            root = root.right
            # stk.append(root)
        return res


if __name__ == '__main__':
    t3 = TreeNode(3)
    t2 = TreeNode(2, t3)
    t1 = TreeNode(1, None, t2)
    s = Solution()
    res = s.inorderTraversal(t1)
    print(res)