class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and value >= current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

sorted_list = SortedList()

sorted_list.insert(5)
sorted_list.insert(2)
sorted_list.insert(8)
sorted_list.insert(1)
sorted_list.insert(4)

sorted_list.display()