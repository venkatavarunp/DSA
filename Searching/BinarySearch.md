# Binary Search
Works only when the input is in sorted order

It runs in `O(logn)` Time Complexity and `O(1)` Space Complexity.

```python
def binarySearch(array,target):
    left,right=0,array length-1
    while left <= right:
        mid=(left+right)//2
        if target>array[mid]:
            left=mid+1
        else if target<array[mid]:
            right=mid-1
        else:
            return mid
    return -1
```
