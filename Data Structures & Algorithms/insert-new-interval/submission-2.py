class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start, new_end = newInterval

        for i, interval in enumerate(intervals):
            start, end = interval
            # if the new interval is less than the start 
            if new_end < start:
                res.append([new_start, new_end])
                return res + intervals[i:]

            # if the new interval is more then the current intervals
            if new_start > end:
                res.append(interval)
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        res.append([new_start, new_end])
        return res
             