import random
import msvcrt
import os


board = [[0 for i in range(12)] for j in range(12)]
snack = []
food = [0,0]
direction = 0


def init_board(board):
    for row_numer in range(12):
        if row_numer == 0 or row_numer == 11:
            board[row_numer] = [1 for i in range(12)]
        else:
            board[row_numer] = [1,0,0,0,0,0,0,0,0,0,0,1]


def init_snack(snack):
    global direction
    row = random.randrange(3,9)
    col = random.randrange(3,9)
    direction = random.randrange(0,4)

    snack.append([row, col])
    if direction == 0:
        snack.append([row + 1, col])
        snack.append([row + 2, col])
    if direction == 1:
        snack.append([row - 1, col])
        snack.append([row - 2, col])
    if direction == 2:
        snack.append([row, col + 1])
        snack.append([row, col + 2])
    if direction == 3:
        snack.append([row, col - 1])
        snack.append([row, col - 2])

def random_food(board):
    global food
    size = 0
    while size == 0:
        i = random.randrange(1,11)
        j = random.randrange(1,11)
        if board[i][j] == 0:
            food = [i,j]
            board[i][j] = 3
            size = 1

def update_snack(snack,board):
    for i,j in snack:
        board[i][j] = 2

def move_snack(snack,board,food):

    if direction == 0:
        i,j = snack[0]
        head = [i-1,j]

        for body in snack:
            if head == body:
                print("you are stupid！！！")
                os.system("pause")

        if head[0] == 0:
            print("you are stupid！！！")
            os.system("pause")
        elif head == food:
            snack.insert(0, head)
            random_food(board)
        else:
            snack.insert(0,head)
            tail = snack.pop(-1)
            board[tail[0]][tail[1]] = 0


    if direction == 1:
        i, j = snack[0]
        head = [i + 1, j]
        for body in snack:
            if head == body:
                print("you are stupid！！！")
                os.system("pause")
        if head[0] == 11:
            print("you are stupid！！！")
            os.system("pause")
        elif head == food:
            snack.insert(0, head)
            random_food(board)
        else:
            snack.insert(0,head)
            tail = snack.pop(-1)
            board[tail[0]][tail[1]] = 0

    if direction == 2:
        i, j = snack[0]
        head = [i, j - 1]
        for body in snack:
            if head == body:
                print("you are stupid！！！")
                os.system("pause")
        if head[1] == 0:
            print("you are stupid！！！")
            os.system("pause")
        elif head == food:
            snack.insert(0, head)
            random_food(board)
        else:
            snack.insert(0,head)
            tail = snack.pop(-1)
            board[tail[0]][tail[1]] = 0


    if direction == 3:
        i, j = snack[0]
        head = [i, j + 1]
        for body in snack:
            if head == body:
                print("you are stupid！！！")
                os.system("pause")
        if head[1] == 11:
            print("you are stupid！！！")
            os.system("pause")
        elif head == food:
            snack.insert(0, head)
            random_food(board)
        else:
            snack.insert(0,head)
            tail = snack.pop(-1)
            board[tail[0]][tail[1]] = 0

    update_snack(snack,board)

def view_board(board):

    def deal_number(number):
        if number == 0:
            return '  '
        if number == 1:
            return '★'
        if number == 2:
            return '■'
        if number == 3:
            return '○'

    board_list = []

    for i in range(12):
        for j in range(12):
            board_list.append(deal_number(board[i][j]))

    return board_list

def init():

    init_board(board)
    init_snack(snack)
    update_snack(snack,board)
    random_food(board)

    display()

def game():
    global direction
    init()

    while True:
        event = 0
        while event == 0:

            event = msvcrt.getch()

            if event == b'a':

                direction = 2

            if event == b'd':
                direction = 3

            if event == b'w':
                direction = 0

            if event == b's':
                direction = 1


        move_snack(snack,board,food)
        display()



def display():
    os.system("cls")
    print("\r\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n\
            %s%s%s%s%s%s%s%s%s%s%s%s\n" % tuple(view_board(board)))

game()

