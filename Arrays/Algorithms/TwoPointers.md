# Two Pointers 
Difference between two pointer and sliding window algorithm is that **In two pointer algorithm we care about the value at the two pointers where as in sliding window we carea about whole window**

**Check if an array is a Palindrome**


```python
intiate left pointer = 0, right pointer = length of array-1
while left pointer < right pointer
    if left pointer value != right pointer
        return false
    increase left pointer by 1
    decrease right pointer by 1
    return true
```
```python
# Find the length of longest subarray with the same 
# value in each position: O(n)
def isPalindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False 
        L+=1
        R-=1
    return True
```
**Given a sorted input array, return the two indices of two elements which sum up to target value.**
```python
intiate left pointer = 0, right pointer = length of array-1
while left pointer < right pointer
    if left pointer value + right pointer > target
        right pointer-=1
    else if left pointer value + right pointer <target
        left pointer+=1
    else:
        return left pointer,right pointer
```
```python
# Given a sorted array of integers, return the
#indices of two elements that sum up to the  target value
def targetSum(nums,target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1 
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L,R]
