from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        time = []
        for obj in intervals:
            time.append((obj.start, 1))
            time.append((obj.end, -1))

        time.sort(key=lambda i: (i[0], i[1]))

        count = 0
        maxCount = 0
        for t in time:
            count += t[1]
            maxCount = max(maxCount, count)

        return maxCount
