# This file takes an input of blocks, each block contains the total number of websites,
# the number of websites to be sorted, and then the required information to rank each
# website based on popularity.

# Setting up basic variables to be used in the algorithm.
currentLine = 0
currentMatrixSize = 0
currentPopularity = 1
tempList = []
finalList = []
printList = []

# We need to use try/except to catch the EOF error that will end the infinite
# while loop that takes in the input from the system.
try:
    while True:
        
        # Taking in new lines from the system and changing said input to be
        # workable.
        newInput = input()
        if newInput != "":
            newInput = newInput.replace("\n", "")

        # The first line of each block has the number of websites to be processed and
        # the number of websites to be sorted (this is number k).
        if currentLine == 0:
            tempList = newInput.split(" ")
            currentMatrixSize = int(tempList[0])
            currentPopularity = int(tempList[1])-1
            tempList = [0] * currentMatrixSize
        else:

            # Now the algorithm actually processes the blocks.
            if newInput != "":
                newList = newInput.split(" ")
                try:
                    for number in newList:
                        tempList[int(number)] += 1
                except:
                    pass

            # When the final line of the block is reached, the websites will be sorted.
            if currentLine == currentMatrixSize:
                for index in range (currentMatrixSize):
                    finalList.append((tempList[index], index))
                finalList = sorted(finalList, key=lambda x: (-x[0], x[1]))

                # Prints the block of websites in the sorted order.
                print(finalList[currentPopularity][1])

                # Resets the used variables.
                finalList = []
                tempList = []
                currentMatrixSize = 0
                currentPopularity = 1
                currentLine = -1
        currentLine += 1

# This section of code is similar to the previous section. It is used to process
# the final block of websites.
except EOFError as e:

    # Instead of using "while True" we use this instead because there is only one more
    # block that needs to be processed.
    while currentLine != 0:
        newInput = ""
        if newInput != "":
            newInput = newInput.replace("\n", "")
        if currentLine == 0:
            tempList = newInput.split(" ")
            currentMatrixSize = int(tempList[0])
            currentPopularity = int(tempList[1])-1
            tempList = [0] * currentMatrixSize
        else:
            if newInput != "":
                newList = newInput.split(" ")
                try:
                    for number in newList:
                        tempList[int(number)] += 1
                except:
                    pass
            if currentLine == currentMatrixSize:
                for index in range (currentMatrixSize):
                    finalList.append((tempList[index], index))
                finalList = sorted(finalList, key=lambda x: (-x[0], x[1]))
                print(finalList[currentPopularity][1])
                finalList = []
                tempList = []
                currentMatrixSize = 0
                currentPopularity = 1
                currentLine = -1
        currentLine += 1
