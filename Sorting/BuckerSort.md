# Bucket Sort
Used when the range of values to be sorted is very low
```python
def quickSort(array,start,end):
    array=[2,1,2,0,0,2]
    counts=[0,0,0]
    for i from 0 to arr length:
        counts[n]+=1
    i=0
    for n from o to counts length:
        for j from o to counts[n]:
            array[i]=n
            i+=1
```
It is a `Unstable` sorting algorithm
Sorts array in `O(n)` Time and `O(c)` space complexity
```python
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```
