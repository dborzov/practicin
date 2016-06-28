class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        i = 0
        stack = [(root, 'left')]
        while True:
            top, status = stack[-1]
            if status=='left':
                stack[-1] = (top, 'cur')
                if top.left:
                    stack.append( (top.left, 'left') )
            if status=='cur':
                stack[-1] = (top, 'right')
                i++
                if i==k:
                    return top.val
            if status=='right':
                stack[-1] = (top, 'done')
                if top.right:
                    stack.append( (top.right, 'left') )
            if status=='done':
                stack = stack[:-1]
