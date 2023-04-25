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
```python
arr = [1, 3, 3, 4, 5, 6, 7, 8]

# Python implementation of Binary Search
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1
```
