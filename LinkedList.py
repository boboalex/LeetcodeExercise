class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def get_length(self):
        tail = self.head
        N = 1
        while tail.next:
            tail = tail.next
            N += 1
        return N

    def get_nodes_val(self):
        temp = self.head
        while temp:
            yield temp.val
            temp = temp.next
