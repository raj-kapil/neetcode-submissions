"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        for index in range(1, len(intervals)):
            last_meeting_end = intervals[index-1].end
            new_meeting_start = intervals[index].start 
            if new_meeting_start < last_meeting_end:
                return False

        return True
            