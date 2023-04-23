# Dynamic Arrays
Helps with fixed size problem from static arrays 

Dynamic arrays are default in `python` as `list` and as `Arrays` in `Javascript`

we need to use `ArrayList` in `java` and `vector` in `c++` to use dynamic arrays

In Dynamic arrays lenght of array is a pointer that points towards last element od array.

If we need to add an element to array if it exceeds the size of array then it is optimal to 
- Allot a new array with 2*size 
- copy old array to new array
now insertion are done with `O(1)` Amortized complexity

| Operation | Big O Time |
|:---| :---|
| Read/Write at i-th Position | O(1) |
| Insert/Deletion End| O(1)|
| Insert/Deletion Middle| O(n)|

Codes for operations on dynamic arrays

**Python**
```python
# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 
        
        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        
    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1
    
    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        # Here we would throw an out of bounds exception

    # Insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception       

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()
```
**Javascript**
```javascript
class DynamicArray {
    constructor() {
        this.capacity = 2;
        this.length = 0;
        this.arr = new Array(2);
    }

    // Insert n in the last position of the array
    pushback(n) {
        if (this.length == this.capacity) {
            this.resize();
        }
               
        // insert at next empty position
        this.arr[this.length] = n;
        this.length++;
    }

    resize() {
        // Create new array of double capacity
        this.capacity = 2 * this.capacity;
        const newArr = new Array(this.capacity); 
        
        // Copy elements to newArr
        for (let i = 0; i < this.length; i++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    } 

    // Remove the last element in the array
    popback() {
        if (this.length > 0) {
            this.length--;
        }  
    }    

    // Get value at i-th index
    get(i) {
        if (i < this.length) {
            return this.arr[i];
        }    
        // Here we would throw an out of bounds exception
        return;
    }    

    // Insert n at i-th index
    insert(i, n) {
        if (i < this.length) {
            this.arr[i] = n;
            return;
        }    
        return;
        // Here we would throw an out of bounds exception  
    } 

    print() {
        let s = "";
        for (let i = 0; i < this.length; i++) {
            s+= this.arr[i] + " ";
        }      
        console.log(s);
    }
}
```
**Java**
```java
public class DynamicArray {
    int capacity;
    int length;;
    int[] arr;

    public DynamicArray() {
        capacity = 2;
        length = 0;
        arr = new int[2];
    }

    // Insert n in the last position of the array
    public void pushback(int n) {
        if (length == capacity) {
            this.resize();
        }
               
        // insert at next empty position
        arr[length] = n;
        length++;
    }

    public void resize() {
        // Create new array of double capacity
        capacity = 2 * capacity;
        int[] newArr = new int[capacity]; 
        
        // Copy elements to newArr
        for (int i = 0; i < length; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }  

    // Remove the last element in the array
    public void popback() {
        if (length > 0) {
            length--;
        }  
    }     

    // Get value at i-th index
    public int get(int i) {
        if (i < length) {
            return arr[i];
        }    
        // Here we would throw an out of bounds exception
        return -1;
    }    

    // Insert n at i-th index
    public void insert(int i, int n) {
        if (i < length) {
            arr[i] = n;
            return;
        }    
        return;
        // Here we would throw an out of bounds exception  
    }        

    public void print() {
        for (int i = 0; i < length; i++) {
            System.out.println(arr[i]);
        }
    }
} 
```
