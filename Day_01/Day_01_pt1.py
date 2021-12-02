from get_digits_from_file import get_digits_from_file

def count_increases(array: list) -> list:
    
    #zip the element after to the element before
    zippedArray = zip(array[1:], array[:-1])

    #track when the element after is greater than the element before
    booleanArrayOfIncrease = map(lambda x: x[0] > x[1], zippedArray)

    #return the sum
    return sum(booleanArrayOfIncrease)

#get a list of inputs from the file given
inputArray = get_digits_from_file("Day_01_input.txt")

#print the answer
print(count_increases(inputArray))
