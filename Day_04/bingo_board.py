from typing import List

class BingoBoard():
    def __init__(self, board = List[List[int]]):
        self._validate_board(board)
        self.board = board
        self.reset_unmarked()
        self.calledNumbers = []
        self.hitNumbers = []
        self.winner = False
        self.winningNumber = None

    def _validate_board(self, board):
        assert len(board) == 5
        for index in range(5):
            assert len(board[index]) == 5

    def reset_unmarked(self) -> None:
        self.unmarked = [[True] * 5 for row in range(5)]

    @staticmethod
    def index_of_rows(matrix: List[List[int]], index: int = 0):
        values = []

        for column in range(len(matrix)):
            values += [matrix[column][index]]

        return values

    def sum_unmarked(self) -> int:
        unmarkedSum = 0

        for row in range(5):
            for column in range(5):
                if self.unmarked[row][column]:
                    unmarkedSum += self.board[row][column]

        return unmarkedSum

    def account_for_called(self, calledNumber = int) -> bool:

        self.calledNumbers += [calledNumber]


        for row in range(5):
            for column in range(5):
                if self.board[row][column] == calledNumber:
                    self.hitNumbers += [calledNumber]
                    self.unmarked[row][column] = False
                    return True

        return False

    def check_if_won(self) -> bool:

        for index in range(5):
            rowCondition = not any(self.unmarked[index])
            columnCondition = not any(self.index_of_rows(self.unmarked, index))

            if (rowCondition) or (columnCondition):
                self.winner = True
                return True

 
        return False

    def process_bingo_pull(self, calledNumber: int) -> bool:

        if self.account_for_called(calledNumber):

            if self.check_if_won():
                self.winningNumber = calledNumber
                return True

        return False
