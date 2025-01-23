class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, iv in enumerate(intervals):
            if newInterval[1] < iv[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > iv[1]:
                result.append(iv)
            else:
                newInterval = [min(newInterval[0], iv[0]), max(newInterval[1], iv[1])]
            
        result.append(newInterval)
        return result

        