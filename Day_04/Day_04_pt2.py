from typing import Tuple

from extract_bingo_board import extract_bingo_boards_from_file
from bingo_board import BingoBoard

def find_winners(numbersBeingCalled, allBoards) -> None:
    for number in numbersBeingCalled:
        for board in allBoards:
            if not board.__dict__["winner"]:
                board.process_bingo_pull(number)

def find_last_winner(numbersBeingCalled, allBoards) -> Tuple[int, int]:

    lastWinningIndex = -1

    for board in allBoards:
        
        winningNumber = board.__dict__["winningNumber"]

        if winningNumber == None:
            continue

        indexInCalls = numbersBeingCalled.index(winningNumber)

        if indexInCalls > lastWinningIndex:
            lastWinningIndex = indexInCalls

            lastWinningBoard = board


    return lastWinningBoard.__dict__["winningNumber"], lastWinningBoard.sum_unmarked()

if __name__ == "__main__":
    numbersBeingCalled, allBoards = extract_bingo_boards_from_file("Day_04_input.txt")

    find_winners(numbersBeingCalled, allBoards)

    lastWinningNumber, lastWinningUnmarkedSum = find_last_winner(numbersBeingCalled, allBoards)

    print("Answer", lastWinningNumber * lastWinningUnmarkedSum)