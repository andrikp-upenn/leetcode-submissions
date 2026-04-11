class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Valid Sudoku:
        INPUTS: Given 9x9 board

        Rules:
        1. Each row must contain the digits 1-9 without duplicates
        2. Each column must contain the digit 1-9 without duplicates
        3. Each of the nine 3x3 sub-boxes of the grid must contain the digits
        1-9 without duplicates

        OUTPUTS: 
        bool --> true if Sudoku board is valid, otherwise --> false

        Constraints:
        board.length == 9
        board[i].length == 9
        board[i][j] is a digit 1-9 or '.'.
        """

        # Before thinking of DS, what needs to happen.
        # 9 rows x 9 cols without duplicates --> can be brute forced with nested for loops (not recommended)
        # build a hashmap with each row & col as an key, with the value 1-9 ex: 1,1 --> num --> 1,2 --> num
        # no row,col pair can be duplicates 
        # no 3x3 sub-boxes can be duplicates


        row = {}# Only checking for duplicates
        col = {} 
        sub_box = {}
        
        # Build a set for each row,col and sub_box and check duplicates
        for i in range(9):
            row[i] = set()
            col[i] = set()

        for i in range(3):
            for j in range(3):
                sub_box[(i,j)] = set()

        for i in range(len(board)):
            for j in range(len(board)):
                # i --> row of board
                # j --> col of board
                # board[i,j] --> value @ i,j
                val = board[i][j]

                # Sub_box upper-left corner
                row_idx = i//3 # idx of curr row block
                col_idx = j//3 # idx of curr col block

                if val == '.':
                    continue 
                # If the value exists (repeats) in either i,j or sub_box --> false
                if val in row[i] or val in col[j] or val in sub_box[(row_idx, col_idx)]:
                    return False
                else:
                    # Value has not been seen yet, add it to set
                    row[i].add(val)
                    col[j].add(val)
                    sub_box[row_idx, col_idx].add(val)
    
        return True # no duplicates found --> return True

            

                



        