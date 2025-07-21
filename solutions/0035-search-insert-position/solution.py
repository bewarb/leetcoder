class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        #upper bound
        while l < r:  
            m = l + (r - l) // 2  

            if nums[m] < target:  
                l = m + 1  
            else:  
                r = m  

        #lower
        if nums[l] < target:
            return l + 1
        else:
            return l
