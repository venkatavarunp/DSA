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
```
