class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Validate Rows - create a set when checking dupl
        for i in range(9): # 9 as there is 9 rows
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    # checks for dupl
                    return False
                elif item != '.':
                    s.add(item)


        # Validate Columns - same thing
        for i in range(9): # 9 as there is 9 cols
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    # checks for dupl
                    return False
                elif item != '.':
                    s.add(item)

        # Validate Boxes
        # find the starting points
        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i,j in starts:
            s = set()
            for row in range(i,i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
        