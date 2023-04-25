# Merge Sort
Sorts the array by dividing Array into two havles and goes on and on until we can't split them anymore and then merge them in sorting order

```python
def mergeSort(array,start,end):
    # to check whether we have reached divided array into single elements
    if(end-start+1<=1):
        return array
    mid=(start+end)/2
    mergeSort(array,start,mid)
    mergeSort(array,mid+1,end)
    merge(array,start,mid,end)
    return array
```
It is a `stable` sorting algorithm
Sorts array in `O(nlogn)` Time.
```python
# Implementation of MergeSort
def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    m = (s + e) // 2

    # Sort the left half
    mergeSort(arr, s, m)

    # Sort the right half
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    merge(arr, s, m, e)
    
    return arr

# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
```
