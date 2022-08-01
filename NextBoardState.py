from Board import Board
from Coordinate import Coordinate


class NextBoardState:

    cur_board = None

    isKing = False

    piece = ""

    def __init__(self, board, piece):
        self.cur_board = board
        self.piece = piece

    def getNext(self, move, piece):
        # returns the boardstate in "////" format
        coord = Coordinate()
        coord.loadFromCoordinate(move)
        if piece == "K":
            self.isKing = True
            self.piece = "T"
        elif piece == "T":
            self.piece = "T"
        else:
            self.piece = "t"

        return self.checkLegal(move)

    def checkLegal(self, coord):
        if coord is self.isCorner(coord) and not self.isKing:
            return "Illegal Move"
        elif coord is self.isCorner(coord) and self.isKing:
            return "Victory Defenders"
        else:
            self.checkMove(coord)

    def isCorner(self, coord: Coordinate):
        if coord.getYIndex() == len(self.cur_board.board) and coord.getXIndex() == len(
            self.cur_board.board[0]
        ):
            return True
        elif coord.getYIndex() == 0 and coord.getXIndex() == 0:
            return True
        elif coord.getYIndex() == len(self.cur_board.board) and coord.getXIndex() == 0:
            return True
        elif coord.getYIndex() == 0 and coord.getXIndex() == len(
            self.cur_board.board[0]
        ):
            return True
        else:
            return False

    def checkMove(self, coord):
        if self.cur_board.checkCoord(coord):
            self.checkCapture(coord)

    def checkCapture(self, coord):
        direction = ["up", "down", "right", "left"]
        captures = []
        for direct in direction:
            capped = self.possibleCapture(coord, direct)
            if capped is not None:
                captures.append(capped)
        return captures

        # check all directions +2 for teamate piece
        # check all directions with teamate for enemy inbetween
        # return list of all killed pieces

    def possibleCapture(self, coord, desig):
        pass

    def checkShield(self, coord):
        pass

    def checkEdge(self, coord):
        pass
