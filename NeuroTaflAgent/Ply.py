from .Move import Move
from .Board import Board


class Ply:
    def __init__(
        self,
        plyNumber: int = 0,
        plyMove: Move = None,
        board: Board=None,
        positionRecord: str = None,
        whoMoved: str = None,
    ):
        self.number = plyNumber
        self.move = plyMove
        self.board = board
        self.positionRecord = positionRecord
        self.whoMoved = whoMoved

        # Create a board for this ply if it wasn't given one
        if not board and positionRecord:
            self.board = Board(positionRecord)

    def getPositionRecord(self):
        if self.positionRecord:
            return self.positionRecord
        elif self.board:
            return self.board.getBoardPositionString()
        else:
            return "No board state available."

    def __str__(self) -> str:
        ret = f"{self.number} - {self.move} - {self.whoMoved} - {self.getPositionRecord()}"
        return ret

    # Makes Ply objects sortable by their number member values
    def __lt__(self, other):
        return self.number < other.number

    def getBoard(self):
        return self.board

