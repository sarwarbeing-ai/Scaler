# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        head=A
        # if the length of the linkedlist is zero
        if head is None:
            return head
        # use two pointers
        temp1=head
        temp2=temp1.next
        # loop until temp2 is None
        while temp2 is not None:
            # check if the node temp1 and temp2 have same value
            # then delete temp2 by updating temp1.next=temp2.next
            # and also update temp2
            if temp1.val==temp2.val:
                temp1.next=temp2.next
                temp2=temp2.next
            else:
                # otherwise do as usual
                temp1=temp2
                temp2=temp1.next
        return head
