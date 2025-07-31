class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_index():
            l, r = 0, len(nums)

            while l < r:
                m = l + (r - l) //2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l #first index

        def last_index():
            l, r = 0, len(nums)

            while l < r:
                m = l + (r - l) //2

                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l - 1 # last index

        start = first_index()
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = last_index()
        return [start, end]


        

            
        
