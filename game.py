import time

import pygame
from constants import *
from Board import *
from Logic import *
from fonctions import *


class Game:
    def __init__(self, win, fen):
        self.win = win
        self.logic = Logic(fen)
        self.board = Board(BOARDSIZE)
        self.board.update(self.logic)

    def run(self):

        game_on = True
        clock = pygame.time.Clock()
        while game_on:
            clock.tick(60)
            self.win.fill(BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # si on appuie sur la croix
                    game_on = False

                # si on clique sur l'echequier
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                        isInrectangle(event.pos, BOARDTOPLEFTPOS, BOARDSIZE, BOARDSIZE):
                    self.board.attacked_cases = self.logic.cases_attacked_by(self.logic.turn)
                    # si on clique sur une case vide qui est un legal move
                    move = self.board.coord_from_pos(*event.pos)
                    if move in self.board.legal_moves_to_output:
                        previous_coord = self.board.clicked_piece_coord
                        self.logic.move(*previous_coord, *move)
                        self.board.update(self.logic)
                        self.board.legal_moves_to_output = []
                        self.board.clicked_piece_coord = None
                        self.board.legal_moves_to_output = []

                    # si on clique sur une pièce
                    elif self.board.isNotempty(*self.board.coord_from_pos(*event.pos)):
                        self.board.set_to_gone(*event.pos)
                        self.board.state = "dragging"

                        i, j = self.board.coord_from_pos(*event.pos)

                        moves = self.logic.board[i][j].legal_moves(self.logic)
                        self.board.legal_moves_to_output = moves
                    # si on clique sur une case vide
                    else:
                        self.board.legal_moves_to_output = []
                # si on lache la piece
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.board.state == "dragging":
                    move = self.board.coord_from_pos(*event.pos)
                    previous_coord = self.board.dragged_piece_coord
                    if move in self.board.legal_moves_to_output:
                        self.logic.move(*previous_coord, *move)
                        self.board.set_to_not_gone()
                        self.board.update(self.logic)
                        self.board.legal_moves_to_output = []
                    else:
                        self.board.set_to_not_gone()
                    self.board.state = "idle"

                # si on bouge la souris
                elif self.board.state == "dragging" and event.type == pygame.MOUSEMOTION:
                    self.board.dragged_piece_pos = event.pos

            self.draw_everything()
            pygame.display.flip()  # update l'affichage
        pygame.quit()

    def draw_everything(self):
        self.board.draw(self.win, *BOARDTOPLEFTPOS)
