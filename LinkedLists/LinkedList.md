# Linked Lists
Linked lists are similar to array but they are non linear and non contigous data strucure.

Linked Lists is an object that encapsulates minimum of two things
- Value of list node
- next listnode address

By using next listnode address we can connect the lists together to form a linked list.

**Python**
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr:
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, ' -> ')
            curr = curr.next
        print()
  ```
  **Javascript**
  ```javascript
  class ListNode {    
    constructor (val) {
        this.val = val;
        this.next = null;
    } 
}

class LinkedList {
    constructor() {
        // Init the list with a 'dummy' node which makes 
        // removing a node from the beginning of list easier.
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    insertEnd(val) {
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next; 
    }

    remove(index) {
        let i = 0;
        let curr;
        curr = this.head;
        while(i < index && curr != null) {
            i++;
            curr = curr.next;
        }

        // Remove the node ahead of curr
        if (curr != null) {
            curr.next = curr.next.next;
        }
    }

    print() { 
        let curr = this.head.next;
        let s = "";
        while (curr != null) {
            s+= curr.val + "->";     
            curr = curr.next;
        }
        console.log(s);
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

// Implementation for Singly Linked List
public class SinglyLinkedList {
    ListNode head;
    ListNode tail;

    public SinglyLinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    public void insertEnd(int val) {
        tail.next = new ListNode(val);
        tail = tail.next; 
    }

    public void remove(int index) {
        int i = 0;
        ListNode curr = head;
        while (i < index && curr != null) {
            i++;
            curr = curr.next;
        }
        
        // Remove the node ahead of curr
        if (curr != null) {
            curr.next = curr.next.next;
        }
    }

    public void print() {
        ListNode curr = head.next;
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }

        System.out.println();
    }
    
}
```
