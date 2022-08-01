from Board import Board
from Coordinate import Coordinate

class NextBoardState:

    cur_board = None

    isKing = False

    piece = ""

    def __init__(self, board, piece):
        self.cur_board = board
        self.piece = piece


    def getNext(self, move):
        # returns the boardstate in "////" format
        (origin, ending) = move.split("-", 1)
        originCoord = Coordinate()
        originCoord.loadFromCoordinate(origin)
        endingCoord = Coordinate()
        endingCoord.loadFromCoordinate(ending)
        piece = self.cur_board.board[originCoord.getYIndex()][originCoord.getXIndex()]
        if piece == "K":
            self.isKing = True
            self.piece = "T"
        elif piece == "T":
            self.piece = "T"
        else:
            self.piece = "t"

        return self.checkLegal(endingCoord)
    

    def checkLegal(self, coord):
        if coord is self.isCorner(coord) and not self.isKing:
            return "Illegal Move"
        elif coord is self.isCorner(coord) and self.isKing:
            return "Victory Defenders"
        else:
            self.checkMove(coord)


    def isCorner(self, coord: Coordinate):
        if coord.getYIndex() == len(self.cur_board.board) and coord.getXIndex() == len(self.cur_board.board[0]):
            return True
        elif coord.getYIndex() == 0 and coord.getXIndex() == 0:
            return True
        elif coord.getYIndex() == len(self.cur_board.board) and coord.getXIndex() == 0:
            return True
        elif coord.getYIndex() == 0 and coord.getXIndex() == len(self.cur_board.board[0]):
            return True
        else:
            return False



    def checkMove(self, coord):
        if self.cur_board.checkCoord(coord):
            self.checkCapture(coord)


    def checkCapture(self, coord):
        direction = ["up", "down","right", "left"]
        captures = []
        for direct in direction:
            capped = self.possibleCapture(coord, direct)
            if capped is not None:
                captures.append(capped)
        return captures

    def possibleCapture(self, coord, desig):
        toCheckTeam = Coordinate()
        toCheckOpp = Coordinate()

        if desig == "up":
            toCheckTeam.x = coord.getXIndex()
            toCheckTeam.y = coord.getYIndex() - 2
            toCheckOpp.x = coord.getXIndex()
            toCheckOpp.y = coord.getYIndex() - 1
        elif desig == "down":
            toCheckTeam.x = coord.getXIndex()
            toCheckTeam.y = coord.getYIndex() + 2
            toCheckOpp.x = coord.getXIndex()
            toCheckOpp.y = coord.getYIndex() + 1
        elif desig == "right":
            toCheckTeam.x = coord.getXIndex() + 2
            toCheckTeam.y = coord.getYIndex()
            toCheckOpp.x = coord.getXIndex() + 1
            toCheckOpp.y = coord.getYIndex()
        else:
            toCheckTeam.x = coord.getXIndex() - 2
            toCheckTeam.y = coord.getYIndex()
            toCheckOpp.x = coord.getXIndex() - 1
            toCheckOpp.y = coord.getYIndex()

        if self.checkPossilbe(toCheckTeam):
            if self.cur_board[toCheckTeam.getYIndex()][toCheckTeam.getXIndex()] == self.piece:
                between = self.cur_board[toCheckOpp.getYIndex()][toCheckOpp.getXIndex()]
                if between != self.piece and between != "e":
                    return toCheckOpp
        return None

    def checkPossilbe(self, coord):
        if coord.getYIndex > len(self.cur_board):
            return False
        if coord.getXIndex > len(self.cur_board[0]):
            return False
        if coord.getYIndex < 0:
            return False
        if coord.getXIndex < 0:
            return False
        return True

        ## FIX BOARD BEFORE MOVING ON


    def checkShield(self, coord):
        pass

    def checkEdge(self, coord):
        pass