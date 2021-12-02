from typing import List

from get_digits_from_file import get_digits_from_file
from Day_01_pt1 import count_increases

def get_three_in_row_sums(array: list) -> List[int]:

    #zip the 3 important elements to sum
    zipped_arrays = zip(array[:-2], array[1:-1], array[2:])

    #sum the triple elements
    summed_array = map(sum, zipped_arrays)

    #expand to list
    return list(summed_array)

if __name__ == "__main__":
    
    #get a list of inputs from the file given
    inputArray = get_digits_from_file("Day_01_input.txt")

    #follow the directions to sum up the triple rows
    summed_array = get_three_in_row_sums(inputArray)

    #print the answer
    print(count_increases(summed_array))