class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board),len(board[0])
        visit = set()
        self.root = TrieNode()
        
        for word in words:
            self.root.addWord(word)
        res = set()

        

        
        
        def dfs(r,c,word,curr):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in curr.children):
                return 
            
            visit.add((r,c))
            word+=board[r][c]
            curr = curr.children[board[r][c]]

            if curr.word:
                res.add(word)
        
            dfs(r+1,c,word,curr)
            dfs(r-1,c,word,curr)
            dfs(r,c+1,word,curr)
            dfs(r,c-1,word,curr)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,"",self.root)

        return list(res)
            
            







