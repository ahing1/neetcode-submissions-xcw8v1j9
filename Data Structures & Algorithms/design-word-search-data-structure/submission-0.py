class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        def dfs(root, i):
            if not root:
                return False
            if i == len(word):
                return root.isEnd
            
            if word[i] == ".":
                for child in root.children:
                    if dfs(root.children[child], i+1):
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(root.children[word[i]], i+1)
        
        return dfs(cur, 0)