# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, depth):
            if node.left  is None and node.right is None:
                return depth
            min_depth = 999999999
            return min([traverse(each, depth+1) for each in [node.left, node.right] if each])
        if root is None:
            return 0
        return traverse(root,1)
