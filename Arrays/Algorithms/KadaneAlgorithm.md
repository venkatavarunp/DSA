# Kadane's Algorithm
It is similar to two pointers, sliding window algorithms 

It is technically Dynamic Programming and a Greedy Algorithm.

**We will be given an array and we need to find a `non-empty subarray` with largest sum.**
- If array consists of all negative values then we will return the smallest negative value.

## 1st Way - Brute Force
```python
# Brute Force: O(n^2)
def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum
```
## 2nd Way - Kadane's Algorithm
We use a window to calculate the current sum of the window and if the sum of the window turns as negative we discard that sum and start to calculate the new sum as there is no use adding negative sum to the next values.
```python
Create winsowsum and maxsum variabales
loop through every element of array using for loop
    if(windowsum negative)
        make windowsum = 0
        add element to windowsum
    if(windowsum>maxsum)
        assign maxsum=windowsum
return maxsum
```
```python
# Kadane's Algorithm: O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum
```
## 3rd Way - Adding sliding window technique
In this with addition to 2nd way we update left and right pointers to know the sub array indexes.
```python
# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]
```
