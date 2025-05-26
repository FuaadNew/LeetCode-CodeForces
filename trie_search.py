# Trie node definition
class Trienode():
    def __init__(self):
        self.children = {}
        self.index = -1  # Store index of the word

    # Add combined prefix#suffix into the Trie
    def addWord(self, word, index):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.index = index  # Mark the index at the leaf node

    # Search for the prefix#suffix pattern
    def find(self, prefix_suffix):
        curr = self
        for c in prefix_suffix:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.index

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = Trienode()
        # Insert all combinations of prefix#suffix
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    prefix_suffix = word[:i] + "#" + word[j:]
                    self.root.addWord(prefix_suffix, index)

    # Query function for prefix and suffix
    def f(self, pref: str, suff: str) -> int:
        prefix_suffix = pref + "#" + suff
        return self.root.find(prefix_suffix)
