# การทำ Binary Search Tree 

# สร้าง Class สำหรับการกำหนดค่าข้อมูล
class TressNode :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# กำหนดโครงสร้างข้อมูลแบบ BST
root = TressNode(13)
node7 = TressNode(7)
node15 = TressNode(15)
node3 = TressNode(3)
node8 = TressNode(8)
node14 = TressNode(14)
node19 = TressNode(19)
node18 = TressNode(18)

# การกำหนด Edge หรือ กิ่ง
root.left = node7
root.right = node15
node7.left = node3
node7.right = node8
node15.left = node14
node15.right = node18
node18.right = node19
# สร้าง Function สำหรับการค้นหา
def search(node, target):
    #ถ้าค่าที่ส่งเข้ามาเป็นค่าว่างให้ส่งกลับ
    if node is None:
        return None
    #ถ้าสิ่งที่รับเข้ามามีค่าเท่ากับ Root Node 
    elif node.data == target:
        return node
    # ถ้าสิ่งที่รับเข้ามามีค่าน้อยกว่า
    elif target < node.data:
        return search(node.left,target)
    elif target > node.data:
        return search(node.right,target)
# การค้นหาหรือการ Search
result = search(root,target = int(input()))

if result:
    print('Found')
else:
    print('Not Found')
