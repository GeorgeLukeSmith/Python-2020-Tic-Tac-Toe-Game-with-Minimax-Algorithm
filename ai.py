import math
import random
import tic_tac_toe as ttt


PLAYER_TOKEN = 1
AI_TOKEN = 2
ROW_NUM = 3
COL_NUM = 3
WINDOW_LEN = 3
EMPTY = 0


def eval_window(window, token):
    opp_token = PLAYER_TOKEN
    if token == PLAYER_TOKEN:
        opp_token = AI_TOKEN
    score = 0
    if window.count(token) == 3:
        score += 100
    elif window.count(token) == 2 and window.count(EMPTY) == 1:
        score += 10
    if window.count(opp_token) == 2 and window.count(EMPTY) == 1:
        score -= 80
    return score


def score_position(matrix, token):
    score = 0
    # Horizontal Score
    for r in range(3):
        row_array = [int(i) for i in list(matrix[r, :])]
        for c in range(3):
            window = row_array[c:c + WINDOW_LEN]
            score += eval_window(window, token)
    # Vertical Score
    for c in range(COL_NUM):
        col_array = [int(i) for i in list(matrix[:, c])]
        for r in range(3):
            window = col_array[r:r + WINDOW_LEN]
            score += eval_window(window, token)
    # Positive gradient Diagonals
    for r in range(1):
        for c in range(1):
            window = [matrix[r + i][c + i] for i in range(WINDOW_LEN)]
            score += eval_window(window, token)
    # Negative gradient diagonals
    for r in range(1):
        for c in range(1):
            window = [matrix[r + 2 - i][c + i] for i in range(WINDOW_LEN)]
            score += eval_window(window, token)
    return score


def get_valid_locations(matrix):
    valid_locations = []
    for r in range(ROW_NUM):
        for c in range(COL_NUM):
            if ttt.check_valid_move(matrix, r, c):
                valid_locations.append(r)
                valid_locations.append(c)

    return valid_locations


def is_terminal_node(matrix):
    return ttt.test_win_state(matrix, PLAYER_TOKEN) \
           or ttt.test_win_state(matrix, AI_TOKEN) or len(get_valid_locations(matrix)) == 0


def minimax(matrix, depth, maximising_player):
    valid_locations = get_valid_locations(matrix)
    terminal_node = is_terminal_node(matrix)
    if depth == 0 or terminal_node:
        if terminal_node:
            if ttt.test_win_state(matrix, AI_TOKEN):
                return None, None, 1000000000000000000
            elif ttt.test_win_state(matrix, PLAYER_TOKEN):
                return None, None, -1000000000000000000
            else:  # No more moves
                return None, None, 0
        else:  # Depth is zero
            return None, None, score_position(matrix, AI_TOKEN)
    if maximising_player:
        value = -math.inf
        arbitrary_choice = random.randrange(0, len(valid_locations), 2)
        row_choice = valid_locations[arbitrary_choice]
        col_choice = valid_locations[arbitrary_choice + 1]
        num_of_possible = len(valid_locations)
        for i in range(0, num_of_possible, 2):
            r = valid_locations[i]
            c = valid_locations[i + 1]
            test_matrix = matrix.copy()
            test_matrix[r][c] = AI_TOKEN
            score = minimax(test_matrix, depth - 1, False)[2]
            if score > value:
                value = score
                row_choice = r
                col_choice = c
        return row_choice, col_choice, value
    else:  # minimising player
        value = math.inf
        arbitrary_choice = random.randrange(0, len(valid_locations), 2)
        row_choice = valid_locations[arbitrary_choice]
        col_choice = valid_locations[arbitrary_choice + 1]
        num_of_possible = len(valid_locations)
        for i in range(0, num_of_possible, 2):
            r = valid_locations[i]
            c = valid_locations[i + 1]
            test_matrix = matrix.copy()
            test_matrix[r][c] = PLAYER_TOKEN
            score = minimax(test_matrix, depth - 1, True)[2]
            if score < value:
                value = score
                row_choice = r
                col_choice = c
        return row_choice, col_choice, value


def choose_ai_move(matrix, token):
    valid_locations = get_valid_locations(matrix)
    high_score = -10000
    try:
        best_move = random.choice(get_valid_locations(matrix))
        num_of_possible = len(valid_locations)
        for i in range(0, num_of_possible, 2):
            r = valid_locations[i]
            c = valid_locations[i + 1]
            test_matrix = matrix.copy()
            test_matrix[r][c] = token
            score = score_position(test_matrix, token)
            if score > high_score:
                high_score = score
                best_move = (r, c)
        return best_move
    except IndexError:
        exit(0)