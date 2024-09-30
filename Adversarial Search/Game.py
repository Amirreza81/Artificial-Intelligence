import pygame
import numpy as np
import random
from Board import BoardUtility

ROWS = 6
COLS = 6
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SQUARESIZE = 100


class Game:
    def __init__(self, player1, player2, graphics=True):
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((ROWS, COLS))

        # GUI
        if graphics:
            pygame.init()
            self.width = COLS * SQUARESIZE
            self.height = (ROWS + 1) * SQUARESIZE
            self.circle_radius = int(SQUARESIZE / 2 - 5)
            self.screen = pygame.display.set_mode((self.width, self.height))
            self.font = pygame.font.SysFont(None, 24)

    def draw_board(self):
        pygame.time.wait(500)
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(self.screen, BLUE,
                                 (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                if self.board[r][c] == 0:
                    pygame.draw.circle(self.screen, BLACK, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                        self.circle_radius)
                elif self.board[r][c] == 1 or self.board[r][c] == 2:
                    pygame.draw.circle(self.screen, RED if self.board[r][c] == 1 else YELLOW, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                        self.circle_radius)
        pygame.display.update()

    def start_game(self):
        turn = random.randint(0, 1)
        print('player1 is red. player2 is yellow.')
        print(f'player{turn + 1} goes first.')
        self.draw_board()
        run = True
        win = 0
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            print(f'player{turn + 1} move:')
            if turn == 0:
                player_move = self.player1.play(self.board)
                print(player_move)
                row = player_move[0][0]
                col = player_move[0][1]
                region = player_move[1]
                rotation = player_move[2]
                BoardUtility.make_move(self.board, row, col, region, rotation, 1)
            elif turn == 1:
                player_move = self.player2.play(self.board)
                print(player_move)
                row = player_move[0][0]
                col = player_move[0][1]
                region = player_move[1]
                rotation = player_move[2]
                BoardUtility.make_move(self.board, row, col, region, rotation, 2)
            self.draw_board()

            if BoardUtility.has_player_won(self.board, 1 if turn == 1 else 2):
                print(f"PLAYER {1 if turn == 1 else 2} WINS!")
                win = 1 if turn == 1 else 2
                pygame.time.wait(70000)
                # run = False
                break
            if BoardUtility.has_player_won(self.board, 2 if turn == 1 else 1):
                print(f"PLAYER {2 if turn == 1 else 1} WINS!")
                win = 2 if turn == 1 else 1
                pygame.time.wait(7000)
                # run = False
                break

            if BoardUtility.is_draw(self.board):
                win = -1
                print("NO ONE WON DRAW!")
                pygame.time.wait(7000)
                # run = False
                break
            # pygame.time.wait(7000)
            turn = 0 if turn == 1 else 1
        pygame.quit()
        return win
