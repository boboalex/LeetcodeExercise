from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], []
        if root:
            queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level)
        return res