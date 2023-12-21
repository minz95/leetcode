class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ans = 0

        for i in range(0, len(points)-1):
            width = points[i+1][0]-points[i][0]
            if width > ans:
                ans = width

        return ans