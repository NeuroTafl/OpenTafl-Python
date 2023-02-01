from .Move import Move
from .Board import Board


class Ply:
    def __init__(
        self,
        plyNumber: int = 0,
        plyMove: Move = None,
        plyBoard: Board = None,
        positionRecord: str = "",
        whoMoved: str = "",
    ):
        self.number = plyNumber
        self.move = plyMove
        self.board = plyBoard
        self.positionRecord = positionRecord
        self.whoMoved = whoMoved

        # Create a board for this ply if it wasn't given one
        if not plyBoard and positionRecord:
            self.board = Board(positionRecord)

    def getPositionRecord(self):
        if self.positionRecord:
            return self.positionRecord
        elif self.board:
            return self.board.getBoardPositionString()
        else:
            return "No board state available."

    def getBoard(self):
        return self.board

    def getMove(self):
        return self.move

    def getWhoMoved(self):
        return self.whoMoved

    def getTerminalStr(self):
        ret = f"{self.getWhoMoved():11} | {str(self.getMove()):10} |\n"
        ret += self.board.getTerminalStr()
        return ret

    def __str__(self) -> str:
        ret = f"{self.number} - {self.move} - {self.whoMoved} - {self.getPositionRecord()}"
        return ret

    # Makes Ply objects sortable by their number member values
    def __lt__(self, other):
        return self.number < other.number

