# design LinkedList
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

llist = LinkedList()

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    if position == 1:
        node = Node(value)
        node.next = llist.head
        llist.head = node
    else:
        current = llist.head
        current_pos = 1
        while current:
            if current_pos == position-1:
                nxt = current.next
                current.next = Node(value)
                current.next.next = nxt
                return
            else:
                current = current.next
                current_pos += 1

def delete_node(position):
    # @param position, integer
    # @return an integer
    if position == 1:
        llist.head = llist.head.next
    else:
        current = llist.head
        current_pos = 1
        while current.next:
            if current_pos == position-1:
                current.next = current.next.next
                return
            else:
                current = current.next
                current_pos += 1
        return

def print_ll():
    # Output each element followed by a space
    if llist.head == None:
        return None
    else:
        current = llist.head
        while current.next:
            print(current.val, end= " ")
            current = current.next
        print(current.val)
