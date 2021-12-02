from typing import List, Iterator, Tuple

def extract_direction_value_from_string(string: str) -> List[str]:

    #remove the new line after each input
    cleanedString = string.replace("\n", "")

    #separate out the direction and the value
    separateString = cleanedString.split(" ")

    #return the string of digits casted to integer
    return separateString

def extract_velocity_from_file(file_name: str) -> Iterator[Tuple[str, str]]:

    #initialize an input array
    directionArray = []
    valueArray = []

    #retrieve all of the lines
    with open(file_name) as file:
        data = file.readlines()

    #for each line, clean the string direction and value and append to our list
    for line in data:
        direction, value = extract_direction_value_from_string(line)

        directionArray.append(direction)
        valueArray.append(value)

    #zip the arrays togethers to now have a generator with both values
    zippedArray = zip(directionArray, valueArray)

    return zippedArray

if __name__ == "__main__":
    
    #test reading the input file
    print(list(extract_velocity_from_file("Day_02_input.txt")))