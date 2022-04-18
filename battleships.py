"""This is a game simulator of battleships that is on a grid size of 10 with 8 different ships you have 50 bullets to win the game  A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down

    i learnt how to code this with youtube as all i got from asking for help was youtube videos that was brocken english or not help from my mantor as when i told him what i was doing or what i wanted to do all i got back was i do not understand you

        """
        #legend
        #x is placing a ship and hit ship
        #' ' for available space to placed
        #'_' missed shot
from random import randint

HIDDEN_BOARD = [[' '] * 10 for x in range(10)]
GUESS_BOARD = [[' '] * 10 for x in range(10)]

letters_to_numbers ={
  'A':0, 
  'B':1, 
  'C':2, 
  'D':3, 
  'E':4, 
  'F':5, 
  'G':6, 
  'H':7, 
  'I':8,
  'J':9}

def print_board(board):
  print(' A B C D E F G H I J')
  print(' -------------------')
  row_number = 1
  for row in board:
    print('%d|%s|' % (row_number,'|'.join(row)))
  row_number += 1


def create_ships(board):
  for ship in range(8):
    ship_row, ship_column = randint(0,9), randint(0,9)
    while board[ship_row][ship_column] == "x":
      ship_row, ship_column = randint(0,9), randint(0,9)
      board[ship_row][ship_column] ='x'

def get_ship_location():
  row = input('pleas enter ship row 1-10')
  while row not in '12345678910':
    print('please enter a valid rows')
    row = input('pleas enter ship row 1-10')
    column = input("Enter the column of the ship: ").upper()
  while column not in "ABCDEFGHIJ":
    print('please enter a valid column')
    column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns =  10
while turns > 0:
  print('welcome to my game')
  print_board(GUESS_BOARD)
  row, column = get_ship_location()
  if GUESS_BOARD [row] [column] == '_':
    print('you have tried there')
  elif HIDDEN_BOARD [row] [column] == 'x':
    print('hit')
    GUESS_BOARD[row][column] = "x"
    turns -= 1
  else:
    print('missed')
    GUESS_BOARD[row][column] = "-"   
    turns -= 1 
    if count_hit_ships(GUESS_BOARD) == 8:
            print("You win!")
            break
    print('You have ' + str(turns) + 'turns left')
    if turns == 0:
            print('You ran out of turns gave over')
