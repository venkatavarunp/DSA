# Stack 
Considered as LIFO(Last in, First Out)Abstract Data Structure.

Stack can be implemented using Dynamic Arrays
- Pushing element into the top of the Stack - `Push` 
- Removing element from the top of the Stack - `Pop`
- Looking for the top element - `Peek`

Codes for operations on Stacks

**Python**
```python 
# Implementing a stack is trivial using a dynamic array
# (which we implemented earlier).
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()
```
**Javascript**
```javascript
// Implementing a stack is trivial using a dynamic array
// (which we implemented earlier).
class Stack {
    constructor() {
        this.stack = new Array();                                                                   
    }

    push(n) {
        this.stack.push(n);
    }

    pop() {
        return this.stack.pop();
    }

    size() {
        return this.stack.length;
    }
}
```
**Java**
```java
import java.util.ArrayList;

// Implementing a stack is trivial using a dynamic array
// (which we implemented earlier).
public class Stack {

    ArrayList<Integer> stack = new ArrayList<Integer>();

    public Stack() {   
    }

    public void push(int n) {
        stack.add(n);
    }

    public int pop() {
        return stack.remove(stack.size() - 1);
    }

    public int size() {
        return stack.size();
    }
}
```
