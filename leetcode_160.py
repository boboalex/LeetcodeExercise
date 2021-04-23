from LinkedList import LinkedList, ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1, temp2 = headA, headB
        while temp1 != temp2:
            if not temp1 and temp2:
                temp1 = headB
            if not temp2 and temp1:
                tmep2 = headA
            temp1 = temp1.next
            temp2 = temp2.next
        if not temp1 and not temp2:
            return None
        else:
            return temp1


if __name__ == '__main__':
    node_nums1 = [4, 1, 8, 4, 5]
    linked_list1 = LinkedList(node_nums)
    head1 = linked_list1.head

    node_nums2 = [5, 6, 1, 8, 4, 5]
    linked_list2 = LinkedList(node_nums)
    head2 = linked_list2.head
