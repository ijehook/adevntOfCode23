import os 

puzzleInput = r"{0}\inputLists\day1Input.txt" .format(str(os.getcwd()))


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
    for item in input:
        try:
            digitList.append(int(item))
        except:
            pass

    return digitList
    
run()
