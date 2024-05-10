# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev

    def toList(self, node):
        temp=[]
        
        while node:
            temp.append(node.val)
            node=node.next

        return temp

    def toLinkedList(self, result_list):
        prev = None

        for element in result_list:
            node = ListNode(element)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = self.toList(self.reverseList(l1))
        l2 = self.toList(self.reverseList(l2))
        
        l1_int = int(''.join([str(e) for e in l1]))
        l2_int = int(''.join([str(e) for e in l2]))
        
        two_sum = l1_int + l2_int
        
        result = list(str(two_sum))

        return self.toLinkedList(result)
