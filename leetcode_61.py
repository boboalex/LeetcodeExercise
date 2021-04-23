# Definition for singly-linked list.
from LinkedList import LinkedList, ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return None
        current = head
        n = 1
        while current.next:
            current = current.next
            n += 1
        current.next = head
        tail = head
        for i in range(n - k % n):
            current = current.next
            tail = tail.next
        tail.next = None
        return current


if __name__ == '__main__':
    node_nums = [1, 2, 3, 4, 5]
    linked_list = LinkedList(node_nums)
    head = linked_list.head
    s = Solution()
    s.rotateRight(head, 2)
