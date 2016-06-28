# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memoize = {}
        def get_max(node, parent_robbed, memoize):
            memo_key = node.id + str(parent_robbed)
            if memo_key in memoize:
                return memoize[memo_key]
            if node is None:
                return 0
            not_rob_this_one = get_max(node.left, False, memoize) + get_max(node.right, False, memoize)
            if parent_robbed:
                memoize[memo_key] = not_rob_this_one
                return memoize[memo_key]
            rob_this_one = node.val + get_max(node.left, True, memoize) + get_max(node.right, True, memoize)
            memoize[memo_key] = max(not_rob_this_one, rob_this_one)
            return memoize[memo_key]
        return get_max(root, False, memoize)
