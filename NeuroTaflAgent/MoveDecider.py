import random
import logging

from .Coordinate import Coordinate
from .Board import Board



class MoveDecider:
    board = None
    log = None

    def __init__(self):
        self.log = logging.getLogger(__class__.__name__)

    def decideMove(self, board, side):
        if self.board is None:
            self.board = Board(board)
        else:
            self.board.currentBoardState = board
            self.board.updateBoard()

        moves = self.generateAllPossible(side)
        return random.choice(moves)

    def generateAllPossible(self, side) -> list:

        if side == "attackers":
            check = ["t"]
        else:
            check = ["T", "K"]

        possible = []
        for y in range(len(self.board.board)):
            for x in range(len(self.board.board[y])):
                self.log.debug(
                    "checking "
                    + str(x)
                    + " "
                    + str(y)
                    + " "
                    + self.board.board[y][x]
                    + " "
                    + str(check)
                )
                if self.board.board[y][x] in check:
                    coord = Coordinate(x=x, y=y)
                    moveList = self.possibleMoves(coord)
                    for move in moveList:
                        possible.append(move)

        return possible

    def possibleMoves(self, coord: Coordinate) -> list:
        start = coord.__str__()
        moves = []

        new_coord = Coordinate(x=coord.x - 1, y=coord.y)
        # left
        while self.board.checkCoord(new_coord):
            moves.append(start + "-" + new_coord.__str__())
            new_coord.x = new_coord.x - 1

        new_coord = Coordinate(x=coord.x + 1, y=coord.y)
        # right
        while self.board.checkCoord(new_coord):
            moves.append(start + "-" + new_coord.__str__())
            new_coord.x = new_coord.x + 1

        new_coord = Coordinate(x=coord.x, y=coord.y - 1)
        # up
        while self.board.checkCoord(new_coord):
            moves.append(start + "-" + new_coord.__str__())
            new_coord.y = new_coord.y - 1

        new_coord = Coordinate(x=coord.x, y=coord.y + 1)
        # down
        while self.board.checkCoord(new_coord):
            moves.append(start + "-" + new_coord.__str__())
            new_coord.y = new_coord.y + 1

        return moves
