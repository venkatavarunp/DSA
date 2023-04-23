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
