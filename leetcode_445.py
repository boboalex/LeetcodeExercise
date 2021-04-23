class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        carry = 0
        next = None
        while stk1 or stk2:
            a = stk1.pop() if stk1 else 0
            b = stk2.pop() if stk2 else 0
            sum = a + b + carry
            carry = 0 if sum <= 9 else 1
            current = ListNode(sum % 10)
            current.next = next
            next = current
        if carry:
            current = ListNode(1)
            current.next = next
            next = current
        return next