from LinkedList import LinkedList, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode):
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        current = head
        pre = None
        while pre != slow.next:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return slow.next


if __name__ == '__main__':
    node_nums = [-10, -3, 0, 5, 9]
    linked_list = LinkedList(node_nums)
    head1 = linked_list.head
    s = Solution()
    res = s.sortedListToBST(head1)
    print(res)