from random import randint


def field(coord):
    print(f"---------\n"
          f"| {coord[1][3]} {coord[2][3]} {coord[3][3]} |\n"
          f"| {coord[1][2]} {coord[2][2]} {coord[3][2]} |\n"
          f"| {coord[1][1]} {coord[2][1]} {coord[3][1]} |\n"
          f"---------")


def isoccupied(abscissa, ordinate):
    if cells[position[f"{abscissa} {ordinate}"]] != " ":
        return True


def update(array):
    matrix = [[],
              [0, array[6], array[3], array[0]],
              [0, array[7], array[4], array[1]],
              [0, array[8], array[5], array[2]]
              ]
    field(matrix)
    if check_win(matrix, "X"):
        print("X wins")
        exit()
    elif check_win(matrix, "O"):
        print("O wins")
        exit()
    elif not (" " in array):
        print("Draw")
        exit()


def check_win(grid, player):
    if grid[1][1] == player and grid[1][2] == player and grid[1][3] == player:
        return True
    elif grid[2][1] == player and grid[2][2] == player and grid[2][3] == player:
        return True
    elif grid[3][1] == player and grid[3][2] == player and grid[3][3] == player:
        return True
    elif grid[1][1] == player and grid[2][1] == player and grid[3][1] == player:
        return True
    elif grid[1][2] == player and grid[2][2] == player and grid[3][2] == player:
        return True
    elif grid[1][3] == player and grid[2][3] == player and grid[3][3] == player:
        return True
    elif grid[1][1] == player and grid[2][2] == player and grid[3][3] == player:
        return True
    elif grid[1][3] == player and grid[2][2] == player and grid[3][1] == player:
        return True
    else:
        return False


def move(char):
    try:
        x, y = list(map(int, input("Enter the coordinates: ").strip().split(" ")))
    except ValueError:
        print("You should enter numbers!")
        move(char)
    else:
        if 1 <= x <= 3 and 1 <= y <= 3:
            if isoccupied(x, y):
                print("This cell is occupied! Choose another one!")
                move(char)
            else:
                cells[position[f"{x} {y}"]] = char
        else:
            print("Coordinates should be from 1 to 3!")
            move(char)


def easy_move(char, to_print=True):
    if to_print:
        print('Making move level "easy"')
    while True:
        x, y = randint(1, 3), randint(1, 3)
        if not isoccupied(x, y):
            cells[position[f"{x} {y}"]] = char
            break


def med_move(char, to_print=True):
    global moved
    moved = False
    if to_print:
        print('Making move level "medium"')
    if char == "X":
        for index, i in enumerate(cells):
            if i == " ":
                cells[index] = "O"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "O"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
        if not moved:
            easy_move(char, to_print=False)
    elif char == "O":
        for index, i in enumerate(cells):
            if i == " ":
                cells[index] = "X"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "X"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
        if not moved:
            easy_move(char, to_print=False)


def hard_move(char):
    global moved
    moved = False
    print('Making move level "hard"')
    if char == "X":
        for index, i in enumerate(cells):
            if i == " ":
                cells[index] = "X"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "X"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
                cells[index] = "O"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "O"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
        if not moved:
            easy_move(char, to_print=False)
    elif char == "O":
        for index, i in enumerate(cells):
            if i == " ":
                cells[index] = "O"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "O"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
                cells[index] = "X"
                matrix = [[],
                          [0, cells[6], cells[3], cells[0]],
                          [0, cells[7], cells[4], cells[1]],
                          [0, cells[8], cells[5], cells[2]]
                          ]
                if check_win(matrix, "X"):
                    cells[index] = char
                    moved = True
                    break
                else:
                    cells[index] = " "
        if not moved:
            easy_move(char, to_print=False)


player_one_char = "X"
player_two_char = "O"
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
position = {"1 1": 6, "1 2": 3, "1 3": 0, "2 1": 7, "2 2": 4, "2 3": 1, "3 1": 8, "3 2": 5, "3 3": 2}
moves = {"easy": easy_move, "medium": med_move, "hard": hard_move, "user": move}
moved = None

if __name__ == "__main__":
    print("""
Welcome to the game of TIC-TAC-TOE

* There are three difficulty level easy, medium and hard.
* To play the game enter: start [player 1] [player 2]
* To play with your friend: start user user
* To play with AI enter player 1 or player 2 as easy or medium or hard and other player as user: start user easy
* To exit the game: exit  
    """)
    while True:
        menu = input("Input command: ").strip()
        if menu == "exit":
            exit()
        elif menu.split(" ")[0] == "start":
            try:
                player_one, player_two = menu.split(" ")[1], menu.split(" ")[2]
                if player_one and player_two not in moves:
                    print("Bad parameters!")
            except IndexError or Exception:
                print("Bad parameters!")
            else:
                break
        else:
            print("Bad parameters!")
    while True:
        update(cells)
        func = moves[player_one]
        func(player_one_char)
        update(cells)
        func = moves[player_two]
        func(player_two_char)
