# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
양방향은 안되는...듯?
그러면 그냥 next 해주면서 자릿수**10 해서 더해주기
-> 출력도 어차피 역순이므로 그냥 순회하면서 더해주는 게 더 깔끔할 것  같음

입력부터 써줘야하는 줄 알았는데 그냥 Solution class만 완성하면 됨
"""
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_header = ListNode(0)
        p = result_header
        value = 0

        # l1, l2 둘 다 끝나고, value 끝까지 갈 때까지
        while l1 or l2 or value:
            if l1:
                value += l1.val
                l1 = l1.next

            if l2:
                value += l2.val
                l2 = l2.next
            
            p.next = ListNode(value % 10) # 자릿수
            p = p.next
            value = value // 10 # 다음 자릿수

        return result_header.next
