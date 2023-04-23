#  Doubly Linked Lists
We can traverse in two directions using doubly linked list where we will be having address of `previous` as well to traverse
| | Arrays | Linked Lists |
|:-- | :--| :-- |
| Operation | Big O Time | Big O Time |
| Access ith Element | O(1) | O(n) |
| Insert / Delete End | O(1) | O(1) |
| Insert / Delete Middle | O(n) | O(1) |

Codes for Doubly Linked Lists operations

**Python**
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()
```
**JavaScript**
```javascript
class DoublyListNode {    
    constructor (val) {
        this.val = val;
        this.next = null;
    } 
}

// Implementation for Doubly Linked List
class DoublyLinkedList {
    constructor() {
        // Init the list with 'dummy' head and tail nodes which makes 
        // edge cases for insert & remove easier.
        this.head = new DoublyListNode(-1);
        this.tail = new DoublyListNode(-1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    insertFront(val) {
        const newNode = new DoublyListNode(val);
        newNode.prev = this.head;
        newNode.next = this.head.next;
        
        this.head.next.prev = newNode;
        this.head.next = newNode;
    }

    insertEnd(val) {
        const newNode = new DoublyListNode(val);
        newNode.next = this.tail;
        newNode.prev = this.tail.prev;
        
        this.tail.prev.next = newNode;
        this.tail.prev = newNode;
    }

    // Remove first node after dummy head (assume it exists)
    removeFront() {
        this.head.next.next.prev = this.head;
        this.head.next = this.head.next.next;
    }  

    // Remove last node before dummy tail (assume it exists)
    removeEnd() {
        this.tail.prev.prev.next = this.tail;
        this.tail.prev = this.tail.prev.prev;
    }   

    print() { 
        let curr = this.head.next;
        let s = "";
        while (curr != this.tail) {
            s+= curr.val + "->";     
            curr = curr.next;
        }
        console.log(s);
    }
}
```
**Java**
```java
public class DoublyLinkedListNode {
    
    int val;
    DoublyLinkedListNode next;
    DoublyLinkedListNode prev;

    public DoublyLinkedListNode(int val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

// Implementation for Doubly Linked List
public class DoublyLinkedList {
    DoublyLinkedListNode head;
    DoublyLinkedListNode tail;

    public DoublyLinkedList() {
        head = new DoublyLinkedListNode(-1);
        tail = new DoublyLinkedListNode(-1);
        head.next = tail;
        tail.prev = head;
    }

    public void insertFront(int val) {
        DoublyLinkedListNode newNode = new DoublyLinkedListNode(val);
        newNode.prev = head;
        newNode.next = head.next;
        
        head.next.prev = newNode;
        head.next = newNode;
    }

    public void insertEnd(int val) {
        DoublyLinkedListNode newNode = new DoublyLinkedListNode(val);
        newNode.next = tail;
        newNode.prev = tail.prev;
        
        tail.prev.next = newNode;
        tail.prev = newNode;
    }

    public void removeFront() {
        head.next.next.prev = head;
        head.next = head.next.next;
    }   

    public void removeEnd() {
        tail.prev.prev.next = tail;
        tail.prev = tail.prev.prev;
    }   
    
    public void print() {
        DoublyLinkedListNode curr = head.next;
        while (curr != tail) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }           
        System.out.println();
    }
}
```
