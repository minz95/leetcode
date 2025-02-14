class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
        self.prefix_count = 0
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.count += 1
        node.is_end = True
        

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]

        return node.count
        

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count
        

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) == 0:
            return
        node = self.root
        for char in word:
            node = node.children[char]
            node.prefix_count -= 1
        node.count -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)