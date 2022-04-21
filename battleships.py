"""This is a game simulator of battleships that is on a grid size of 9 with 5 different ships you have 17 turns to win to win the game  A ship cannot be placed diagonally, so if a shot hits the rest of
the ship is in one of 4 directions, left, right, up, and down

i learnt how to code this with youtube as all i got from asking for help was youtube videos that was brocken english or not help from my mantor as when i told him what i was doing or what i wanted to do all i got back was i do not understand you
"""
from ast import Try
from calendar import c
import random
from re import A
import re

length_of_ships = [2, 3, 3, 4, 5, ]
Player_Board = [[" "] * 9 for i in range(9)]
computer_board = [[" "] * 9 for i in range(9)]
Player_guess_Board = [[" "] * 9 for i in range(9)]
computer_guess_board = [[" "] * 9 for i in range(9)]
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3,"E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, }


def print_board(board):
    print(" A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def place_ships(board):
    for ship_length in length_of_ships:
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(
                    ["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_ship_fits(ship_length, row, column, orientation):
                    if check_overlaps(board, ship_length, row, column, orientation) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                                break
                    else:
                        place_ship = True
                        print('place the ship with a length of' + str(ship_length))
                        row, column, orientation = user_input(place_ship)
                        if check_ship_fits(ship_length, row, column, orientation):
                            if check_overlaps(board, ship_length, row, column,) == False:
                                if orientation == "H":
                                    for i in range(column, column + ship_length):
                                        board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[column][i] = "X"
                                    print_board(Player_Board)
                                    break


def check_ship_fits(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True


def check_overlaps(board, ship_length, row, column, orientation):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
        else:
            for i in range(row, row + ship_length):
                if board[i][column] == "X":
                    return True
            return False


def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try:
                row = input("Enter the row 1-9 of the ship: ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-9')
        while True:
            try:
                if column in 'ABCDEFGHIJ':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-J')
            return row, column, orientation

    else:
        while True:
            try:
                row = input("Enter the row 1-9 for the ship: ")
                if row in '123456789':
                    row = int(row) - 1
                    break
            except KeyError:
                print('Enter a valid number between 1 and 9')
        while True:
            try:
                column = input("Enter the column of the ship").upper()
                if column in 'ABCDEFGHIJ':
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A to J')
        return row, column


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
                return count


def turn(board):
    if board == Player_guess_Board:
        row, column = user_input(Player_guess_Board)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif computer_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif Player_Board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


place_ships(computer_board)
print_board(computer_board)
print_board(Player_Board)
place_ships(Player_Board)

while True:
    #player
    while True:
        print('guess a ship location')
        print_board(Player_guess_Board)
        turn(Player_guess_Board)
        break
    if count_hit_ships(Player_guess_Board) == 17:
        print("player win!")
        #computer
    while True:
        print('guess a ship location')
        print_board(computer_guess_board)
        turn(computer_guess_board)
        break
    if count_hit_ships(computer_guess_board) == 17:
        print("computer win.")
        break