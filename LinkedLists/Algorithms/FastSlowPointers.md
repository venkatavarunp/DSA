# Fast and Slow Pointers (Floyd's tortoise and hare) Algorithm
**Find the middle of a linked list**

It is a variation of two pointers where one pointer is fast pointer (which travels 2x of slow pointer).

middle of linked list is the point at which slow pointer at when fast pointer reaches at the end.
```python
# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```
**Determine if a linked list has a cycle**

Without the use of hashSets which in turn add `O(n)` Space complexity we use fast and slow pointers to detect cycles.

We detect cycles in linked list when slow and fast pointers are at same node.
```python
# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Determine if a linked list has a cycle and return the head**

in addition to cycle detection we use a 2nd slow pointer and we move it in parallel to slow pointer after cycle is detected.when 2nd pointer and slow pointer meet it indicates the head of the cycle.
```python
# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
```
