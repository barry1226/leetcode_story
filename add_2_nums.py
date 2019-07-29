# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        plus = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            r.next = ListNode((val1 + val2 + plus) % 10)
            plus = (val1 + val2 + plus) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            r = r.next
        if plus == 1:
            r.next = ListNode(1)
        return re.next
