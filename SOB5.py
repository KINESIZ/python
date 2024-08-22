class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# ประกาศตัวแปร
node1 = Node(3)
node2 = Node(5)
node3 = Node(10)
node4 = Node(15)

# เชื่อมโยงโหนดแบบ Circular Linked List
node1.next = node2
node1.prev = node4

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("จากต้นไปท้าย (วนกลับที่โหนดแรก):")
currentnode = node1
while True:
    print(currentnode.data)
    currentnode = currentnode.next
    if currentnode == node1:  
        break

print(">>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<")

print("จากท้ายไปต้น (วนกลับที่โหนดสุดท้าย):")
currentnode = node4
while True:
    print(currentnode.data)
    currentnode = currentnode.prev
    if currentnode == node4:  
        break