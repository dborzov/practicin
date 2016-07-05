class Solution(object):
    def sortList(self, root):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(node):
            if not node.next:
                return node, node
            cur = node.next.next

            if node.val > node.next.val:
                greater, lower = node, node.next
            else:
                greater, lower = node.next, node
            spawn_greater, spawn_lower = greater, lower
            divide_value = greater.val
            greater.next = None
            lower.next = None
            while cur:
                if cur.val >= divide_value:
                    greater.next = cur
                    greater = cur
                else:
                    lower.next = cur
                    lower = cur
                next_cur = cur.next
                cur.next = None
                cur = next_cur
            greater_head, greater_tail = sort(spawn_greater)
            lower_head, lower_tail = sort(spawn_lower)
            lower_tail.next = greater_head
            return lower_head, greater_tail
        if not root:
            return root
        head, tail = sort(root)
        return head
