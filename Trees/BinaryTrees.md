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
