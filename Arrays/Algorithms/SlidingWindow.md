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
**Finding the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive**
```python
intiate left pointer, total , length = max integer value 
loop through array using right pointer till end of array    
    total += right pointer value
    while total >= target value
        length = minimum of (window length, length) 
        total-= left pointer value
        move left pointer by 1
return 0 if length has hasn't changed else return length of window
```
```python
# Find length of the minimum size subarray where the sum is 
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length
 ```
