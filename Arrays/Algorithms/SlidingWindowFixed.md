# Sliding Window - Fixed

**We will be given an array and we need to return true if there are two elements within a window of size k that are equal**

## 1st Way - Brute Force
```python
# Check if array contains a pair of duplicate values,
# where the two duplicates are no farther than k positions from 
# eachother (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
# O(n * k)
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False

```
## 2nd Way - Sliding Window - Fixed
We use `hashSets` to find duplicates in the window 
```python
Create a hashSet for the window
if(window size greater than k)
    remove left most element of window
if (the element we add to the window exist in the hashSet)
    return true
else 
    add element to hashSet
return false if we haven't found 
```
```python
# Same problem using sliding window.
# O(n)
def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False
```
