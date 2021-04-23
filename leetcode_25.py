from LinkedList import LinkedList, ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        # dummy = ListNode(-1, head)
        def reverse(head, tail):
            pre = tail.next
            current = head
            while pre != tail:
                next = current.next
                current.next = pre
                pre = current
                current = next
            return tail, head

        prev = dummy
        while head:

            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            part_head, part_tail = reverse(head, tail)
            prev.next = part_head
            head = part_tail.next
            prev = part_tail
        return dummy.next


if __name__ == '__main__':
    node_nums = [1, 2, 3, 4, 5]
    linked_list = LinkedList(node_nums)
    head = linked_list.head
    s = Solution()
    res = s.reverseKGroup(head, 2)
