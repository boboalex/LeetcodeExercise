class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = head.next
        pre = None
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            if pre:
                pre.next = temp
            pre = head
            head = head.next
        return new_head


class LinkedList:
    def __init__(self, node_nums):
        current = ListNode(node_nums[0])
        self.head = current
        for i in range(1, len(node_nums)):
            temp = ListNode(node_nums[i])
            current.next = temp
            current = current.next

    @property
    def get_head(self):
        return self.head

if __name__ == '__main__':
    node_nums = [1, 2, 3, 4]
    linked_list = LinkedList(node_nums)
    head = linked_list.head
    s = Solution()
    s.swapPairs(head)
