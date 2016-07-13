# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        for level in range(1,99999):
            ptr = None
            for cc in range(2**level):
                idx = 2**(level+1) - 1 - cc
                cur = root
                for i in range(level):
                    shift = (level-1-i)
                    if (idx  >> shift) % 2==0:
                        cur = cur.left
                    else:
                        cur = cur.right
                    if cur is None:
                        break
                if cur is None:
                    continue
                if not ptr is None:
                    cur.next = ptr
                ##############
                # print 'level: ', level, ", idx: ", idx
                # if ptr:
                #     print "    ptr: ", ptr.val
                # if cur:
                #     print "    cur: ", cur.val
                ###############
                ptr = cur
            if ptr is None:
                break

NodeA = TreeLinkNode(1)
Node2 = TreeLinkNode(2)
Node3 = TreeLinkNode(3)
Node4 = TreeLinkNode(4)
Node7 = TreeLinkNode(7)
NodeA.left = Node2
NodeA.right = Node3
Node2.left = Node4
Node3.right = Node7

Solution().connect(NodeA)
nn = NodeA

import pdb; pdb.set_trace()
