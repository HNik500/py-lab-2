def is_safe(board,row,col,q):
    for i in range(row):
        if board[i]==col:
            return False
        if board[i]-i==col-row or board[i]+i==col+row:
            return False
    return True

def solve_nqueen(board,row,q):
    if row==len(board):
        print(board)
        return
    for col in range (q):
        if is_safe(board,row,col,q):
            board[row]=col
            solve_nqueen(board,row+1,q)
            board[row]=-1


def n_queen(q):
    board=[-1]*q
    solve_nqueen(board,0,q)
q=int(input("Enter number of queen:"))
n_queen(q)




def solve_n_queens(n):
    board = [-1] * n
    found = False 
    def safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    def backtrack(row):
        nonlocal found
        if row == n:
            print(board)
            found = True
            return
        for col in range(n):
            if safe(row, col):          
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  
    backtrack(0)
    if not found:
        print("No solution exists")
solve_n_queens(4)


