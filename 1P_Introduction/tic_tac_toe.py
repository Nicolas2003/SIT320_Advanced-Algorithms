import math

board = {"human": [False, False, False, False, False, False, False, False, False],
         "bot": [False, False, False, False, False, False, False, False, False]}

possible_wins = {1: [True, True, True, False, False, False, False, False, False],
                 2: [False, False, False, True, True, True, False, False, False],
                 3: [False, False, False, False, False, False, True, True, True],
                 4: [True, False, False, True, False, False, True, False, False],
                 5: [False, True, False, False, True, False, False, True, False],
                 6: [False, False, True, False, False, True, False, False, True],
                 7: [True, False, False, False, True, False, False, False, True],
                 8: [False, False, True, False, True, False, True, False, False]
                 }


def user_play(board, player_type):
    position = int(input("Which square do you want to place? "))  # Choose between 0 and 8
    if position < 0 or position > 8:
        print("Choose between 0 and 8.")
        user_play(board, player_type)
    elif occupied(board, position):
        print("This square is already occupied.")
        user_play(board, player_type)
    else:
        board[player_type][position] = True


def is_winner(players_position):
    for win in possible_wins.values():
        if match(players_position, win):
            return True
    return False


def match(positions, required):
    match = 0
    for index in range(0, len(positions)):
        if positions[index] and required[index]:
            match = match + 1

    return match == 3

def occupied(board, position):
    return (board["human"][position] or board["bot"][position])


def empty_spaces(human, bot):
    spaces = []
    for i in range(0, 9):
        if (human[i] == False) and (bot[i] == False):
            spaces.append(i)


    return spaces

def occupied_spaces(human, bot):
    occupied = []
    for i in range(0, len(human) and len(bot)):
        if human[i] or bot[i]:
            print("Space is occupied")
            occupied.append(i)

    return occupied


def print_board(human, bot):
    for row in range(3):
        line = []
        for col in range(3):
            i = 3 * row + col
            if bot[i]:
                line.append("X")
            elif human[i]:
                line.append("O")
            else:
                line.append("-")
        print(" | ".join(line))
        if row < 2:
            print("--+---+--")

def minimax(human, bot, depth, is_maximizing_player):
    # Base cases: check for terminal states (win, lose, draw)
    if is_winner(bot):
        return 10 - depth, None # Prioritize faster wins
    if is_winner(human):
        return depth - 10, None # Prioritize blocking losses that are further away
    if empty_spaces(human, bot) == []:
        return 0, None

    best_score = -math.inf
    best_move = None

    if is_maximizing_player:
        for move in empty_spaces(human, bot):
            bot[move] = True
            score, _ = minimax(human, bot, depth + 1, False)
            bot[move] = False

            if score > best_score:
                best_score = score
                best_move = move
    else:
        best_score = math.inf
        for move in empty_spaces(human, bot):
            human[move] = True
            score, _ = minimax(human, bot, depth + 1, True)
            human[move] = False
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move

def main():
    print_board(board["human"], board["bot"])
    running = True

    while running:
        user_play(board, "human")

        score, move = minimax(board["human"], board["bot"], 0, True)
        if move != None:
            board["bot"][move] = True

        print_board(board["human"], board["bot"])

        if is_winner(board["human"]):
            print("Congrats human! You win!")
            running = False
        elif is_winner(board["bot"]):
            print("Congrats bot! You win!")
            running = False
        elif move is None:
            print("It was a draw, GG")
            running = False

main()