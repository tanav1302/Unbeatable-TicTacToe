"""
Tic Tac Toe Player
"""
import math
import json
from pathlib import Path
X = "X"
O = "O"
EMPTY = None
file_path = Path("data.json")
if file_path.is_file():
    with file_path.open('r') as f:
        data = json.load(f)
else:
    data = dict()


def initial_state():
    """
    Returns starting state of the board.
    """
    global data 
    # read json
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num = 0

    for i in board:
        for j  in i:
            if j != EMPTY:
                num = num + 1 
    if num%2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    empty_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_set.add((i,j))
    return empty_set
    


        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = initial_state()
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j] 
    i = action[0]
    j = action[1]
    if new_board[i][j] != EMPTY:
        raise Exception
    
    new_board[i][j] = player(new_board)

    return new_board


            
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        num = 0
        for col_element in  row:
            if col_element == row[0]!= EMPTY:
                num = num +1
        if num == 3:
            return row[0]
        
    for column in range(3):
        num = 0
        for row in  range(3):
            if board[row][column] == board[0][column]!= EMPTY:
                num = num +1
        if num == 3:
            return board[0][column]
        
    if board[0][0] == board[1][1] == board[2][2]!= EMPTY or board[0][2] == board[1][1] == board[2][0]!= EMPTY:
        return board[1][1]
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for col_element in  row: 
            if col_element == EMPTY :
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1 
    if winner_player is None:
        return 0
    return -1

def max(board)-> int:
    if terminal(board):
        return utility(board)
    
    smallest_outcome = 2
    for action in actions(board):
        # print("O- ", action)
        # print("smallest_outcome before ", smallest_outcome)
        outcome = minsub(result(board,action))
        # print("outcome ", outcome)
        if  outcome < smallest_outcome:
            smallest_outcome = outcome
        # print("smallest_outcome after ", smallest_outcome)

    return smallest_outcome

def minsub(board)->int:
    if terminal(board):
        return utility(board)
    
    largest_outcome = -2
    for action in actions(board):
        
        # print("X - ", action)
        # print("largest_outcome before ", largest_outcome)
        outcome = max(result(board,action))
        # print("outcome ", outcome)
        if  outcome > largest_outcome:
            largest_outcome = outcome
        # print("largest_outcome after ", largest_outcome)

    return largest_outcome
            


def min(board)->int:
    if terminal(board):
        return utility(board)
    
    
    largest_outcome = -2
    for action in actions(board):
        print("\n")
        print("X - ", action)
        print("largest_outcome before ", largest_outcome)
        outcome = max(result(board,action))
        print("outcome ", outcome)
        if  outcome > largest_outcome:
            largest_outcome = outcome
        print("largest_outcome after ", largest_outcome)

    return largest_outcome
        
        
def is_empty(board):
    for row in board:
        for coord in row:
            if coord != EMPTY:
                return False
    return True


def minimax(board):
    global data
    """
    Returns the optimal action for the current player on the board.
    """
    print("\n")
    print("-------------------------\n")
    print("\n")
    print("\n")
    print("-------------------------\n")
    print("\n")
    
    board_str = json.dumps(board)
    

    # if is_empty(board):
    #     return (0,0)
    if data.get(board_str):
        return data.get(board_str)

    current_player = player(board)

    

    if current_player == X:
        max_outcome = -2
        ans_action = 0
        for action in actions(board):
            
            
            outcome = max(result(board,action))
            print(" minimaxoutcome ", outcome)
            
            if  outcome > max_outcome:
                max_outcome = outcome
                ans_action = action
            print("minimax largest_outcome after ", max_outcome)
    if current_player == O:
        min_outcome = 2
        ans_action = 0
        for action in actions(board):
            print("\n")
            print("-------------------------\n")
            print("\n")
            print("0 - ",action)
            print("minimax min_outcome before ", min_outcome)
            print("\n")
            outcome = min(result(board,action))
            if  outcome < min_outcome:
                min_outcome = outcome
                ans_action = action
            print("minimax min_outcome after ", min_outcome)
    print(ans_action)
    data[board_str] = ans_action

    return ans_action 