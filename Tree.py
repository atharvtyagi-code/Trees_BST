class Node():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def insert(root, key):
    if root == None:
        return Node(key)
    
    elif root.value > key:
        root.left = insert(root.left, key)

    elif root.value < key:
        root.right = insert(root.right, key)
        
    return root

def search(root, key):
    if root.value == key:
        return root
    
    elif root.value > key and root.left != None:
        return search(root.left, key)
    
    elif root.value < key and root.right != None:
        return search(root.right, key)
    
    else:
        print("The key does NOT exist in the tree!")

def traversal(root):
    if root != None:
        if root.left != None:
            traversal(root.left)

        print(root.value)
        
        if root.right != None:
            traversal(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


n = int(input("How many datas in the tree: "))
root = None

for i in range(n):
    key = int(input("Enter the value: "))
    root = insert(root, key)

traversal(root)
num = int(input("Enter the key value to the search: "))
key_Node = search(root, num)
print(key_Node.value)