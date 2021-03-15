import time
import sys

titles = "    A   B   C\n"
init_board = "| / | / | / |\n"
A, B, C = 4, 8, 12
# creates the game board
board = [f"{x} {init_board}" for x in range(3)]
brod = "test"
user_turn = ""
taken = True
winner = False
turn_number = 0
# keeps the score and determines what symbols will be used
symbols = ["x", "o"]
winner_save = [list(x * 3) for x in symbols]
score = {symbol: 0 for symbol in symbols}
# adds the vertical row keys to the game boards
whole_board = titles + "".join(board)

# does all the background logic to the game
class logic:
    def __init__(self, ctx, turn, win_template):
        self.ctx = ctx
        self.turn = turn
        self.template = win_template

    # check if 3 of the same symbols are in a line
    def winner_check(self):
        # initializes the list containing the rows. rows 0, 1, and 2 are created
        win_check = [
            [board[c][x] for x in range(4, len(board[c])) if x % 4 == 0]
            for c in range(3)
        ]
        # adds the values for every possible row to the list
        for x in range(3):
            win_check.append([win_check[c][x] for c in range(3)])
        win_check.append([win_check[x][x] for x in range(3)])
        win_check.append([win_check[x][c] for x, c in zip(range(3)[::-1], range(3))])
        # determines if someone has won
        for x in win_check:
            if x in self.template:
                print(f"{self.turn} wins!")
                keep = True
                break
            keep = False
        return keep

    # updates the spot value of the given input. ex: input = A1, spot A1 will be occupied by the player
    def take_spot(self):
        append_board = board[int(user[1])]
        append_board = "".join(
            [
                append_board[x] if x != eval(user[0]) else self.turn
                for x in range(len(append_board))
            ]
        )
        return append_board

    # checks to see if a spot on the board is already occupied
    def spot_taken(self):
        board_ctx = board[int(self.ctx[1])][eval(self.ctx[0])]
        check_spot = True if board_ctx in ["o", "x"] else False
        if check_spot == True:
            print("spot already taken :/ try again")
        return check_spot


# takes the location input and checks if it exists
def input_check():
    slow_print("location- \n")
    ctx = input().upper()
    all_input = [x + str(c) for x in ["A", "B", "C"] for c in range(3)]
    if ctx in all_input:
        pass
    else:
        while ctx not in all_input:
            slow_print("invalid location, try again\n")
            slow_print("location- \n")
            ctx = input().upper()
    return list(ctx)


# takes an input and prints it smoothly to the console
def slow_print(inpt):
    for x in inpt:
        sys.stdout.write(x)
        time.sleep(0.01)


slow_print(titles + "".join(board))

# determines what symbol will go first
while True:
    slow_print(f"{symbols[0]}'s or {symbols[1]}'s?- \n")
    user_turn = input()
    if user_turn in [symbols[0], symbols[1]]:
        slow_print(f"{user_turn}'s first!\n")
        break
    else:
        slow_print("incorrent input try again!")

# brings all the functions and logic together
while True:
    outcome = "None"
    while winner == False:
        # keeps track of the amount of turns to determine if the outcome is a tie
        turn_number += 1
        if turn_number == 10:
            slow_print("Tie!\n")
            outcome = None
            break
        # takes spot input and brings the spot_taken logic together to determines==
        # whether a spot is already occupied
        while taken == True:
            user = input_check()
            init = logic(user, user_turn, winner_save)
            taken = init.spot_taken()
        ctx_board = init.take_spot()
        board[int(user[1])] = ctx_board
        slow_print(titles + "".join(board))
        user_turn = symbols[0] if user_turn != symbols[0] else symbols[1]
        taken = True
        winner = init.winner_check()
    # makes sure the point is given to the winner by inverting the current user_turn
    if outcome == None:
        pass
    else:
        score[symbols[0] if user_turn == symbols[1] else symbols[1]] += 1
    slow_print(
        f"Scores: {symbols[0]}-{score[symbols[0]]}, {symbols[1]}-{score[symbols[1]]}\n"
    )
    slow_print("Would you like to play another (Y/N)?- \n")
    repeat = input().upper()
    if repeat == "Y":
        winner = False
        board = [f"{x} {init_board}" for x in range(3)]
        turn_number = 0
        continue
    else:
        break
