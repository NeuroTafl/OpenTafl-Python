from Board import Board
from Coordinate import Coordinate

### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
## Make 3 check, remove, set in board and change classes that use boards
# Move Decider
# Tensor Move Decider
# add wincheck on board


class NextBoardState:

    cur_board = None

    isKing = False

    piece = ""

    startingCoord = None
    endingCoord = None

    def __init__(self, board, piece):
        self.cur_board = board
        self.piece = piece


    def getBoards(self, moveList):
        boardList = []
        for move in moveList:
            boardList.append((move, self.getNext(move)))
        return boardList

    def getNext(self, move):
        # returns the boardstate in "////" format
        (origin, ending) = move.split("-", 1)
        originCoord = Coordinate()
        originCoord.loadFromCoordinate(origin)
        self.startingCoord = originCoord
        endingCoord = Coordinate()
        endingCoord.loadFromCoordinate(ending)
        self.endingCoord = endingCoord
        piece = self.cur_board.getPieceAtCoord(originCoord)
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
            return self.checkMove(coord)


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
            captured = self.checkCapture(coord)
            return self.makeBoard(captured)


    def makeBoard(self, captured):
        new_board = Board(self.cur_board.__str__())
        for coord in captured:
            new_board.removePieceAtCoord(coord)

        if self.isKing:
            new_board.setPieceAtCoord(self.endingCoord, "K")
        else:
            new_board.setPieceAtCoord(self.endingCoord, self.piece)

        new_board.removePieceAtCoord(self.startingCoord)
        return new_board


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
            if self.cur_board.getPieceAtCoord(toCheckTeam) == self.piece:
                between = self.cur_board.getPieceAtCoord(toCheckOpp)
                if between != self.piece and between != "e":
                    return toCheckOpp
        return None

    def checkPossilbe(self, coord):
        if coord.getYIndex() >= len(self.cur_board.board):
            return False
        if coord.getXIndex() >= len(self.cur_board.board[0]):
            return False
        if coord.getYIndex() < 0:
            return False
        if coord.getXIndex() < 0:
            return False
        return True

        ## FIX BOARD BEFORE MOVING ON


    def checkShield(self, coord):
        pass

    def checkEdge(self, coord):
        pass