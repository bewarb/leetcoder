class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i in range(len(intervals)):
            starts.append([intervals[i][0], i]) # [start_time, original_index]
        starts.sort()  # Sort by start time
        
        result = []

        for interval in intervals:
            target = interval[1]
            l, r = 0, len(intervals)

            while l < r:
                m = (l + r) // 2
                if starts[m][0] < target:
                    l = m + 1
                else: 
                    r = m
            
            if l < len(starts):
                result.append(starts[l][1])
            else:
                result.append(-1)

        return result




