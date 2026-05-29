class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0 

        last_end = intervals[0][1]

        index = 1
        while index < len(intervals):
            current_start = intervals[index][0]
            current_end = intervals[index][1]

            if current_start >= last_end:
                # no overlap 
                last_end = current_end 
            else:
                # there is a overlap 
                count += 1

                last_end = min(current_end, last_end)
            index += 1
        return count 
