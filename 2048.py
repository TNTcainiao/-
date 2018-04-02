import random
import msvcrt
import os


table = [[0 for i in range(4)] for j in range(4)]

score = 0

def display():
    global score
    os.system("cls")

    print("\r\
          ┌──┬──┬──┬──┐\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          └──┴──┴──┴──┘" \
          % tuple(table_list(table))
          )
    print("     score:",score)


def table_list(table):

    def notzero(num):
        if num == 0:
            return ' '
        else:
            return num

    list = []
    for i in range(4):
        for j in range(4):
            list.append(notzero(table[i][j]))
    return list


def random_num(table):
    size = 1
    for i in range(4):
        for j in range(4):
            if table[i][j] == 0:
                size = 0

    if size == 0:

        while size < 1:
            row = random.randrange(0,4)
            column = random.randrange(0,4)
            if table[row][column] == 0:
                table[row][column] = 2 if random.randrange(0,4) > 0 else 4
                size += 1
    else:
        print("you are stupid！！！")
        os.system("pause")



def left(table):

    def row_deal(list):
        global score
        size = 1
        while size == 1:
            size = 0
            for i in range(1,4):

                if list[i-1] == 0 and list[i] != 0:
                    list[i-1] = list[i]
                    list[i] = 0
                    size = 1
                if list[i-1]!= 0 and list[i-1] == list[i]:
                    list[i-1] = 2 * list[i-1]
                    score += 1
                    list[i] = 0
                    size = 1


    for i in range(4):
        row_deal(table[i])


def right(table):

    def row_deal(list):
        global score
        size = 1
        while size == 1:
            size = 0
            for i in range(1,4):

                if list[4-i] == 0 and list[3-i] != 0:
                    list[4-i] = list[3-i]
                    list[3-i] = 0
                    size = 1
                if list[4-i]!= 0 and list[4-i] == list[3-i]:
                    list[4-i] = 2 * list[4-i]
                    score += 1
                    list[3-i] = 0
                    size = 1


    for i in range(4):
        row_deal(table[i])

def up(table_copy):
    global table
    table_trans = translate(table_copy)

    left(table_trans)

    table = translate(table_trans)

def down(table_copy):
    global table
    table_trans = translate(table_copy)

    right(table_trans)

    table = translate(table_trans)


def translate(table):
    table_trans = []
    table_trans_list = []
    for i in range(4):
        for j in range(4):
            table_trans_list.append(table[j][i])
        table_trans.append(table_trans_list)
        table_trans_list = []

    return table_trans

def init_game():
    global table
    table = [[0 for i in range(4)] for j in range(4)]
    random_num(table)

    display()


def main():
    init_game()

    while True:

        event = msvcrt.getch()

        if event == b'a':
            left(table)
            random_num(table)
            display()

        if event == b'd':
            right(table)
            random_num(table)
            display()

        if event == b'w':
            up(table)
            random_num(table)
            display()

        if event == b's':
            down(table)
            random_num(table)
            display()


main()



