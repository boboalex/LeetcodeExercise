from LinkedList import LinkedList, ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        pre = dummy
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carry
            carry = sum // 10
            # carry = 1 if sum > 9 else 0
            pre.next = ListNode(sum % 10)
            pre = pre.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            pre.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    nums1 = [9, 9, 9, 9, 9, 9, 9]
    nums2 = [9, 9, 9, 9]
    l1, l2 = LinkedList(nums1), LinkedList(nums2)
    head1, head2 = l1.head, l2.head
    s = Solution()
    res = s.addTwoNumbers(head1, head2)
    print(res)