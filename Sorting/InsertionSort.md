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
