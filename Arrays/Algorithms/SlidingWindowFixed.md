# Sliding Window - Fixed

**We will be given an array and we need to return true if there are two elements within a window of size k that are equal**

## 1st Way - Brute Force
```python
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
```
