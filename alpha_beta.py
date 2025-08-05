import math
import time

# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board =[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    """prints current state of board """
    for i in range(len(board)):
            print(f"{board[i][0]}  {board[i][1]}  {board[i][2]}")
    


def is_winner(board, player):
    """Checks if the given player has won."""
    # for checking rows
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    
    #for checking diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    
    return False

def is_full(board):
    """returns True if the board is full else false"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    """ Minimax algorithm to evaluate board positions two option ,set depth level heuristic
      ,or continue till game end ,return best score  """
    # add conditon beta less than equal to alpha both for minimizer (USER) and maximizer (ai)  and where condition meets break the loop 
    global node_count
    node_count += 1
    if is_winner(board, 'O'): 
        return 10 - depth 
    if is_winner(board, 'X'):
        return depth - 10  
    if is_full(board):
        return 0  

    if is_maximizing:  # AI's turn (maximize score)
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '  
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)  
                    if beta <= alpha:
                        break  

        return best_score
    
    else:  # Player's turn (minimize score)
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '  
                    best_score = min(best_score, score)
                    beta = min(beta, best_score) 
                    
                    if beta <= alpha:
                        break  

        return best_score 

def best_move():
    """finds and returns the best move for the AI using the minimax function ,
      while calling minimax ,set alpha to minus infinty and beta to positive infinity."""
    global node_count
    node_count = 0  
    start_time = time.time() 
    best_score = -math.inf
    move = (-1,-1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  
                score = minimax(board, 0, False,-math.inf,math.inf)  
                board[i][j] = ' ' 
                
                if score > best_score:  
                    best_score = score
                    move = (i, j)

    if move:  
        board[move[0]][move[1]] = 'O'

    end_time = time.time()  
    execution_time = end_time - start_time
    print(f"AI Move Completed: Nodes explored = {node_count}, Time taken = {execution_time:.5f} seconds")

def main():
    """Main game loop."""
    # print board
    global PLY_DEPTH
    PLY_DEPTH = 3
    print_board(board)
    while True:
        # take input , user move 
        row, col = map(int, input("Enter row and column for index with space ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move! enter input again.")
            continue
        
        print_board(board)
        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        best_move()
        print_board(board)
        
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
main()