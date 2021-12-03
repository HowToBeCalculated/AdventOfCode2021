from typing import List

def clean_binary_from_string(string: str) -> str:

    #retain all numeric characters and join then together
    stringOfBinary = string.replace("\n", "")
    
    #return the string of digits casted to integer
    return stringOfBinary

def extract_binary_from_file(file_name: str) -> List[str]:

    #initialize an array to store values
    binaryArray = []

    #retrieve all of the lines
    with open(file_name) as file:
        for line in file:
            binaryArray.append(clean_binary_from_string(line))

    return binaryArray

if __name__ == "__main__":

    #test reading the input file
    print(list(extract_binary_from_file("Day_03_input.txt")))