from typing import List

from bingo_board import BingoBoard

def clean_called_numbers_string(string: str) -> str:

    #retain the binary number after removing the new line
    cleanedString = string.replace("\n", "")
    cleanedString = cleanedString.split(",")
    cleanedArray = [int(number) for number in cleanedString]

    return cleanedArray

def clean_bingo_line(string: str) -> str:

    #retain the binary number after removing the new line
    cleanedString = string.replace("\n", "")
    cleanedString = cleanedString.split(" ")
    cleanedArray = [int(number) for number in cleanedString if len(number) > 0]

    return cleanedArray

def make_numeric_array(binaryString : str) -> List[int]:

    #separate out each character and cast as integer
    integerArray = [int(char) for char in binaryString]

    return integerArray

def extract_bingo_boards_from_file(file_name: str) -> List[List[int]]:

    #initialize an array to store values
    # binaryArray = []

    #retrieve all of the lines
    with open(file_name) as file:
        bingoData = file.readlines()

    numbersBeingCalled = clean_called_numbers_string(bingoData[0])
    allBoards = []

    board = []

    for index, line in enumerate(bingoData[2:] +["\n"]):
        if line == "\n":
            allBoards += [BingoBoard(board)]
            board = []
        else:
            board += [clean_bingo_line(line)]

    return numbersBeingCalled, allBoards

if __name__ == "__main__":

    #test reading the input file
    print(extract_bingo_boards_from_file("Day_04_input.txt"))

    

