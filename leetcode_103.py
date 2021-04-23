# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        res, queue = [], []
        isOrderLeft = True
        if root:
            queue.append(root)
        while queue:
            level = []
            N = len(queue)
            for i in range(N):

                if isOrderLeft:
                    node = queue.pop(0)
                    level.append(node.val)
                else:
                    node = queue.pop()
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
            isOrderLeft = not isOrderLeft
        return res

if __name__ == '__main__':
    t0 = TreeNode(3)
    t1 = TreeNode(9)
    t2 = TreeNode(20)
    t3 = TreeNode(15)
    t4 = TreeNode(7)
    t0.left = t1
    t0.right = t2
    t2.left = t3
    t2.right = t4
    s = Solution()
    res = s.zigzagLevelOrder(t0)
    print(res)