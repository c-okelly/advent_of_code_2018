
def main():

    with open("data/day3.txt","r") as f:
        data = f.read().split("\n")

    # Run and test part 1
    testData1 = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    testData1 = testData1.split("\n")
    assert(part1(testData1) == 4)

    firstAnswer = part1(data)
    print("First answer is: ", firstAnswer)

    # Run and test part 2
    testData1 = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    testData1 = testData1.split("\n")
    assert(part2(testData1) == 3)
    secondAnswer = part2(data)
    print("Second answer is: ", secondAnswer)

def part1(data):

    # print(data)
    seenPositions = {}
    for i in data:
        row = i.split(" ")
        id = row[0]
        startSquare = row[2]
        xStart = startSquare.split(",")[0]
        yStart = startSquare.split(",")[1][:-1]
        size = row[3]
        xSize = size.split("x")[0]
        ySize = size.split("x")[1]
        # print()
        # print(id, xStart, yStart, xSize, ySize)

        for x in range(int(xStart), int(xStart)+int(xSize)):
            for y in range(int(yStart), int(yStart)+int(ySize)):
                # print(x, y)
                position = (x, y)
                count = seenPositions.get(position, 0)
                seenPositions[position] = count + 1
    # print(seenPositions)

    duplicates = 0
    for key in seenPositions.keys():
        if seenPositions[key] >= 2:
            duplicates += 1
    
    # print(duplicates)
    return duplicates

def part2(data):

    seenPositions = {}
    cleanIDs = []
    for i in data:
        row = i.split(" ")
        id = row[0][1:]
        startSquare = row[2]
        xStart = startSquare.split(",")[0]
        yStart = startSquare.split(",")[1][:-1]
        size = row[3]
        xSize = size.split("x")[0]
        ySize = size.split("x")[1]
        # print()
        # print(id, xStart, yStart, xSize, ySize)

        duplicateFound = False
        for x in range(int(xStart), int(xStart)+int(xSize)):
            for y in range(int(yStart), int(yStart)+int(ySize)):
                # print(x, y)
                position = (x, y)
                if seenPositions.get(position, 0) == 0:
                    seenPositions[position] = id
                else:
                    oldID = seenPositions.get(position)
                    if oldID in cleanIDs:
                        cleanIDs.remove(oldID)
                    duplicateFound = True
        
        if duplicateFound == False:
            cleanIDs.append(id)

    return int(cleanIDs[0])


if __name__ == "__main__":
    main()