from Coordinate import Coordinate
from Board import Board

class MoveDecider:

    board = None

    def decideMove(self, board, side):
        self.board = Board(board)
        moves = self.generateAllPossible(side)

    def generateAllPossible(self, side) -> list:

        check = ""
        if side == "attacker":
            check = "T"
        else:
            check = "t"

        possible = []
        for y in range(len(Board.board)):
            for x in range(len(Board.board[y])):
                if Board.board[y][x] == check:
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
        while(self.board.checkCoord(new_coord)):
            moves.append(start + " " + new_coord.__str__())
            new_coord.x = new_coord.x - 1

        new_coord = Coordinate(x=coord.x + 1, y=coord.y)
        # right
        while (self.board.checkCoord(new_coord)):
            moves.append(start + " " + new_coord.__str__())
            new_coord.x = new_coord.x + 1

        new_coord = Coordinate(x=coord.x, y=coord.y - 1)
        # up
        while (self.board.checkCoord(new_coord)):
            moves.append(start + " " + new_coord.__str__())
            new_coord.x = new_coord.y - 1

        new_coord = Coordinate(x=coord.x, y=coord.y + 1)
        # down
        while (self.board.checkCoord(new_coord)):
            moves.append(start + " " + new_coord.__str__())
            new_coord.x = new_coord.y + 1

