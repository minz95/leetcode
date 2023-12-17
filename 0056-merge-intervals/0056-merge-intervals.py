class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp_arr = intervals
        idx = 0
        while idx < len(temp_arr) - 1:
            c = temp_arr[idx]
            n = temp_arr[idx + 1]
            if n[0] <= c[1]:
                temp_arr = temp_arr[:idx] + [[min(c[0], n[0]), max(c[1], n[1])]] + \
                            temp_arr[idx + 2:]
            else:
                idx += 1
                
        return temp_arr
    