class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        whites = 0
        min_cols = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                whites += 1
            if right - left + 1 == k:
                min_cols = min(min_cols, whites)

                if blocks[left] == 'W':
                    whites -= 1
                left += 1
        return min_cols