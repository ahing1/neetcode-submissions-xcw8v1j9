class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_set = defaultdict(set)
        col_set = defaultdict(set)
        for i in range(len(board)):
            row_set = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False
                elif board[i][j] in col_set[j] or board[i][j] in box_set[(i//3, j//3)]:
                    return False
                else:
                    row_set.add(board[i][j])
                    col_set[j].add(board[i][j])
                    box_set[(i//3, j//3)].add(board[i][j])
        
        return True
                
            