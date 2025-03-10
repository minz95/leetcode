class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def _is_vowel(c):
            return c in ['a', 'e', 'i', 'o', 'u']
        def vowel_count(word, k):
            total = 0
            start = 0
            end = 0
            vowel_cnt = {}
            consonant_cnt = 0

            while end < len(word):
                n = word[end]
                if _is_vowel(n):
                    vowel_cnt[n] = vowel_cnt.get(n, 0) + 1
                else:
                    consonant_cnt += 1
                while len(vowel_cnt) == 5 and consonant_cnt >= k:
                    total += len(word) - end
                    start_letter = word[start]
                    if _is_vowel(start_letter):
                        vowel_cnt[start_letter] = vowel_cnt.get(start_letter) - 1
                        if vowel_cnt.get(start_letter) == 0:
                            vowel_cnt.pop(start_letter)
                    else:
                        consonant_cnt -= 1
                    start += 1
                end += 1
            return total
        return vowel_count(word, k) - vowel_count(word, k+1)