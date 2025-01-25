class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = intervals[i-1]
            if curr[0] < prev[1]:
                return False
        return True