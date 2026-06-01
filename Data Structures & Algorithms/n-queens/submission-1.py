class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        negDia = set() # (r - c)
        posDia = set() # (r + c)

        def backtrack(r):

            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDia or (r - c) in negDia:
                    continue
                
                cols.add(c)
                posDia.add(r + c)
                negDia.add(r - c)

                board[r][c] = "Q"
                backtrack(r + 1)

                cols.remove(c)
                posDia.remove(r + c)
                negDia.remove(r - c)
                board[r][c] = "."

            
        backtrack(0)
        return res