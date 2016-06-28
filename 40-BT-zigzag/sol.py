# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        zigzagger = []
        def traverse(node, depth,zigzagger):
            if node is None:
                return
            if len(zigzagger) < depth:
                zigzagger.append([])
            zigzagger[depth-1].append(node.val)
            traverse(node.left, depth+1,zigzagger)
            traverse(node.right, depth+1,zigzagger)
        traverse(root,1,zigzagger)
        for i, z in enumerate(zigzagger):
            if i%2==1:
                z.reverse()
        return zigzagger
