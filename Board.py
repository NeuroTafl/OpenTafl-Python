from Coordinate import Coordinate


class Board:

    board = []
    currentBoardState = ""

    def __init__(self, boardState):
        self.currentBoardState = boardState
        self.updateBoard()

    def __str__(self):
        boardString = "/"
        for row in self.board:
            count = 0
            for piece in row:
                if piece == "e":
                    count += 1
                else:
                    if count != 0:
                        boardString += str(count)
                    boardString += piece
                    count = 0
            if count != 0:
                boardString += str(count)
            boardString += "/"

        print(boardString)
        return boardString

    def updateBoard(self) -> None:
        rows = self.currentBoardState.split(sep="/")
        array = []
        for row in rows:
            new_row = []
            try:
                spaces = int(row)
                for x in range(spaces):
                    new_row.append("e")
                if len(new_row) > 0:
                    array.append(new_row)
            except ValueError as e:
                for piece in row:
                    if piece.__contains__("t"):
                        new_row.append("t")
                    elif piece.__contains__("T"):
                        new_row.append("T")
                    elif piece.__contains__("K"):
                        new_row.append("K")
                    else:
                        spaces = int(piece)
                        for x in range(spaces):
                            new_row.append("e")
                if len(new_row) > 0:
                    array.append(new_row)
        # array.reverse()
        self.board = array

    def checkCoord(self, coord: Coordinate) -> bool:
        if coord.y >= len(self.board) or coord.y < 0:
            return False
        if coord.x >= len(self.board[0]) or coord.x < 0:
            return False
        if self.board[coord.y][coord.x] == "e":
            return True
        return False
