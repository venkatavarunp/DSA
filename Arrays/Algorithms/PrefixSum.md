# Prefix Sums
Prefix are contigous subarray from the beginning of the array.

Can help to find the sum of subarray with left and right ranges.

**Given an array of values, design a data structure that can query the sum of a subarray of the values**
```python

class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
 ```
