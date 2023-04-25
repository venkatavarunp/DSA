# Insertion Sort
Sorts the array by dividing it into subarrays and sorts every subarray and increases the sub array.

```python
for(i from 1 to array length):
    j=i-1
    while j>=0 and array[j+1]<array[j]:
        swap array[j+1],array[j]
        j-=1
```
It is a `stable` sorting algorithm
Sorts array in `O(n)` Time.
```python
# Python implementation of Insertion Sort
def insertionSort(arr):
	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them 
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr
```
