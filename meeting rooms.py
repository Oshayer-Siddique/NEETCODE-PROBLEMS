
from typing import List
import math


print("Meeting Rooms")


# def function(intervals):
#     intervals.sort(key = lambda x : x[0])
#     for i in range(1, len(intervals)):
#         if(intervals[i][0] < intervals[i-1][1]):
#             return False
#     else:
#         return True
    
    

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
