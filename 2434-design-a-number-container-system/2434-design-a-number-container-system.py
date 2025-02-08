from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.indices = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        if index in self.numbers:
            prev = self.numbers[index]
            self.indices[prev].remove(index)
        self.numbers[index] = number
        self.indices[number].append(index)

    def find(self, number: int) -> int:
        if number in self.indices and len(self.indices[number]) > 0:
            self.indices[number].sort()
            return self.indices[number][0]
        else:
            return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)