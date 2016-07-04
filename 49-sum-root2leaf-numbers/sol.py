# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, prefix):
            if not node:
                return 0
            if not node.left and not node.right:
                return int(prefix)
            sum = 0
            for each in [node.left, node.right]:
                sum += traverse(each, prefix + str(node.val))
            return sum
        return traverse(root, "")
