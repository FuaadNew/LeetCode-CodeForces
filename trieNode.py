# Each TrieNode represents a character and its children in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.word = False   # Marks the end of a complete word


# Trie class to support insertion, search, and prefix search
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root of the Trie

    # Inserts a word into the Trie
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()  # Create a new node if not present
            curr = curr.children[c]
        curr.word = True  # Mark the end of the word

    # Searches for a complete word in the Trie
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False  # If any character is missing, word isn't in Trie
            curr = curr.children[c]
        return curr.word  # Return True only if it's a complete word

    # Checks if any word in the Trie starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False  # If prefix path breaks, return False
            curr = curr.children[c]
        return True  # All prefix characters matched
