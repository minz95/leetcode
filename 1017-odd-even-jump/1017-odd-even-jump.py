class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def jump(sorted_indices):
            n = len(arr)
            res = [None] * n
            stack = []

            for i in sorted_indices:
                while stack and stack[-1] < i:
                    res[stack.pop()] = i
                stack.append(i)
            return res

        n = len(arr)
        if n == 1:
            return 1

        si = sorted(range(n), key=lambda x: (arr[x], x))
        sii = sorted(range(n), key=lambda x: (-arr[x], x))

        odd_jumps = jump(si)
        even_jumps = jump(sii)

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n-2, -1, -1):
            if odd_jumps[i] is not None:
                odd[i] = even[odd_jumps[i]]
            if even_jumps[i] is not None:
                even[i] = odd[even_jumps[i]]
        
        return sum(odd)
            