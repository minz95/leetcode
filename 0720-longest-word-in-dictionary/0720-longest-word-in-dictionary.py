class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        dp = set()

        result = []
        max_len = 0
        for w in words:
            dp.add(w)
            for i in range(len(w)):
                if all(w[:k] in dp for k in range(1, len(w))):
                    if max_len < len(w):
                        max_len = len(w)
                        result = [w]
                    elif max_len == len(w):
                        result.append(w)
        result.sort()
        if result:
            return result[0]
        return ""