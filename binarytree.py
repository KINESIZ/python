#โครงสร้างข้อมูลแบบ Tree
class TreeNode: #สร้าง Function การกำหนดค่า
    def __init__(self,data): 
        self.data = data
        self.left = None
        self.right = None

# การเก็บข้อมูลลงโครงสร้างแบบ Tree 
rootnode = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('Peerapong')
# การกำหนด Edge หรือ กิ่ง
rootnode.left = nodeA
rootnode.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeE.left = nodeH

nodeF.right = nodeG

print(rootnode.data)
print(rootnode.right.data)
print(rootnode.right.left.data)
print(rootnode.right.left.left.data)

