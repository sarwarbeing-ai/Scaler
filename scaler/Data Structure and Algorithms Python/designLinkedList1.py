# Definition for singly-linked list.
#lass ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    '''
    Design linked list based on these operations:
    0 x -1: Add a node of value x before the first element of the linked list.
    After the insertion, the new node will be the first node of the linked list.

    1 x -1: Append a node of value x to the last element of the linked list.

    2 x index: Add a node of value x before the indexth node in the linked list.
    If the index equals the length of the linked list, the node will be appended
    to the end of the linked list. If the index is greater than the length,
    the node will not be inserted.

    3 index -1: Delete the indexth node in the linked list, if the index is valid.

    A[i][0] represents the type of operation.

    A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

    Note: Indexing is 0 based.
    '''
    def solve(self, A):
        head=ListNode('')
        c=0
        for i in range(len(A)):
            op=A[i][0]
            x=A[i][1]
            d=A[i][2]
            if op==0:
                temp=head
                new_node=ListNode(x)
                head=new_node
                new_node.next=temp
                c+=1
            elif op==1:
                new_node=ListNode(x)
                if c==0:
                    head=new_node
                    c+=1
                else:
                    if c==1:
                        head.next=new_node
                        c+=1
                    else:
                        temp=head
                        for i in range(c-1):
                            temp=temp.next
                        temp.next=new_node
                        c+=1
            elif op==2:
                if d>c:
                    pass
                elif d<0:
                    pass
                elif d==0:
                    new_node=ListNode(x)
                    temp=head
                    head=new_node
                    new_node.next=temp
                    c+=1
                elif d==c:
                    temp=head
                    new_node=ListNode(x)
                    for i in range(c-1):
                        temp=temp.next
                    temp.next=new_node
                    c+=1
                else:
                    new_node=ListNode(x)
                    temp=head
                    if d==1:
                        temp1=temp.next
                        temp.next=new_node
                        new_node.next=temp1
                        c+=1
                    else:
                        temp=head
                        for i in range(d-1):
                            temp=temp.next
                        temp1=temp.next
                        temp.next=new_node
                        new_node.next=temp1
                        c+=1
            else:
                # operation 3
                if x>=c:
                    pass
                elif x<0:
                    pass
                elif x==0:
                    head=head.next
                    c-=1
                else:
                    if x==1:
                        temp1=head.next
                        head.next=temp1.next
                        c-=1
                    else:
                        temp=head
                        for i in range(x-1):
                            temp=temp.next
                        temp1=temp.next.next
                        temp.next=temp1
                        c-=1
        return head
