class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= lmax:
                    lmax = height[left]
                else:
                    total += (lmax - height[left])
                left += 1
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                else:
                    total += (rmax - height[right])
                right -= 1
        return total