from typing import Tuple

from extract_bingo_board import extract_bingo_boards_from_file
from bingo_board import BingoBoard

def find_winner(numbersBeingCalled, allBoards) -> Tuple[int, int]:
    for number in numbersBeingCalled:
        for board in allBoards:
            if board.process_bingo_pull(number):
                return number, board.sum_unmarked()

    return 0, 0

if __name__ == "__main__":
    numbersBeingCalled, allBoards = extract_bingo_boards_from_file("Day_04_input.txt")

    winningNumber, unmarkedSum = find_winner(numbersBeingCalled, allBoards)

    print("Answer", winningNumber * unmarkedSum)