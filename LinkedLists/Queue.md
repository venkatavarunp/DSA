#  Queues
It is an abstract data structure that excutes `FIFO - First in, First out`
- Enqueue is an operation of adding element to the end of the queue
- Dequeue is an operation of removing element from the begining of the queue

| Operation | Big O Time |
|:-- | :--| 
| Enqueue | O(1) |
| Dequeue | O(1) |

Codes for operations on queues 

**Python**
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end ="")
            cur = cur.next
        print() # new line
```
**Javascript**
```javascript
class ListNode {    
    constructor (val) {
        this.val = val;
        this.next = null;
    } 
}

class Queue {

    // Implementing this with dummy nodes would be easier!
    constructor() {
        this.left = null;
        this.right = null;
    }

    enqueue(val) {
        const newNode = new ListNode(val);
        if (this.right != null) {  
        // Queue is not empty 
            this.right.next = newNode;
            this.right = this.right.next;
        } else {       
        // Queue is empty             
            this.left = newNode;
            this.right = newNode;
        }
    }

    dequeue() {
        if (this.left == null) {
        // Queue is empty 
            return;
        }
        // Remove left node and return value
        const val = this.left.val;
        this.left = this.left.next;
        return val;    
    }

    print() {
        let cur = this.left;
        let s = "";
        while(cur != null) {
            s+= cur.val + "->";
            cur = cur.next;
        }
        console.log(s)
    }
}
```
**Java**
```java
public class ListNode {
     int val;
     ListNode next;

     public ListNode(int val) {
         this.val = val;
         this.next = null;
     }
 }

public class Queue {
    ListNode left;  // front of Queue   front -> [1,2,3]
    ListNode right; // back of Queue   [1,2,3] <- back
    
    public Queue() {
        this.left  = null;
        this.right = null;
    }

    public void enqueue(int val) {
        ListNode newNode = new ListNode(val);
        if (this.right != null) {  
        // Queue is not empty 
            this.right.next = newNode;
            this.right = this.right.next;
        } else {       
        // Queue is empty             
            this.left = newNode;
            this.right = newNode;
        }
    }

    public int dequeue() {
        if (this.left == null) {
        // Queue is empty 
            System.exit(0);
        }
        int val = this.left.val;
        this.left = this.left.next;
        return val;
        
    }

    public void print() {
        ListNode cur = this.left;
        while(cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println();
    }

}
```
