class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        l,r=0,n-1
        if l==r and nums[l]==val:
            return 0
        while l<=r:
            print(nums)
            if nums[r]==val:
                r-=1
                continue
            if nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            l+=1
        return r+1
      # can simply be written as nums.remove(val) as well
