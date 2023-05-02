# Binary Trees
![image](https://user-images.githubusercontent.com/130353146/235651628-1b6e29bc-b45f-41c6-b0d8-25ebba2b9545.png)

In the above example
- node `2` is called as `root` and node `1`,`3` are children of it
- nodes `4`,`3` are called as leaf nodes as they don;t have any children 
- for the node `4` the node `1` is called as parent and nodes `1`,`2` are called as ancestors nodes.
- the height of of node `2` in the tree will be 2 and for node `1` that will be 1 
- the depth of node `2` in the tree will be 0 and for node `1` that will be 1
# Binary Search Trees (BST)
they are same as binary trees but they use sorted property

![image](https://user-images.githubusercontent.com/130353146/235653882-92fb08e0-4058-4653-9dc0-d09b1dc45bb3.png)

the sorted property is **the elements of left sub tree of a every single node is always less than the node value and the elements of the right sub tree of a every single node is always greater than the node value**

By arranging the tree in BST form we can easily search for the values as the searching operation takes `O(h)` where `h` is `height of the tree`

Removing and adding the elements in BST is complex when compared to searching and takes `O(n)`
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
```
## Insertion & Deletion
codes for insertion and deletionj opeartions in BST
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root
```

## Depth First Search

we traverse from root to leaf nodes in this way to find the element and we can do it in three ways
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```
## Breadth First Search
in this method we travel in level wise from root to last level and we make use of `queue` to achieve this
```python
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
  ```
