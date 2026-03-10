from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None        # Each node's next attribute is another node, just like the dictionary method

class LinkedList:
    def __init__(self):         # Constructor
        self.head = None        # The head will equal the first node

    def prepend(self, data):
        new_node = Node(data)           # Create a new node
        new_node.next = self.head       # Make the new node point to where the head points to
        self.head = new_node            # Make the head point to the new node

    def append(self, data):
        new_node = Node(data)           # Create a new node

        if self.head == None:           # If the linked list is empty...
            self.head = new_node        # ...make the head point to the new node
            return

        last_node = self.head           # This will be used to find the last node

        while last_node.next != None:   # While we haven't found the last node...
            last_node = last_node.next  # ...move to the next node in the linked list

        last_node.next = new_node       # Make the last node point to the new node

    def insert_after(self, data):
        new_node = Node(data)               # Create a new node
        before_node = self.head             # This will be used to find the node before where we want it

        # While we haven't found our desired node, and there is still a linked list...
        while before_node.data != data and before_node.next != None:
            before_node = before_node.next                              # ...move to the next node

        if before_node.next == None:        # If the linked list is empty or the item doesn't exist...
            print("Item not found")         # ...stop and output an error
            return

        if before_node.data == data:            # If we found our node...
            new_node.next = before_node.next    # ...make the new node point to whatever the previous node points to...
            before_node.next = new_node         # ...and make the previous node point to the new node


    def remove(self, data):
        before_node = self.head             # This will be used to find the node before the one to delete

        # While we haven't found our desired node, and there is still a linked list...
        while before_node.next.data != data and before_node.next != None:
            before_node = before_node.next                                  # ...move to the next node

        if before_node.next == None:        # If the linked list is empty or the item doesn't exist...
            print("Item not found")         # ...stop and output an error
            return

        if before_node.data == data:                        # If we found our node...
            before_node.next = before_node.next.next        # ...make the node before our one point to the node after our one

    def print_list(self):
        current_node = self.head            # This will cycle through all items

        if current_node == None:            # If the list is empty, print an appropriate message
            print("None")
            return

        while current_node != None:             # Whilst the list isn't over...
            print(current_node.data)            # ...print the current node...
            current_node = current_node.next    # ..and move to the next node


    # EXTRAS

    def reverse(self):
        curr_node = self.head
        prev_node = None
        next_node = self.head.next

        while next_node != None:
            curr_node.next = prev_node
            prev_node = curr_node

            curr_node = next_node
            next_node = next_node.next

        curr_node.next = prev_node
        prev_node = curr_node

        self.head = prev_node



h = LinkedList()
h.append("A")
h.append("B")
h.append("C")
h.append("D")
h.append("E")
h.reverse()
h.print_list()