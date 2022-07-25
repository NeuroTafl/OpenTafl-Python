class Ply:
    whoMoved = 0  # should be 1 if attackers, 2 in defenders
    lastMove = ""  # will be a string of the move send by the opponent-move command
    board = ""  # current board string

    def updatePly(self, whoMoved: int, move: str, board: str) -> None:
        self.whoMoved = whoMoved
        self.lastMove = move
        self.board = board
