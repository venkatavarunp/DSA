# Quick Sort
Same as Merge sort but instead of spliting array into two we make use of a pivot value and make sure that elements on the left of pivot are smaller than pivot element and right of pivot are greater than the pivot element.

After we achieve the above case we divide the array to two halfs from pivot and repeat the process untill the whole array is sorted.
```python
def quickSort(array,start,end):
    if(end-start+1<=1):
        return array
    pivot=array[end]
    left=start
    # Partition: elements smaller than pivot ob the left side
    for i from start to end:
        if(array[i]<pivot):
            swap array[left],array[i]
            left+=1
    # Moving pivot in between left and right sides
    array[end]=array[left]
    array[left]=pivot
    quickSort(array,start,left-1)
    quickSort(array,left+1,end)
    return array
```
It is a `Unstable` sorting algorithm
Sorts array in `O(nlogn)` Time and `O(n2)` in worst cases.
```python
# Implementation of QuickSort
def quickSort(arr, s, e):
    if e - s + 1 <= 1:
        return

    pivot = arr[e]
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot
    
    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
```
