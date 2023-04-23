# Sliding Window

**We will be given an array and we need to return longest subarray, with the same value in each position**

In this case we expand window until same value is present at right pointer
```python
intiate left pointer = 0
loop through right pointer to create a window
    if(value at left pointer != value at right pointer)
        left pointer = right pointer
    calculate length of window and compare with maxvalue of window
return maxvalue of window
```
```python
# Find the length of longest subarray with the same 
# value in each position: O(n)
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length
```
