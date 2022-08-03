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
            doubledigit = False
            for index in range(len(row)):
                if row[index] == "t":
                    new_row.append("t")
                elif row[index] == "T":
                    new_row.append("T")
                elif row[index] == "K":
                    new_row.append("K")
                else:
                    if doubledigit:
                        doubledigit = False
                    else:
                        if len(row) > index + 1 and self.isInt(row[index + 1]):
                            num = str(row[index]) + str(row[index + 1])
                            doubledigit = True
                        else:
                            num = str(row[index])
                        spaces = int(num)
                        for x in range(spaces):
                            new_row.append("e")
            if len(new_row) > 0:
                array.append(new_row)
        # array.reverse()
        self.board = array

    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError as e:
            return False

    def checkCoord(self, coord: Coordinate) -> bool:
        if coord.y >= len(self.board) or coord.y < 0:
            return False
        if coord.x >= len(self.board[0]) or coord.x < 0:
            return False
        if self.board[coord.y][coord.x] == "e":
            return True
        return False
