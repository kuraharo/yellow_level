#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self,headA, headB):
        lenA=0
        lenB=0
        A=headA
        B=headB
        while A:
            A=A.next
            lenA=lenA+1
        while B:
            B=B.next
            lenB=lenB+1
        A=headA
        B=headB
        if lenA>lenB:
            for i in range(lenA - lenB):
                A = A.next
        else:
            for i in range(lenB - lenA):
                B = B.next
        while A and B:
            if (A == B):
                return A
            A=A.next
            B=B.next
    
        return None
    

        