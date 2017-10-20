### *** Example Battleship ***

## Simplified version of Battleship game for one player

# Initialize board to an empty list
board = []

# Create a 5x5 board game with "O" inside
for i in range(5):
  board.append(['O'] * 5)

# Print the board as a grid 5x5
def print_board(board_in):
  # row gives you the row
  for row in board:
    print row
    
print_board(board)

# Remove the "" in the board with " ".join(row)
def print_board(board_in):
  for row in board:
    print " ".join(row)
    
print_board(board)

# Hide the ships in the board with randit() function
# Define the random_row/col functions
from random import randint

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# @debug the game
# print ship_row
# print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    # If success then go out of the game
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)
    
    

