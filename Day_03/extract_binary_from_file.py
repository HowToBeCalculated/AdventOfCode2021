from typing import List

def clean_binary_from_string(string: str) -> str:

    #retain the binary number after removing the new line
    stringOfBinary = string.replace("\n", "")

    return stringOfBinary

def make_numeric_array(binaryString : str) -> List[int]:

    #separate out each character and cast as integer
    integerArray = [int(char) for char in binaryString]

    return integerArray

def extract_binary_from_file(file_name: str) -> List[List[int]]:

    #initialize an array to store values
    binaryArray = []

    #retrieve all of the lines
    with open(file_name) as file:
        for line in file:
            cleaned_string = clean_binary_from_string(line)
            binaryArray.append(make_numeric_array(cleaned_string))

    return binaryArray

if __name__ == "__main__":

    #test reading the input file
    print(list(extract_binary_from_file("Day_03_input.txt")))