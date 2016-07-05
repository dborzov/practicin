# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            children = [depth(node.left), depth(node.right)]
            if -1 in children:
                return -1
            if abs(children[0] - children[1])>1:
                return -1
            return max(children) + 1
        if depth(root)==-1:
            return False
        return True
