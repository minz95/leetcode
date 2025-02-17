from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def help():
            total = 0
            for ch in count:
                if count[ch] > 0:
                    count[ch] -= 1
                    total += 1 + help()
                    count[ch] += 1
            return total
        return help()