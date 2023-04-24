# Fast and Slow Pointers (Floyd's tortoise and hare) Algorithm
**Find the middle of a linked list**

It is a variation of two pointers where one pointer is fast pointer (which travels 2x of slow pointer).

middle of linked list is the point at which slow pointer at when fast pointer reaches at the end.
```python
```
**Determine if a linked list has a cycle**

Without the use of hashSets which in turn add `O(n)` Space complexity we use fast and slow pointers to detect cycles.

We detect cycles in linked list when slow and fast pointers are at same node.
```python
```
**Determine if a linked list has a cycle and return the head**

in addition to cycle detection we use a 2nd slow pointer and we move it in parallel to slow pointer after cycle is detected.when 2nd pointer and slow pointer meet it indicates the head of the cycle.
```python
```
