from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        colors = defaultdict(int)
        colorset = set()
        balls = {}

        for i, q in enumerate(queries):
            b, color = q[0], q[1]
            if b in balls:
                if balls[b] != color:
                    colors[balls[b]] -= 1
                    if colors[balls[b]] == 0:
                        colorset.remove(balls[b])
                    colors[color] += 1
            else:
                colors[color] += 1
            balls[b] = color
            colorset.add(color)
            result.append(len(colorset))
        return result 