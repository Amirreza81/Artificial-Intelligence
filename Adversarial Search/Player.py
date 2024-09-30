import copy
import math

from Board import BoardUtility
import random


class Player:
    def __init__(self, player_piece):
        self.piece = player_piece

    def play(self, board):
        return 0


class RandomPlayer(Player):
    def play(self, board):
        return [random.choice(BoardUtility.get_valid_locations(board)), random.choice([1, 2, 3, 4]),
                random.choice(["skip", "clockwise", "anticlockwise"])]


class HumanPlayer(Player):
    def play(self, board):
        move = input("row, col, region, rotation\n")
        move = move.split()
        print(move)
        return [[int(move[0]), int(move[1])], int(move[2]), move[3]]


class MiniMaxPlayer(Player):
    def __init__(self, player_piece, depth=5):
        super().__init__(player_piece)
        self.depth = depth
        self.piece = player_piece

    def play(self, board):
        row = -1
        col = -1
        region = -1
        rotation = -1
        # Todo: implement minimax algorithm
        children = BoardUtility.get_valid_locations(board)
        alpha = -1 * math.inf
        beta = math.inf
        value = -1 * math.inf

        for child in children:
            for help_region in range(1, 5):
                for help_rotation in ["clockwise", "anticlockwise", "skip"]:
                    help_board = copy.deepcopy(board)
                    help_row = child[0]
                    help_col = child[1]
                    BoardUtility.make_move(help_board, help_row, help_col, help_region, help_rotation, self.piece)
                    help_value = minimax_value(self.depth - 1, alpha, beta, help_board, self.piece, False)

                    if help_value > value:
                        row = help_row
                        col = help_col
                        region = help_region
                        rotation = help_rotation
                        value = help_value

                    alpha = max(alpha, help_value)
                    if beta < alpha:
                        return [[row, col], region, rotation]

        return [[row, col], region, rotation]


class MiniMaxProbPlayer(Player):
    def __init__(self, player_piece, depth=5, prob_stochastic=0.1):
        super().__init__(player_piece)
        self.depth = depth
        self.prob_stochastic = prob_stochastic

    def play(self, board):
        row = -1
        col = -1
        region = -1
        rotation = -1
        # Todo: implement minimaxProb algorithm
        alpha = -1 * math.inf
        beta = math.inf
        value = -1 * math.inf
        children = BoardUtility.get_valid_locations(board)
        for child in children:
            for help_region in range(1, 5):
                for help_rotation in ["clockwise", "anticlockwise", "skip"]:
                    help_board = copy.deepcopy(board)
                    help_row = child[0]
                    help_col = child[1]
                    BoardUtility.make_move(help_board, help_row, help_col, help_region, help_rotation, self.piece)
                    help_value = minimax_value(self.depth - 1, alpha, beta, help_board, self.piece, False)

                    if help_value > value:
                        row = help_row
                        col = help_col
                        region = help_region
                        rotation = help_rotation
                        value = help_value

        random_choice = [random.choice(BoardUtility.get_valid_locations(board)), random.choice([1, 2, 3, 4]),
                         random.choice(["clockwise", "anticlockwise", "skip"])]
        best_choice = [[row, col], region, rotation]
        return \
            random.choices([random_choice, best_choice], weights=[self.prob_stochastic, (1 - self.prob_stochastic)],
                           k=1)[0]


def evaluation_function(board, piece, depth):
    if BoardUtility.has_player_won(board, 1 if piece == 2 else 2):
        return -99999999999
    if BoardUtility.has_player_won(board, piece):
        return 99999999999

    noa1 = 0
    noa1 += counting_adjacency(board, piece, depth)
    noa2 = 0
    noa2 += counting_adjacency(board, 1 if piece == 2 else 2, depth)

    nom1 = 0
    nom1 += calculating_value(board, piece, depth)
    nom2 = 0
    nom2 += calculating_value(board, 1 if piece == 2 else 2, depth)

    return nom1 + noa1 - nom2 - noa2


def calculating_value(board, piece, depth):
    n = 0

    if board[1][1] == piece:
        n += 1
    if board[1][4] == piece:
        n += 1
    if board[4][1] == piece:
        n += 1
    if board[4][4] == piece:
        n += 1
    if n == 4:
        return 24 - depth
    return 3 * n - depth


def counting_adjacency(board, piece, depth):
    noa1 = 0
    for col in range(5):
        for row in range(6):
            if board[row][col] == piece and board[row][col + 1] == piece:
                noa1 += 2

    # checking vertically
    for col in range(6):
        for row in range(5):
            if board[row][col] == piece and board[row + 1][col] == piece:
                noa1 += 2

    # checking diagonally
    for col in range(5):
        for row in range(6):
            if row == 0:
                continue
            if board[row][col] == piece and board[row - 1][col + 1] == piece:
                noa1 += 1
    # checking diagonally
    for col in range(6):
        for row in range(6):
            if row == 0 or col == 0:
                continue
            if board[row][col] == piece and board[row - 1][col - 1] == piece:
                noa1 += 1

    return noa1


def how_to_win(board, piece, depth):
    n = 0
    for col in range(0, 3):
        for row in range(0, 3):
            if board[col][row] == piece and board[col + 1][row + 1] == piece and board[col + 2][row + 2] == piece and \
                    board[col + 3][row + 3] == piece:
                n += 1

    for col in range(6):
        for row in range(0, 3):
            if board[col][row] == piece and board[col][row + 1] == piece and board[col][row + 2] == piece and \
                    board[col][row + 3] == piece:
                n += 1

    for col in range(0, 3):
        for row in range(6):
            if board[col][row] == piece and board[col + 1][row] == piece and board[col + 2][row] == piece and \
                    board[col + 3][row] == piece:
                n += 1

    return n / 2


def minimax_value(depth, alpha, beta, board, piece, is_maximizing):
    if depth == 0 or BoardUtility.is_terminal_state(board):
        return evaluation_function(board, piece, depth)
    if not is_maximizing:
        value = math.inf
        children = BoardUtility.get_valid_locations(board)
        for child in children:
            for help_region in range(1, 5):
                for help_rotation in ["clockwise", "anticlockwise", "skip"]:
                    help_board = copy.deepcopy(board)
                    help_row = child[0]
                    help_col = child[1]
                    BoardUtility.make_move(help_board, help_row, help_col, help_region, help_rotation, piece)
                    help_value = minimax_value(depth - 1, alpha, beta, help_board, piece, True)
                    value = min(help_value, value)
                    beta = min(help_value, beta)
                    if beta <= alpha:
                        return value
    else:
        value = -1 * math.inf
        children = BoardUtility.get_valid_locations(board)
        for child in children:
            for help_region in range(1, 5):
                for help_rotation in ["clockwise", "anticlockwise", "skip"]:
                    help_board = copy.deepcopy(board)
                    help_row = child[0]
                    help_col = child[1]
                    BoardUtility.make_move(help_board, help_row, help_col, help_region, help_rotation, piece)
                    help_value = minimax_value(depth - 1, alpha, beta, help_board, piece, False)
                    value = max(help_value, value)
                    alpha = max(help_value, beta)
                    if beta <= alpha:
                        return value
    return value
