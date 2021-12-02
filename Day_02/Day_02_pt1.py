from typing import List, Iterator, Tuple

from extract_velocity_from_file import extract_velocity_from_file

#define all directions and their affect on position
DIRECTION_DICTIONARY = {
    "forward" : {"type" : "horizontal", "multiplier":  1},
    "backward" : {"type" : "horizontal", "multiplier" : -1},
    "down" : {"type" : "depth", "multiplier" : 1},
    "up" : {"type" : "depth", "multiplier" : -1},
}

def calculate_position_given_velocity(zippedVelocity: Iterator[Tuple[str, str]]) -> Tuple[int, int]:

    #initialize a dictionary to store values
    position = {
        "horizontal" : 0,
        "depth" : 0,
    }

    #iterate over each velocity update
    for velocity in zippedVelocity:

        #separate out direction and value
        direction, value = velocity

        #retrieve the direction's effect on position
        directionType = DIRECTION_DICTIONARY[direction]["type"]
        directionMultiplier = DIRECTION_DICTIONARY[direction]["multiplier"]

        #cast the value to integer and account for its multiplier
        value = int(value)
        value = value * directionMultiplier

        #record the update in our position dict
        position[directionType] += value

    #return our ending position
    return position["horizontal"], position["depth"]


if __name__ == "__main__":

    #get the velocities from the file
    velocityIterator = extract_velocity_from_file("Day_02_input.txt")

    #get the ending horizontal and depth positions
    posHorizontal, posDepth = calculate_position_given_velocity(velocityIterator)

    #print the answers
    print(f"horizontal_position = {posHorizontal} ~ depth_position = {posDepth}")
    print("Answer:", posHorizontal * posDepth)

