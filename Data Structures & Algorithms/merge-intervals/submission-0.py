class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]

        index = 1 
        while index < len(intervals):
            last_start = result[-1][0]
            last_end = result[-1][1]

            current_start = intervals[index][0]
            current_end = intervals[index][1]

            if current_start <= last_end:
                # overlap detected 
                result[-1][0] = min(last_start, current_start)
                result[-1][1] = max(last_end, current_end)
            else:
                result.append(intervals[index])
            index += 1
        return result