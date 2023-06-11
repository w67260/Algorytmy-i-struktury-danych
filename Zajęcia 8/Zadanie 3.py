class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    merged_head = Node(None)
    current = merged_head

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1

    if head2:
        current.next = head2

    return merged_head.next


head1 = Node(1)
node2 = Node(3)
node3 = Node(5)
head1.next = node2
node2.next = node3

head2 = Node(2)
node4 = Node(4)
node5 = Node(6)
head2.next = node4
node4.next = node5

current = head1
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

current = head2
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

merged_head = merge_sorted_lists(head1, head2)

current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")