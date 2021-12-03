from typing import List

from extract_binary_from_file import extract_binary_from_file

def get_common_binary_of_each_index(binaryArry: List[List[int]]) -> List[int]:

    #use the first element as a proxy for the length of each element
    lengthOfEachElement = len(binaryArray[0])

    #record the number of elements in an array
    numberOfElements = len(binaryArray)

    #create a dictionary to store values and initialize each value to 0
    indexDict = {index: 0 for index in range(lengthOfEachElement)}

    #iterate through each binary list
    for listElement in binaryArray:

        #iterate through each element
        for index, element in enumerate(listElement):

            #update the index total value
            indexDict[index] += element

    #initialize a list to store the common binaries
    commonBinary = []

    #iterate through each index to calculate and store
    for index in range(lengthOfEachElement):

        #get index sum
        indexSum = indexDict[index]

        #get the average by dividing by number of list elements
        indexAvg = indexSum / numberOfElements

        #determine if the index leans towards 0 or 1
        common = int(indexAvg >= .5)

        #append to our list
        commonBinary.append(common)

    return commonBinary

def reverse_binary_list(binaryList: List[int]) -> List[int]:
    
    #reverse the binary array
    reversedBinaryList = [abs(binary - 1) for binary in binaryList]
    
    return reversedBinaryList

def convert_binary_list_to_int(binaryList: List[int]) -> List[int]:
    
    #make binary value into string for processing
    stringValue = "".join([str(binary) for binary in binaryList])

    #use python's built-in casting to convert binary to int
    convertedValue = int(stringValue, 2)

    return convertedValue

if __name__ == "__main__":

    #extract our data
    binaryArray = extract_binary_from_file("Day_03_input.txt")

    #process the common digits
    commonBinary = get_common_binary_of_each_index(binaryArray)
    reversedBinary = reverse_binary_list(commonBinary)

    #convert both binaries to ints
    commonInteger = convert_binary_list_to_int(commonBinary)
    reservedInteger = convert_binary_list_to_int(reversedBinary)

    #produce the answer
    print("Answer:", commonInteger * reservedInteger)