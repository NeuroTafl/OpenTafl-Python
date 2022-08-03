from .Move import Move


class Ply:
    def __init__(
        self,
        plyNumber: int,
        plyMove: Move = None,
        boardstate=None,
        positionRecord: str = None,
        whoMoved: str = None,
    ):
        self.number = plyNumber
        self.move = None
        self.boardstate = None
        self.positionRecord = None
        self.whoMoved = None

    def getPositionRecord(self):
        if self.positionRecord:
            return self.positionRecord
        elif self.boardstate:
            raise Exception("boardstate needs to provide position record")
            return boardstate.getPositionRecord

    def __str__(self) -> str:
        ret = f"{self.number} - {self.move} - {self.whoMoved} - {self.getPositionRecord()}"
        return ret

    # Makes Ply objects sortable by their number member values
    def __lt__(self, other):
        return self.number < other.number
