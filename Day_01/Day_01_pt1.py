with open("Day_01_input.txt") as file:
    data = file.readlines()

inputArray = []

def clean_digit_from_string(string: str) -> str:

    #retain all numeric characters and join then together
    stringOfDigits = "".join([char for char in string if char.isnumeric()])

    #return the string of digits casted to integer
    return int(stringOfDigits)

def count_increases(array: list) -> list:
    
    #zip the element after to the element before
    zippedArray = zip(array[1:], array[:-1])

    #track when the element after is greater than the element before
    booleanArrayOfIncrease = map(lambda x: x[0] > x[1], zippedArray)

    #return the sum
    return sum(booleanArrayOfIncrease)

#read each line and append it to our input array after cleaning it
for line in data:
    inputArray.append(clean_digit_from_string(line))

#print the answer
print(count_increases(inputArray))
