# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        temp=A
        if temp.next is None:
            return temp.val
        temp1=A
        try:
           while temp1 is not None:
                 temp,temp1=temp.next,temp1.next.next
           return temp.val
        except:
            return temp.val
