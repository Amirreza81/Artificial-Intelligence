import numpy as np
import copy
import time
ROWS = 6
COLS = 6


class BoardUtility:

    @staticmethod
    def rotate_region(game_board, region, rotation):
        if rotation == "skip":
            return
        copy_board = copy.deepcopy(game_board)
        c_row = 1 if region < 3 else 4
        c_col = 1 if region % 2 == 1 else 4

        if rotation == "clockwise":
            game_board[c_row-1][c_col-1] = copy_board[c_row+1][c_col-1]
            game_board[c_row-1][c_col]   = copy_board[c_row][c_col-1]
            game_board[c_row-1][c_col+1] = copy_board[c_row-1][c_col-1]
            game_board[c_row+1][c_col-1] = copy_board[c_row+1][c_col+1]
            game_board[c_row+1][c_col]   = copy_board[c_row][c_col+1]
            game_board[c_row+1][c_col+1] = copy_board[c_row-1][c_col+1]
            game_board[c_row][c_col-1]   = copy_board[c_row+1][c_col]
            game_board[c_row][c_col+1]   = copy_board[c_row-1][c_col]

        elif rotation == "anticlockwise":
            game_board[c_row+1][c_col-1]  = copy_board[c_row-1][c_col-1]
            game_board[c_row][c_col-1] = copy_board[c_row-1][c_col]
            game_board[c_row-1][c_col-1]  = copy_board[c_row-1][c_col+1]
            game_board[c_row+1][c_col+1]  = copy_board[c_row+1][c_col-1]
            game_board[c_row][c_col+1] = copy_board[c_row+1][c_col]
            game_board[c_row-1][c_col+1]  = copy_board[c_row+1][c_col+1]
            game_board[c_row+1][c_col] = copy_board[c_row][c_col-1]
            game_board[c_row-1][c_col] = copy_board[c_row][c_col+1]
        return

    @staticmethod
    def make_move(game_board, row, col, region, rotation, piece):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """
        assert game_board[row][col] == 0
        game_board[row][col] = piece
        time.sleep(50)
        BoardUtility.rotate_region(game_board, region, rotation)

    @staticmethod
    def is_location_full(game_board, row, col):
        return game_board[row][col] != 0

    @staticmethod
    def get_next_open_row(game_board, col):
        """
        returns the first empty row in a column from the top.
        useful for knowing where the piece will fall if this
        column is played.
        """
        for r in range(ROWS - 1, -1, -1):
            if game_board[r][col] == 0:
                return r

    @staticmethod
    def has_player_won(game_board, player_piece):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        # checking horizontally
        for c in range(2):
            for r in range(ROWS):
                if game_board[r][c] == player_piece and game_board[r][c + 1] == player_piece and game_board[r][
                        c + 2] == player_piece and game_board[r][c + 3] == player_piece and game_board[r][c + 4] == player_piece:
                    return True

        # checking vertically
        for r in range(2):
            for c in range(COLS):
                if game_board[r][c] == player_piece and game_board[r + 1][c] == player_piece and game_board[r + 2][
                        c] == player_piece and game_board[r + 3][c] == player_piece and game_board[r + 4][c] == player_piece:
                    return True

        # checking diagonally
        for c in range(COLS - 4):
            for r in range(4, ROWS):
                if game_board[r][c] == player_piece and game_board[r - 1][c + 1] == player_piece and game_board[r - 2][
                    c + 2] == player_piece and \
                        game_board[r - 3][c + 3] == player_piece and game_board[r - 4][c + 4] == player_piece:
                    return True

        # checking diagonally
        for c in range(4, COLS):
            for r in range(4, ROWS):
                if game_board[r][c] == player_piece and game_board[r - 1][c - 1] == player_piece and game_board[r - 2][
                    c - 2] == player_piece and \
                        game_board[r - 3][c - 3] == player_piece and game_board[r - 4][c - 4] == player_piece:
                    return True

        return False

    @staticmethod
    def is_draw(game_board):
        return not np.any(game_board == 0)

    @staticmethod
    def score_position(game_board, piece):
        """
        compute the game board score for a given piece.
        you can change this function to use a better heuristic for improvement.
        """
        score = 0
        if BoardUtility.has_player_won(game_board, piece):
            return 100_000_000_000  # player has won the game give very large score
        if BoardUtility.has_player_won(game_board, 1 if piece == 2 else 2):
            return -100_000_000_000  # player has lost the game give very large negative score

        # todo score the game board based on a heuristic.

        return score

    @staticmethod
    def get_valid_locations(game_board):
        """
        returns all the valid columns to make a move.
        """
        valid_locations = []
        for row in range(ROWS):
            for column in range(COLS):
                if not BoardUtility.is_location_full(game_board, row, column):
                    valid_locations.append([row, column])

        return valid_locations

    @staticmethod
    def is_terminal_state(game_board):
        """
        return True if either of the player have won the game or we have a draw.
        """
        return BoardUtility.has_player_won(game_board, 1) or BoardUtility.has_player_won(game_board,
                                                                                         2) or BoardUtility.is_draw(
            game_board)
