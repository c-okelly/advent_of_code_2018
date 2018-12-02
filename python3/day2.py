
def main():

    with open("data/day2.txt","r") as f:
        data = f.read().split("\n")

    # Run and test part 1
    firstAnswer = part1(data)
    print("First answer is: ", firstAnswer)

    # Run and test part 2
    secondAnswer = part2(data)
    print("Second answer is: ", secondAnswer)

def part1(data):

    two = 0
    three = 0
    for i in data:
        count = dict()
        for letter in i:
            currentCount = count.get(letter, 0)
            currentCount += 1
            count[letter] = currentCount
        # print(count.values())
        for c in (set(count.values())):
            # print(c)
            if c == 2:
                two += 1
            if c == 3:
                three += 1

    return three * two

def part2(data):

    for firstWord in data:
        for secondWord in data:
            if firstWord == secondWord:
                pass
            count = 0
            position = -1
            for letter in range(0,len(firstWord)):
                if firstWord[letter] != secondWord[letter]:
                    count += 1
                    position = letter
            if count == 1:
                return firstWord[0:position] + firstWord[position+1:]

if __name__ == "__main__":
    main()