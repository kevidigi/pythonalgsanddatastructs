# Singly Linked List - Nodes with data and a pointer to the next node
# Head pointer indicates which node we are looking at
# Null (None in python) pointer indicates the end of the list

# Array insertion/deletion - O(n) 
# LL insertion/deletion - O(1)
# Array lookup - O(1)
# LL lookup - O(n)

# Arrays exist in contiguous blocks of memory, LLs do not.

# NB - this implementation is a bit shite

# LL Node Class
class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

# LL Class
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, node, data):
        pointer = self.head
        while pointer.next:
            if pointer.data == node:
                new_node = Node(data)
                new_node.next = pointer.next
                pointer.next = new_node
                return
            else:
                pointer = pointer.next
        print("Chosen insertion point is not in list")
        return
    
    def delete(self, node):
        
        if self.head.data == node:
            self.head.data = None
            self.head = self.head.next
            return

        pointer = self.head
        while pointer.next:
            if pointer.next.data == node:
                remove = pointer.next
                pointer.next = remove.next
                remove.data = None
                remove.next = None
                return
            else: pointer = pointer.next
        print("Chosen node to delete is not in list")
        return





llist = LinkedList()
llist.append("A")
llist.append("B")
llist.print_list()
print()
llist.prepend("C")
llist.print_list()
print()
llist.insert("A", "D")
llist.print_list()
print()
llist.delete("C")
llist.print_list()
