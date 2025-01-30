class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        start, end = 0, len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                count += 1
                start += 1
                end -= 1
            else:
                count += 1
                end -= 1
        return count