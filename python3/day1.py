

def main():

    with open("data/day1.txt","r") as f:
        data = f.read().split("\n")

    # Run and test part 1
    firstAnswer = part1(data)
    print("First answer is: ", firstAnswer)

    # Run and test part 2
    secondAnswer = part2(data)
    print("Second answer is: ", secondAnswer)


def part1(data):

    total = 0

    for i in data:
        # print(i[0], i[1:])
        if i[0] == "+":
            total += int(i[1:])
        elif i[0] == "-":
            total -= int(i[1:])
        else:
            raise Exception("Unknown symbol")
    return total

def part2(data):

    total = 0
    seenFrequencies = set()
    seenFrequencies.add(0)
    listPosition = 0

    while True:
        relativePosition = listPosition % len(data)
        listPosition += 1
        i = data[relativePosition]
        # print(i[0], i[1:])
        if i[0] == "+":
            total += int(i[1:])
        elif i[0] == "-":
            total -= int(i[1:])

        # Add to seen or return first duplicate
        if total in seenFrequencies:
            return total
        else:
            seenFrequencies.add(total)


if __name__ == "__main__":
    main()