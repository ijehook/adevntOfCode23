import os 

puzzleInput = r"{0}\inputLists\day1Input.txt" .format(str(os.getcwd()))

numberDict={
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def start():
    # open up input list
    inputFile = open(puzzleInput, "r")

    # read the puzzle input
    puzzleInputList = []
    for entry in inputFile:
        puzzleInputList.append(str((entry.split('\n')[0])))

    return puzzleInputList


def run():
    """ 
    """

    puzzleInputList = start()
    
    # get the list of digits per line
    digitListTotal = []
    for line in puzzleInputList:
        digitList = getDigitList(line)
        print("digi list is {0}" .format(digitList))
        digitListTotal.append(int("{0}{1}" .format(digitList[0], digitList[-1])))

    print(sum(digitListTotal))


def getDigitList(input):
    digitList = []
    
    numberList = []
    for key in numberDict.keys():
        if key in input:
            print("Found {0} in input {1}" .format(key, input))

    
    digitCount = []
    for count, item in input:
        try:
            digitCount.append((int(item), count))
        except:
            pass

    return digitList
    
run()
