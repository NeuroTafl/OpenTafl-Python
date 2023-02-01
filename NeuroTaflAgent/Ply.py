from .Move import Move
from .Board import Board
from .Side import Side


class Ply:
    def __init__(
        self,
        number: int = 0,
        move: Move = None,
        board: Board = None,
        whoMoved: Side = "",
    ):
        self.number = number
        self.move = move
        self.board = board
        self.whoMoved = whoMoved

    def getPositionRecord(self):
        return self.board.getBoardPositionString()

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

