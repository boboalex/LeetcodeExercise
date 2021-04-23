# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            preRoot = preLeft
            node = TreeNode(preorder[preRoot])
            inRoot = index_dict[preorder[preRoot]]
            sub_left_size = inRoot - inLeft
            node.left = myBuildTree(preLeft + 1, sub_left_size + preLeft, inLeft, inRoot - 1)
            node.right = myBuildTree(sub_left_size + preLeft + 1, preRight, inRoot + 1, inRight)
            return node

        index_dict = {element: index for index, element in enumerate(inorder)}
        N = len(preorder)
        return myBuildTree(0, N - 1, 0, N - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    res = s.buildTree(preorder, inorder)
    print(res)
