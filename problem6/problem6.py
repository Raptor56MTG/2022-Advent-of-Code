def problem6p1():
    """problem 6 part 1"""
    with open('problem6.txt', 'r') as f:
        signal = f.read()
        start = 0
        end = 4
        search = set(signal[start:end])
        while len(search) != 4 and end <= len(signal) - 1:
            start += 1
            end += 1
            search = set(signal[start:end])
        return end


def problem6p2():
    """problem 6 part 2"""
    with open('problem6.txt', 'r') as f:
        signal = f.read()
        start = 0
        end = 14
        search = set(signal[start:end])
        while len(search) != 14 and end <= len(signal) - 1:
            start += 1
            end += 1
            search = set(signal[start:end])
        return end


if __name__ == '__main__':
    print(problem6p1())
    print(problem6p2())
