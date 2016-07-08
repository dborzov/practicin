# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        values = {head.val: True}
        pre = head
        cur = head.next
        while cur:
            if cur.val in values:
                pre.next = cur.next
            else:
                values[cur.val] = True
                pre = cur
            cur = cur.next
        return head
