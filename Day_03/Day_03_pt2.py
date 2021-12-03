from typing import List

from extract_binary_from_file import extract_binary_from_file
from Day_03_pt1 import convert_binary_list_to_int

def get_common_binary_in_index(binaryArray: List[List[int]], indexOfElement: int, get_common: bool = True) -> int:
    
    #initialize a sum to keep record
    sumOfIndex = 0

    for elementList in binaryArray:

        #add each sum to our record
        sumOfIndex += elementList[indexOfElement]

    #calculate our common binary
    avgOfIndex = sumOfIndex / len(binaryArray)

    #determine if the index leans towards 0 or 1
    common = int(avgOfIndex >= .5)

    #either return the common or least common
    if get_common:
        return common

    else:
        return abs(common - 1)


def get_running_common_binary(binaryArray: List[List[int]], get_common: bool = True) -> List[int]:
    ##TODO I feel like recursion would work well here to practice, refactor in the future

    #use the first element as a proxy for the length of each element
    lengthOfEachElement = len(binaryArray[0])

    #make a copy for us to work off of
    binaryArrayCopy = binaryArray.copy()

    #iterate through each index
    for indexOfElement in range(lengthOfEachElement):

        #determine the common/noncommon binary
        commonBinaryOfIndex = get_common_binary_in_index(binaryArrayCopy, indexOfElement, get_common)

        #create a filter condition based on the common/noncommon binary
        filter_condition = lambda x: x[indexOfElement] == commonBinaryOfIndex

        #produce a proposed replacement
        proposedNewBinaryArrayCopy = list(filter(filter_condition, binaryArrayCopy))

        #if the replace is empty, it will not replace the binary Array
        if proposedNewBinaryArrayCopy:
            binaryArrayCopy = proposedNewBinaryArrayCopy

    #return the first element, at this point, either 1 remains or all are the same
    return binaryArrayCopy[0]

if __name__ == "__main__":

    #extract our data
    binaryArray = extract_binary_from_file("Day_03_input.txt")

    #process the common digits
    commonBinary = get_running_common_binary(binaryArray)
    nonCommonBinary = get_running_common_binary(binaryArray, get_common = False)

    #convert both binaries to ints
    commonInteger = convert_binary_list_to_int(commonBinary)
    nonCommonInteger = convert_binary_list_to_int(nonCommonBinary)

    #produce the answer
    print("Answer:", commonInteger * nonCommonInteger)