from LinkedList import ListNode, LinkedList


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small, large = ListNode(-1), ListNode(-1)
        smallHead, largeHead = small, large
        while head:
            if head.val >= x:
                large.next = head
                large = large.next
            else:
                small.next = head
                small = small.next
            head = head.next
        if not smallHead.next:
            return largeHead.next
        else:
            small.next = largeHead.next
            return smallHead.next


if __name__ == '__main__':
    node_nums = [1, 4, 3, 2, 5, 2]
    linked_list = LinkedList(node_nums)
    head = linked_list.head
    s = Solution()
    res = s.partition(head, 3)
