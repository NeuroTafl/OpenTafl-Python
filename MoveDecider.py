class MoveDecider:

    board = []

    def decideMove(self, board, side):
        self.board = board
        moves = self.generateAllPossible(side)

    def generateAllPossible(self, side) -> list:

        # for every tile
            # if correct piece
            # for each direction
                # add to list of places to go
                # give score (monty carlo will be all score 1)
        # return list
