class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            rows = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rows:
                    rows.add(board[i][j])
                else:
                    return False
        
        for i in range(m):
            cols = set()
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in cols:
                    cols.add(board[j][i])
                else:
                    return False
        
        boxes = defaultdict(set)
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in boxes[(i//3, j//3)]:
                    boxes[(i//3, j//3)].add(board[i][j])
                else:
                    return False
        
        return True