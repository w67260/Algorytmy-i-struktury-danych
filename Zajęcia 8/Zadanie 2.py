class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_ith_node(head, i):
    if i == 1:
        return head.next
    curr = head
    prev = None
    count = 1
    while curr and count < i:
        prev = curr
        curr = curr.next
        count += 1
    if curr:
        prev.next = curr.next
    return head


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

head = remove_ith_node(head, 3)

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")