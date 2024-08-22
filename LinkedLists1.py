# การสร้างคลาส Node สำหรับการกำหนดค่า
class Node:
    def __init__(self, data): # 3
        self.data = data
        # self.data = 3
        self.next = None
        # self.next = null
# ประกาศตัวแปร
node1 = Node(3)
node2 = Node(5)
node3 = Node(10)
node4 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4

currentnode = node1

while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next