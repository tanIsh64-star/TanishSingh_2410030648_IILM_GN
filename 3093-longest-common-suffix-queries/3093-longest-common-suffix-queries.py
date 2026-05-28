class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        self.words = wordsContainer
        self.root = TrieNode()

        # Insert all words into reversed trie
        for i, word in enumerate(wordsContainer):
            self.insert(word, i)

        # Answer queries
        ans = []
        for q in wordsQuery:
            ans.append(self.query(q))

        return ans

    def better(self, a, b):
        # Return True if index a is better than b
        if b == -1:
            return True

        if len(self.words[a]) != len(self.words[b]):
            return len(self.words[a]) < len(self.words[b])

        return a < b

    def insert(self, word, idx):
        node = self.root

        # Update root best index
        if self.better(idx, node.best_idx):
            node.best_idx = idx

        # Insert reversed word
        for ch in reversed(word):
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            if self.better(idx, node.best_idx):
                node.best_idx = idx

    def query(self, word):
        node = self.root

        for ch in reversed(word):
            if ch not in node.children:
                break

            node = node.children[ch]

        return node.best_idx