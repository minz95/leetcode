class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        dp = {}
        
        def dfs(position, jump):
            if (position, jump) in dp:
                return dp[(position, jump)]
            if position == stones[-1]:
                return True
            if jump <= 0 or position not in stone_set:
                return False

            for step in (jump - 1, jump, jump + 1):
                if step > 0 and dfs(position + step, step):
                    dp[(position, jump)] = True
                    return True
            dp[(position, jump)] = False
            return False

        if 1 not in stone_set:
            return False
        return dfs(1, 1)