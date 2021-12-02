from typing import List

def clean_digit_from_string(string: str) -> str:

    #retain all numeric characters and join then together
    stringOfDigits = "".join([char for char in string if char.isnumeric()])

    #return the string of digits casted to integer
    return int(stringOfDigits)

def get_digits_from_file(file_name: str) -> List[int]:

    #initialize an input array
    inputArray = []

    #retrieve all of the lines
    with open(file_name) as file:
        data = file.readlines()

    #for each line, clean the string for digits and append
    for line in data:
        inputArray.append(clean_digit_from_string(line))

    return inputArray
    