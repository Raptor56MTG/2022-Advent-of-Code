def problem4p1():
    """problem 4 part 1"""
    with open('problem4.txt', 'r') as f:
        total = 0
        for line in f:
            pairs = [int(x) for x in line.rstrip().replace('-', ',').split(',')]
            if ((pairs[0] <= pairs[2] and pairs[1] >= pairs[3]) or
               (pairs[0] >= pairs[2] and pairs[1] <= pairs[3])):
                total += 1
        return total


def problem4p2():
    """problem 4 part 2"""
    with open('problem4.txt', 'r') as f:
        total = 0
        for line in f:
            pairs = [int(x) for x in line.rstrip().replace('-', ',').split(',')]
            if ((pairs[0] <= pairs[2] and pairs[1] >= pairs[3]) or
               (pairs[0] >= pairs[2] and pairs[1] <= pairs[3]) or
               (pairs[2] >= pairs[0] and pairs[2] <= pairs[1]) or
               (pairs[0] >= pairs[2] and pairs[0] <= pairs[3])):
                total += 1
        return total


if __name__ == '__main__':
    print(problem4p2())
