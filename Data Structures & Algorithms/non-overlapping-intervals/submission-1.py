class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        index = 1 
        res = 0

        last_end = intervals[0][1]
        
        while index < len(intervals):
            current_start = intervals[index][0]
            current_end = intervals[index][1]
            if current_start >= last_end:
                # no overlapping 
                last_end = current_end
            else:
                res += 1
                # which one to delete
                # delete the min one
                last_end = min(current_end, last_end)


            index += 1
        return res
