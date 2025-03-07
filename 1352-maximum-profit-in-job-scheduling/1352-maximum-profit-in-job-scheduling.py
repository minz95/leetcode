from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1) 
        end_times = [job[1] for job in jobs]

        for i in range(1, len(jobs) + 1):
            curr_profit = jobs[i-1][2]
            last_non_conflicting = bisect_right(end_times, jobs[i-1][0]) - 1
            dp[i] = max(dp[i-1], curr_profit + dp[last_non_conflicting + 1])
            
        return dp[-1]
