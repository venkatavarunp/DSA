# Kadane's Algorithm
It is similar to two pointers, sliding window algorithms 

It is technically Dynamic Programming and a Greedy Algorithm.

**We will be given an array and we need to find a `non-empty subarray` with largest sum.**
- If array consists of all negative values then we will return the smallest negative value.

## 1st Way - Brute Force
```python
```
## 2nd Way - Kadane's Algorithm
We use a window to calculate the current sum of the window and if the sum of the window turns as negative we discard that sum and start to calculate the new sum as there is no use adding negative sum to the next values.
```python
```
## 3rd Way - Adding sliding window technique
In this with addition to 2nd way we update left and right pointers to know the sub array indexes.
```python
```
